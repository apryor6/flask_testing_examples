def with_magic_string(magic_string):
    """A decorator that attaches a magic string to a function"""

    def inner(f):
        f.magic_string = magic_string
        return f
    return inner