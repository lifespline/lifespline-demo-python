==============
Python Imports
==============

About
-----

The sample teaches about importing python modules and packages.

Getting Started
---------------

The ``import`` keyword makes code in one ``module`` (python file) or ``package`` available in another ``module``. A ``package`` is a ``module`` decoupled into different modules, or a set of modules. The structure of a ``package`` is simply a directory containing the ``modules`` (A package can have sub-packages). The ``__init__.py`` file in a package specifies which package modules are imported when the package is imported, allowing the package to have private modules/packages. If a package does not have an ``__init__.py`` file, it is called a ``namespace package`` and it requires that all its modules be imported individually (:ref:`example 3 <example_3>`.)

Example 1
~~~~~~~~~

.. code:: python

   # interpreter at sample root
   >>> import mod_2
   >>> dir()
   [
       ...
       'mod_2'
    ]
   >>> dir(mod_2)
   [
      ...
      'mod',
      'mod_1'
   ]
   >>> dir(mod_2.mod_1)
   [
      ...
      'mod',
      'pkg_2'
   ]
   >>> dir(mod_2.mod_1.pkg_2)
   [
      ...
      'mod',
      'pkg'
   ]
   >>> dir(mod_2.mod_1.pkg_2.pkg)
   [
      ...
      'mod'
   ]
   >>> mod_2.mod
   'mod_2'
   >>> mod_2.mod_1.mod
   'mod_1'
   >>> mod_2.mod_1.pkg_2.mod.mod
   'pkg_2.mod'
   >>> mod_2.mod_1.pkg_2.pkg.mod.mod
   'pkg_2.pkg.mod'

Example 2
~~~~~~~~~

.. code:: python

   # package interpreter at sample root
   >>> from pkg_3 import mod
   >>> dir(mod)
   [
      ...
      'mod',
      'mod_1'
   ]
   >>> mod.mod
   'pkg_3.mod'
   >>> mod.mod_1.mod
   'mod_1'

.. _example_3:

Example 3
~~~~~~~~~

.. code:: python

   # interpreter at sample root
   >>> import pkg_3
   >>> dir(pkg_3)
   [...]
   >>> import pkg_1
   >>> dir(pkg_1)
   [..., 'mod']
   >>> pkg_1.mod
   <module 'pkg_1.mod' from '.../samples-python/samples/importModulesAndPackages/pkg_1/mod.py'>
   >>> pkg_3.mod
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: module 'pkg_3' has no attribute 'mod'

Import Path
-----------

The import of a ``module`` inspects paths in the following order:

* The directory of the current/main script (or the current directory if there’s no script, such as when Python is running interactively)
* ``sys.path`` is a list of directories where the Python interpreter searches for modules.
* Other, installation-dependent directories

.. warning::

   Since the import path starts at the current script, be careful with the names of your own modules, they can override built-in modules like ``math``.

.. code:: python

   >>> sys.path
   [
       '',
       '/usr/lib/python38.zip',
       '/usr/lib/python3.8',
       '/usr/lib/python3.8/lib-dynload',
       '.../samples-python/.env/lib/python3.8/site-packages'
   ]


Important To Retain
-------------------

* a package is a module decoupled into different modules, private or public.
* ``from pkg import mod`` adds ``mod`` to the current namespace, not ``pkg``. ``import pkg`` adds ``pkg`` to the current namespace, not ``mod``. ``pkg.mod`` is available iff ``pkg/__init__.py`` contains ``from . import mod``.
* Developing your modules, mind to delete the ``__pycache__`` directory. It contains the compiled python files. If you don't, you may get unexpected results.
* The ``import path`` is not the same as the ``system path``. The ``system path`` is used to find the location of the ``python interpreter`` and the ``standard library``. The ``import path`` is used to find the location of ``modules`` and ``packages``.

Literature
----------

* `realpython.com <https://realpython.com/python-import/>`_