  Part A Analysis

The analysis of four functions 
---

   Function 1

    Step 0: Code
```python
def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total
```

    Step 1: Establish variables and functions
Let `n` represent the input parameter `number`.  
Let `T(n)` represent the total number of operations required.

    Step 2: Count operations
```python
total = 0                  1
for i in range(number):    n iterations + 1 initialization + 1 comparison = n + 2
    x = i + 1              2 * n
    total += x * x         2 * n
return total               1
```

    Step 3: Mathematical Expression
T(n) = 1 + (n + 2) + 2n + 2n + 1

    Step 4: Simplify
T(n) = 5n + 4

    Step 5: Final Result
T(n) ∈ O(n)

---

   Function 2

    Step 0: Code
```python
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6
```

    Step 1: Establish variables and functions
Let `n` represent the input parameter `number`.  
Let `T(n)` represent the total number of operations required.

    Step 2: Count operations
```python
(number * (number + 1) * (2 * number + 1)) // 6     constant number of operations = 6
```

    Step 3: Mathematical Expression
T(n) = 6

    Step 4: Simplify
T(n) = O(1)

    Step 5: Final Result
T(n) ∈ O(1)

---

   Function 3

    Step 0: Code
```python
def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp
```

    Step 1: Establish variables and functions
Let `n` represent the length of the list.  
Let `T(n)` represent the total number of operations required.

    Step 2: Count operations
- Outer loop runs `n - 1` times.  
- Inner loop runs decreasingly: (n - 1) + (n - 2) + ... + 1 = n(n - 1)/2 times.  
- Inside inner loop operations are constant (≈ 4).

    Step 3: Mathematical Expression
T(n) = (n(n - 1))/2 * 4 = 2n² - 2n

    Step 4: Simplify
T(n) ∈ O(n²)

    Step 5: Final Result
T(n) ∈ O(n²)

---

   Function 4

    Step 0: Code
```python
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total
```

    Step 1: Establish variables and functions
Let `n` represent the input parameter `number`.  
Let `T(n)` represent the total number of operations required.

    Step 2: Count operations
```python
total = 1                          1
for i in range(1, number):         n - 1 iterations + 2
    total *= i + 1                 2 * (n - 1)
return total                       1
```

    Step 3: Mathematical Expression
T(n) = 1 + (n - 1 + 2) + 2(n - 1) + 1

 Step 4: Simplify
T(n) = 3n + 1

 Step 5: Final Result
T(n) ∈ O(n)

---

Test Results

Lab2 Function Performance
Running `test_lab2.py` on the implemented functions:

```
time for fib(39) = 1.6100000038932194e-05
time for sum_to_goal= 2.38940810000031
```

 Analysis of Results:
- Fibonacci(35): ~0.0000161 seconds - Very fast execution due to iterative O(n) approach
- Sum_to_goal: ~2.389 seconds - Slower execution due to O(n²) nested loop algorithm searching through large dataset


