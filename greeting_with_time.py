import time
current_time = int(time.strftime('%H'))
print(current_time)
if current_time < 12:
    print("Good Morning")
elif current_time < 18:
    print("Good Afternoon")
else:
    print("Good Night")
