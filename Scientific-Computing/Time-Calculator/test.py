var_1 = "200:25"
hours, mins = map(int, var_1.split(":"))
days = hours // 24
remianing_hours = 200 % 24

print(days)
print(remianing_hours)