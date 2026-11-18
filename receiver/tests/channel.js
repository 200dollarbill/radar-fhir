// An async source the test feeds by hand.
export function channel() {
  const queue = [];
  let wake = null;
  let ended = false;
  let failure = null;
  const it = {
    push(v) { queue.push(v); wake?.(); },
    end() { ended = true; wake?.(); },
    fail(e) { failure = e; wake?.(); },
    async *[Symbol.asyncIterator]() {
      for (;;) {
        if (queue.length) { yield queue.shift(); continue; }
        if (failure) throw failure;
        if (ended) return;
        await new Promise((r) => { wake = r; });
        wake = null;
      }
    },
  };
  return it;
}

