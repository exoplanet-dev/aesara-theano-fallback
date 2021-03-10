# -*- coding: utf-8 -*-


def test_core_imports():
    from aesara_theano_fallback import tensor

    tensor.dot


def test_tensor_imports():
    from aesara_theano_fallback.tensor import nlinalg, slinalg  # noqa


def test_graph_basic_imports():
    from aesara_theano_fallback.graph import basic

    basic.Apply
    basic.Node


def test_graph_op_imports():
    from aesara_theano_fallback.graph import op

    op.Op
    op.ExternalCOp
