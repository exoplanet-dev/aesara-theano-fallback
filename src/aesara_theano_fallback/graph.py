# -*- coding: utf-8 -*-

try:
    from theano.graph import *  # noqa

except ImportError:
    from theano.gof import *  # noqa
    import theano.gof.graph as basic  # noqa

    op.ExternalCOp = op.COp  # noqa
