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

from . import graph, tensor
from .compat import USE_AESARA, aesara, sparse, change_flags, ifelse
from .aesara_theano_fallback_version import version as __version__  # noqa

__author__ = "Dan Foreman-Mackey, Rodrigo Luger"
__email__ = "foreman.mackey@gmail.com"
__uri__ = "https://github.com/exoplanet-dev/aesara-theano-fallback"
__license__ = "MIT"
__description__ = "Striving towards backwards compatibility with the Theano -> Aesara transition"
__copyright__ = "Copyright 2021 Daniel Foreman-Mackey, Rodrigo Luger"
