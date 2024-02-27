from gendiff_package.gendiff import generate_diff

stylish_fixture = generate_diff('tests/fixtures/nested1.json',
                                'tests/fixtures/nested2.yml', 'stylish')
plain_fixture = generate_diff('tests/fixtures/nested1.json',
                              'tests/fixtures/nested2.yml', 'plain')


def test_gendiff():
    stylish_excepted = open('tests/fixtures/output1.txt', 'r')
    plain_excepted = open('tests/fixtures/output2.txt', 'r')

    assert stylish_fixture == stylish_excepted.read(), \
        'unexpected output for \'stylish\' format!'

    assert plain_fixture == plain_excepted.read(), \
        'unexpected output for \'plain\' format!'
