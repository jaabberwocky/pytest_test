import pytest
from tobiasPackage import TobiasClass, prettyFunction

@pytest.fixture # can be received by any function as an argument
def testerclass():
    t = TobiasClass('James')
    return t

def test_getChars(testerclass):
    assert testerclass.name == 'James'

def test_prettyFunction(capsys):
    prettyFunction()
    captured = capsys.readouterr() # captures all
    assert captured.out == 'Hello from prettyFunction\n'
