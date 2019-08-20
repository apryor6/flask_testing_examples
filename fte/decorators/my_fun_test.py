from unittest.mock import patch, MagicMock


def test_my_fun_with_mocked_decorator():
    import fte.decorators

    def fake_decorator(magic_string):
        """A fake decorator"""

        def inner(f):
            f.magic_string = "You know nothing, Jon Snow"
            return f

        return inner

    fte.decorators.with_magic_string = fake_decorator
    from .my_fun import my_fun

    assert hasattr(my_fun, "magic_string")
    assert my_fun.magic_string == "You know nothing, Jon Snow"
