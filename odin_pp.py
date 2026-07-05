import gdb
import gdb.printing
import gdb.types


class OdinString(gdb.ValuePrinter):
    def __init__(self, val):
        self.__val = val

    def display_hint(self):
        return 'string'

    def to_string(self):
        len = int(self.__val['len'])
        return self.__val['data'].string(encoding='utf-8', length=len)


class OdinDynamicArray(gdb.ValuePrinter):
    def __init__(self, val):
        self.__val = val

    def display_hint(self):
        return 'array'

    def to_string(self):
        len = int(self.__val['len'])
        len = min(gdb.print_options()['max_elements'], len)
        res = ''
        res += '{'
        for i in range(len):
                 res += f'{(self.__val['data'] + i).dereference()}, '
        res += '}'

        return res


class OdinUnion(gdb.ValuePrinter):
    def __init__(self, val):
        self.__val = val

    def to_string(self):
        tag = int(self.__val['tag'])
        if 0 == tag and not gdb.types.has_field(self.__val.type, 'v0'):
            return 'nil'
        return self.__val[f'v{tag}']


pp = gdb.printing.RegexpCollectionPrettyPrinter('odin')

pp.add_printer('odin_string', '^string$', OdinString)
pp.add_printer('odin_dynamic_array', r'^\[dynamic][a-zA-Z0-9:_]+', OdinDynamicArray)
pp.add_printer('odin_maybe', '^runtime::Maybe\\\x28', OdinUnion)

gdb.printing.register_pretty_printer(gdb.current_objfile(), pp, replace=True)
