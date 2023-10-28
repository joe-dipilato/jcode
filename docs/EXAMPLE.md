# Example

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

```python
# 2sum
two-sum:a n =
  a:i:f
    a:j:s
      f+s==n
        <- i j
two-sum:a n = > a:i:f > a:j:s > f+s==n > <- i j
```
