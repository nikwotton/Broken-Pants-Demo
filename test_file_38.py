import sys

import my_file


def test_foobar_37():
    assert(my_file.my_function() == '1.21.6')
    assert sys.version_info[1] == 8
