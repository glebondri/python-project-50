from gendiff_package.gendiff import generate_diff


def test_generate_diff():
    diff1 = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
    diff2 = generate_diff('fixtures/file3.json', 'fixtures/file4.json')

    with (open('fixtures/output1.txt', 'r') as output1,
          open('fixtures/output2.txt', 'r') as output2):
        assert diff1 == output1.read()
        assert diff2 == output2.read()

    diff_empty = generate_diff('fixtures/empty_a.json', 'fixtures/empty_b.json')

    with open('fixtures/output_empty.txt', 'r') as empty:
        assert diff_empty == empty.read()
