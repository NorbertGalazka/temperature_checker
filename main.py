from bs4 import BeautifulSoup
import requests


def get_weather_site_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    return None


def get_temperature(soup) -> str:
    bs4_element = soup.find('span', {'class': "air-temp"})
    temperature = str(bs4_element)
    return temperature[-11:-7].strip()


def main():
    city = input('Dla jakiej miejscowości chcesz sprawdzić pogodę?: ')
    city_with_dash = city.replace(' ', '-')

    adress = f'https://www.pogodairadar.pl/pogoda/{city_with_dash}'

    return f'\nW miejscowości {city.title()} aktualna temperatura to' \
           f' {get_temperature(get_weather_site_html(adress))} Celsjusza'


if __name__ == '__main__':
    print(main())