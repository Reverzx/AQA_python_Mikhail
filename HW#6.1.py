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
hours_t, minutes_t = time.split(':')
if int(hours_t) < 12:
    if int(hours_t) == 0:
        print(f"12:{minutes_t} a.m.")
    else:
        print(f"{int(hours_t)}:{minutes_t} a.m.")
elif int(hours_t) == 12:
    print(f"12:{minutes_t} p.m.")
else:
    print(f"{int(hours_t)-12}:{minutes_t} p.m.")
