from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

day = datetime.now()
current_day = day.strftime("%A")

if current_time == '15:08':
    print("test complete")
    
