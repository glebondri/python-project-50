from gendiff_package.gendiff import generate_diff


diff_1 = generate_diff('tests/fixtures/file1.json',
                       'tests/fixtures/file2.json')

diff_2 = generate_diff('tests/fixtures/file3.json',
                       'tests/fixtures/file4.json')

diff_empty = generate_diff('tests/fixtures/empty_a.json',
                           'tests/fixtures/empty_b.json')


def test_generate_diff():
    with (open('tests/fixtures/output1.txt', 'r') as output1,
          open('tests/fixtures/output2.txt', 'r') as output2):

        assert diff_1 == output1.read(), 'test "1" has been failed!'
        assert diff_2 == output2.read(), 'test "2" has been failed!'

    assert diff_empty == '{}', \
        'comparison of empty "a" & "b" should return empty brackets!'
