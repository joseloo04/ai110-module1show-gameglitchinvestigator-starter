from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# New tests for parse_guess
def test_parse_guess_valid_integer():
    ok, guess, err = parse_guess("42")
    assert ok == True
    assert guess == 42
    assert err is None

def test_parse_guess_valid_float():
    ok, guess, err = parse_guess("42.0")
    assert ok == True
    assert guess == 42
    assert err is None

def test_parse_guess_invalid_string():
    ok, guess, err = parse_guess("not a number")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_empty_string():
    ok, guess, err = parse_guess("")
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."

# New tests for update_score
def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score == 80  # 100 - 10*(1+1) = 80

def test_update_score_too_high_even_attempt():
    score = update_score(0, "Too High", 2)  # even attempt
    assert score == 5

def test_update_score_too_high_odd_attempt():
    score = update_score(0, "Too High", 1)  # odd attempt
    assert score == -5

def test_update_score_too_low():
    score = update_score(0, "Too Low", 1)
    assert score == -5

# New tests for get_range_for_difficulty
def test_get_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_get_range_invalid():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 100  # default
