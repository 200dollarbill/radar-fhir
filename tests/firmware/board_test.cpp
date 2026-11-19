// Host test for firmware/radar_json/board.h. Built and run by
// tests/test_firmware_board.py, which also parses the printed BOARD line as JSON.
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include "../../firmware/radar_json/board.h"

static bool feed(LineReader& r, const char* text) {
  bool done = false;
  for (const char* p = text; *p; ++p) done = r.push(*p);
  return done;
}

static void reads_a_line_with_cr_lf() {
  LineReader r;
  assert(!feed(r, "BOARD"));
  assert(feed(r, "?\r\n"));
  assert(strcmp(r.line(), "BOARD?") == 0);
  assert(isBoardQuery(r.line()));
}

static void next_line_starts_clean() {
  LineReader r;
  assert(feed(r, "hello\n"));
  assert(feed(r, "BOARD?\n"));
  assert(strcmp(r.line(), "BOARD?") == 0);
}

static void overlong_line_is_dropped_whole() {
  LineReader r;
  char longLine[100];
  memset(longLine, 'x', 80);
  longLine[80] = '\0';
  assert(!feed(r, longLine));
  assert(!r.push('\n'));           // the overlong line never completes
  assert(feed(r, "BOARD?\n"));     // and does not poison the next one
  assert(isBoardQuery(r.line()));
}

static void empty_lines_are_ignored() {
  LineReader r;
  assert(!feed(r, "\n\r\n"));
}

static void query_must_match_exactly() {
  assert(isBoardQuery("BOARD?"));
  assert(!isBoardQuery("BOARD? "));
  assert(!isBoardQuery("board?"));
  assert(!isBoardQuery("BOARD"));
}

static void mac_is_printed_in_transmission_order() {
  // ESP.getEfuseMac(): first MAC octet in the lowest byte
  const uint64_t mac = 0x0000563412CDAB12ULL;  // octets 12 AB CD 12 34 56
  char id[13];
  hexId(mac, id);
  assert(strcmp(id, "12ABCD123456") == 0);
}

static void key_hex_and_validation() {
  uint8_t raw[32];
  for (int k = 0; k < 32; k++) raw[k] = static_cast<uint8_t>(k * 7 + 1);
  char key[65];
  toHex(raw, 32, key);
  assert(strlen(key) == 64);
  assert(keyIsValid(key));
  assert(!keyIsValid("ABC"));
  char upper[65];
  strcpy(upper, key);
  upper[0] = 'A';
  assert(!keyIsValid(upper));
}

static void board_line_fits_or_reports_failure() {
  const char* key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef";
  char out[160];
  const int n = formatBoardLine(out, sizeof(out), "AB12CD34EF56", key);
  assert(n > 0 && out[n - 1] == '\n' && static_cast<int>(strlen(out)) == n);
  char tiny[20];
  assert(formatBoardLine(tiny, sizeof(tiny), "AB12CD34EF56", key) < 0);
  printf("%s", out);  // parsed as JSON by the Python runner
}

int main() {
  reads_a_line_with_cr_lf();
  next_line_starts_clean();
  overlong_line_is_dropped_whole();
  empty_lines_are_ignored();
  query_must_match_exactly();
  mac_is_printed_in_transmission_order();
  key_hex_and_validation();
  board_line_fits_or_reports_failure();
  printf("board ok\n");
  return 0;
}
