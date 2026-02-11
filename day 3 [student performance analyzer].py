# Personalization Logic:
# The program checks the length of each student’s name.
# If the name length is even, 5 marks are added to the student’s score.
# If the name length is odd, the marks remain unchanged.
# This makes the result depend on each student’s individual name.
N = int(input("Enter number of students: "))

names = [""] * N
marks = [0] * N

for i in range(N):
    names[i] = str(input(f"Enter name of Student {i+1} :"))
    marks[i] = int(input(f"Enter mark of Student {i+1}:"))

valid_count = 0
fail_count = 0



for i in range(N):

    name = names[i]
    mark = marks[i]

    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")

    else:
        if len(name) % 2 == 0:
            mark = mark + 5
            if mark > 100:
                mark = 100

        valid_count = valid_count + 1

        if mark >= 90:
            print(mark, "→ Excellent")

        elif mark >= 75:
            print(mark, "→ Very Good")

        elif mark >= 60:
            print(mark, "→ Good")

        elif mark >= 40:
            print(mark, "→ Average")

        else:
            print(mark, "→ Fail")
            fail_count = fail_count + 1


print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)

