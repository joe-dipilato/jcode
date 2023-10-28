# Return

```python
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
```

```python

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
```
