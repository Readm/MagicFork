# MagicFork
Fork in a new terminal in python.

## Usage:

use `magicfork.magicfork()` in stead of `fork()`

`magicfork()` takes one argument: `terminal`, valid value:

+ `'gnome'`or`'gnome-terminal'` (defualt)
+ `'xterm'`

## Sample:

---
```
import magicfork

a = 'a'
b = 'b'
if magicfork.magicfork():
    print a
    a = raw_input('a?')
    print 'a:', a
else:
    print b
    b = raw_input('b?')
    print 'b:', b
```

### Others

Report any bug in issue.
Star this if you like it.