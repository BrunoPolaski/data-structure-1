numbers = []
biggest = 0
for i in range(0, 3):
    numbers.append(float(input("Digite o número: ")))
    if i == 0:
        biggest = numbers[i]
    else:
      if numbers[i] > biggest:
          biggest = numbers[i]
print("O maior número é", biggest)