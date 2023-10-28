# Sequence

```python
# Sequence
# A sequence is a series of executions that evaluates to the last value
# Since 2 is evaluated after 7, the value 2 is returned
7 2 #= 2
( 7 2 ) #= 2
s1 = 7 2 4 #= 4
(1, 2) (3, 4) #= 3, 4
1
2
3 #= 3
aseq = #= 3
  1
  2
  3

# if a sequence contains a function pointer the return value of the previous
# expression will be passed in as an argument

add1 val: val + 1
add2 val: val + 2

res = 5 &add1 &add2 #= 8
# this is equivalent to
res = add2 (add1 5)

# return a function that increments a given value by n
add n:
  addv v:
    v + n
add n: addv v: v + n

res = 5 (add 1) (add 2) #= 8
res = (add 2) ( (add 1) 5 )
res = addv[n=2] (addv[n=1] 5)

```

```python
### ####################################
### Sequence
### ####################################
# (...) evaluates to the return value of the contained statmenets
zerotwo: ( 0 2 )
# The parens are implicit for functions
zerotwo: 0 2
# Since 2 is evaluated after 0, the value 2 is returned
.zerotwo #= 2
# [...] is a list type
onetwothreefour: [1, 2] [3, 4]
.onetwothreefour #= [3, 4]
onetwothreefour2: [1, 2], [3, 4]
.onetwothreefour #= [ [1, 2], [3, 4] ]
# [1, 2] [3, 4] is a sequence
  [1, 2], [3, 4] is a list
# zerothree are all the same list
zerothree: ( 0, 3 )
zerothree: 0, 3
zerothree: [ 0, 3 ]
.zerothree #= [ 0, 3 ]
# zerotwo are also the same sequence
zerotwo: ( 0 2 )
zerotwo: 0 2
.zerotwo #= 2
# sequences can span multiple lines
( 1 2 3 ) #= 3
1 2 3 #= 3
1
2
3 #= 3
aseq = ( 1 2 3 ) #= 3
aseq = 1 2 3 #= 3
aseq = #= 3
  1
  2
  3
```

```python

### ####################################
### Function sequence .
### ####################################
# This function logs a and b and returns .L b, which is the string b
l2 a, b: ( .L a ) ( .L b )
#= 
  .L
    X
    Y
  Y
.l2 "X", "Y"
# We might think that this is the same, but it is not.
l3 a, b: .L a .L b
#= 
  .L
    Y
    Y
  Y
.l3 "X", "Y"
# Adding implicit parentheses, this is equivalent to
l3 a, b: ( .L ( a ( .L b ) ) )
# This is because functions are greedy and will accept
  all arguments to the end of the line.
  So when executing it with "X". "Y"
    first ( .L b ) logs "Y" and evaluates to ( "Y" )
    second ( a ( "Y" ) ) evaluates to ( "X" "Y" )
      which evaluates to ( "Y" )
    third ( .L ( "Y" ) ) logs "Y" and evaluates to ( "Y" )
    then the function returns "Y"
# The "." character ends the line for function arguments.
l4 a, b: ( .L a ) ( .L b )
# Is equivalent to.
l4 a, b: .L a. .L b
# The . only applies to the preceding function
l5 a, b: .L .L a. .L b
# Equivalent to
l5 a, b: .L ( .L a. .L b )
#= 
  .L
    X
    Y
    Y
  Y
.l5 "X" "Y"
```

```python
# multiple values in sequence are a tuple, e.g, 1 -2 = 1 -2 evaluates to 1 (true).

# function arguments are provided as a tuple which can be wrapped in parens, or indented on the next line.
# the following are identical
res = myfun 1 2
res = myfun 1 , 2
res = myfun ( 1 2 )
res = myfun ( 1 , 2 )
res = myfun
  1 2
res = myfun
  1 , 2
res = myfun
  ( 1 , 2 )
res =
  myfun
    1
    2
res =
  myfun
    1 ,
    2
```

```python
# more examples
add: a b ( < a + b )
subtract: a b ( < a - b )
res = #= 7
  add
    add
      1
      3
    subtract
      5
      2
res = ( #= 7
  add (
    add (
      1 ,
      3 ) ,
    subtract (
      5 ,
      2 ) ) )
res = ( add ( add ( 1 , 3 ) , subtract ( 5 , 2 ) ) ) #= 7
res = add ( add ( 1 , 3 ) , subtract ( 5 , 2 ) ) #= 7
res = add ( add ( 1 3 ) , subtract ( 5 2 ) ) #= 7
res = add ( add 1 3 , subtract 5 2 ) #= 7
res = add
  add 1 3 , subtract 5 2 #= 7
res = add add 1 3 , subtract 5 2 #= 7

res = add add 1 3 subtract 5 2 #= 7
# v =  f   f  v v      f   v v
#      |   |  | |      |   | |
#      |   | (   )     |  (   )
#      |   +++++++     ++++++++
#      f      v           v
#      ++++++++++++++++++++++++
#                 v
# values next to each other are a tuple
# functions evaluate to values. (Tuples are values)
```
