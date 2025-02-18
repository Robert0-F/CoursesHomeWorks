import requests

class Form:
    def __init__(self, name=None, user_name=None, email=None, url=None):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.url = url

    def set_web_url(self, site_url=None):
        if site_url is None:
            url = self.url
        else:
            url = site_url

        try:
            res = requests.get(url)
            return True
        except Exception:
            return False


form = Form('Admin', "qwerty")

form2 = Form('Modest', 'qwerty123', 'example@mail.ru', 'https://itproger.com')

print(form.set_web_url('https://itpr23232oger.com'))