package = 'mypack_cythongen'     # top-level python package name
packagedir = 'mypack_cythongen'  # location of the python package

stlcontainers = [
    ('vector', 'str'),
    ('set', 'uint'),
    ('map', 'int', 'float'),
    ]

# classes = []
# functions =[]
classes = [
    ('A', 'src/hoover.*'),
    ('B', 'src/hoover.*', 'hoover_b'),
    ]

functions = [('do_nothing_ab', 'src/hoover.*')]
