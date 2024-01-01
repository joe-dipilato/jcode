
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

```python
# read a file
Pathlib,path$import
# get set of lines
lines = "file.jc"$path.read.splitlines
# make a function to convert lines into lists of blocks
toblk = lines,ilvl:
  # define function to get indent in spaces
  topre = ilvl:"  "*ilvl
  # block stack
  bstack = ,
  # for each line, determine if indented
  lines@line
    # check against next indent
    ?line;ilvl+1$topre.startswith
      # add prev block to stack and start a new one
      bstack+=block
      block=line,
      ilvl+=1
    |?line;ilvl$topre.startswith # current indent
      block[,]+=line # update block
    | # smaller indent
      # pop block from stack
      pblock=bstack.popr
      # add the previous block
      pblock+=block
      block=line,
      ilvl-=1
    # add to stack and return
    bstack+=block


#lines=[line for line in lines if line.startswith("#")]
lines@line # lines as line
lines@line?line,"#".startswith<line.lower # lowercase comment lines
lines@line?line,"#".startswith<line.lower|line # lines with lowercase comments
lines@@line<line.lower # lines = lowercase lines
lines@@line?line,"#".startswith<line.lower|?line,".".startswith<line.upper|"other"
lines@@line
  ?line,"#".startswith
    <line.lower
  |?line,".".startswith
    <line.upper
  |
    "other" #implicit return last statement without <
    
content,comment=lines@line
  ?line,"#".startswith<,line # add comment
  c=line.split@word
    word@@char # capitalize first A of each word
      ?char=="a"<"A"|char
  c" ".join, # add content

# scrub comments
lines@line
  line,"#".startswith
    < #= continue?
  contents[,],line.append # default to empty set
contents$print # default applies even if not run


F="file.jc"
E="Utf-8"
P=path(F,E)
P = (F,E) -> path
P = "file.jc","Utf-8"$path = (F,E)$path  not … F;E$path = (F),(E$path)
…. $ pulls left past commas, not semicolons
R=P.read()
R = () -> P.read
R = ()$P.read = $P.read
R = "file.jc","Utf-8"$path.read = (("file.jc","Utf-8")$path)$pathobj'read
S=R.split("\n",1)
S = ("\n",1) -> R.split
S = "\n",1$R.split
S = "file.jc","Utf-8"$path.read,"\n",1.split = 
  (((("file.jc","Utf-8")$path)$pathobj'read),"\n",1)$str'split

"A","b".split
"A",.split

# This is saying, lookup attribute name "split" from the return value type of the first arg ("A") which is (str) and pass the args in ("A","b") to the attribute. str.split("A","b")

"A","b"$path

#This is saying pass the args into the symbol "path" in the namespace. 
#  ( path("A","b") )

path("A").read(1)
"A"$path,1.read # saves 2 chars

P="/base/path/file.jc"
Cs="Utf-8","other"
P,"/".split


# If dict vars aren’t defined, use from outer scope.

thing = s:
  val=s,
  v2=self:s,
  O=a:a,
  split=self,param:...
  get=self:s,
  g2=self:self.val

# If dict vars aren’t defined, use from outer scope.

S="abc"$thing
S’val #= "abc"
"",S.split
S.v2 #= "abc"
S.get #= "abc"
S.g2 #= "abc"
S.val #= "def"
S.get #= "abc"
S.g2 #= "def"
"X"$S’O #= "X"
S.O #= S$S'O #= S$a:a #= S

C=v:
  _a=v,
  _b=0,
  U=self,b,c:self'_b=b+c,
  a=self:self'_a,
  b=self:self'_b

x=2$C
x.a #= 2
x.b #= 0
x.U #= x$x'U #= x$self,b,c:self'_b=b+c # error
x,3,4.U  #= x,3,4$self,b,c:self'_b=b+c
                           #= x'_b=3+4
x.b #= 7

a=:
  f=5,
  g=self,x,y:self,x+y
  h=self:3
  i=self:self'f
b=2
c=4
args=a,b,c
args.g #= args$args[0]'g #= a,b,c$a'g #= a,b,c$self,x,y:self,x+y
       #= a,6
args.f #= args$args[0]'f #= a,b,c$a'f #= a,b,c$5 #= error
a,b,c.f                  #= a,b,c$a'f #= a,b,c$5 #= error
a.f #=    args$args[0]'f #= a$a'f #= a$5 #= error
a'f #= 5
a.h #=    args$args[0]'h #= a$a'h #= a$self:3 #= 3
a.i #=                   #= a$a'i #= a$self:self'f #= 5

# instead of using self, we can use an _ item

a=:
  f=5,
  i=_:_'f

```



## Character Map

```python
# ALWAYS
"#" # Comment
"_" # Underscore character
'"' # A String
"\"" # A backslash
```

}}} TODO: AND vs kind

```python
"a&b" # Logical AND (With short circuit)
" &b " # TODO
" b& " # TODO
" & " # TODO

"a|b" # Logical OR (With short circuit)
" |b " # None OR b (With short circuit)
" b| " # TODO
" | " # OR Else (With short circuit)

"a^b" # A XOR B
" ^b " # TODO
" b^ " # TODO
" ^ " # TODO

"a!b" # TODO
" !b " # NOT b
" b! " # TODO
" ! " # TODO
```

```python
"a*b" # a times b
"a-b" # a minus b
"a+b" # a plus b
"a/b" # a divided by b
"a%b" # a modulus b
```

```python
"a=b" # a is assigned to b
"a:b" # Map a to b
```

```python
"a`b" # TODO
"a@b" # At??? TODO
"a~b" # TODO
"a$b" # TODO
"a?b" # TODO
```

```python
"a'b" # attribute b of object a
"a.b" # execute function b on object a
```

```python
"a,b" # The set with items 'a and b'
"a;b" # TODO
```

```python
"a<b" # TODO
"a>b" # TODO
```

```python
"a()b" # TODO
"a[]b" # TODO
"a{}b" # TODO
```

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
```

}}} TODO: set not executable?

#### Not-Executable

```python
1 # 1 was not executed
1,2,3 # 1,2,3 was not executed
a:1,b:2 # a:1,b:2 was not executed
```

#### Executable

}}} TODO: Execution without a space?

```python
a:a+1 # a:a+1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
# when a function pointer is preceded by an object and a space, the function is executed with the preceding object
# as the argument to the function.
3 a:a+1 # a:a+1 was executed and returned 4
# Functions can also be executed when followed by parentheses enclosing arguments
a:a+1(3) # executed and returned 4
add1=a:a+1 # add1 now holds the function pointer to a:a+1
3 add1 # evaluates to 4

# All functions take exactly 1 argument even if the function is defined with no arguments
:1 # :1 was not executed, it evaluates to a function pointer e.g. <ptr:xyz>
~ :1 # :1 was executed and returned 1
# :1 is equivalent to ~:1
:1(~) # executed and returned 1
:1() # This is equivalent to :1(~). executed and returned 1.
return1=:1 # return1 now holds the function pointer to :1
~ return1 # evaluates to 1
```

### Sequences

```python
# Expressions separated by spaces create a sequence
1 1,2,3 "abc" a:1,b:2 # This is a sequence of 4 expressions
# Expressions in a sequence are executed from left to right.
# The evaluation of the sequence is just the evaluation of the rightmost expression.
# In this case, the sequence evaluates to the set a:1,b:2

# Variables can be set based on the evaluation of a sequence
seqres=7,7,7 9.5 "abc",1 # seqres is set to the set: "abc",1
```

### Indentation

#### Without Indentation

```python
# Each new line continues the previous sequence at the same indendation level
1
1,2,3
"abc"
a:1,b:2
# This multiline sequence is identical to: 1 1,2,3 "abc" a:1,b:2
```

#### With Indentation

```python
# Different objects and syntaxes define different behaviour for how indended sequences are handled
1
  5
  3
# When a simple value is followed by an indented block, the indented block is only evaluated
#   if the simple value evaluates to True
# In this case, the indented sequence 5 3 is evaluated.
# The return value of the simple value is set to the evaluation of the indented sequence.
# The sequence 5 3 evalues to the rightmost expression of 3, so the whole statement returns 3.

-2
  5
  6
# Since -2 does not evaluate to True, 5 6 is not evaluated, and the original value of -2 is returned

# Indented blocks can also be represented on a single line with '{' and '}' characters
-2{5 6} # This is equivalent to the above 
# '{' is indentical to an indendation of all items in the following sequence. '}' is identical to a deindentation.

indentres=
  1
    5
    3
# An Assignment operation followed by an indent, simply assigns the result of the indented sequence,
# just as if the block was on the same line.
# indentres is assigned to the value: 3
# The statements are evaluated in the following order: 1 (true), 5, 3

indentres2=
  3
    4
    5
  -3
    6
# indentres2 is assigned to the value: -3
# The statements are evaluated in the following order: 3 (true), 4, 5, -3 (false) <6 is not evaluated>
```

### Evaluation Delimiters

```python
# The following items can occur sequentially: map, set, sequence, function_call, Assignment
a:1 # A map
1,2 # A set
1 2 # A sequence
7 add1 # A Function Call
one=1 # An Assignment
```

}}} TODO: a map to a map?
}}} TODO: a map of 2 sets?

```python
# MAPS
a:b:2 #= (a):(b:2) A map to a map
a:1,2 #= (a):(1,2) A map to a set
a,b:1,2 #= (a,b):(1,2) a map of two sets
a:{1 2} #= (a):(1 2) a map to a sequence
a:{7 add1} #= (a):(7 add1) a map to a function call
a:one=1 #= (a):(one=1) a map to an assignment
```

}}} TODO: a set of sequences?

```python
# SETS
a:1;b:2;c:3 #= (a:1),(b:2),(c:3) A set of maps
1,2;3,4;5,6 #= (1,2),(3,4),(5,6) A set of sets
1 2;3 4;5 6 #= (1 2),(3 4),(5 6) A set of sequences

```


### Comments

```python

```

## Advanced

### Sequences with assignment

```python

```

### Sequences with functions

```python

```

### Accessing memebers of a set

```python

```

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
