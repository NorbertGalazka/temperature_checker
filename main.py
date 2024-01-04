from bs4 import BeautifulSoup
import requests


def get_weather_site_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')


def get_temperature(soup) -> str:
    try:
        bs4_element = soup.find('span', {'class': "air-temp"})
        temperature = str(bs4_element.text)
        return temperature.strip()
    except AttributeError:
        print('Niestety, nie ma takiej miejscowości')


def main():
    again = 'Wpisz miasto'
    while True:
        city = input(f'{again}, dla którego chcesz sprawdzić pogodę: ')
        city_with_dash = city.replace(' ', '-')

        adress = f'https://www.pogodairadar.pl/pogoda/{city_with_dash}'
        temperature = get_temperature(get_weather_site_html(adress))
        if temperature:
            return f'\nW miejscowości {city.title()} aktualna temperatura to' \
                f' {get_temperature(get_weather_site_html(adress))} Celsjusza'
        else:
            again = '\nSpróbuj ponownie wpisać miasto'
            continue


if __name__ == '__main__':
    print(main())
