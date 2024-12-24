n = input()

n = list(map(int, n.split()))

unique_numbers = []
seen = set()

for number in n:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(" ".join(map(str, unique_numbers)))