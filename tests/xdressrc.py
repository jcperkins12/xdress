package = 'xdtest'

packagedir = 'xdtest'

extra_types = 'xdtest_extra_types'  # non-default value

stlcontainers = [
    ('set', 'int'),
    ('set', 'str'),
    ('map', 'str', 'str'),
    ('map', 'str', 'int'),
    ('map', 'int', 'str'),
    ('map', 'str', 'uint'),
    ('map', 'uint', 'str'),
    ('map', 'uint', 'uint'),
    ('map', 'str', 'float'),
    ('map', 'int', 'int'),
    ('map', 'int', 'float'),
    ('map', 'uint', 'float'),
    ('map', 'int', 'complex'),
    ('map', 'int', ('vector', 'int')),
    ('map', 'int', ('vector', 'uint')),
    ('map', 'int', ('vector', 'float')),
    #('map', 'int', ('vector', 'char')),
    #('map', 'int', ('vector', 'str')),
    #('map', 'int', ('vector', 'complex')),
    ]

stlcontainers_module = 'xdstlc'
