print("\033c")

print("enter marks obtained in 4 subjects: ")

math = int(input("mathematics: "))
eg = int(input("english: "))
bg = int(input("bangla: "))
sci = int(input("science: "))

sum = math + eg + bg + sci

print(f"sum = {sum}")

perc = (sum / 400) * 100

print(f"percentage mark: {perc}")