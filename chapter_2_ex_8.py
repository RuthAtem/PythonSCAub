# A program to give the time after setting alarm

intitial_time = float(input("Enter the current time in hours: "))
alarm_time = int(input("Enter the alarm time in hours: "))
time_after_alarm = intitial_time + alarm_time
print("The alarm will set off after ", round(time_after_alarm/24),"day(s) at", time_after_alarm % 24, "o'clock" )
