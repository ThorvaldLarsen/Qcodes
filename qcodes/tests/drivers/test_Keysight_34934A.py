"""
This is to test the numbering function for the module 34934A
the 'g' functions are copied from the table on P168 of the 34934A User's Guide
the 'f' function is a simplified version, see the keysight_34934A class for
detail
"""
from hypothesis import given
import hypothesis.strategies as st
from qcodes.instrument_drivers.Keysight.keysight_34980A_submodules import \
    Keysight_34934A


@given(
    st.sampled_from(("M1H", "M1L", "M2H", "M2L")),
    st.integers(1, 4),
    st.integers(1, 32)
)
def test_4x32(config, row, column):
    f = Keysight_34934A.get_numbering_function("4x32", config)
    g = numbering_function_4x32(config)
    assert f(row, column) == g(row, column)


@given(
    st.sampled_from(("MH", "ML")),
    st.integers(1, 4),
    st.integers(1, 64)
)
def test_4x64(config, row, column):
    f = Keysight_34934A.get_numbering_function("4x64", config)
    g = numbering_function_4x64(config)
    assert f(row, column) == g(row, column)


@given(
    st.integers(1, 4),
    st.integers(1, 128)
)
def test_4x128(row, column):
    f = Keysight_34934A.get_numbering_function("4x128")
    g = numbering_function_4x128()
    assert f(row, column) == g(row, column)


@given(
    st.sampled_from(("MH", "ML")),
    st.integers(1, 8),
    st.integers(1, 32)
)
def test_8x32(config, row, column):
    f = Keysight_34934A.get_numbering_function("8x32", config)
    g = numbering_function_8x32(config)
    assert f(row, column) == g(row, column)


@given(
    st.integers(1, 8),
    st.integers(1, 64)
)
def test_8x64(row, column):
    f = Keysight_34934A.get_numbering_function("8x64")
    g = numbering_function_8x64()
    assert f(row, column) == g(row, column)


@given(
    st.integers(1, 16),
    st.integers(1, 32)
)
def test_16x32(row, column):
    f = Keysight_34934A.get_numbering_function("16x32")
    g = numbering_function_16x32()
    assert f(row, column) == g(row, column)


def numbering_function_4x32(wiring_config):
    offsets = {
        "M1H": 0,
        "M2H": 32,
        "M1L": 64,
        "M2L": 96
    }

    def numbering_function(row, col):
        n = 100 * (2 * row - 1) + col + offsets[wiring_config]
        return str(int(n))

    return numbering_function


def numbering_function_4x64(wiring_config):
    offsets = {
        "MH": 0,
        "ML": 64
    }

    def numbering_function(row, col):
        n = 100 * (2 * row - 1) + col + offsets[wiring_config]
        return str(int(n))

    return numbering_function


def numbering_function_4x128():
    def numbering_function(row, col):
        n = 100 * (2 * row - 1) + col
        return str(int(n))

    return numbering_function


def numbering_function_8x32(wiring_config):
    offsets = {
        "MH": 0,
        "ML": 32
    }

    def numbering_function(row, col):
        n = 100 * row + col + offsets[wiring_config]
        return str(int(n))

    return numbering_function


def numbering_function_8x64():
    def numbering_function(row, col):
        n = 100 * row + col
        return str(int(n))

    return numbering_function


def numbering_function_16x32():
    def numbering_function(row, col):
        n = 50 * (row + 1) + col
        return str(int(n))

    return numbering_function
