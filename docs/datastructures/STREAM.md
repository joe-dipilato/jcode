# Stream

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
