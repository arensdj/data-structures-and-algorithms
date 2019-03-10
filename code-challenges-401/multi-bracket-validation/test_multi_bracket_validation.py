from multi_bracket_validation import multi_bracket_validation

def test_one_set_bracket():
    assert multi_bracket_validation('{}') == True

def test_multiple_set_brackets():
    assert multi_bracket_validation('{}(){}') == True
    
def test_unbalanced_brackets():
    assert multi_bracket_validation('(](') == False

def test_single_bracket():
    assert multi_bracket_validation('[') == False

def test_brackets_with_text():
    assert multi_bracket_validation('()[[Extra Characters]]') == True

def test_deep_multiple_set_brackets():
    assert multi_bracket_validation('(){}[[]]') == True

def test_deep_unbalanced_brackets():
    assert multi_bracket_validation('[({}]') == False
