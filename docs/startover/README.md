
# Startover

- [Basic Syntax](#basic-syntax)
  - [Symbols](#symbols)
    - [Values](#values)
    - [Variables](#variables)
    - [Operators](#operators)
    - [Syntaxes](#syntaxes)
  - [Assignment](#assignment)
  - [Evaluation](#evaluation)
- [Basic Data Structures](#basic-data-structures)
  - [Map](#map)
  - [Set](#set)

## Basic Syntax

### Symbols

```python
# All variables, operators, values, and syntaxes types of symbols
1 # This is a symbol for the numerical value: 1
"abc" # This is a symbol for the string value: "abc"
number_one=1
number_one # This is a symbol for the variable: number_one
```

#### Values

```python
# Values are a type of symbol that always represents a specific value
1 # This is the symbol that represents the value 1
"abc" # This is the symbol that represents the value "abc"
3.6 # This is the symbol that represents the value 3.6
```

#### Variables

```python
# Variables are a type of named symbol that represent a value
number_one=1
number_one # This is a variable named "number_one" which is assigned to the value 1
```

#### Operators

}}} TODO: operators are a type of function? consider metaprogramming and operator overrides.

```python
# Operators are a type of symbol that performs an operation and evaluates to a value
= # The '=' operator 
+ # The '+' operator 
```

#### Syntaxes

}}} TODO: syntaxes such as parentheses

### Assignment

```python
# Variables can be assigned and reassigned to values with the "=" operator
changing_variable=3.14
changing_variable # changing_variable represents the value: 3.14
changing_variable="pi"
changing_variable # changing_variable now represents the value: "pi"
```

### Evaluation

```python
# All symbols are evaluated and the location where their symbol appears is treated identically to the evaluation result
3.14 # The symbol 3.14 evalues to the value 3.14
var_pi=3.14 # The evaluation result (3.14) of the symbol '3.14' is used in the assignment
var_pi # The symbol 'var_pi' evalues to the value 3.14
some_variable=var_pi # The evaluation result (3.14) of the symbol 'var_pi' is used in the assignment
some_variable # The symbol 'some_variable' evalues to the value 3.14
```

## Basic Data Structures

}}} TODO: basic datastructures

### Namespace

```python
# A namespace is a set of named symbols
ns1=a: # a namespace with symbol name a
ns2=a,b,c: # a namespace with symbol names a, b, and c
ns3=~: # a namespace with no symbol names
ns4=: # a namespace with no symbol names
```

### Routine

```python
# A routine is a series of instructions associated with a namespace
rt1=1 # a routine that executes and returns 1
rt2=a # a routine that executes and returns the symbol a in the namespace
rt3=a+1,b+1 # a routine that executes the set: a+1,b+1 based on the namespace
```

### Map

```python
# A map is a datastructure that associates a namespace with a routine
mp1=a:1 # associates symbol name 'a' with routine: 1
mp2=b:b # associates symbol name 'b' with routine: b
mp3=a,b:a+1,b+1 # associates symbol names: a,b with routine: a+1,b+1
```

### Set

```python
# A set is a collection of contents into a single object
st1=1,2 # set with values 1 and 2
a=1
b=2
st2=a,b # set with values 1 and 2 evaluated from the namespace
st3=a:a;b:b+1 # Set with maps a:a and b:b+1. no namespace evaluation in map
```

### Function

```python
# A Function is another name for a map
add1=a:a+1
addab=a,b:a+b
swap=l,r:r,l
```

### Execution

```python
# Objects can be separated into the following categories:
#   executable vs not-executable
#   executable:
#        takes-args vs no-args
```

}}} TODO: set not executable?

#### Not-Executable

```python
1 # 1 was not executed
number=1
number # number was not executed

"abc" # "abc" was not executed
string="abc"
string # string was not executed

1,2,3 # 1,2,3 was not executed
num_set=1,2,3
num_set # num_set was not executed

a:1,b:2 # a:1,b:2 was not executed
simple_map=a:1,b:2
simple_map # simple_map was not executed
```

#### Executable

}}} TODO: how to execute functions with no args

```python
a:a+1 # a:a+1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
3 a:a+1 # a:a+1 was executed and returned 4
# when a function pointer is preceded by an object and a space, the function is executed with the preceding object
# as the argument to the function.

# All functions take exactly 1 argument even if the function is defined with no arguments
:1 # :1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
~ :1 # :1 was executed and returned 1
# :1 is equivalent to ~:1
```

```python
# Functions can also be executed when followed by parentheses enclosing arguments
a:a+1(3) # executed and returned 4
:1(~) # executed and returned 1
:1() # This is equivalent to :1(~). executed and returned 1.
```

```python
return1=:1 # Assignments are not executions. return1 was not-executed on this line
return1 # return1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
~ return1 # return1 was executed and returned 1
return2=. return1 # return1 is executed. return2 is set to 1


return1=:1 # Assignments are not executions. return1 was not-executed on this line
return1 # return1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
. return1 # return1 was executed and returned 1
return2=. return1 # return1 is executed. return2 is set to 1
```

### Indentation

### Comments

## datastructures

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
