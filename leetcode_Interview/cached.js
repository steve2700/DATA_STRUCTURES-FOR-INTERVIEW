class TimeLimitedCache {
  constructor() {
    this.cache = new Map();
  }

  set(key, value, duration) {
    if (this.cache.has(key) && this.cache.get(key).timeoutId) {
      clearTimeout(this.cache.get(key).timeoutId);
    }

    const timeoutId = setTimeout(() => {
      this.cache.delete(key);
    }, duration);

    const exists = this.cache.has(key);
    this.cache.set(key, { value, timeoutId });

    return exists;
  }

  get(key) {
    if (!this.cache.has(key) || !this.cache.get(key).timeoutId) {
      return -1;
    }

    return this.cache.get(key).value;
  }

  count() {
    return Array.from(this.cache.values()).filter((entry) => entry.timeoutId).length;
  }
}
