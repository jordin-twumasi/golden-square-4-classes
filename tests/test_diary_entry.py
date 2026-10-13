from lib.diary_entry import DiaryEntry

"""
Given title and contents, return formatted string

"""

def test_given_title_and_contents_return_formatted_string():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.format() == 'My Title: These are the contents.'

"""
Given contents, return number of words in the entry

"""

def test_given_contents_return_word_count():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.count_words() == 4

"""
Given average wpm of 2 , return reading time 

"""
def test_given_wpm_return_reading_time():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.reading_time(2) == 2

"""
Given wpm and amount of time user has to read, return string og amount of text that can be read
wpm: 2, time to read: 1 minute
"""

def test_given_wpm_and_time_return_chunk_to_read_in_given_time():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.reading_chunk(2,1) == 'These are'

"""
If reading chunk called again, return next chunk
"""

def test_return_next_chunk_to_read_in_given_time():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.reading_chunk(2,1) == "These are"
    assert entry.reading_chunk(2,1) == "the contents."

"""
If all chunks read start again
"""


def test_given_all_contents_returned_restart_contents():
    entry = DiaryEntry('My Title', 'These are the contents.')
    assert entry.reading_chunk(2,1) == "These are"
    assert entry.reading_chunk(2,1) == "the contents."
    assert entry.reading_chunk(2,1) == "These are"
