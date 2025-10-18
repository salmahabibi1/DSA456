# DSA456 - Lab 4

**Team Members:**
- Salma

---

## Part A: Questions about the video

### 1. What sorting algorithm was the speaker trying to improve?

Quicksort - specifically, he was improving the small array sorting routine that quicksort delegates to when arrays get small (the insertion sort fallback).

### 2. At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?

Visual Studio uses a threshold of 32 elements.

### 3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?

GNU uses a threshold of 16 elements.

### 4. Regular insertion sort does a linear search backwards from end of array for correct spot to insert. According to the speaker, why does switching to a binary search not improve performance?

Binary search actually made things 13% *slower* despite reducing comparisons by 15%. The problem is branch prediction. Linear search has a ~90% success rate on comparisons (very predictable), while binary search extracts one bit of information per comparison - it's 50/50 whether it goes left or right. This makes the branch predictor powerless, and the CPU can't predict which way the code will jump.

### 5. Describe what is meant by branch prediction. (this may require further research)

Branch prediction is when the CPU tries to guess which way a conditional branch (like an if statement) will go before it actually evaluates it. When predictions are accurate, the code runs faster. When they're wrong, there's a performance penalty. Linear search has predictable patterns (mostly failures until success), but binary search is unpredictable (50/50 at each step).

### 6. What is meant by the term informational entropy? (this may require further research)

Informational entropy measures how much new information each comparison reveals. Binary search has high entropy - each comparison extracts exactly one bit of information and reveals the maximum possible. Linear search has low entropy - most comparisons fail predictably until you find what you're looking for. High entropy means more information gained but worse branch prediction.

### 7. Speaker suggests the following algorithm: make_heap() and unguarded_insertion_sort(). He suggests that by doing make_heap() first, you can do something called unguarded_insertion_sort(). Please explain what unguarded_insertion_sort() is and why it is faster than regular insertion sort. How does performing make_heap() allow you to do this?

Unguarded insertion sort skips bounds checking during the backward search. Normally, you need to check "am I at the beginning of the array?" to avoid going out of bounds. But if you first do make_heap(), the smallest element is guaranteed to be at position 0. Since nothing can be smaller than the smallest element, you'll always hit it before going out of bounds - no bounds check needed. This saves one comparison per iteration. He also starts at position 3 (begin+3) instead of 0 because the first two elements are already sorted (first is smallest, second is larger than first).

### 8. The speaker talks about incorporating your conditionals into your arithmetic. What does this mean? Provide an example from the video and explain how the conditional is avoided.

Instead of using if statements, you integrate the condition into the calculation itself.

**Example:** `auto right = first + 1 + (size & 1);`

This positions the algorithm in the middle of the array differently based on whether the size is odd or even. `(size & 1)` equals 1 for odd, 0 for even - no if statement needed. The conditional becomes a number (0 or 1) that flows through the arithmetic. This avoids a compare-with-jump (just does a compare without jumping), which is much faster.

### 9. The speaker talks about a bug in gnu's implementation. Describe the circumstances of this bug.

With rotated data (where the smallest element is at the end of the array - a plausible real-world scenario), GNU's nth_element function hits worst-case behavior and becomes quadratic. The quicksort implementation falls back to heapsort, making it unmeasurable. The speaker calls this a bug because it's a realistic data pattern, not some artificial edge case.

### 10. The speaker shows several graphs about what happens as the threshold increases using his new algorithm. The metric of comparison is increased, and the metric of moves is increased, but time drops... What metric does the author think is missing? Describe the missing metric he speaks about in the video. What is the metric measuring?

The missing metric is **D(n)** - the average distance between two consecutive array accesses. This measures cache locality without being cache-specific. The speaker creates a composite metric:

**Cost = Comparisons + Moves + (K × Distance)**

Where K is about 1/500. This composite metric actually predicts runtime, unlike comparisons or moves alone. It captures how the algorithm jumps around in memory, which affects cache performance.

### 11. What does the speaker mean by fast code is left-leaning?

Code that stays to the left side of the page - minimal indentation, few nested ifs and loops. Simple, straightforward code without deep nesting runs faster. The speaker jokes about this with a "Communist" reference, but his point is serious: complexity kills performance. He even mentions Linux kernel's 8-character tabs and 80-character line limits prevent writing slow code.

### 12. What does the speaker mean by not mixing hot and cold code?

Hot code is executed frequently; cold code rarely runs. Keep them separated. Hot code should be together so the CPU can optimize it. Cold code (error handling, edge cases, fix-ups) should be elsewhere. The speaker says he breaks/returns early to get out of the hot path and handle the cold stuff separately. Mixing them means the hot path carries baggage it doesn't need.

---

## Part B: Reflection

### 1. What did you/your team find most challenging to understand in the video?

The most challenging concept was understanding why doing *more* work could make code faster. It goes against everything we're taught - that efficiency means doing less. The idea that making a heap and then completely ignoring its structure by running insertion sort over it would somehow be 9% faster is counterintuitive. Also, the composite metric combining comparisons, moves, and distance was hard to grasp at first - why those three specifically, and how they interact to predict actual runtime instead of just theoretical complexity.

### 2. What is the most surprising thing you learned that you did not know before?

The most shocking thing was that binary search made the code *slower* even though it reduced comparisons by 15%. I always thought fewer comparisons = faster code. Learning that branch prediction matters more than the number of operations completely changed my understanding. It's wild that the CPU's ability to guess which way an if statement will go is more important than doing less work. The fact that all our algorithm textbooks focus on minimizing comparisons, yet that's not actually what makes code fast in practice, was eye-opening.

### 3. Has the video given you ideas on how you can write better/faster code? If yes, explain what you plan to change when writing code in the future. If not, explain why not.

Yes. I'll write simpler, "left-leaning" code with minimal nesting, use arithmetic instead of conditionals where possible, separate hot/cold code paths with early returns, prioritize branch prediction over operation count, and actually measure performance instead of assuming. Most importantly, I'll test with realistic data patterns, not just theoretical worst-cases.

---

## References

- [High Performance Computing Guide - Algorithmica](https://en.algorithmica.org/hpc/)
- [Sorting Algorithms: Speed Is Found In The Minds of People - Andrei Alexandrescu - CppCon 2019](https://www.youtube.com/watch?v=FJJTYQYB1JQ)

- [High Performance Computing Guide - Algorithmica](https://en.algorithmica.org/hpc/)
- [Sorting Algorithms: Speed Is Found In The Minds of People - Andrei Alexandrescu - CppCon 2019](https://www.youtube.com/watch?v=FJJTYQYB1JQ)
