# pytz is a library for working with timezones in Python. code example
# Print all supported timezones
import pytz
import datetime as dtime

print('this is the time zone suppot by pytz:\n', pytz.all_timezones, '\n')
# Retrieve the current date
date_current = dtime.datetime.now()
# Print the current data and time
print('current date and time:\n', date_current)

# Set the timezone to poland
currentTimeZone = pytz.timezone('Africa/Kigali')
print('\nThe time-zone is set to:\n', currentTimeZone)
# Read and print the current date and time of the time-zone
currentDateWithTimeZone = currentTimeZone.localize(date_current)
print('The date and time of this time-zone:\n', currentDateWithTimeZone)

# here we can the Set the target time-zone
newTimeZone = pytz.timezone('Asia/Karachi')
print('\nThe time-zone is set to:\n', newTimeZone)
# Read and print the current date and time of the newly defined time-zone
newDateWithTimezone = currentDateWithTimeZone.astimezone(newTimeZone)
print('The date and time of this time-zone:\n', newDateWithTimezone)