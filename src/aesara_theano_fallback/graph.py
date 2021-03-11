# -*- coding: utf-8 -*-

from .compat import USE_AESARA

if USE_AESARA:
    from aesara.graph import *  # noqa

else:
    try:
        from theano.graph import *  # noqa

    except ImportError:
        from theano.gof import *  # noqa
        import theano.gof.graph as basic  # noqa

        op.ExternalCOp = op.COp  # noqa
