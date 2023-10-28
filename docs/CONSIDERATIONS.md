# considerations

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

```python
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
```
