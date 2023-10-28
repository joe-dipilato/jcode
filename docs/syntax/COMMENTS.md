# Comments

```python

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
```

```python
C=0 #:counter ;{C} is zero
F:A B C #:add-l :add-r C:subtract
  D=3 #:add
  A+B-C+D #:sum
V=F 50 700 100 #:calculated-sum
print V #=653
F:A B #:
```

```python
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
```
