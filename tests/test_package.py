from __future__ import annotations

import importlib.metadata

import sp_test_copier as m


def test_version():
    assert importlib.metadata.version("sp_test_copier") == m.__version__
