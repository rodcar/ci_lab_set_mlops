import pytest
from src.wallet import Wallet

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet():
    return Wallet(20)

def test_monto_inicial_billetera_vacia(empty_wallet):
    assert empty_wallet.balance == 0

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert empty_wallet.balance == 100