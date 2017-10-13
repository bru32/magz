"""
My datetime utils
Bruce Wernick
10 October 2017 15:38:10
"""

__all__ = ['Now, Nowdict']

from datetime import datetime

'''
%a Weekday as locale's abbreviated name.
%A Weekday as locale's full name.
%w Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d Day of the month as a zero-padded decimal number.
%b Month as locale's abbreviated name.
%B Month as locale's full name.
%m Month as a zero-padded decimal number. 01, ..., 12
%y Year without century as a zero-padded decimal number. 00, ..., 99
%Y Year with century as a decimal number. 1970, 1988, 2001, 2013
%H Hour (24-hour clock) as a zero-padded decimal number. 00, ..., 23
%I Hour (12-hour clock) as a zero-padded decimal number. 01, ..., 12
%p Locale's equivalent of either AM or PM.
%M Minute as a zero-padded decimal number. 00, ..., 59
%S Second as a zero-padded decimal number. 00, ..., 59
%f Microsecond as a decimal number, zero-padded on the left. 000000, ..., 999999
%z UTC offset in the form +HHMM or -HHMM (empty if naive), +0000, -0400, +1030
%Z Time zone name (empty if naive), UTC, EST, CST
%j Day of the year as a zero-padded decimal number. 001, ..., 366
%U Week number of the year (Sunday is the first) as a zero padded decimal number.
%W Week number of the year (Monday is first) as a decimal number.
%c Locale's appropriate date and time representation.
%x Locale's appropriate date representation.
%X Locale's appropriate time representation.
%% A literal '%' character.
'''

class Now(object):
  def __new__(*args):
    c=datetime.now()
    return {"day":c.day,"month":c.month,"year":c.year,"hour":c.hour,"min":c.minute,"sec":c.second}

def Nowdict():
  c=datetime.now()
  return dict(day=c.day,month=c.month,year=c.year,hour=c.hour,min=c.minute,sec=c.second)


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  # use class to get datetime dict
  print '{day} {month} {year} {hour}:{min}:{sec}'.format(**Now())

  # use function
  print '{day} {month} {year} {hour}:{min}:{sec}'.format(**Nowdict())


  # get the datetime
  dt = datetime.now()

  # format with strftime
  print dt.strftime('%d %B %Y %H:%M:%S')

  # use format str directly
  print '{:%d %B %Y %H:%M:%S}'.format(dt)
  print '{0.day}/{0.month}/{0.year}'.format(dt)
