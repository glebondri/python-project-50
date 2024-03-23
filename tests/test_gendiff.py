import pytest
import os
from gendiff.comparison import generate_diff

FIXTURES = r'tests/fixtures/'
EXPECTED = os.path.join(FIXTURES, 'expected/')


@pytest.mark.parametrize('format',
                         ['stylish', 'plain', 'json'])
def test_gendiff(format):
    fixture_json = os.path.join(FIXTURES, 'fixture.json')
    fixture_yml = os.path.join(FIXTURES, 'fixture.yml')
    expected_path = os.path.join(EXPECTED,
                                 format + '.txt')

    if not os.path.exists(expected_path):
        raise Exception(f'Couldn\'t find sample for \"{format}\" format!')

    fixture = generate_diff(fixture_json,
                            fixture_yml, format)
    expected = open(expected_path, 'r')

    assert fixture == expected.read()
