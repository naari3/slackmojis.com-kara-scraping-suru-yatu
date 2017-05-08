import crawler
import requests


def prefix(filename):
    return f'./icons/{filename}'

def main():
    icons = crawler.fetch_icons()

    for icon in icons:
        icon_raw = requests.get(icon.href)
        with open(prefix(icon.download), 'wb') as icon_file:
            icon_file.write(icon_raw.content)


if __name__ == '__main__':
    main()
