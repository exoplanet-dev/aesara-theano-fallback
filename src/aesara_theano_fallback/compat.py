# -*- coding: utf-8 -*-

__all__ = ["aesara", "sparse", "tensor", "change_flags", "ifelse", "slinalg"]


try:
    import aesara

except ImportError:

    try:
        import theano.graph

    except ImportError:

        try:
            import theano.gof

        except ImportError:
            raise ImportError(
                "None of 'aesara', 'theano-pymc', or 'theano' are installed"
            )

    # General imports: these are the same for both theano and theano-pymc
    import theano as aesara
    from theano import sparse, tensor
    from theano.ifelse import ifelse
    from theano.tensor import slinalg

    try:
        from theano.configparser import change_flags
    except ImportError:
        change_flags = theano.config.change_flags

else:
    # Aesara is installed
    from aesara import sparse, tensor
    from aesara.configparser import change_flags
    from aesara.ifelse import ifelse
    from aesara.tensor import slinalg
