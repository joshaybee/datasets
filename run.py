
from fortune import fortunate_tweet as ft

if __name__ == '__main__':
    cookie = ft.generate_fortune_cookie()
    ft.send_to_twitter(cookie)
