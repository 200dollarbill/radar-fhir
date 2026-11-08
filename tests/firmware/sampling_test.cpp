// Host test for arduino/radar_json/sampling.h. Built and run by
// tests/test_firmware_sampling.py. Kept outside the sketch folder because
// arduino-cli compiles every .cpp in the sketch.
#include <cassert>
#include <cstdint>
#include <cstdio>
#include "../../arduino/radar_json/sampling.h"

static const uint32_t P = 10000;  // 10 ms

static void on_time_slots_are_consecutive() {
  SampleClock c(1000, P);
  for (uint32_t k = 0; k < 5; k++) {
    SampleTick t = c.tick(1000 + k * P);
    assert(t.emit && t.index == k && t.skipped == 0);
  }
}

static void small_jitter_skips_nothing() {
  SampleClock c(0, P);
  assert(c.tick(0).emit);
  SampleTick t = c.tick(P + 3000);
  assert(t.emit && t.index == 1 && t.skipped == 0);
  t = c.tick(2 * P - 1000);
  assert(t.emit && t.index == 2 && t.skipped == 0);
}

static void same_slot_never_emits_twice() {
  SampleClock c(0, P);
  assert(c.tick(0).emit);
  assert(!c.tick(1000).emit);
  assert(!c.tick(4000).emit);
}

// The measured bug: 30 s stall replayed as a burst with continuous sample_idx.
static void stall_jumps_the_index_and_does_not_burst() {
  SampleClock c(0, P);
  c.tick(0);
  uint64_t now = 30000000;
  SampleTick t = c.tick(now);
  assert(t.emit && t.index == 3000 && t.skipped == 2999);
  for (uint64_t later = now + 100; later < now + 4000; later += 100) {
    assert(!c.tick(later).emit);  // no catch-up samples
  }
  t = c.tick(now + P);
  assert(t.emit && t.index == 3001 && t.skipped == 0);
}

// The measured bug: missed reached 171 million by recounting lateness.
static void skipped_is_counted_once() {
  SampleClock c(0, P);
  c.tick(0);
  uint64_t total = 0;
  for (uint64_t now = 25000000; now < 25000000 + 50 * P; now += P) {
    total += c.tick(now).skipped;
  }
  assert(total == 2499);
}

static void line_must_fit_whole() {
  assert(lineFits(200, 200));
  assert(!lineFits(199, 200));
  assert(!lineFits(-1, 200));
}

int main() {
  on_time_slots_are_consecutive();
  small_jitter_skips_nothing();
  same_slot_never_emits_twice();
  stall_jumps_the_index_and_does_not_burst();
  skipped_is_counted_once();
  line_must_fit_whole();
  puts("sampling ok");
  return 0;
}
