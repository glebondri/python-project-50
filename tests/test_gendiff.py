from gendiff_package.gendiff import generate_diff
from gendiff_package.formation import format_stylish


plain = generate_diff('tests/fixtures/plain1.json',
                      'tests/fixtures/plain2.json')
nested = generate_diff('tests/fixtures/nested1.json',
                       'tests/fixtures/nested2.yml')


def test_gendiff():
    excepted = open('tests/fixtures/output1.txt', 'r')

    empty = generate_diff('tests/fixtures/empty.json',
                          'tests/fixtures/empty.json')

    assert str(nested) == excepted.read(), 'unexpected output!'
    assert empty == [], 'diff could be empty!'


def test_gendiff_formation():
    formatted_plain = format_stylish(plain)
    formatted_nested = format_stylish(nested)

    expected_plain = open('tests/fixtures/output2.txt', 'r')
    expected_nested = open('tests/fixtures/output3.txt', 'r')

    assert formatted_plain == expected_plain.read(), \
        'unexpected output for plain data!'

    assert formatted_nested == expected_nested.read(), \
        'unexpected output for plain data'
