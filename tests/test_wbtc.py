import pytest

@pytest.fixture
def wbtc(interface):
  yield interface.IERC20("0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f");

def test_wbtc(wbtc):
    print(wbtc.totalSupply())