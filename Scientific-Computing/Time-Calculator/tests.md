add_time('3:30 PM', '2:12') # '5:42 PM'.

add_time('11:55 AM', '3:12') # '3:07 PM'.

add_time('2:59 AM', '24:00') # '2:59 AM (next day)'.

add_time('11:59 PM', '24:05') # '12:04 AM (2 days later)'.

add_time('8:16 PM', '466:02') # '6:18 AM (20 days later)'.

adding 0:00 to return the initial time.

add_time('3:30 PM', '2:12', 'Monday') # '5:42 PM, Monday'.

add_time('2:59 AM', '24:00', 'saturDay') # '2:59 AM, Sunday (next day)'.

add_time('11:59 PM', '24:05', 'Wednesday') # '12:04 AM, Friday (2 days later)'.

add_time('8:16 PM', '466:02', 'tuesday') # '6:18 AM, Monday (20 days later)'.

time to end with '(next day)' when it is the next day.

period to change from AM to PM at 12:00.
