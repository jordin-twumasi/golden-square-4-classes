from lib.grammar_stats import GrammarStats

"""
Return true if sentence starts with capital and ends with punctuation
"""
def test_true_given_starts_with_capital_and_ends_with_punctuation():
    stats = GrammarStats()
    assert stats.check('Hello, my name is Jo.') == True



"""
Return false if sentence starts with capital but doesn't end with punctuation
"""
def test_false_given_starts_with_capital_not_ends_with_punctuation():
    stats = GrammarStats()
    assert stats.check('Hello, my name is Jo') == False



"""
Return false if sentence doesn't start with capital and doesn't end with punctuation
"""
def test_false_given_not_starts_with_capital_not_ends_with_punctuation():
    stats = GrammarStats()
    assert stats.check('hello, my name is Jo') == False

"""
Return percentage of tests passed so far 25%
"""

def test_percentage_passed():
     stats = GrammarStats()
     stats.check('hello, my name is Jo') 
     stats.check('Hello, my name is Jo') 
     stats.check('Hello, my name is Jo.') 
     stats.check('hello, my name is Jo') 
     assert stats.percentage_good() == 25