# Operators

```python
### ####################################
### Logical Operators
### ####################################
# Like functions, operators are greedy.
  Operators are treated the same as other functions
  except that the first argument is the value before the operator
and3ind2 a, b, c: a & b & c & @ c.. @ b.. @ a.. 0
# Note that this syntax is usually less readable

### ####################################
### OR operator
### ####################################
# "|" is the logical or operator.
  it evaluates to the first non-zero value or zero
or3 a, b, c: a | b | c
.or3 3, 2, 1 #= 3
.or3 0, 2, 1 #= 2
.or3 3, 0, 1 #= 3
.or3 3, 2, 0 #= 3
# an indent is identical to logical and of the indented values in parens
andor a, b, c: ( a & ( b | c ) )
andor a, b, c: a & ( b | c )
andor a, b, c: 
  a & ( b | c )
andor a, b, c: 
  a
    b | c
# here is how andor would evaluate
# 1 is good, so we check (2 | 3). 2 is good, so return it
.andor 1, 2, 3 #= 2
# a is 0 so return it
.andor 0, 2, 3 #= 0
# 1 is good, so check (2 | 0). 2 is good, so return it
.andor 1, 2, 0 #= 2
# 1 is good, so check (0 | 3). 0 is not good. return c
.andor 1, 0, 3 #= 3
# 1 is good, so check (0 | 0). 0 is not good. return c
# note that 1 0 3 and 1 0 0 both returned the last element
  and didn't need to evaluate it in the or statmenet
  This is the case with all or statements,
  we can always return the last element without evaluating it
.andor 1, 0, 0 #= 0
# to create a max function
max a, b:
  a > b
    @ a
  @ b
max a, b:
  ( ( a > b ) & ( @ a ) )
  ( @ b )
max a, b:
  ( ( a > b ) & ( @ a ) ) ( @ b )
max a, b: ( ( ( a > b ) & ( @ a ) ) ( @ b ) )
max a, b: ( ( a > b & ( @ a ) ) @ b )
max a, b: ( a > b & @ a ) @ b
# another example
myexample a, b:
  a > 5
    .L "A"
    .L a
    b > 5
      .L "B"
      .L b
    .L "C"
  .L "D"
myexample a, b: a > 5 & ( .L "A". .L a. b > 5 & ( .L "B". .L b ) .L "C" ) .L "D"
# "|" is also the else / elif operator
printmax a b:
  a > b
    .L "A"
    .L a
  | a < b
    .L "B"
    .L b
  |
    .L "Z"
    .L 0
printmax a b:
  a > b
    .L "A". .L a
  | a < b
    .L "B". .L b
  |
    .L "Z". .L 0
printmax a b:
  a > b & ( .L "A". .L a )
  | a < b & ( .L "B". .L b )
  | (.L "Z". .L 0)
# A line starting with an operator is a continuation of the previous statement 
printmax a b:
  a > b & ( .L "A". .L a ) | a < b & ( .L "B". .L b ) | (.L "Z". .L 0)
# note that the else / elif operator is identical to logical or, since we don't evaluate content after the first true value in an "or" statement.
printmax a b: a > b & ( .L "A". .L a ) | a < b & ( .L "B". .L b ) | (.L "Z". .L 0)
addex a b c:
  a
    b
  + b
    c
  + c
    a
addex a b c:
  a & ( b )
  + b & ( c )
  + c & ( a )
addex a b c: a & ( b ) + b & ( c ) + c & ( a )
# 1 & ( 2 ) + 2 & ( 3 ) + 3 & ( 1 )
  ( 2 )     + 2 & ( 3 ) + 3 & ( 1 )
  ( 2 )     + ( 3 )     + ( 1 )
.addex 1, 2, 3 #= 6
# 0 & ( 2 ) + 2 & ( 3 ) + 3 & ( 0 )
  ( 0 )     + 2 & ( 3 ) + 3 & ( 0 )
  ( 0 )     + ( 3 )     + ( 0 )
.addex 0, 2, 3 #= 3
# 1 & ( 0 ) + 0 & ( 3 ) + 3 & ( 1 )
  ( 0 )     + 0 & ( 3 ) + 3 & ( 1 )
  ( 0 )     + ( 0 )     + ( 1 )
.addex 1, 0, 3 #= 1
# 1 & ( 2 ) + 2 & ( 0 ) + 0 & ( 1 )
  ( 2 )     + 2 & ( 0 ) + 0 & ( 1 )
  ( 2 )     + ( 0 )     + ( 0 )
.addex 1, 2, 0 #= 2
```

```python
result = func arg arg
v1 = 1 & 0 #= 0
v2 = 1 | 0 #= 1
v3 = 1 ( @ 3 ) #= 3
v3b = 1
  @ 3 #= 3
v4 = 1 3 #= 1 3
v5 = 2 & 3 #= 1
v6 = | 3 #= 1
v7 = | -3 #= 0
```

```python
isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                       |
# & is the logical and operator
```
