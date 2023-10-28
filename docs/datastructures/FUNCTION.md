# Function

```python
### ####################################
### Functions
### ####################################
# Functions are greedy, a function will accept
  every item to the end of the line as it's argument
# This takes argument a and returns it
returnme a: a
# function calls start with '.'
.returnme "A" #= "A"
.returnme 1, 2, 3 #= 1 2 3
# ".L" logs
.L "hello world"
# func_name arg1 ...: expressions
log a: .L a
.log "hi" #= .L "hi"
# " " delimits sequential statements
log2 a: ( .L a ) ( .L a )
.log2 "hi" #= .L "hi\nhi"
# Functions only receive and return a single argument
```

```python
# Recall printmax
pm a, b: a > b & ( .L "A". .L a ) | a < b & ( .L "B". .L b ) | (.L "Z". .L 0)
#= 
  .L
    B
    2
    A
    4
    Z
    0
  [ "2", "4", "0" ]
pmres = (.pm 1, 2) (.pm 4, 3) (.pm 5, 5) 
pmres #= [ "2", "4", "0" ]
# This performs the log operations
  and evaluates to [ "2", "4", "0" ]
  This is based on the last evaluated statement for each function.
  the .L statement in this instance
# Let's update this to both print the value and return the numerical value
pm2 a, b: a > b & ( .L a. a ) | a < b & ( .L b. b ) | ( .L "0". 0 )
#= 
  .L
    2
    4
    0
  [ 2, 4, 5 ]
pm2res = (.pm2 1, 2), (.pm2 4, 3), (.pm2 5, 5)
pm2res #= [ 2, 4, 5 ]
# this is the same as
pm2res = [ .pm2 1, 2; .pm2 4, 3; .pm2 5, 5 ]
# This is different from
#= 
  .L
    2
    4
    0
  5
pm2res2 = .pm2 1, 2. .pm2 4, 3. .pm2 5, 5
pm2res2 #= 5
# This is the same as
pm2res2 = (.pm2 1, 2) (.pm2 4, 3) (.pm2 5, 5)
# Let's use .T INT to convert to int
ti a: .T INT a
pm3 a b: a > b & ( .ti .L a. ) | a < b & ( .ti .L b. ) | ( .ti .L "0". )

# This functions similar to the above
#= 
  .L
    2
    4
    0
  [ 2, 4, 5 ]
pm3res = (.pm2 1 2) (.pm2 4 3) (.pm2 5 5)
pm3res #= [ 2, 4, 5 ]
# This will return an error if non integer values are provided however
.pm2 "a" "b" #= .L "b", "b"
.pm3 "a" "b" #= .L "b", ERR
# Functions arguments can be set by indented values
.L ( "A", "B", "C" ) #= .L C
# This is the same as
.L
  "A"
  "B"
  "C"
# this only Logs "C" since that is what was returned
.L [ "A", "B", "C" ] #= .L [ A, B, C ]
.L "A" "B" "C" #= .L [ A, B, C ]
.L #= .L [ A, B, C ]
  "A",
  "B",
  "C" 
```

```python
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
  .add
    .add
      1
      3
    .subtract
      5
      2
res = ( #= 7
  .add (
    .add (
      1 ,
      3 ) ,
    .subtract (
      5 ,
      2 ) ) )
res = ( .add ( .add ( 1 , 3 ) , .subtract ( 5 , 2 ) ) ) #= 7
res = .add ( .add ( 1 , 3 ) , .subtract ( 5 , 2 ) ) #= 7
res = .add ( .add ( 1 3 ) , .subtract ( 5 2 ) ) #= 7
res = .add ( .add 1 3 , .subtract 5 2 ) #= 7
res = .add
  .add 1 3 , .subtract 5 2 #= 7
res = .add #= 7
  .add 1 3 
  .subtract 5 2 

get1: < 1
mul1: a ( < a * 2 )
res = add get1 subtract 5 2 #= 4

res = get1 2 #= 1 2
res = get1 mul1b get1 #


printmax4 a b c d:
  .L max
    max
      a b
    max
      c d

printmax4 a b c d: @ max max a b max c d

printmax5 a b c d:
  .L max
    a max
      b max
        c d

printmax5 a b c d: @ max a max b max c d

printallsamebool a b c:
  a & b & c
    .L 1
  | a | b | c
    .L ~
  |
    .L 0
  
printallsamebool a b c: a & b & c @ 1 | a | b | c @ ~ | @ 0

getallsamebool a b c:
  a & b & c
    < 1
  a | b | c
    < ~
  < 0

getallsamebool a b c: a & b & c ( < 1 ) a | b | c ( < ~ ) < 0

isallsamebool a b c:
  < a & b & c  |  !  a | b | c
isallsamebool a b c: <  a & b & c  |  !  a | b | c
isallsamebool a b c: < a&b&c | ! a|b|c

isallsamebool2 a b c:
  all := a & b & c
    < all
  | any := ! a | b | c
    < any
isallsamebool2 a b c: all := a & b & c < all | any := ! a | b | c < any
isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0


isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#    |
# new letters followed by space = function declaration

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                |
# Letters before : = arguments

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                     |
# old letters = var reference

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                       |
# & is the logical and operator

example a b c: a ( < a ) b ( < b ) c ( < c )
v1 = example 5 0 10 #= 5
v2 = example 0 10 5 #= 10
v3 = example -1 0 -2 #= ~
v4 = -3
```

```python
# :do-stuff function declaration
d:a n = #:array:number
  # indent
  v=n+1 #:value
  # iterate over $a
  a:i:x #:index:item
    # indent
    sq=x*x #:x-squared set $sq to $x times $x
    # add $x and $n to $s
    #:running-sum declare $s initialize to default of implied type
    s+sq+n
    # if $s is greater than $v return $i
    s>v
      # indent
      # return $i
      <- i
    # else add 1 to $v
    |
      # indent
      v+1
  # iterate over $a again, but no index. No reusing variables
  a:j #:item we can reuse annotations
    # indent
    # call the print function with $j
    print(j)
  # if we have reached the end
  # return $s and $i
  # last statement is returned
  s i

# again without comments
d:a n =
  v=n+1
  a:i:x
    sq=x*x
    s+sq+n
    s>v
      <- i
    |
      v+1
  a:j
    Print(j)
  s i

# again inline
d:a n = > v=n+1 ; a:i:x > sq=x*x ; s+sq+n ; s>v > <- i < | > v+1 << a:j > Print(j) < s i

# as you can see, spaces are important!
# we can also break it up like this :

d:a n = > v=n+1 ; a:i:x > sq=x*x ; s+sq+n ; s>v
  <- i < | > v+1 << a:j > Print(j) < s i
```

```python
get1: < 1
mul1: a ( < a * 2 )
res = add get1 subtract 5 2 #= 4

res = get1 2 #= 1 2
res = get1 mul1b get1 #


printmax4 a b c d:
  .p max
    max
      a b
    max
      c d

printmax4 a b c d: @ max max a b max c d

printmax5 a b c d:
  .p max
    a max
      b max
        c d

printmax5 a b c d: @ max a max b max c d

printallsamebool a b c:
  a & b & c
    .p 1
  | a | b | c
    .p ~
  |
    .p 0
  
printallsamebool a b c: a & b & c @ 1 | a | b | c @ ~ | @ 0

getallsamebool a b c:
  a & b & c
    < 1
  a | b | c
    < ~
  < 0

getallsamebool a b c: a & b & c ( < 1 ) a | b | c ( < ~ ) < 0

isallsamebool a b c:
  < a & b & c  |  !  a | b | c
isallsamebool a b c: <  a & b & c  |  !  a | b | c
isallsamebool a b c: < a&b&c | ! a|b|c

isallsamebool2 a b c:
  all := a & b & c
    < all
  | any := ! a | b | c
    < any
isallsamebool2 a b c: all := a & b & c < all | any := ! a | b | c < any
isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0


isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#    |
# new letters followed by space = function declaration

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                |
# Letters before : = arguments

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                     |
# old letters = var reference

isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                       |
# & is the logical and operator


example a b c: a ( < a ) b ( < b ) c ( < c )
v1 = example 5 0 10 #= 5
v2 = example 0 10 5 #= 10
v3 = example -1 0 -2 #= ~
v4 = -3
```
