import crawler
import yaml


def main():
    icons = crawler.fetch_icons()

    icon_dict = {
        'title': 'emojis',
        'emojis': []
    }

    for icon in icons:
        icon_dict['emojis'].append({ 'name': icon.name, 'src': icon.href })

    print(yaml.dump(icon_dict, default_flow_style=False))


if __name__ == '__main__':
    main()
