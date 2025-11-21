# Part A   Analysis of SortedTable

Below I analyzed each required member function of `SortedTable` in terms of the number of Records currently stored, n, and then suggested concrete improvements. I’m focusing on the actual behavior of the provided code, not the ideal behavior of a “well-implemented” sorted array.

---

## What I’m analyzing (quick recap)
- insert(key, value)
- modify(key, value)
- remove(key)
- search(key)
- capacity()
- __len__()

Notation: n = number of stored records (not capacity). 
---

## __len__(self)
- What it does: Counts how many non-None entries exist by scanning the whole internal list.
- Cost details: It loops through every slot in the underlying list. The length of that list is the current capacity C. If C is much larger than n, this still scans all C entries.
- Time complexity (in terms of n): O(n) if we assume C = Θ(n) due to resizing. More accurately it’s O(C), which can be worse than O(n) if C >> n.
- Note: This is surprisingly expensive for something that should be O(1). It also harms other functions when they call len(self) inside loops.

## search(self, key)
- What it does: Linear scan from the start until it finds the key or reaches size.
- Internals: It first calls `size = len(self)` (which itself is O(n)), then scans up to n records linearly.
- Time complexity: O(n) overall (O(n) to compute len + O(n) scan ⇒ still O(n)). There’s no binary search even though the table is sorted after inserts.

## insert(self, key, value)
- What it does: 
  1) Checks for duplicates with `self.search(key)`.
  2) If full, doubles capacity and copies elements.
  3) Puts the new record at index `len(self)`.
  4) Sorts the entire array using a nested bubble-sort style pass.
- Cost drivers:
  - Duplicate check: `search` is O(n).
  - Potential grow: copy C items (amortized O(1) per insert overall, but O(C) when it happens).
  - `len(self)`: O(n) to compute.
  - The big one: the nested loops re-sort everything using bubble sort ⇒ O(n^2) per insert in the steady state.
- Time complexity: O(n^2) per insert (dominated by the full re-sort), even when not growing. This is the main performance problem.

## modify(self, key, value)
- What it does: Linear scan to find the key; then updates the value in-place.
- Important detail: The loop condition uses `while (i < len(self) and …)`. That calls `len(self)` every iteration, and each call is O(n), making the loop far more expensive than it looks.
- Time complexity: O(n^2) in the worst case (n calls to O(n) `len(self)`), though with a tiny refactor it’d be O(n).

## remove(self, key)
- What it does: 
  1) Gets `size = len(self)` (O(n)).
  2) Linear scan to find the index (O(n)).
  3) Shifts all following records left by one (O(n)).
- Time complexity: O(n). The upfront `len(self)` adds O(n) but total remains O(n).

## capacity(self)
- What it does: Returns `self.cap`.
- Time complexity: O(1).

---

## What’s inefficient (quick bullets)
- Re-sorting the whole array on every insert with bubble sort ⇒ O(n^2) inserts.
- `len(self)` is O(n) and is sometimes called inside loops, turning linear scans into quadratic work.
- Linear search in a sorted table instead of binary search.

---

## How I’d make it more efficient (and still use a sorted array)
1) Track size explicitly
   - Keep `self.size` and update it on insert/remove. Then implement `__len__` to return `self.size` in O(1).
   - This instantly fixes the accidental O(n^2) in `modify` (no more O(n) `len(self)` calls per loop iteration).

2) Binary search anywhere we locate by key
   - `search`, `modify`, and `remove` should use binary search (O(log n)) to find the index.
   - For `remove`, once we know the index, shifting is still O(n) but we avoid the O(n) search cost and any hidden O(n) `len` calls.

3) Insert by binary-searching the correct spot, then shifting the suffix
   - Instead of appending then bubble-sorting the entire list, do: 
     - Binary search to find the insertion index in O(log n).
     - Shift the tail right by one and place the new record in O(n).
   - Overall `insert` becomes O(n) (not O(n^2)).

4) Minor cleanups
   - Avoid calling `len(self)` repeatedly inside loops; compute size once.
   - When growing, copy only the n actual elements (not necessary for complexity, but cleaner). Doubling capacity keeps amortized insert O(1) for capacity growth overhead.

---

## Final complexity summary (after fixes)
- With a sorted array + the fixes above:
  - search: O(log n)
  - insert: O(n) (binary search + shift one suffix)
  - modify: O(log n)
  - remove: O(n) (binary search + shift one suffix)
  - capacity: O(1)
  - __len__: O(1)

This keeps the sorted-array design but removes the pathological O(n^2) behavior, especially for inserts and the accidental quadratic cost in modify.
# DSA456
