import pytest
import os
from gendiff.comparison import generate_diff

FIXTURES = r'tests/fixtures/'
EXPECTED = os.path.join(FIXTURES, 'expected/')


# stylish_fixture = generate_diff('tests/fixtures/nested1.json',
#                                 'tests/fixtures/nested2.yml', 'stylish')
#
# plain_fixture = generate_diff('tests/fixtures/nested1.json',
#                               'tests/fixtures/nested2.yml', 'plain')
#
# json_fixture = generate_diff('tests/fixtures/nested1.json',
#                              'tests/fixtures/nested2.yml', 'json')
#
# pytest.mark.parametrize()
# def test_gendiff():
#     stylish_expected = open('tests/fixtures/output1.txt', 'r')
#     plain_expected = open('tests/fixtures/output2.txt', 'r')
#     json_expected = open('tests/fixtures/output3.txt', 'r')
#
#     assert stylish_fixture == stylish_expected.read(), \
#         'unexpected output for \'stylish\' format!'
#
#     assert plain_fixture == plain_expected.read(), \
#         'unexpected output for \'plain\' format!'
#
#     assert json_fixture == json_expected.read(), \
#         'unexpected output for \'json\' format!'


# stylish_expected = open('tests/fixtures/output1.txt', 'r')
# plain_expected = open('tests/fixtures/output2.txt', 'r')
# json_expected = open('tests/fixtures/output3.txt', 'r')
#
# format_pairs = [
#     (stylish_fixture, stylish_expected),
#     (plain_fixture, plain_expected),
#     (json_fixture, json_expected),
# ]
#
#
# @pytest.mark.parametrize('fixture, expected', format_pairs)
# def test_parametrize(fixture, expected):
#     assert fixture == expected.read()

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
