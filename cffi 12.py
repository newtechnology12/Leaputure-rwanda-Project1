
#cffi is an extennal package proving a C foreign function interface for python
from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("float pi_approx(int n);")
ffibuilder.set_source("_pi",  # name of the output C extension
"""
here we have to including this
    #include "pi.h"
""",
    sources=['pi.c'],   # includes pi.c as additional sources
    libraries=['m'])    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
#pyrsistent is a Python library for immutable data structures.
def test_addition(pvector):
    v = pvector([1, 2]) + pvector([3, 4])

    assert list(v) == [1, 2, 3, 4]