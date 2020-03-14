import pytest

from workouts import print_workout_days, WORKOUTS


def test_print_workout_days_2_days(capfd):
    print_workout_days('lower')
    output = capfd.readouterr()[0].strip()
    assert output == 'Tue, Fri'

def test_print_workout_days_no_match(capfd):
    print_workout_days('squats')
    output = capfd.readouterr()[0].strip()
    assert output == 'No matching workout'

def test_print_workout_days_4_days(capfd):
    print_workout_days('body')
    output = capfd.readouterr()[0].strip()
    assert output == 'Mon, Tue, Thu, Fri'

def test_print_workout_days_all_days(capfd):
    print_workout_days(' ')
    output = capfd.readouterr()[0].strip()
    assert output == 'Mon, Tue, Wed, Thu, Fri'