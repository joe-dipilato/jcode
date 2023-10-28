# List

```python
# (...) evaluates to the return value of the contained statmenets

# List / tuple
# A list is a comma separated series of values
1, 2, 3 #= 1, 2, 3
( 1, 2, 3 ) #= 1, 2, 3
a1 = 1, 2, 3 #= 1, 2, 3
v1, v2, v3 = a1 #= 1, 2, 3
v4, v5, v6 = 4, 5, 6 #= 4, 5, 6
a2 = v4, v5, v6 #= 4, 5, 6
(1, 2), (3, 4) #= ((1, 2), (3, 4))
((1, 2), (3, 4)) #= ((1, 2), (3, 4))
1,
2,
3 #= 1, 2, 3
alist =
  1,
  2,
  3 #= 1, 2, 3
alist[0] #= 1
```

```python
### ####################################
### List
### ####################################
# A list is represented by a series of values
[ 1, 2, 3 ] #= [1, 2, 3]
a1 = 1, 2, 3 #= [1, 2, 3]
v1, v2, v3 = a1 #= [1, 2, 3]
v4, v5, v6 = 4 5 6 #= [4, 5, 6]
a2 = v4, v5, v6 #= [4, 5, 6]
# & is logical and operator
and a b: a & b
# since 3 was the last evaluated statmenet it is returned
.and 5, 3 #= 3
.and 3, 5 #= 5
.and 5, 0 #= 0
# Since we know 0 & 5 is 0 by the time we evaluate 'a' we
  don't have to evaluate 'b' and we return right
  after evaluating 'a' which is '0'. 'a' is returned
.and 0, 5 #= 0
# Lists can span multiple lines with the ',' key
[ 1, 2, 3 ] #= 1, 2, 3
1, 2, 3 #= 1, 2, 3
1,
2,
3 #= 1, 2, 3
alist = [ 1, 2, 3 ] 
alist = 1, 2, 3
alist =
  1,
  2,
  3
```

```python
### ####################################
### Function list ;
### ####################################
# To terminate the function and be part of a list
  use the ; character instead of .
  This is functionally equivalent to writing .,
l6 a, b: .L .L a; .L b
l6 a, b: .L ( .L a; .L b )
#= 
  .L
    X
    Y
    X, Y
  X, Y
.l6 "X" "Y"
# mixing them
l7 a, b, c: .L .L a; .L b.. .L c
l7 a, b, c: ( .L .L a; .L b.. .L c )
l7 a, b, c: ( .L .L a; ( .L b ). ( .L c ) )
l7 a, b, c: ( .L ( .L a ), ( .L b ). ( .L c ) )
l7 a, b, c: ( ( .L ( .L a ), ( .L b ) ) ( .L c ) )
# ( ( .L ( .L "X" ), ( .L "Y" ) ) ( .L "Z" ) )
    first evaluate ( .L "X" )
      Log X, return "X"
  ( ( .L "X", ( .L "Y" ) ) ( .L "Z" ) )
    second evaluate ( .L "Y" )
      Log Y, return "Y"
  ( ( .L  "X", "Y" ) ( .L "Z" ) )
    third evaluate ( .L  "X", "Y" )
      Log [ X, Y ]. return [ "X", "Y" ]
  ( [ "X", "Y" ] ( .L "Z" ) )
    fourth evaluate ( .L "Z" )
      Log Z, return "Z"
  ( [ "X", "Y" ] "Z" )
    fifth evaluate ( [ "X", "Y" ] "Z" )
      return "Z"
#= 
  .L
    X
    Y
    X, Y
    Z
  Z
.l7 "X", "Y", "Z"
```

```python
a = 5
v1 = a @ 1
v1 = a ( @ 1 )
# Is v1 a tuple of ( 5 , 1 )?
# Is v1 the evaluation of the body of a? #= 1 ?
# in order to disambiguate, tuples always have a comma between terms…?
```
