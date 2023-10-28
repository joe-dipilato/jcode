
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

### Map

```python
# 
```

### Set

```python
# 
```

### Function

```python
# A Function is a mapping of arguments to a routine
```

#### Function.Arguments

```python
# Arguments are a set of variables or values
```

#### Function.Routine

```python
# A Routine is a sequence of instructions
```

#### Functions.Arguments

```python
# 
```

#### Functions.Execution

```python
# 
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
