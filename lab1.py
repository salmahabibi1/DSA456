# Function 1: wins_rock_scissors_paper
def wins_rock_scissors_paper(player, opponent):
    # Manual lowercase conversion
    def to_lower(s):
        result = ""
        for c in s:
            if 'A' <= c <= 'Z':
                result += chr(ord(c) + 32)
            else:
                result += c
        return result

    player = to_lower(player)
    opponent = to_lower(opponent)

    if player == opponent:
        return False
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True
    return False


# Function 2: factorial
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


# Function 3: fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    i = 2
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    return b


# Function 4: sum_to_goal
def sum_to_goal(numbers, goal):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
            j += 1
        i += 1
    return 0


# UpCounter class
class UpCounter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def count(self):
        return self.value

    def update(self):
        self.value += self.step


# DownCounter class
class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step


# print("Select function to test:")
# print("1. wins_rock_scissors_paper")
# print("2. factorial")
# print("3. fibonacci")
# print("4. sum_to_goal")
# print("5. UpCounter")
# print("6. DownCounter")
# choice = input("Enter choice (1-6): ")

# if choice == "1":
#     player = input("Enter player's throw (rock/paper/scissors): ")
#     opponent = input("Enter opponent's throw (rock/paper/scissors): ")
#     result = wins_rock_scissors_paper(player, opponent)
#     print("Player wins:" if result else "Player does not win.")

# elif choice == "2":
#     n = int(input("Enter a non-negative integer for factorial: "))
#     print("Factorial:", factorial(n))

# elif choice == "3":
#     n = int(input("Enter a non-negative integer for fibonacci: "))
#     print("Fibonacci:", fibonacci(n))

# elif choice == "4":
#     raw_list = input("Enter numbers separated by spaces: ")
#     numbers = []
#     for part in raw_list.split():
#         numbers.append(int(part))
#     goal = int(input("Enter goal value: "))
#     print("Product of two numbers that sum to goal:", sum_to_goal(numbers, goal))

# elif choice == "5":
#     step = input("Enter step size for UpCounter (default 1): ")
#     step = int(step) if step else 1
#     counter = UpCounter(step)
#     print("Initial count:", counter.count())
#     while True:
#         cmd = input("Type 'u' to update, 'q' to quit: ")
#         if cmd == 'u':
#             counter.update()
#             print("Count:", counter.count())
#         elif cmd == 'q':
#             break

# elif choice == "6":
#     step = input("Enter step size for DownCounter (default 1): ")
#     step = int(step) if step else 1
#     counter = DownCounter(step)
#     print("Initial count:", counter.count())
#     while True:
#         cmd = input("Type 'u' to update, 'q' to quit: ")
#         if cmd == 'u':
#             counter.update()
#             print("Count:", counter.count())
#         elif cmd == 'q':
#             break

# else:
#     print("Invalid choice.")
