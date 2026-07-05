GDB Pretty-Printer for Odin lang
================================

Pretty print builtin types for Odin lang

- [x] string
- [x] union
- [x] dynamic array
- [ ] map
- [ ] slice
- [ ] endian specific integer
- [ ] endian specific float
- [ ] vector and matrix
- [ ] complex and quaternion
- [ ] rune
- [ ] typeid
- [ ] any


Installation
------------

```
source <path to odin_pp.py>
```

Future work
-----------

### Remaining builtin types

Not all types has been implemented yet

### Custom user defined types

Currently I have not made any public API available to integrate user defined types

### Code generator

Parse odin types to detect unions and underlying distinct type.

