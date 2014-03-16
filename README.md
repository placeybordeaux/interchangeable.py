interchangeable.py is an experiment in automatically choosing the best suited of multiple interchangeable functions for the given arguments. There are currently three use cases in mind.

1. Automatically choose the fastest implementation of a function based off of previous emperical evidence for a given set of arguments
2. Provide tools for gaining insight into which implementations are faster than others
3. Be memory consumption aware, i.e. intelligently fall back to slower but less memory intensive implementations when memory is scarse

Currently this is just a proof of concept and only attempts to accomplish #1.

# Usage

fib\_example.py is a contrived, but real example of how using interchangeable should work. In place of choosing either `fib\_dynamic` or `fib_closed_form` we declare `fib = interchangeable(fib_dynamic, fib_closed_form)` and simply use `fib`. Each time `fib` is used with arguments it has not seen it will randomly choose either `fib_dynamic` or `fib_closed_form`, execute it and transparently record the run time.

Licensed under [MIT License](http://opensource.org/licenses/MIT)
