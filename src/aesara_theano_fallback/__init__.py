# -*- coding: utf-8 -*-

__all__ = [
    "USE_AESARA",
    "graph",
    "aesara",
    "sparse",
    "tensor",
    "change_flags",
    "ifelse",
]

from .compat import USE_AESARA, aesara, sparse, change_flags, ifelse
from .aesara_theano_fallback_version import version as __version__  # noqa

if USE_AESARA:
    # Oh boy!
    import sys
    from aesara import graph, tensor
    sys.modules["aesara_theano_fallback.graph"] = graph
    sys.modules["aesara_theano_fallback.tensor"] = tensor

else:
    from . import graph, tensor

__author__ = "Dan Foreman-Mackey, Rodrigo Luger"
__email__ = "foreman.mackey@gmail.com"
__uri__ = "https://github.com/exoplanet-dev/aesara-theano-fallback"
__license__ = "MIT"
__description__ = "Striving towards backwards compatibility with the Theano -> Aesara transition"
__copyright__ = "Copyright 2021 Daniel Foreman-Mackey, Rodrigo Luger"
