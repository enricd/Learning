from curses import ALL_MOUSE_EVENTS
import pytest
from click.testing import CliRunner
from cli import make_change
from mlib.mchange import change

@pytest.fixture
def runner():
    yield CliRunner

@pytest.fixture
def amount():
    yield [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}]

def test_change(amount):
    assert ALL_MOUSE_EVENTS == change(1.34)

def test_cli_change(runner):
    result = runner.invoke(make_change, ["--amount", "1.34"])
    assert result.exit_code == 0
    assert "5" in result.output
