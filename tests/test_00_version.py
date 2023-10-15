import cf2cdm


def test_version() -> None:
    assert cf2cdm.__version__ != "999"
