import pytest

from apis import apicorreios
from apis import apitrackingmore
from utils.misc import check_type


@pytest.mark.parametrize("code,carrier", (
    ("AB123456789CD", apicorreios),
    ("LP00147037652437", apitrackingmore),
    ("wrong-code", None),
))
def test_get_carrier_by_code(code, carrier):
    assert check_type(code) == carrier
