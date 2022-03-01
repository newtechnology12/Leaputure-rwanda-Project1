#python-dateutil is a library for manipulating dates in a variety of formats.
#code example
from dateutil.relativedelta import *
import datetime as dtime

source_date = dtime.datetime.now()
month_next = source_date+ relativedelta(months=+1)
print('Date of next month:')
print(month_next)