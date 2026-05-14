class InMemoryQueue:
    def enqueue(self, fn, *args, **kwargs):
        return fn(*args, **kwargs)
