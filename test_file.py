from cmt import my_code


def test_foobar():
    my_code.print_version()
    # Raised just so this fails and the print is shown
    raise Exception("foobar")
