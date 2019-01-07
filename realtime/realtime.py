# -*- coding: utf-8 -*-

import contextlib
import functools
import sys


def realtime_import(f):
    @contextlib.contextmanager
    def _realtime_import_cxt():
        try:
            before = list(sys.modules.keys())
            yield
        finally:
            after = list(sys.modules.keys())
            del_list = [i for i in after if i not in before]
            for i in del_list:
                del sys.modules[i]

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        results = None
        with _realtime_import_cxt():
            results = f(*args, **kwargs)
        return results

    return wrapped
