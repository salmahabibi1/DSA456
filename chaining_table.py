class ChainingTable:
    # Simple key/value holder
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        if capacity < 1:
            capacity = 1
        # Each bucket is a Python list of Records
        self._buckets = [[] for _ in range(capacity)]
        self._cap = capacity
        self._size = 0

    def _index(self, key):
        return hash(key) % self._cap

    def _grow(self):
        new_cap = self._cap * 2
        new_buckets = [[] for _ in range(new_cap)]
        for bucket in self._buckets:
            for rec in bucket:
                idx = hash(rec.key) % new_cap
                new_buckets[idx].append(rec)
        self._buckets = new_buckets
        self._cap = new_cap

    def insert(self, key, value):
        # grow if adding one would push load factor over 1.0
        if (self._size + 1) / self._cap > 1.0:
            self._grow()
        idx = self._index(key)
        bucket = self._buckets[idx]
        for rec in bucket:
            if rec.key == key:
                return False
        bucket.append(ChainingTable.Record(key, value))
        self._size += 1
        return True

    def modify(self, key, value):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for rec in bucket:
            if rec.key == key:
                rec.value = value
                return True
        return False

    def remove(self, key):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for i, rec in enumerate(bucket):
            if rec.key == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def search(self, key):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for rec in bucket:
            if rec.key == key:
                return rec.value
        return None

    def capacity(self):
        return self._cap

    def __len__(self):
        return self._size


# Simple demo / main so running this file shows the table working
def _demo():
    print("Demo: ChainingTable")
    t = ChainingTable(4)
    print("Initial capacity:", t.capacity())
    print("Initial length:", len(t))

    # Insert a few items
    print("Inserting a, b, c, d ...")
    for k, v in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
        print(" insert", k, "->", v, t.insert(k, v))
    print("Length after inserts:", len(t))

    # Duplicate insert should fail
    print("Trying duplicate key 'b':", t.insert("b", 999))

    # Search
    print("Search 'c':", t.search("c"))
    print("Search missing 'zzz':", t.search("zzz"))

    # Modify
    print("Modify 'c' to 30:", t.modify("c", 30))
    print("Search 'c' after modify:", t.search("c"))

    # Remove
    print("Remove 'b':", t.remove("b"))
    print("Remove missing 'b' again:", t.remove("b"))
    print("Length after removals:", len(t))

    # Trigger growth (load factor > 1.0)
    print("Capacity before growth:", t.capacity())
    # Insert enough new keys to force a resize
    i = 0
    while t.capacity() == 4:  # keep inserting until it grows
        key = f"x{i}"
        t.insert(key, i)
        i += 1
    print("Capacity after growth:", t.capacity())
    print("Final length:", len(t))

    print("Done.")


if __name__ == "__main__":
    _demo()
