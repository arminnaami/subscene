from bs4 import BeautifulSoup
import requests
from .Tools import Tools
class Subtitle:
    def __init__(self, base_url):
        self.base_url = base_url
        self.name = None

    def __parse_url(self, url):
        '''
        get url and parse with BeautifulSoup
        '''
        url_file = requests.get(url).text
        return BeautifulSoup(url_file, 'lxml')

    def __create_search_page(self):
        '''
        create url search page then parse with BeautifulSoup
        '''
        return self.__parse_url(self.base_url+'/subtitles/title?l=&q='+self.name)

    def __get_movie(self, category):
        '''
        find all link subtitles page based on genere
        '''
        search_result = self.__create_search_page().find('div', class_='search-result')
        headers = search_result.find_all('h2')
        i = 0
        for header in headers:
            if header.text == category:
                break
            i = i + 1
        categories = search_result.find_all('ul')
        return categories[i].find_all('a')

    def search(self, name, category="TV-Series"):
        '''
        get movie name and movie category for searching
        '''
        name = Tools(name).change_space_to_plus()
        self.name = name
        movies = self.__get_movie(category)
        return movies

    def show_movies(self, movies):
        '''
        show all movies base on selected category
        '''
        for index,movie in enumerate(movies):
            print(index+1, " : ",movie.text)

    def get_subtitles_page_link(self, movies, index):
        '''
        get movies and index then return subtitles page link for selected movie
        '''
        return movies[index]['href']

    def get_subtitles_node(self, subtitles_page_link):
        '''
        get subtitles page link then return all sutitles node
        '''
        subtitles_page = self.__parse_url(subtitles_page_link)
        return subtitles_page.find_all('td', class_='a1')

    def get_subtitles_node_lang(self, subtitles_node, lang='Farsi'):
        '''
        get all subtitles node base on selected language
        '''
        subtitles = []
        for subtitle in subtitles_node:
            if lang in subtitle.span.text:
                subtitles.append(subtitle)
        return subtitles

    def show_subtitles_node(self, subtitles_node):
        '''
        get subtitles_node then show all details
        '''
        for index,subtitle in enumerate(subtitles_node):
            subtitle_name = self.get_subtitle_name(subtitle)
            print(index+1, " : ", subtitle_name)

    def get_subtitle_name(self, subtitle):
        '''
        get one subtitle node then return subtitle name
        '''
        subtitle_name = subtitle.find_all('span')[1].text
        subtitle_name = Tools(subtitle_name).remove_spaces_enter_tab()
        return subtitle_name

    def get_subtitle_page_link(self, subtitles_node,index):
        '''
        get subtitles_node and index and return subtitle page link
        '''
        return subtitles_node[index].a['href']

    def get_subtitle_link(self, subtitle_page_link):
        '''
        get subtitle page link then return download link
        '''
        bottom_download = self.__parse_url(subtitle_page_link).find('div', 'download')
        return bottom_download.a['href']
