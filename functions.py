import requests
import json
import re


def on_key_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except KeyError:
            pass
    return wrapper


class ScrappingFunctions:
    def __init__(self, url, print_all=False):
        self.url = url
        self.print_all = print_all
        self.soup = None
        self.data = None
        self.information_dict = dict()
        self.setup_information_dict()

    def setup_information_dict(self):
        self.information_dict['artist'] = ''
        self.information_dict['title'] = ''
        self.information_dict['record'] = ''
        self.information_dict['year'] = ''
        self.information_dict['genre'] = ''

    def get_response(self) -> str:
        return requests.get(self.url).text

    def get_information(self):
        self.data = self.get_json_data()
        if self.data:
            self.get_artist()
            self.get_title()
            self.get_genre()
            self.get_year()
            self.get_records()

    def get_json_data(self):
        try:
            response = self.get_response()
            pattern = r'<script type="application\/ld\+json" id="release_schema">(.*?)<\/script>'
            results = re.search(pattern, response).group(1)
            return json.loads(results)
        except AttributeError:
            return None

    @on_key_error
    def get_artist(self):
        self.information_dict['artist'] = self.data['releaseOf']['byArtist'][0]['name']
        if self.print_all:
            print(f"ARTIST IS: {self.information_dict['artist']}")

    @on_key_error
    def get_title(self):
        self.information_dict['title'] = self.data['releaseOf']['name']
        if self.print_all:
            print(f"TITLE IS: {self.information_dict['title']}")

    @on_key_error
    def get_records(self):
        self.information_dict['record'] = self.data['recordLabel'][0]['name']
        if 'Records' in self.information_dict['record']:
            self.information_dict['record'] = self.information_dict['record'].replace('Records', '').strip()
        if self.print_all:
            print(f"RECORD IS: {self.information_dict['record']}")

    @on_key_error
    def get_year(self):
        self.information_dict['year'] = str(self.data['releaseOf']['datePublished'])
        if self.print_all:
            print(f"YEAR IS: {self.information_dict['year']}")

    @on_key_error
    def get_genre(self):
        genre_list = [element.strip().upper() for element in self.data['genre']]

        if 'STAGE & SCREEN' in genre_list:
            self.information_dict['genre'] = 'STAGE & SCREEN'
        elif "CHILDREN'S" in genre_list:
            self.information_dict['genre'] = "CHILDREN'S"
        else:
            self.information_dict['genre'] = genre_list[0]

        if 'FUNK / SOUL' in self.information_dict['genre']:
            self.information_dict['genre'] = 'FUNK'
        elif 'STAGE & SCREEN' in self.information_dict['genre']:
            self.information_dict['genre'] = 'FILMOWA'
        elif 'FOLK, WORLD, & COUNTRY' in self.information_dict['genre']:
            self.information_dict['genre'] = 'FOLK'
        elif 'ELECTRONIC' in self.information_dict['genre']:
            self.information_dict['genre'] = 'ELEKTRONICZNA'
        elif 'CLASSICAL' in self.information_dict['genre']:
            self.information_dict['genre'] = 'KLASYCZNA'
        elif 'HIP HOP' in self.information_dict['genre']:
            self.information_dict['genre'] = 'RAP'
        elif "CHILDREN'S" in self.information_dict['genre']:
            self.information_dict['genre'] = 'DLA DZIECI'
        elif "NON-MUSIC" in self.information_dict['genre']:
            self.information_dict['genre'] = 'POZOSTAŁE'
        elif "BRASS & MILITARY" in self.information_dict['genre']:
            self.information_dict['genre'] = 'POZOSTAŁE'
        if self.print_all:
            print(f"GENRE IS: {self.information_dict['genre']}")


if __name__ == '__main__':
    url0 = 'https://www.discogs.com/Chicago-Chicago-V/release/941534'
    url1 = 'https://www.discogs.com/Metallica-Ride-The-Lightning/release/8381512'
    url2 = 'https://www.discogs.com/Queen-Queen-II/release/10542595'
    url_test = 'https://www.discogs.com/master/55658-Paul-Simon-Graceland'
    # test = ScrappingFunctions(url_test, print_all=True)
    # test.get_information()
    response = requests.get(url2)
    pattern = '<script type="application\/ld\+json" id="release_schema">(.*?)<\/script>'
    results = re.search(pattern, response.text).group(1)
    temp = json.loads(results)
    print(json.dumps(temp, indent=2))
