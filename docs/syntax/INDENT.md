# Indent

```python
### ####################################
### Indents
### ####################################
# Indented blocks are evaluated if the root evaluates to true
ind: #= 0
  1
    0
      3
# First ind: is evaluated. it is true
  then 1 is evaluated. it is true
  then 0 is evaluated. it is false.
    don't evaluate the indented 3
  return the last evaluated value, which was 0
# we can do the same with a variable
ind = #= 0
  1
    0
      3
ind2 = #= 3
  1
    2
      3
# ind: evaluates the function address
# ind= evaluates the variable address
# an example with returns
ind2 a, b, c:
  a
    b
      c
        @ c
      @ b
    @ a
  0
# This is functionally equivalent to the following python function
##. example
def ind2(a, b, c):
  if a:
    if b:
      if c:
        return c
      return b
    return a
  return 0
##.
# an example without returns
ind3 a, b, c:
  a
    b
      c
        .L c
      .L b
    .L a
  0
# This is functionally equivalent to the following python function
##. example
def ind2(a, b, c):
  if a:
    if b:
      if c:
        print(c)
      print(b)
    print(a)
  return 0
##.
### ####################################
### Indent equivalent And
### ####################################
# an indent is equivalent to the logical and operator
ind: #= 0
  1
    0
      3
# Equivalent
andind: 1 & 0 & 3 #= 0
# Example
ind2 = #= 3
  1
    2
      3
# Equivalent
# note that the 3 is evaluated last so it is returned
andind2 = 1 & 2 & 3 #= 3
# Example
ind2 a, b, c:
  a
    b
      c
        @ c
      @ b
    @ a
  0
# Equivalent
andind2 a, b, c:
  a &
    (b &
      (c &
        (@ c)
      @ b)
    @ a)
  0
and2ind2 a, b, c: a & (b & (c & (@ c) @ b) @ a) 0
```

```python

# this replaced the ' > ' with a new line and an indent
# every time ' > ' appears it is identical to being replaced by a new indented line
# same with ' < ' a new line de-indented and ' << ' double de-indent etc..
# the ' | ' is the or operator
# when it begins a line it evaluates the previous statement at the same level and only
# triggers if the statement is false.

# here is an implementation of the max function
max:a b > a>b > <- a < | > <- b


# if $b is true and $n - $k are greater than 0 return $s1 otherwise return $s2
select:b n k s1 s2 = b > n-k>0 > <- s1 << s2
  
b=1
n=4
k=3
s1="a"
s2="b"
v=b > n-k>0 > <- s1 << s2
v2=select(b n k s1 s2)
Print(v==v2) #= true
```

```python
# “(“ is identical to new line and indent
# “)” is identical to new line and un-indent
# @ is return
# func_name arg1 arg2: expressions

max a b:
  a > b
    @ a
  @ b
max a b:
  a > b ( @ a ) @ b
max a b: ( a > b ( @ a ) @ b )
max a b: a > b ( @ a ) @ b

printmax1: a b
  a > b
    .p “got max from first”
    .p a
  | a < b
    .p “got max from second”
    .p b
  |
    .p “no max”
    .p 1

# “,” is identical to new line with same indent

printmax: a b ( a > b ( .p “got max from first”, .p a ) | a < b ( .p “got max from second” , .p b ) | ( .p “no max” , .p 0 ) )

# note that the else / elif operator is identical to logical or, since we don't evaluate content after the first true value in an “or” statement.

# Extra space around a statement is equivalent to wrapping the statement in ()


printmax2: a b c d
  b > a  |  c > a  |  d > a
    .p max  max b c  max c d
  |  b = a  |  c = a  |  d = a
    .p ~
  |
    .p a
printmax2: a b c d ( b > a  |  c > a  |  d > a ( .p max  max b c  max c d ) | b = a  |  c = a  |  d = a ( .p ~ ) | ( .p a ) )
printmax3: a b c d
  b > a  |  c > a  |  d > a
    .p max
      max b c
      max c d
  | b = a  |  c = a  |  d = a
    .p ~
  |
    .p a
printmax3: a b c d (
  b > a  |  c > a  |  d > a (
    .p max (
      max b c ,
      max c d ) )
  | b = a  |  c = a  |  d = a (
    .p ~ )
  | (
    .p a ) )
printmax3: a b c d ( b > a  |  c > a  |  d > a ( .p max ( max b c , max c d ) ) | b = a  |  c = a  |  d = a ( .p ~ ) | ( .p a ) )
```
