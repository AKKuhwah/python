import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def get_tv_details(tv):
    return str(tv)

#__init__ method
def test_init(tv):
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'


#power method
def test_power(tv):
    tv.power()
    assert get_tv_details(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.power()
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'


#mute method
def test_mute(tv):
    tv.power()

    tv.mute()
    assert get_tv_details(
        tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert get_tv_details(
        tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.power()
    tv.mute()
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'


#channel_up method
def test_channel_up(tv):
    tv.channel_up()
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_up()
    assert get_tv_details(
        tv) == 'Power = True, Channel = 1, Volume = 0'

    tv._Television__channel = tv.MAX_CHANNEL  # Set channel to max
    tv.channel_up()
    assert get_tv_details(
        tv) == 'Power = True, Channel = 0, Volume = 0'


#channel_down method
def test_channel_down(tv):
    tv.channel_down()
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_down()
    assert get_tv_details(tv) == 'Power = True, Channel = 3, Volume = 0'

    tv._Television__channel = tv.MIN_CHANNEL  # Set channel to min
    tv.channel_down()
    assert get_tv_details(tv) == 'Power = True, Channel = 3, Volume = 0'


#volume_up method
def test_volume_up(tv):
    tv.volume_up()
    assert get_tv_details(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.volume_up()
    assert get_tv_details(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.volume_up()
    assert get_tv_details(tv) == 'Power = True, Channel = 0, Volume = 2'

    tv.mute()
    tv.volume_up()
    assert get_tv_details(tv) == 'Power = True, Channel = 0, Volume = 3'
