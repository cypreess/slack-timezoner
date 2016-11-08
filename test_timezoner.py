import datetime

import pytz

from timezoner import convert_to_time, process, parse_text_time


def test_parse_text_time_1a():
    assert parse_text_time("Lets meet at 7pm") == [(7, 0, 'pm')]


def test_parse_text_time_1b():
    assert parse_text_time("Lets meet at 7PM") == [(7, 0, 'pm')]


def test_parse_text_time_1c():
    assert parse_text_time("Lets meet at 7 PM") == [(7, 0, 'pm')]


def test_parse_text_time_1d():
    assert parse_text_time("Lets meet at 7 pm") == [(7, 0, 'pm')]


def test_parse_text_time_1e():
    assert parse_text_time("Lets meet at 7:01pm") == [(7, 1, 'pm')]


def test_parse_text_time_1f():
    assert parse_text_time("Lets meet at 7:01PM") == [(7, 1, 'pm')]


def test_parse_text_time_1g():
    assert parse_text_time("Lets meet at 7:01 PM") == [(7, 1, 'pm')]


def test_parse_text_time_1h():
    assert parse_text_time("Lets meet at 7:01 pm") == [(7, 1, 'pm')]


def test_parse_text_time_2a():
    assert parse_text_time("Lets meet at 7") == []


def test_parse_text_time_2b():
    assert parse_text_time("Lets meet at 7:01") == [(7, 1, '')]


def test_parse_text_time_2c():
    assert parse_text_time("Lets meet at 17:01") == [(17, 1, '')]


def test_parse_text_time_3():
    assert parse_text_time(
        "<@U02LBM6HH> there are two possible hours: "
        "12:30 and 16:30 11pm or 8:30 am (this is a test)") == [
               (12, 30, ''),
               (16, 30, ''),
               (11, 0, 'pm'),
               (8, 30, 'am')
           ]


def test_convert_to_time():
    now = datetime.datetime.now()
    convert_to_time(1, 0, 'am', 'Europe/Warsaw') == datetime.datetime(
        year=now.year, month=now.month, day=now.day,
        hour=1, minute=0,
        tzinfo=pytz.timezone('Europe/Warsaw'))


def test_process():
    assert process("Lets meet at 17:35", 'Europe/Warsaw',
                   [('Europe/Warsaw', 'H:m'), ('US/Pacific', 'h:m a')]) == [
               ('17:35', [('Europe/Warsaw', 'H:m'), ('US/Pacific', 'h:m a')])]
    assert process("Lets meet at 17:35 or 18:35", 'Europe/Warsaw',
                   [('Europe/Warsaw', 'H:m'), ('US/Pacific', 'I:m p')]) == []
