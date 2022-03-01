from pycparser import *

def _make_scope():
    ALL_TYPES =""
    BASIC_TYPES =""
    SimTypeFunction =""
    SimTypeString = ""
    SimTypeWString = ""
    scope = dict()
    for ty in ALL_TYPES:
        if ty in BASIC_TYPES:
            continue
        if ' ' in ty:
            continue

        typ = ALL_TYPES[ty]
        if isinstance(typ, (SimTypeFunction , SimTypeString, SimTypeWString)):
            continue

        scope[ty] = True
    return [scope]