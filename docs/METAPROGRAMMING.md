# metaprogramming

```python
# every type supports indent evaluation
# on indent, the methods 'enter 'next 'exit are called
# the next result will be set to the @ variable

# 'exit will be called after an error signal is returned from 'next

# the $ is the self attribute. when $ is used in a function
# the self argument is implied
counter:
  data: 1, 2, 3
  idx: -1
  iter: False
  'enter:
    $iter = True
  'next:
    $idx += 1
    data $idx # returns error signal when outofbounds
  'exit:
    $iter = False

c @ counter
  s += c
s #= 6

# a type containing a sequence of definitions can use the definitions as arguments
add1 val:
  val + 1
add1 3 #= 4
addn val:
  n: 1
  val + n
addn(3) 4 #= 7
addn(n=3) val=4 #= 7
addtoday[t=Day] val &t:
  n &t: 1
  val + n
addtoday[t=DayOfMonth](2) 3 #= 5
addday[t=Day]:
  n &t: 1
  'call val &t:
    val + $n
add5day = addday[t=DayOfYear](n=5) #= construct a type ref and return the ref
add5day 3 #= 8


# a signal is a special type that always returns immediately when evaluated.
# all functions return Result types.
# Results are of 2 kinds
  # Ok, Error

# a sequence of named attributes evaluates to a list??

# templating is done with []
# 'V is the value type. it has a val and sring attribute
'V[t='Any]:
  str &'Str
  val &t
'Error[t='V]:
  v &'V[t]
  'call:
    << $ # << returns until caught
'Ok[t='Any]:
  v &'V[t]

getitem list idx:
  list'has idx
    < list idx
  'Signal "out of bounds"

# 'Error "msg" constructs the type by overriding attributes positionally
# 'Error has attributes v and 'call
# 'Error "msg" constructs the type with v="msg"
# we can be more explicit
err='Error v="msg"
# the err is constructed and its reference is assigned to err.
# evaluation of an assignment returns the reference address of the variable
# calling err, invokes 'call, wich raises until caught
err
# evaluation of a reference address, runs the 'call function of that reference
# if we don't assign to err first, the error will also be called at the same time
'Error "msg"

# Result is one of these types
Result& 'Ok,'Error

# when we define the return type of a function, we only need
# to define the value type.
&Bool weekendissunday day&Weekday:
  ! Weekend'has day
    'Error "Not a weekend" day
  day != Weekend.Sunday
    < 'Error "Not Saturday", day
  True

# builtin values have 'enter 'next 'exit behavior also

checkdays:
  d @ Weekday.Saturday, Weekday.Sunday
    res = weekendissunday d
    'print res
  'print "-"
  d @ Weekday
    res = weekendissunday d
    'print res
  True
result = checkdays #= 'Signal "Not a weekend" Weekday.Monday
# Error: Not Sunday Weekday.Saturday
# True
# -
# True
sw result:
  'Error: result.v.str
  'Ok: result.v.val


```
