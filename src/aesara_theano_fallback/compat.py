# -*- coding: utf-8 -*-

__all__ = ["USE_AESARA", "aesara", "sparse", "change_flags", "ifelse"]


USE_AESARA = False
try:
    import aesara
except ImportError:
    aesara = None
else:
    try:
        import pymc3.theanof  # noqa
    except ImportError:
        USE_AESARA = True


if aesara is None or not USE_AESARA:
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
    from theano import sparse
    from theano.ifelse import ifelse

    try:
        change_flags = theano.config.change_flags
    except (ImportError, AttributeError):
        from theano.configparser import change_flags

else:
    # Aesara is installed
    from aesara import sparse
    from aesara.configparser import change_flags
    from aesara.ifelse import ifelse
