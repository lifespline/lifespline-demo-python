exercise-1
==========

Execute ``ls | grep sample > res``. Don't leave ``res`` in the file system.

Solution
--------

.. code:: python

   import subprocess as sp
   import os

   ls = sp.Popen("ls", stdout=sp.PIPE)
   buffer = open('res', 'wb')
   grep = sp.run("grep sample".split(), stdin=ls.stdout, stdout=buffer)
   os.system("cat res")
   os.remove('res')
