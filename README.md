## Mamba programming language
Mamba is a simple dynamic typed, programming language.
Thanks to [maldoinc](https://github.com/maldoinc/mamba) for a good thing to start with and modify!
Sadly he's no longer working on it, so I made this and will continue updating it.

I am working on this right now and there are lots of features to add, e.g. modules and limitation on loops and HTTP operations or modules.

### Installation requirements ###

* Python3
* ply

### Features ###
* Variables
* Functions
* Flow control statements
* Loops (for in, for, inf loop, while)
* Loop exit statement
* Compound operators
* Pythonic sequence (array, string) slicing 

### Data types ###
* Integer
* Float
* String
* Boolean
* Arrays

### Language description ###

#### Variables ####

variables are dynamically typed immediately declared upon use `foo = "bar";`

### Operators ###

logic: `and` `or` `not` `in` `not in` `>` `>=` `<` `<=` `==` `!=`

arithmetic: `+` `-` `*` `/` `**`

binary: `~` `^` `|` `&` `>>` `<<`

ternary: `test ? true_value : false_value`

#### Functions ####

functions are declared via the following grammar

    function func_name( [<arguments>,] ){
        < statements >
    }

    function random(){
        return 4;
    }

return value is specified with the `return` keyword which, as expected, immediately halts function execution upon being called. Functions can have their private functions which are inaccessible to the outer scope.

#### Flow control ####

Mamba supports `if` statements for flow control via the following syntax

    if < expression > {
        < statements >
    }

nb: Brackets are mandatory, while parenthesis on the expression are optional


### Loops ###

Mamba supports two kind of loops, `for` and `while`

**for syntax**

    for variable in sequence {
        < statements >
    }

nb: sequence accepts arrays and strings

    for variable in low -> high {
        < statements >
    }
    
down to loops are constructed as

    for variable in high <- low {
        < statements >
    }

nb: loop indexes are inclusive

**while syntax**

    while < expression > {
        < statements >
    }

there is also the alternative `for` syntax

    for {
        < statements >
    }

which acts as an infinite loop (which internally is expressed as a `while true {}` statement)

All loops can be prematurely exited via the `exit` statement when necessary


### Arrays ###

Arrays have dynamic length and can be declared via the  `[ ... ]` expression


### Printing ###

Printing is supported via the `say` keyword which accepts a list of values to print.

### Standard library ###

#### 1. Constants ###

* `e`
* `pi`

#### 2. Globals

* `argv`

#### 3. Functions

* `ask(prompt)` *shows the prompt and returns the result as a string*
* `int(x [, base])` 
* `float(x)`
* `round(value, precision)`
* `abs(x)`
* `log(x)`
* `rand`
* `randrange(lo, hi)`
* `randint(lo, hi)`
* `range(lo, hi, inc)` *behaves like the python 2.x range()*
* `sin(x)`
* `cos(x)`
* `tan(x)`
* `atan(x)`
* `str(x)`
* `substr(str, start, length)`
* `len(str)`
* `pos(substr, str)`
* `upper(str)`
* `lower(str)`
* `replace(str, find, replace)`
* `format(string [, ... ])`
* `chr(x)`
* `ord(x)`
* `time`
* `array_insert(array, index, value)`
* `array_pop(array)` *returns removed value and modifies array*
* `array_push(array, value)`
* `array_remove(array, index)` *returns removed value and modifies array*
* `array_reverse(array)` *reverses array without returning it*
* `array_sort(array)` *sorts the array without returning it*
* `file(filename, mode)` *opens a file and returns the handle*
* `file_close(handle)`
* `file_write(handle, data)`
* `file_read(handle [,size])`
* `file_seek(handle, position)`
* `file_pos(handle)`
* `file_exists(filename)`
