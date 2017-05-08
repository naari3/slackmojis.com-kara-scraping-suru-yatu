import requests
from bs4 import BeautifulSoup


ICONS_TITLE = 'Logo'


class Icon(object):
    """docstring for Icon."""
    def __init__(self, element=None, name=None, emoji_id=None, emoji_id_name=None, download=None, href=None):
        self.download = download or element.attrs['download']
        self.emoji_id = emoji_id or element.attrs['data-emoji-id']
        self.emoji_id_name = emoji_id_name or element.attrs['data-emoji-id-name']
        self.href = href or element.attrs['href']
        self.name = name or element.find(class_='name').text.replace('\n', '').replace(':', '')

    def __repr__(self):
        return f'<Icon {self.emoji_id} {self.name}>'


def fetch_icons():
    result = requests.get('https://slackmojis.com/')
    html = result.text

    soup = BeautifulSoup(html, "lxml")
    soup.find_all('div', class_='title')

    icons_titles = soup.find_all('div', class_='title')

    for icon_title in icons_titles:
        if ICONS_TITLE in icon_title.next_element:
            icon_elements = icon_title.next_element.next_element.next_element
            break

    icons = icon_elements.find_all(class_='downloader')
    icon_list = []
    for icon in icons:
        icon_list.append(Icon(icon))

    return icon_list
