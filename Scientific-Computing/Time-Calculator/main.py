def add_time(start, duration, day_of_week=None):
    pieces = start.split()
    day_time = pieces[1]
    hours, mins = map(int, pieces[0].split(":"))
    add_hours, add_mins = map(int, duration.split(":"))
    
    new_hours = hours + add_hours
    new_mins = mins + add_mins
   
    if new_mins >= 60:
        new_hours += 1
        new_mins -= 60
    if new_mins < 10:
        new_mins = f"0{new_mins}"
    else:
        new_mins = str(new_mins)

    if day_time == "PM":
        new_hours += 12
    
    new_time = convert_time(new_hours, new_mins)
    return new_time

def convert_time(hours, mins):
    if hours > 24:
        days = hours // 24
        remaining_hours = hours % 24
        if remaining_hours == 0:
            return f"{12}:{mins} AM {days_later(days)}"
        elif remaining_hours == 12:
            return f"{12}:{mins} PM {days_later(days)}"
        elif remaining_hours > 12:
            return f"{remaining_hours}:{mins} PM {days_later(days)}"
        else:
            return f"{remaining_hours}:{mins} AM {days_later(days)}"
    else:
        if hours == 0:
            return f"{12}:{mins} AM"
        elif hours == 12:
            return f"{12}:{mins} PM"
        elif hours > 12:
            return f"{hours - 12}:{mins} PM"
        else:
            return f"{hours}:{mins} AM"

def days_later(days):
    if days == 1:
        return "(next day)"
    else:
        return f"({days} days later)"





# print(add_time('3:30 PM', '2:12', 'Monday')) # '5:42 PM, Monday'.
# print(add_time('2:59 AM', '24:00', 'saturDay'))  # '2:59 AM, Sunday (next day)'.
# print(add_time('11:59 PM', '24:05', 'Wednesday'))  # '12:04 AM, Friday (2 days later)'.
# print(add_time('8:16 PM', '466:02', 'tuesday'))  # '6:18 AM, Monday (20 days later)'.

# done
print(add_time('3:30 PM', '2:12'))  # '5:42 PM'.
print(add_time('11:55 AM', '3:12'))  # '3:07 PM'.
print(add_time('2:59 AM', '24:00'))  # '2:59 AM (next day)'.
print(add_time('8:16 PM', '466:02'))  # '6:18 AM (20 days later)'.
print(add_time('11:59 PM', '24:05'))  # '12:04 AM (2 days later)'.