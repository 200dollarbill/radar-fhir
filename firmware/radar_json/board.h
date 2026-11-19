// Board identity over serial, with no Arduino dependency so tests/firmware/ can
// run it on the host. The host sends "BOARD?"; the board answers
// BOARD {"id":"<12 hex>","key":"<64 hex>","fw":"radar_json"}.
//
// KNOWN VULNERABILITY (owner's choice for now, spec 2026-11-18 "Known
// vulnerability"): the key is sent in clear text to anyone who asks over the
// port. The later fix is challenge and response (HMAC of a server nonce), so
// the key never leaves the board after registration.
#pragma once
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

// Collects command lines sent by the host. Lines longer than kMax are dropped
// whole; CR is ignored so both "\n" and "\r\n" endings work.
class LineReader {
 public:
  static constexpr size_t kMax = 63;

  // True when a complete, non-empty line is ready in line().
  bool push(char c) {
    if (c == '\r') return false;
    if (c == '\n') {
      const bool ok = !overflow_ && len_ > 0;
      buf_[len_] = '\0';
      len_ = 0;
      overflow_ = false;
      return ok;
    }
    if (len_ >= kMax) {
      overflow_ = true;
      return false;
    }
    buf_[len_++] = c;
    return false;
  }

  const char* line() const { return buf_; }

 private:
  char buf_[kMax + 1] = {0};
  size_t len_ = 0;
  bool overflow_ = false;
};

inline bool isBoardQuery(const char* line) { return strcmp(line, "BOARD?") == 0; }

inline void toHex(const uint8_t* bytes, size_t n, char* out) {
  static const char digits[] = "0123456789abcdef";
  for (size_t k = 0; k < n; k++) {
    out[2 * k] = digits[bytes[k] >> 4];
    out[2 * k + 1] = digits[bytes[k] & 0x0f];
  }
  out[2 * n] = '\0';
}

// ESP.getEfuseMac() keeps the first MAC octet in the lowest byte.
inline void hexId(uint64_t mac, char out[13]) {
  static const char digits[] = "0123456789ABCDEF";
  for (int k = 0; k < 6; k++) {
    const uint8_t b = static_cast<uint8_t>(mac >> (8 * k));
    out[2 * k] = digits[b >> 4];
    out[2 * k + 1] = digits[b & 0x0f];
  }
  out[12] = '\0';
}

inline bool keyIsValid(const char* key) {
  if (strlen(key) != 64) return false;
  for (const char* p = key; *p; ++p) {
    if (!((*p >= '0' && *p <= '9') || (*p >= 'a' && *p <= 'f'))) return false;
  }
  return true;
}

// Returns the line length including '\n', or -1 if it does not fit.
inline int formatBoardLine(char* out, size_t size, const char* id, const char* key) {
  const int n = snprintf(out, size, "BOARD {\"id\":\"%s\",\"key\":\"%s\",\"fw\":\"radar_json\"}\n",
                         id, key);
  return (n > 0 && static_cast<size_t>(n) < size) ? n : -1;
}
