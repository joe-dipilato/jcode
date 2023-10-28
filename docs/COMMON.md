# common

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
