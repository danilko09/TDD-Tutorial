import add

def test_two_numbers():
    assert add.Add("1,2") == 3

def test_three_numbers():
    assert add.Add("1,2,3") == 6

def test_different_separators():
    assert add.Add("1\n2,3") == 6

def test_split():
    assert add.split("1,2", [","]) == ['1','2']

def test_split_multiple_separators():
    assert add.split("1\n2,3", [",", "\n"]) == ['1','2','3']

def test_split_long_delimiter():
    assert add.split("1delim2", ['delim']) == ['1','2']
