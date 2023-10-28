# jcode

## [Docs](docs/README)

## Datastructures

### goals

remove the need for parens in most situations 
reduce number of chars
have a consistent and simple rule set that unifies language features
whitespace is meaningful
most ways to represent code is meaningful and not error

### startover

```python
# if a func takes an arg it takes the prev val in the sequence
# a fun with parens takes args from paren
fun=a,b:
  mod=x:x square add1
  am=a mod square + 1
  amm=square(mod(a)) + 1
  bm=b square mod + 1
  bmm=mod(square(b)) + 1
  am,amm,bm,bmm
af,aff,bf,bff=2,2 fun
# am=2 mod square + 1
  # ((2 mod) square) + 1
  # ((2 square add1) square) + 1
  # (((2 square) add1) square) + 1
  # (((2*2) add1) square) + 1
  # ((4+1) square) + 1
  # (5*5) + 1
  # 26
# amm=square(mod(2)) + 1
  # square(2 square add1) + 1
  # square((2 square) add1) + 1
  # square((2*2) add1) + 1
  # square(4 + 1) + 1
  # (5*5) + 1
  # 26
# bm=2 square mod + 1
  # ((2 square) mod) + 1
  # ((2 square) square add1) + 1
  # (((2 square) square) add1) + 1
  # (((2*2) square) add1) + 1
  # ((4*4) add1) + 1
  # (16+1) + 1
  # 18
# bmm=mod(square(2)) + 1 #= 18
# af,aff,bf,bff=2,2 fun #= 26,26,18,18
fun2=a:
  mod=x:x square add1
  a
  mod;2
  square;2
  + 1
am2=2,2 fun2 #= 26,26,5,3
# a = 2,2
# mod;2
  # (2,2:2,2 square add1);2 = 5,5,2
# square;2
  # (5,5,2:(5,5,2)*(5,5,2));2 = 25,25,4,2
# + 1 = 26,26,5,3

# evaluate left to right from every '.' ';' ':' to the start of a sequence
same=a:a
var=b:3
arr=9,9
fun=var c:4 same var;var. a,b:a+b;a,b:a+b+1;b:7,8;5,6,var,arr
# b:3 c:4 a:a b:3;b:3
# (b:3):4 a:a b:3 ...
        # 4:4 b:3 ...
            # 4:3 ...
            # 3   ...

# v map
6 b:4 #= 4
abc=c:3,b:4,b:5
abc.c #= 3
abc&c #= c:4
abc.b #= 4,5
abc&b #= b:3,5
# f map
6 a:a+1 #= 7
6 x:a+1 # a+1 #= 0+1 #= 1
fm = a:a+1;b:b+2
4 a:fm.a #= a:a+1 #= 5
4 fm&a #= a:a+1 #= 5
4 x:fm.a #= 1
a=3
fm.a #= a+1 #= 4
# n map
3,4 a,b:a #= 3
nab=a,b:4 ######## rule: : delimits left past ,
nab.(a,b) #= 4
b:4,a:3 a,b:a #= b:4
fab=b:4;a:3 ######### rule: ; delimits left past :
fab a,b:a #= b:4
&fab a,b:a #= 3
&(b:4,a:3) a,b:a #= 3
# nn map
xyz=x:v1;x,y:v2;x,y,z:v3;x,y:v4;y:v5;x:v6;y:v6
xyz.x #=     v1,v2,v3,v4,   v6
xyz.y #=        v2,v3,v4,v5,v6
xyz.(x,y) #=    v2,v3,v4,   v6
# nm map
nmm = a:x:x+v1;b:x:x+v2;c::v3 # rule: : doesn,t delimit left past :
v1=1
v2=2
v3=3
v1=1 nmm.a #= 2
v2=1 nmm.b #= 3
v3=nmm.c . #= 3 ######## ?
f1=nmm.a #= x:x+v1
f2=nmm.b #= x:x+v2
f3=nmm.c #= :v3
v1=4
v2=5
v3=6
1 f1 #= 5
1 f2 #= 6
f3 #= 6
nmm.a .x #= x+v1 #= 0+v1 = 4

```

# code

```python

# ast
# combine all items with the same indentation
pathlib,path 'import
treelib,tree 'import
# read the file
lines="file.jc" path .read .split("\n")
ident=str:
  # (cnt+=1 for ch in str if ch==" ")
  ch@str:ch==" ":cnt+=1
  cnt
# init list
node=tr=tree
# scan lines to add to the tree
pcnt=0
lines @ line
  icnt=ident line
  icnt>pcnt
    node=.spawn
  |icnt<pcnt
    node=.parent.next
  |
    node=.next
  node.val=line
  pcnt=icnt





```

### common

```python

# everything is an object

# const
years: 1979..9999
# type
Year& 1979..9999
# var
y = &Year 2000
# complex type (struct)
Date&
  year &Year
  month &Month
  day &DayOfMonth
# simple function
add1 val: val + 1
add v1, v2: v1 + v2
first v1,v2:v1
# passthrough function
same val: val
noop: ~
# function
doy @ &DayOfYear dayofyear d &Date:
  m @ Month'first..d.month
    doy += dayofmonth m
# list
# all items are a list
res = 1 # a list of item 1
res = 1,2,3 # a list of items 1,2,3
r1,r2,r3 = 4,5,6
# sequence inline
res = 4 5 6 #= 6
# ; combines everything to the left, to a single value. to the start of the sequence item
res = 1,2;3 # a list of 2 items (1,2),3
res = 1,2;3,(1;2,(3,4;5,6),7),4
res = (1,2),3,((1),2,((3,4),5,6),7),4
# ex
res = 1,2;3,4 # length 2. #= (1,2),(3,4)
# sequence multiline
# functions are greedy and take all args from innermost func to outermost
# all functions take 1 argument, a list of 0 or more items
## example
res = same 1 same 5 # sequence (same 1) (same 5)
res = same 1 5 # sequence (same 1) (5)
# sequences evaluate left to right, sequence returns the last value
res = same 5
res = 5 #= 5
## example
res = same noop same same 5
res = same noop same 5
res = same noop 5
res = same 5
res = 5 #= 5
# example
res = 1, noop, add (add 2, add1 5), add 7, add1 3
# functions are greedy, so we first pass args to each function
# right to left. inner to outer
res = 1, noop, add (add 2, 6), add 7, 4
res = 1, noop, add (8), 11
res = 1, noop, 19 #= 1, noop, 19
## example
res = same same 2, same 5, 3
res = same same 2, 5, 3
res = same 2, 5, 3
res = 2, 5, 3
## example
res = same same 2; same 5, 3
res = same 2; 5, 3
res = 2; 5, 3
res = 2, 5, 3
# evaluations happen right to left from every ; or .
res = same same 2. same 5, 3
res = same 2. 5, 3
res = 2 5, 3
res = 5, 3
# ex
res = same (same 2; same) 5
res = same (2;~) 5
res = same 5
res = 5
## example
res = same same 2 same 5 3
res = same same 2 same 3
res = same same 2 3
res = same same 3
res = same 3
res = 3
# ex
res = first 1,2;,3,4 # ; evaluates to the start of a sequence
res = 1;,3,4 #= 1,3,4
# ex
# first v1,v2:v1
res = first 1,2 # first 1,2:1 #= 1
# variable assignment is greedy, and will take as many as possible, right to left
# 1,2,3 is a single object.
# if len args != len input, the input will be assigned to the last arg
res = first 1,2,3 # first ~,(1,2,3):~ #= ~
res = first 1,(2,3) # first 1,(2,3):1 #= 1
res = first (1,2),3 # first (1,2),3:(1,2) #= 1,2
res = first 1,2;,3 #= first (1,2),3

# all lists are dicts
res = 4,5,6
# multiple keys map to the same value
res.a = 2
res.a = 3
res'keys #= ~,~,~,a
res'values #= 4,5,6,3
res'len #= 4
res'items #= (~,4),(~,5),(~,6),(a,3)
res 1 #= 5
#
res = a:1,b:2,c:3
res.b #= 2
res'keys #= a,b,c
res = a:1,a:2,c:(3,3),1,a:1
res.b = {4,5,6} # a map
res'keys #= a,c,~,b
res'values #= {1,2,1},(3,3),1,{4,5,6}
res'items #= ...
res'len #= 8
res 1 #= 2
res.c #= 3,3
res.a #= {1,2,1} # a mapping
res.a:3 # adds another item to the map {1,2,1,3}
res.b #= {4,5,6}
res.b'len #= 3
# definitions
a:1 # is a mapping
# a dict is just a list of mappings
var=2
var=3
var #= 3
map:2
map:3
map #= {2,3}
m @ map # prints 2 3
  'print m
# a map is just a list that duplicates keys


# everything is a list of maps
1 #= returns a ref to a list len 1 of map with key ~ len 1
1 # (~:1)
#how to distinguish between list of map maps and map of maps
v=a:1,a:2
# is this a list ((a:1),(a:2))
# or a map (a:(1,a:2))
# following thenright to left rule, we can conclude the later
v=a:1,(a:2)
v=a:(1,(a:2))
v=(a:(1,(a:2)))
# to fix this
v=a:1;,a:2
# we may expect this to returns a list of len 2 where both items have map of key a
# (a:{1},a:{2})
# however, since all lists are dicts, all elements with shared key are indexed with ther first instance
v#=(a:{1,2})
#the same can be achieved with
v=a:1 a:2#=(a:{1,2})
# since a:2 is evaluated last and it returns the ref to map key 'a'
#also
v=a:1; a:2 # the ; is unnecessary in this case, since the def doesnt take args
a:1#=a:{1}
a:2#=a:{1,2}
a:1#=a:{1,2,1}
a #returns a ref to list len 3 with a map with key a
c=1,2,3#=1,2,3
c #returns a ref to a list len 3 with a map with key ~
b=1#=1
b#returns a ref to a list len 1 with 1 int
va=a:1,a:2,a:1,3#=a:{1,2,1},3
va#returns a ref to a list
# we need to talk about namespacing now.
# we want to define a function
val1:1 # we see that this is a function named val1 that returns 1
# this is the exact same syntax of a map of key val1
# so functions are just maps with a namespace
add1 v:v+1 # this is a function definition add1 with arg v
#but this also looks like a sequence of 'add1' and map 'v:{v+1}'
# what we want is 'add1' to be the referenceto of the function that takes 1 arg
#what if we did this
add1=v:v+1 # add1 is the ref to map with key v #=v:{v+1}
#lets go back to a simpler func
ret2=~:2 #= ~:{2}
# shorthand
ret2=:2 #= ~:{2} or just :{2}
# ret2 returns the map of key ~
# we want to assign 2 to a variable
# we want :2 to return value 2 when it is called.
# recall however that value 2 is itself a map of key ~
2#=~:{2} and since this is precisely what ret2 is a reference of it is equivalent
var2=ret2 #=~:{2} = 2
# ok lets go back to add1=v:v+1
add1 # this is just a ref to list len 1 of map key v
# recall that lists are dicts, and dicts can get elements by key
add1.v #= v+1
val=v:1 # a function that takes arg v and returns 1
# this is also just a ref to list len 1 with map key v
val.v #= 1
val 9 #= 1
# when a list is called as a function with an arg, it returns the item at that index
v2=4,5,6
v2 1 #=~:5
m1=a:4,b:5,c:6 # err a:(4,b:(5,c:6))
m1 0 #= a:4
m2=a:4
m2 0 #= a:4
ret4=a:4 # want a func that takes arg a and returns 4
ret4 7#=4
```

### considerations


```python
# we have a problem. if ret4 is a list of len 1 and the arg is the index
# we cant call the function
# lists of len 1 are special. such that it behaves as the value at index 0.
# this is problematic since we may want to use lists of len 1 as a list
# therefore, not everything is a list. unless it has a comma.
# this means that we two datastructures  lists/dicts and values/maps
# and finally we have bits
# a dict contains 0 or more maps
# a map contains 1 or more dicts, maps, or bits.
7#=bits
1,7#=dict
a:7#=map
b=7
b 0 #=0 (sequence) last element returns 0
d=1,7
d 0 #= 1
m=a:7
m 0 #= 7
# lets get more compex
b=7
b 3 #= 3 (sequence)
b.a #= error
b'len #= 1 (byte)
b'keys #= error
b'values #= error
m=a:7
d1=a:7,b:4
m 0 #= 7
d1 0 #= a:7
d1.a #= 7
m2=a:a
d1=a:a;b:b;a:a+1
m2 3 #= 3
m3=d1 0 #= a:a
m3 7 #= 7
d1.a #= a:(a,a+1)
df=(a,b):a+b
d2=(a,b):a+b;(a,b):a+b+1;a:a;b:7
d2'keys#=a,b;a;b
d2'values#=(a+b;a+b+1),a,7
# a def with variables is lazy
d2 0 #= (a,b):(a+b;a+b+1)
d2.(a,b) #= (a+b;a+b+1)
d2&(a,b) #= (a,b):(a+b;a+b+1)
df #= (a,b):(a+b)
df 1,2 #= 3
d2&(a,b) 0 #= (a,b):(a+b)
d2&(a,b) 1 #= (a,b):(a+b+1)
d2&(a,b) 1 3,4 #= 7

d2.a #= {a}
d2&a #= a:a
d2&a 6 #= 6
d2.b #= 7
d2&b #= ???
m=a:a,b:b
m&b 3 #= 3
m2=b:b
m2 3 #= 3

d=a:1;b:7;a:6;2
d#=a:{1,6},b:7,2
d 0 #= a:{1,6}
d.a #= {1,6}
d'len #= 3
d.b #= 7
d.c #= error
d 3 #= error
d'keys #= a,b,~
d'values #= {1,6},7,2
d.a:9 # appends to list
d.a#={1,6,9}
d.a=4
d.a#=4
v=d.a #= {1,6}
v'len #= 2
v 1 #= 6

# it can be tedious to do ;, for items in a list
# so just doing ; is the same.
# therefore, we need a new way to delimit in a sequence.
# we use a period followed by a space
# ret1 4. ret1 5. ret1 6.

```


### List

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

### Sequence

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

### Stream

```python

# Stream / pipe
# a stream is a series of expressions where results flow from left to right.
# streams are lazy sequences such that evaluation follows definition.
# the final value is returned from the stream when the stream is run
msg = "hello world"
p1 = $( (replace "world", "universe") (append "!") )
res1 = p1 msg #= "hello universe!"
p2 = $( replace "hello", "goodbye" )
p3 = $( p1 p2 (append "?") )
res2 = p3 msg #= "goodbye universe!?"

p1 v=~: ((replace "world", "universe") v) (append "!")
p2 v=~: ((replace "hello", "goodbye") v)
p3 v=~: (p1 v) (p2) (append "?")
res2 = p3 msg #= "goodbye universe!?"
```

### Dict

```python

# dict / hashmap
# a dict is represented by a sequence of definitions
a:1 b:2 #= a:1 b:2
m1 =
  a:1
  b:2
m1 = a:1 b:2

s1 = "apple"
s2 = "banana"
fruit =
  (s1):4 # use variable values by wrapping in parens
  (s2):2
  orange:3 # default is to use string representation for definition
fruit.apple #= 4
fruit.orange #= 3

```


## Types

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

### metaprogramming 

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



```

# line comment
nothing
# comment indent block
    comment indent block
  comment indent block
nothing
## comment block
  comment block
comment block
##

#
nothing
#

##
nothing
##

#. doc line comment
nothing
#. doc comment indent block
    doc comment indent block
  doc comment indent block
nothing
##. doc comment block
  doc comment block
doc comment block
##.

#.
nothing
#.

##.
nothing
##.

#: doc line comment
nothing
#: doc comment indent block
    doc comment indent block
  doc comment indent block
nothing
##: doc comment block
  doc comment block
doc comment block
##:

#:
nothing
#:

##:
nothing
##:

#! doc line comment
nothing
#! doc comment indent block
    doc comment indent block
  doc comment indent block
nothing
##! doc comment block
  doc comment block
doc comment block
##!

#!
nothing
#!

##!
nothing
##!

aaa #a
aaa #a a
aaa #= a
aaa # a
aaa #########
aaa ######### 
aaa ######### a
aaa #########a
aaa #########a 
aaa #
aaa # 
aaa #a
aaa #a 
#a
#a a
#= a
# a
#########
######### 
######### a
#########a
#########a 
#
# 
#a
#a 
aaa#a
aaa#a a
aaa#= a
aaa# a
aaa########
aaa########
aaa########
aaa########
aaa########
aaa#
aaa# 
aaa#a
aaa#a 


#+pname plugin line comment
nothing
#+pname plugin comment indent block
    plugin comment indent block
  plugin comment indent block
nothing
##+pname plugin comment block
  plugin comment block
plugin comment block
##+

#+pname
nothing
#+pname

##+pname
nothing
##+

#= test line comment
nothing
#= test comment indent block
    test comment indent block
  test comment indent block
nothing
##= test comment block
  test comment block
test comment block
##=

#=
nothing
#=

##=
nothing
##=

### important line
nothing
### important indent block
  important indent block
    important indent block
nothing
#### important block
  important block
important block
####

###
nothing
###

####
nothing
####

nothing
  # indent
  nothing # fdafdsa gdadgd

### expect
# expect
1 #= 1
#= 57
57
### ####################################
### Variables
### ####################################
# " 0 " is Boolean false
# " 1 " is Boolean true
# "~" is the None value
# = is assignment for new symbols
# == is comparison for existing symbols
#= 1
45 == 45
#= 0
45 == 46
#= 7
v = 7
#= 1
v == 7
#= 0
v == 8
r1 = v == 7 #= 1
r2 = v == 8 #= 0
r1 == r2 #= 0
r3 = 9 #= 9
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
### ####################################
### Return @
### ####################################
# @ returns
# @ is a special type of function. and behaves like functions do
ret1: @ "A" #= "A"
isbigger a, b: @ a > b
.isbigger 5, 2 #= 1
.isbigger 2, 5 #= 0
# The last evaluated statement is always returned
# isbigger receives a list containing 2 elements
isbigger a, b: a > b
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
### ####################################
### Logical Operators
### ####################################
# Like functions, operators are greedy.
  Operators are treated the same as other functions
  except that the first argument is the value before the operator
and3ind2 a, b, c: a & b & c & @ c.. @ b.. @ a.. 0
# Note that this syntax is usually less readable
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
# reviewing list vs sequence
  when space delimited, you have a list.
  all elements in a list are always evaluated
# The .L statement returns the string
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
### ####################################
### Sequence vs List
### ####################################
[ a, b, c ] #= [ a, b, c ] 
( a b c ) #= c
a, b, c #= [ a, b, c ] 
a b c #= c
[ a b c ] #= [ c ]
( a, b, c ) #= [ a, b, c ]
a,
b,
c #= [a, b, c]
a
b
c #= c
# Every values has properties.
# you can append
# you can get errors / or
a = 1
a.len() #= 1
a.log() #= 1
a.append("x")
a.len() #= 2
a.log() #= 1, "x"
a.append("yy")
a.len() #= 3
a.log() #= 1, "x", "yy"
a.extend("z")
a.len() #= 4
a.log() #= 1, "x", "yy", z
a.extend("w")
a.len() #= 5
a.log() #= 1, "x", "yy", zw
a.append([3, 4])
a.len() #= 6
a.log() #= 1, "x", "yy", zw, [3, 4]
a.extend([5, 6])
a.len() #= 8
a.log() #= 1, "x", "yy", zw, [3, 4], 5, 6





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

# a variable is evaluated for a condition check when used as a function
# numbers > 0 pass the condition check
v1 (.L "v1 > 0") #= @ "v1 > 0"
v2 (.L "v2 > 0") #= @ "v2 > 0"
v3 (.L "v3 > 0") #= ~
v4 (.L "v4 > 0") #= ~
57 (.L "57 > 0") #= @ "57 > 0"
0 (.L "0 > 0") #= ~
-7 (.L "-7 > 0") #= ~
~ (.L "~ > 0") #= ~

a = 5
v1 = a @ 1
v1 = a ( @ 1 )
# Is v1 a tuple of ( 5 , 1 )?
# Is v1 the evaluation of the body of a? #= 1 ?
# in order to disambiguate, tuples always have a comma between terms…?

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

# since @ is return, it doesn't make sense to assign it to a value
# as such, if it is assigned, it returns a lambda function
v8 = @ 3 #= x: @ 3
v9 = 1 @ 3 #= 1 x: @ 3
t1 t2 = v9
t1 #= 1
t2 #= x: @ 3
w1 w2 = 1 @ 3 #= 1 x: @ 3
w1 #= 1
w2 #= x: @ 3







isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                       |
# & is the logical and operator






…………

C=0 #:counter ;{C} is zero
F:A B C #:add-l :add-r C:subtract
  D=3 #:add
  A+B-C+D #:sum
V=F 50 700 100 #:calculated-sum
print V #=653
F:A B #:


# 2sum
two-sum:a n =
  a:i:f
    a:j:s
      f+s==n
        <- i j




two-sum:a n = > a:i:f > a:j:s > f+s==n > <- i j

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



```
All content after # is always non-runtime

# with single char, it will continue comments
  When indented by at least 2 spaces
  and continues until the next line not starting with space.

## all non-runtime types can have a second char to
Allow unindented
Non-runtime blocks
this always terminates with the same chars
##


# regular comment
#. RST
#: yaml
#! Raw comment
#+plugin

# expect
1 #= 1
#= 57
57

# “|” is the else / elif operator
# “|” is also the logical or operator
# “ 0 “ is Boolean false
# “ 1 “ is Boolean true
# “~” is the None value
# “.p“ prints

# = is assignment for new symbols
# = is comparison for existing symbols
#= 1
45 == 45
#= 0
45 == 46
#= 7
v = 7
#= 1
v = 7
#= 0
v = 8
r1 = v = 7 #= 1
r2 = v = 8 #= 0
r1 = r2 #= 0
r3 = 9 #= 9

# ? commands are runtime
# assert
? 1 = 1
?+plugin

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

# a variable is evaluated for a condition check when used as a function
# numbers > 0 pass the condition check
v1 (.p “v1 > 0”) #= @ “v1 > 0”
v2 (.p “v2 > 0”) #= @ “v2 > 0”
v3 (.p “v3 > 0”) #= ~
v4 (.p “v4 > 0”) #= ~
57 (.p “57 > 0”) #= @ “57 > 0”
0 (.p “0 > 0”) #= ~
-7 (.p “-7 > 0”) #= ~
~ (.p “~ > 0”) #= ~

a = 5
v1 = a @ 1
v1 = a ( @ 1 )
# Is v1 a tuple of ( 5 , 1 )?
# Is v1 the evaluation of the body of a? #= 1 ?
# in order to disambiguate, tuples always have a comma between terms…?

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

# since @ is return, it doesn't make sense to assign it to a value
# as such, if it is assigned, it returns a lambda function
v8 = @ 3 #= x: @ 3
v9 = 1 @ 3 #= 1 x: @ 3
t1 t2 = v9
t1 #= 1
t2 #= x: @ 3
w1 w2 = 1 @ 3 #= 1 x: @ 3
w1 #= 1
w2 #= x: @ 3




isallsamebool3 a b c: a & b & c < 1 | ! a | b | c < 1 < 0
#                       |
# & is the logical and operator




…………

C=0 #:counter ;{C} is zero
F:A B C #:add-l :add-r C:subtract
  D=3 #:add
  A+B-C+D #:sum
V=F 50 700 100 #:calculated-sum
print V #=653
F:A B #:


# 2sum
two-sum:a n =
  a:i:f
    a:j:s
      f+s==n
        <- i j




two-sum:a n = > a:i:f > a:j:s > f+s==n > <- i j

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
s1=“a”
s2=“b”
v=b > n-k>0 > <- s1 << s2
v2=select(b n k s1 s2)
Print(v==v2) #= true
```
