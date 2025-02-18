import pytest
import form



def test_data_set():
    user1 = form.Form('Admin', 'qwerty')
    assert user1.name == 'Admin'
    assert user1.user_name == 'qwerty'
    assert user1.set_web_url('https://www.google.com/') == True
    assert user1.set_web_url('https://www.g1111gle.com/') == False
