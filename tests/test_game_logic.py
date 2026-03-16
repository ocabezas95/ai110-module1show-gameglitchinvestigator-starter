import pytest
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# Tests for check_guess function
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


# Tests for get_range_for_difficulty function
def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 50


def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200


def test_unknown_difficulty_defaults_to_normal():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# Tests for parse_guess function
def test_parse_valid_integer_guess():
    ok, guess, error = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_float_as_integer():
    ok, guess, error = parse_guess("42.5")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_empty_string():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_none_input():
    ok, guess, error = parse_guess(None) # type: ignore
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_non_numeric_input():
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_parse_guess_too_low():
    ok, guess, error = parse_guess("0", low=1, high=100)
    assert ok is False
    assert guess is None
    assert error == "Out of range! Please guess between 1 and 100."


def test_parse_guess_too_high():
    ok, guess, error = parse_guess("101", low=1, high=100)
    assert ok is False
    assert guess is None
    assert error == "Out of range! Please guess between 1 and 100."


def test_parse_guess_in_custom_range():
    ok, guess, error = parse_guess("50", low=1, high=100)
    assert ok is True
    assert guess == 50
    assert error is None


# Tests for update_score function
def test_update_score_on_first_attempt_win():
    score = update_score(100, "Win", 1)
    assert score == 100


def test_update_score_on_second_attempt_win():
    score = update_score(85, "Win", 2)
    assert score == 85


def test_update_score_on_fifth_attempt_win():
    score = update_score(60, "Win", 5)
    assert score == 60


def test_update_score_minimum_points_on_win():
    score = update_score(5, "Win", 15)
    assert score == 5


def test_update_score_on_too_high():
    score = update_score(100, "Too High", 5)
    assert score == 95


def test_update_score_on_too_low():
    score = update_score(100, "Too Low", 3)
    assert score == 95


def test_update_score_accumulates():
    score = update_score(100, "Win", 1)
    score = update_score(score, "Too High", 2)
    assert score == 95
