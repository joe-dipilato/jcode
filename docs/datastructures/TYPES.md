# Types

```python
# : is define
# = is assign
# & is kind
# . is attribute
# @ is as
# ! is not
# < is return
# ' is meta programming attrib
# $ is self

# Basictypes: char, byte, uint16, uint32, int16, int32, ulong64, long64, float32, double64, bool.
# Types: u8, u16, u32, u64, s8, s16, s32, s64, f32, d64

#Types indicate the following:
  #Valid range
  #Size
  #Interpretation e.g. float is packed in a particular way, useful for assembly / conversion

years: 1979..9999
years: 1979,1980,9998,9999
years'first
years'last


# Year is kind 1979 to 9999
Year& 1979..9999
Year& years
# y is set to of kind Year 2000
y = &Year 2000
# Month is kind Jan is 1, Feb is 2, Dec is 12
Month&
  Jan: 1
  Feb: 2
  Dec: 12
Month& (Jan:1) (Feb:2) (Dec:12)
# m is set to of kind Month Month.Jan
m = &Month Month.Jan
# Day is kind 1 to u16.last
Day& 1..u16.last
# DayOfMonth is kind of kind Day 1 to 31
DayOfMonth& &Day 1..31
DayOfYear& &Day % 365
Weekday& Sunday:1, Monday:2, Saturday:7
# Weekend is kind of kind Weekday Sunday, Saturday
Weekend& &Weekday Weekday.Sunday, Weekday.Saturday
# Date is kind year of kind Year, month of kind Month, day..
Date&
  year &Year
  month &Month
  day &DayOfMonth
Date: year&Year, month&Month, day&dayOfMonth
# dt is set to of kind Date year is 1988, month is April, ... 
dt = &Date year=&Year 1988, month=Month.April, day=27
dt = &Date 1988 &Month Month.April 27
dt = &Date 1988 4 27
```

```python

&DayOfMonth dayofmonth m&Month:
  sw =
    Jan: 31
    Feb: 28
    Dec: 31
  sw m
# a switch is implemented by defining a dict
# a dict implements a function with 2 args
dict self key default=~:
  self'has key
    < self.(key)
  default
# so, sw m, returns sw.(m) or ~
&DayOfMonth dayofmonth m&Month:
  ((Jan: 31) (Feb: 28) (Dec: 31)) m
# this creates the dict and calls its funct with arg m
# ; is shorthand to separate items in a sequence
# by default function args are greedy, but they stop at ;
&DayOfMonth dayofmonth m&Month:
  Jan: 31; Feb: 28; Dec: 31;; m
&DayOfYear dayofyear d&Date:
  doy &DayOfYear # starts undefined
  m @ Month'first..d.month
    doy += dayofmonth m # += of undefined is just =
  doy # we return doy since the last statement was m'exit
&DayOfYear dayofyear d&Date:
  m @ Month.'first..d.month
    doy += dayofmonth m # we can implicitly define doy
  doy
# we can declare the return variable in the function signature
# this implicitly returns doy
# this is a function that returns doy as kind DayOfYear
# function named dayofyear with argument d of kind Date
doy @ &DayOfYear dayofyear d &Date:
  # with m as the range month first to the month attribute of d
  m @ Month'first..d.month
    # increment day with the result of function dayofmonth with arg m
    doy += dayofmonth m
  # doy will be implicitly returned


```
