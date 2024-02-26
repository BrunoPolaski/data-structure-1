income = float(input("Qual seu salário base?"))
extraHours = float(input("Quantas horas extras você fez?"))

def calcExtraHours(income, extraHours):
    baseHourIncome = income / 176
    return income + (extraHours * ((1 + 50/100) * baseHourIncome))

print("Seu salário final é", calcExtraHours(income, extraHours))