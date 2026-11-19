// Returns schedule(): runs async fn at most once per ms, never two at once.
// Calls made while a run or timer is pending collapse into one later run.
export function coalesce(fn, ms, { setTimer = setTimeout } = {}) {
  let timer = null;
  let running = false;
  let dirty = false;
  const arm = () => {
    if (timer !== null || running) return;
    timer = setTimer(fire, ms);
  };
  async function fire() {
    timer = null;
    running = true;
    dirty = false;
    try { await fn(); } finally {
      running = false;
      if (dirty) arm();
    }
  }
  return () => { dirty = true; arm(); };
}
