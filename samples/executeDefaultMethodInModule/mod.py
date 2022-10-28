
if __name__ == '__main__':
    print('function executed by default when the module is executed, not when it\'s imported.')
else:
    # >>> import mod
    print('The module was imported. Execute it directly to execute its default function.')

# $ python mod.py
# function executed by default when the module is executed, not when it's imported.
# >>> import mod
# The module was imported. Execute it directly to execute its default function.
