// Sample timing with no Arduino dependency, so tests/firmware/ can run it on the host.
// sample_idx is the time slot since boot, so lost time shows up as a jump in the
// index instead of being replayed as a burst of samples.
#pragma once
#include <stdint.h>

struct SampleTick {
  bool emit;         // this call opened a new slot: take one sample
  uint32_t index;    // the slot number, used as sample_idx
  uint32_t skipped;  // slots that passed without a sample since the last one
};

class SampleClock {
 public:
  SampleClock(uint64_t startUs, uint32_t periodUs) : start_(startUs), period_(periodUs) {}

  SampleTick tick(uint64_t nowUs) {
    const uint64_t slot = (nowUs - start_ + period_ / 2) / period_;
    if (slot < next_) return {false, 0, 0};
    const uint32_t skipped = static_cast<uint32_t>(slot - next_);
    next_ = slot + 1;
    return {true, static_cast<uint32_t>(slot), skipped};
  }

 private:
  uint64_t start_;
  uint32_t period_;
  uint64_t next_ = 0;
};

// Write a line only when all of it fits, so a stalled host costs whole samples
// (counted in missed) and never leaves a truncated line.
inline bool lineFits(int freeBytes, int lineBytes) {
  return freeBytes >= lineBytes;
}
