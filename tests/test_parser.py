from checker.parser import SetupParser

from .utils import fixture_path


class TestSetupParser:
    """
    Tests parsing install_requires in different scenarios
    """

    def test_variable_reference(self):
        requirements = SetupParser(fixture_path('setup_reference.py')).parse()
        assert requirements == [
            'requests==2.23.0',
            'markdown',
        ]

    def test_variable_list(self):
        requirements = SetupParser(fixture_path('setup_list.py')).parse()
        assert requirements == [
            'requests==2.23.0',
            'markdown',
        ]

    def test_variable_empty(self):
        requirements = SetupParser(fixture_path('setup_empty.py')).parse()
        assert requirements == []
