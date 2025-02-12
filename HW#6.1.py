# Time
n = 808
hours, minutes = n // 60, n % 60
print(hours, minutes)
result = hours // 10 + hours % 10 + minutes // 10 + minutes % 10
print(result)

# Level Up
experience = 10
threshold = 15
reward = 5
if (experience + reward) >= threshold:
    print("true")
else:
    print("false")

# Time converter
time = '00:00'
hours, minutes = time.split(':')
if int(hours) < 12:
    if int(hours) == 0:
        print(f"12:{minutes} a.m.")
    else:
        print(f"{int(hours)}:{minutes} a.m.")
elif int(hours) == 12:
    print(f"12:{minutes} p.m.")
else:
    print(f"{int(hours)-12}:{minutes} p.m.")