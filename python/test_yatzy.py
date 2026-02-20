from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance():
        d1 = d2 = d3 = d4 = d5 = 5
        expected = 25
        assert Yatzy.chance(d1,d2,d3,d4,d5) == expected

def test_yatzy():        
        assert Yatzy.yatzy(Yatzy(1,1,1,1,1)) == 50

def test_not_yatzy():
        assert Yatzy.yatzy(Yatzy(1,1,2,1,1)) == 0

def test_ones():
        assert Yatzy.ones(1,1,1,2,3) == 3

def test_twos():
        assert Yatzy.twos(1,1,2,2,3) == 4

def test_threes():
        assert Yatzy.threes(1,1,2,3,3) == 6

def test_fours():
        assert Yatzy.fours(Yatzy(1,2,4,4,4)) == 12

def test_fives():
        assert Yatzy.fives(Yatzy(1,2,3,5,5)) == 10

def test_sixes():
        assert Yatzy.sixes(Yatzy(1,2,4,6,6)) == 12

def test_score_pair():
        assert Yatzy.score_pair(1,1,6,2,6) == 12

def test_two_pair():
        assert Yatzy.two_pair(1,2,2,4,4) == 12

def test_three_of_a_kind():
        assert Yatzy.three_of_a_kind(3,3,3,4,5) == 9

def test_four_of_a_kind():
        assert Yatzy.four_of_a_kind(2,2,2,2,5) == 8

def test_small_straight():
        assert Yatzy.smallStraight(1,2,3,4,5) == 15

def test_large_straight():
        assert Yatzy.largeStraight(2,3,4,5,6) == 20

def test_full_house():
        assert Yatzy.fullHouse(1,1,2,2,2) == 8


