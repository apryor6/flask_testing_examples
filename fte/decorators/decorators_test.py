from .decorators import with_magic_string


def test_decorator():
    @with_magic_string("Hello there")
    def my_fun():
        pass

    assert hasattr(my_fun, "magic_string")
    assert my_fun.magic_string == "Hello there"

