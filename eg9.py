"""Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time"""

from datetime import datetime     #importing datetime module

#defining start_time and end_time 
start_time = "11:00:00:PM"
end_time = "12:00:00:AM"

#datetime.strptime() converting string-time to date and matching the given time to specified format
start = datetime.strptime(start_time, "%H:%M:%S:%p")  
end = datetime.strptime(end_time, "%H:%M:%S:%p")

time = end - start     #it substract the start_time from end_time

#then can see differance between both time by hourse,minutes and seconds
print("Time difference is=")

hourse=time.total_seconds()/3600    #it calculates the hourse
print(hourse,"hourse")

minutes = time.total_seconds()/60   #it calculates the minutes
print(minutes, "minutes")

seconds=time.total_seconds()        #it calculates the seconds
print(seconds,"seconds")