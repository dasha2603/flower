# Вариант 1
# Задание 6.1
s = "Hello, World!"
print(s[:1])
print(s[12:])
print(s[7:12])

# Задание 6.2
b = input("Введите строку: ")
if len(b) % 2 == 0:
    print(b.upper())
else:
    print(b.lower())

# Задание 6.3
c = input("Введите строку: ")
_lower = 'aeiou'
_upper = 'AEIOU'
count_lower = 0
count_upper = 0
for char in c:
    if char in _lower:
        count_lower += 1
    elif char in _upper:
        count_upper += 1

print(f"Строчные гласные: {count_lower}")
print(f"Заглавные гласные: {count_upper}")

# Задание 6.4
d = input("Введите строку: ")
result = ""
for i in range(len(d)):
    if i == 0 or d[i] != d[i-1]:
        result += d[i]

print("Резултат после удаления: ", result)


# Задание 6.5
word1 = input("Введите слово 1: ").lower()
word2 = input("Введите слово 2: ").lower()
if len(word1) != len(word2):
    print(False)
else:
    count1 = {}
    count2 = {}

    for char in word1:
        count1[char] = count1.get(char, 0) + 1

    for char in word2:
        count2[char] = count2.get(char, 0) + 1

    if count1[char] == count2[char]:
        print(True)
    else:
        print(False)




