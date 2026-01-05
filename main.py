from datetime import date

birth_year = int(input("Tug‘ilgan yilingiz: "))
today = date.today()
age = today.year - birth_year

print("Hozirgi sana:", today)
print("Sizning yoshingiz:", age)
