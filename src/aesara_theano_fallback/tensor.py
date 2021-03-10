# -*- coding: utf-8 -*-

try:
    from aesara.tensor import *  # noqa

except ImportError:
    from theano.tensor import *  # noqa
    from theano.tensor import slinalg

else:
    from aesara.tensor import slinalg  # noqa
