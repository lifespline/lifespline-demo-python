============================
Python Namespaces and Scopes
============================

About
-----

What are python namespaces, scopes and how to use them.

Warning
-------

You'll learn about change variables from one scope to the other with keywords like ``global`` and ``nonlocal``, but it recommended to use this technology only if you can manage the increased complexity arriving from the **side-effects** of doing so.

Namespace
---------

A namespace is a structure used to organize the symbolic names assigned to objects in a Python program, it is as a dictionary in which the keys are the object names and the values are the objects themselves. The assignment statement creates a symbolic name that you can use to reference an object. The statement ``foo = 'bar'`` creates a symbolic name ``foo`` that refers to the string object ``'bar'``.

Types of namespaces:

* Built-In
* Global
* Enclosing
* Local

These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed.

Built-In
~~~~~~~~

The built-in namespace contains the names of all of Python’s built-in objects, available at all times when Python is running.

.. code:: python

   # listing the contents of the __builtins__ namespace
   >>> dir(__builtins__)
   ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


Global Namespace
~~~~~~~~~~~~~~~~

The global namespace contains any names defined at the level of the main program (plus a global namespace for any module that your program loads with the ``import`` statement).

Access the global namespace as:

.. code::python

   # the data structure holding the global namespace
   >>> globals()
   {
       '__name__': '__main__',
       '__doc__': None,
       '__package__': None,
       '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
       '__spec__': None,
       '__annotations__': {},
       '__builtins__': <module 'builtins' (built-in)>
   }

   >>> foor = 'bar'
   >>> globals()
   {
       '__name__': '__main__',
       '__doc__': None,
       '__package__': None,
       '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
       '__spec__': None,
       '__annotations__': {},
       '__builtins__': <module 'builtins' (built-in)>,
       'foo': 'bar'
   }

   # listing the contents of the global namespace
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__'
   ]

   >>> foor = 'bar'
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo'
   ]

.. warning::

    globals returns a reference to the globals object.

A function can create global variables (``side-effects``) with:

.. code:: python

   >>> x = 20
   >>> def f():
       global x
       x = 40
       print(x)

   >>> f()
   40
   >>> x
   40

   # also with
   >>> x = 20
   >>> def f():
       globals()['x'] = 40
       print(x)

   >>> f()
   40
   >>> x
   40


Local and Enclosing
~~~~~~~~~~~~~~~~~~~

The interpreter creates a new namespace whenever a function executes. That namespace is local to the function and remains in existence until the function terminates. Creating a function ``f`` inside the main program ``main`` assigns to ``f`` a local namespace, and ``main``'s namespace becomes the enclosing namespace.

Access the global namespace as:

.. code:: python

    >>> def f():
      foo = 'bar'
      print(locals())

    >>> f()
    {'foo': 'bar'}

    >>> def f():
      foo = 'bar'
      print(dir())

    >>> f()
    ['foo']

.. warning::

    locals returns a clone of the locals object.

Variable Scope
--------------

The existence of multiple, distinct namespaces means several different instances of a particular name can exist simultaneously while a Python program runs. As long as each instance is in a different namespace, they’re all maintained separately and won’t interfere with one another.

Upon encountering a name, Python searches the namespaces in the following order **LEGB**:

* local
* enclosing
* global
* built-in

Have a look at the following examples:

.. code:: python

   >>> my_list = ['foo', 'bar', 'baz']
   >>> def f():
       my_list[1] = 'quux'

   >>> f()
   >>> my_list
   ['foo', 'quux', 'baz']

   >>> def f():
        my_list = ['qux', 'quux']

   >>> f()
   >>> my_list
   ['foo', 'bar', 'baz']

.. code:: python

   >>> def f():
       x = 20
       def g():
           global x
           x = 40
       g()
       print(x)
    
   >>> f()
   20
   >>> x
   40

   # Accessing the nearest outer scope
   >>> def f():
           x = 20
           def g():
               nonlocal x
               x = 40
           g()
           print(x)
   >>> f()
   40

Important To Retain
-------------------

* scopes are evaluated as **LEGB**
* it is not recommended to use ``global`` and ``nonlocal`` keywords
* ``locals()`` returns a dictionary with the names and references to clones of the objects in the local namespace
* ``globals()`` returns a dictionary with the names and references to the objects in the global namespace
* ``dir()`` lists the names of the objects in the namespace closest in scope
* ``dir(foo)`` lists the names of the objects in the namespace of the object named ``foo`` (if ``foo`` is an object, it lists the attributes of the object, if ``foo`` is a module, it lists the namespace of the module, or the names of the objects contained in the module). See example below.

.. code:: python

   # mod.py
   foo = 'bar'

   # python interpreter
   >>> foo = 'bar'
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo'
   ]

   >>> import mod
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo',
       'mod'
   ]

   >>> dir(foo)
   ['__add__', '__class__', '__contains__', '__delattr__', '__dir__','__doc__', '__eq__', '__format__', '__ge__', '__getattribute__','__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__','__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__','__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__','__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__','__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode','endswith', 'expandtabs', 'find', 'format', 'format_map', 'index','isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier','islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace','rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split','splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate','upper', 'zfill']

   >>> dir(mod)
   [
       '__builtins__',
       '__cached__',
       '__doc__',
       '__file__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo'
   ]

   >>> dir(mod.foo)
   ['__add__', '__class__', '__contains__', '__delattr__', '__dir__','__doc__', '__eq__', '__format__', '__ge__', '__getattribute__','__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__','__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__','__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__','__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__','__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode','endswith', 'expandtabs', 'find', 'format', 'format_map', 'index','isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier','islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace','rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split','splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate','upper', 'zfill']

   # pkg/mod.py
   foo = 'bar'

   # python interpreter
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__'
   ]

   >>> import pkg
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'pkg'
   ]
   >>> dir(pkg)
   [
       '__builtins__',
       '__cached__',
       '__doc__',
       '__file__',
       '__loader__',
       '__name__',
       '__package__',
       '__path__',
       '__spec__'
   ]
   # necessary to import explicitly for there was no __init__.py
   # file specifying which modules are imported by default with the
   # package import
   >>> from pkg import mod
   >>> dir(mod)
   [
       '__builtins__',
       '__cached__',
       '__doc__',
       '__file__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo'
   ]

   # pkg/mod.py
   foo = 'bar'

   # pkg/__init__.py
   import mod

   # python interpreter
   >>> import pkg
   >>> dir()
   [
       '__annotations__',
       '__builtins__',
       '__doc__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'pkg'
   ]
   >>> dir(pkg)
   [
       '__builtins__',
       '__cached__',
       '__doc__',
       '__file__',
       '__loader__',
       '__name__',
       '__package__',
       '__path__',
       '__spec__',
       'mod'
   ]
   >>> dir(pkg.mod)
   [
       '__builtins__',
       '__cached__',
       '__doc__',
       '__file__',
       '__loader__',
       '__name__',
       '__package__',
       '__spec__',
       'foo'
   ]

Literature
----------

* `realpython.com <https://realpython.com/python-namespaces-scope/>`_