# -*- coding: utf-8 -*-

from .compat import USE_AESARA

if USE_AESARA:
    from aesara.tensor import *  # noqa
    from aesara.tensor import slinalg  # noqa
else:
    from theano.tensor import *  # noqa
    from theano.tensor import slinalg  # noqa
