# Lab 3 - Recursive Functions Analysis

## Part A: Recursive Functions Implementation

All recursive functions have been implemented and tested successfully:
- `factorial(number)` - Recursive factorial calculation
- `linear_search(list, key)` - Recursive linear search
- `binary_search(list, key)` - Recursive binary search

## Part B: Analysis of Recursive Functions

### Function 1 Analysis
```python
def function1(value, number): 
    if (number == 0): 
        return 1 
    elif (number == 1): 
        return value 
    else: 
        return value * function1(value, number-1)
```

**Step 1: Establish variables and functions**
Let `n` represent the input parameter `number`.
Let `T(n)` represent the total number of operations required.

**Step 2: Identify base cases and recursive case**
- Base case 1: `number == 0` → returns 1 (2 operations: comparison + return)
- Base case 2: `number == 1` → returns value (2 operations: comparison + return)  
- Recursive case: `number > 1` → multiplication + recursive call

**Step 3: Set up recurrence relation**
```
T(0) = 2 (comparison + return)
T(1) = 4 (comparison for n==0, comparison for n==1, return)
T(n) = 4 + T(n-1) for n > 1 (comparisons + multiplication + recursive call)
```

**Step 4: Solve the recurrence**
```
T(n) = 4 + T(n-1)
     = 4 + (4 + T(n-2))
     = 4 + 4 + T(n-2)
     = 4k + T(n-k) where k = n-1
     = 4(n-1) + T(1)
     = 4(n-1) + 4
     = 4n
```

**Step 5: Final Result**
T(n) ∈ O(n)

**Note:** This function calculates value^number (exponentiation) using repeated multiplication.

---

### Function 2 Analysis
```python
def recursive_function2(mystring, a, b): 
    if(a >= b): 
        return True 
    else: 
        if(mystring[a] != mystring[b]): 
            return False 
        else: 
            return recursive_function2(mystring, a+1, b-1)

def function2(mystring): 
    return recursive_function2(mystring, 0, len(mystring)-1)
```

**Step 1: Establish variables and functions**
Let `n` represent the length of `mystring`.
Let `T₁(n)` represent operations for `function2`.
Let `T₂(a,b)` represent operations for `recursive_function2`.

**Step 2: Analysis of function2**
```python
def function2(mystring): 
    return recursive_function2(mystring, 0, len(mystring)-1)  # 3 operations
```
T₁(n) = 3 + T₂(0, n-1)

**Step 3: Analysis of recursive_function2**
- Base case: `a >= b` → return True (2 operations: comparison + return)
- Recursive case: 
  - String comparison: `mystring[a] != mystring[b]` (3 operations)
  - If different: return False (1 operation)
  - If same: recursive call with a+1, b-1 (3 operations + recursive call)

**Step 4: Set up recurrence relation for T₂**
Let k = b - a (the range being checked)
```
T₂(a,b) = 2 if a >= b (base case)
T₂(a,b) = 3 + 1 = 4 if mystring[a] != mystring[b] (early termination)
T₂(a,b) = 3 + 3 + T₂(a+1,b-1) = 6 + T₂(a+1,b-1) if mystring[a] == mystring[b]
```

**Step 5: Worst case analysis (all characters match)**
In worst case, we check all pairs: (0,n-1), (1,n-2), ..., until a >= b
Number of recursive calls: ⌊n/2⌋

```
T₂(0,n-1) = 6 + T₂(1,n-2)
          = 6 + 6 + T₂(2,n-3)
          = 6k + T₂(k,n-1-k) where we make k calls
          = 6⌊n/2⌋ + 2
          = 3n + 2 (approximately)
```

**Step 6: Combined analysis**
T(n) = T₁(n) = 3 + T₂(0,n-1) = 3 + 3n + 2 = 3n + 5

**Step 7: Final Result**
T(n) ∈ O(n)

**Note:** This function checks if a string is a palindrome.

---

### Function 3 Analysis (Optional Challenge)
```python
def function3(value, number): 
    if (number == 0): 
        return 1 
    elif (number == 1): 
        return value 
    else: 
        half = number // 2 
        result = function3(value, half) 
        if (number % 2 == 0): 
            return result * result 
        else: 
            return value * result * result
```

**Step 1: Establish variables and functions**
Let `n` represent the input parameter `number`.
Let `T(n)` represent the total number of operations required.

**Step 2: Identify cases**
- Base case 1: `number == 0` → return 1
- Base case 2: `number == 1` → return value
- Recursive case: `number > 1` → divide by 2 and recurse

**Step 3: Set up recurrence relation**
```
T(0) = 2
T(1) = 4  
T(n) = 7 + T(⌊n/2⌋) for n > 1
```
(7 operations: 2 comparisons + division + recursive call + modulo + multiplication)

**Step 4: Solve the recurrence**
This follows the pattern: T(n) = 7 + T(n/2)

Using the Master Theorem or substitution:
```
T(n) = 7 + T(n/2)
     = 7 + 7 + T(n/4)
     = 7k + T(n/2^k)
```
When n/2^k = 1, then k = log₂(n)
```
T(n) = 7·log₂(n) + T(1) = 7·log₂(n) + 4
```

**Step 5: Final Result**
T(n) ∈ O(log n)

**Note:** This function calculates value^number using fast exponentiation (divide and conquer).

---

## Part C: Reflection

### How to approach writing recursive functions:

1. **Identify the base case(s)**: Determine when the recursion should stop
   - What is the simplest input that can be solved directly?
   - Examples: empty list, n=0, single element

2. **Define the recursive case**: How to reduce the problem
   - Break down the problem into smaller subproblems
   - Ensure progress toward the base case
   - Examples: n-1, splitting list in half, moving indices

3. **Establish the relationship**: Connect current problem to subproblem
   - How does the solution to the smaller problem help solve the current one?
   - Examples: n * factorial(n-1), search in remaining elements

4. **Implement and test**: Write the function and verify with simple cases
   - Test base cases first
   - Test simple recursive cases
   - Verify correctness before optimization

### Process of analyzing recursive functions:

**Similarities to non-recursive analysis:**
- Count operations in each part of the function
- Identify dominant terms
- Express final complexity in Big O notation
- Consider best, worst, and average cases

**Differences from non-recursive analysis:**
- **Recurrence relations**: Instead of direct counting, set up equations
  - T(n) = f(n) + T(smaller problem)
- **Base cases**: Must analyze stopping conditions separately
- **Recursive depth**: Consider the number of recursive calls (stack depth)
- **Solving techniques**: Use substitution, Master Theorem, or recursion trees

**Key steps for recursive analysis:**
1. Identify base case complexity
2. Count operations in recursive case (excluding recursive calls)
3. Set up recurrence relation: T(n) = operations + T(reduced_input)
4. Solve recurrence using appropriate method
5. Verify the solution makes intuitive sense

**Common patterns:**
- Linear recursion (like factorial): T(n) = c + T(n-1) → O(n)
- Divide and conquer (like binary search): T(n) = c + T(n/2) → O(log n)
- Tree recursion (like Fibonacci): T(n) = T(n-1) + T(n-2) → O(2^n)
                                     
- Tree recursion (like Fibonacci): T(n) = T(n-1) + T(n-2) → O(2^n)
