
start = int(input("Введіть початкове число (з): "))
end = int(input("Введіть кінцеве число (по): "))

print("Числа у діапазоні від", start, "до", end, ":")
for number in range(start, end + 1):
    print(number)
