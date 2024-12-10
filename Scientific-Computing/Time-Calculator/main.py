def add_time(start, duration, day_of_week=None):
    # Split the start time into hours, minutes, and AM/PM
    pieces = start.split()
    day_time = pieces[1]
    hours, mins = map(int, pieces[0].split(":"))
    add_hours, add_mins = map(int, duration.split(":"))
    
    # Add the duration to the current hours and minutes
    new_hours = hours + add_hours
    new_mins = mins + add_mins
   
    # Minutes overflow
    if new_mins >= 60:
        new_hours += 1
        new_mins -= 60
    if new_mins < 10:
        new_mins = f"0{new_mins}"
    else:
        new_mins = str(new_mins)

    # Convert PM times to 24-hour format
    if day_time == "PM":
        new_hours += 12
    
    # Calculate the number of days passed
    total_days_later = new_hours // 24
    remaining_hours = new_hours % 24

    # Convert remaining_hours to 12-hour format
    if remaining_hours == 0:
        display_hours = 12
        display_period = "AM"
    elif remaining_hours == 12:
        display_hours = 12
        display_period = "PM"
    elif remaining_hours > 12:
        display_hours = remaining_hours - 12
        display_period = "PM"
    else:
        display_hours = remaining_hours
        display_period = "AM"

    
    new_time = f"{display_hours}:{new_mins} {display_period}"

    
    if day_of_week:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_of_week = day_of_week.capitalize()
        
        # Find the index of the current day
        start_day_index = days_of_week.index(day_of_week)
        
        # Calculate the new day of the week
        new_day_index = (start_day_index + total_days_later) % 7
        new_time += f", {days_of_week[new_day_index]}"

    
    if total_days_later == 1:
        new_time += " (next day)"
    elif total_days_later > 1:
        new_time += f" ({total_days_later} days later)"
    
    return new_time


def days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


print(add_time('3:30 PM', '2:12'))  # '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # '2:59 AM (next day)'
print(add_time('8:16 PM', '466:02'))  # '6:18 AM (20 days later)'
print(add_time('11:59 PM', '24:05'))  # '12:04 AM (2 days later)'


print(add_time('3:30 PM', '2:12', 'Monday'))  # '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # '2:59 AM, Sunday (next day)'
print(add_time('8:16 PM', '466:02', 'tuesday'))  # '6:18 AM, Monday (20 days later)'
