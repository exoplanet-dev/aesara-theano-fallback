# aesara-theano-fallback

Striving towards backwards compatibility as
[Theano](https://github.com/theano/theano) is replaced by
[Aesara](https://github.com/pymc-devs/aesara) by the [PyMC3
project](https://docs.pymc.io). The idea is to provide a nearly drop in
replacement for importing `aesara` that will fall back onto `theano` when
`aesara` is not installed. This was specifically designed to support the
[exoplanet](https://github.com/exoplanet-dev/exoplanet) and
[starry](https://github.com/rodluger/starry) projects so it might not support
all of the features that you need. If you find something that isn't supported,
please submit a pull request!

## Installaion

This library can be installed using pip:

```bash
python -m pip install aesara-theano-fallback
```

## Usage

The syntax is designed to mostly follow `aesara`, so things like the following will often work:

```python
import aesara_theano_fallback.tensor as aet
```

For top-level access, use

```python
from aesara_theano_fallback import aesara
```

One place where the syntax has changed significantly between Theano and Aesara
is the `theano.gof` module was re-named to `aesara.graph` and the contents were
moved around a little bit. For exoplanet and starry, we define a few custom `Op`s
and you can use this library to do that as follows:

```python
from aesara_theano_fallback.graph import basic, op

class MyPythonOp(op.Op):
    def make_node(self, *args):
        # ...
        return basic.Apply(self, in_args, out_args)

class MyCOp(op.ExternalCOp):
    func_file = "./cpp_impl.cc"
    func_name = "APPLY_SPECIFIC(my_op_name)"
    # ...
```
