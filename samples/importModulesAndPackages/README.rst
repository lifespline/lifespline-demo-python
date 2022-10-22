==============
Python Imports
==============

About
-----

Importing python modules and packages.

Getting Started
---------------

The ``import`` keyword makes code in one ``module`` or ``package`` available in another ``module`` or ``package``. A module is a python file. A ``package`` is a directory containing ``modules``. Directories without an ``__init__.py`` file are ``namespace packages``, otherwise ``packages``.

The ``__init__.py`` file contains the contents of the package when it’s treated as a module. It can be left empty. Below, ``package_one.module_one.whoami`` throws an ``AttributeError`` error if ``__init__.py__`` is empty or doesn't exist.

.. code:: python

    >>> (.env) samples-python/samples/importModulesAndPackages
    >>> dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

    >>> import module_one
    module_one
    >>> dir()
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'var_one']

    >>> import package_one
    module_one
    package_one.module_one
    >>> dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'module_one', 'package_one']

    >>> package_one
    <module 'package_one' (namespace)>

    >>> module_one.whoami
    'module_one'
    >>> package_one.module_one.whoami
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: module 'package_one' has no attribute 'module_one'

    >>> dir(module_one)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'whoami']

    >>> dir(package_one)
    ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

    >>> from package_one import module_one as pkg_module_one
    >>> dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'module_one', 'package_one', 'pkg_module_one']
    >>> pkg_module_one.whoami
    'package_one.module_one'

``__init__.py`` defines which modules are imported. Adding a file ``__init__.py__`` with the following contents:

.. code:: python

    from . import module_one

Enables the following:

.. code:: python

    >>> (.env) samples-python/samples/importModulesAndPackages
    >> import package_one

    >>> package_one
    <module 'package_one' from '.../samples-python/samples/importModulesAndPackages/package_one/__init__.py'>

    >>> package_one.module_one.whoami
    'package_one.module_one'

Notice how ``import module_one`` in ``package_one/module_one.py`` recognized the module ``module_one.py``. *TODO*: continue with ``namespace`` and ``sys.path``.

Literature
----------

* `realpython.com <https://realpython.com/python-import/>`_