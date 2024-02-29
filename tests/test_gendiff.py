from gendiff_package.gendiff import generate_diff

stylish_fixture = generate_diff('tests/fixtures/nested1.json',
                                'tests/fixtures/nested2.yml', 'stylish')

plain_fixture = generate_diff('tests/fixtures/nested1.json',
                              'tests/fixtures/nested2.yml', 'plain')

json_fixture = generate_diff('tests/fixtures/nested1.json',
                             'tests/fixtures/nested2.yml', 'json')


def test_gendiff():
    stylish_expected = open('tests/fixtures/output1.txt', 'r')
    plain_expected = open('tests/fixtures/output2.txt', 'r')
    json_expected = open('tests/fixtures/output3.txt', 'r')

    assert stylish_fixture == stylish_expected.read(), \
        'unexpected output for \'stylish\' format!'

    assert plain_fixture == plain_expected.read(), \
        'unexpected output for \'plain\' format!'

    assert json_fixture == json_expected.read(), \
        'unexpected output for \'json\' format!'
