import Subscene.Subtitle as Subtitle
import requests
def main():
    # put api or site subscene
    base_url = 'http://s.iranfilm.info'
    movie_name = input("Enter name movie : ")

    subtitle = Subtitle(base_url)

    print("1.TV-Series\n2.Popular")
    movies_category = int(input("enter what do you want ? : "))

    if movies_category is 1:
        movies = subtitle.search(movie_name, 'TV-Series')
    elif movies_category is 2:
        movies = subtitle.search(movie_name,'Popular')

    subtitle.show_movies(movies)
    movie_number = int(input("what do yo want ?"))

    subtitles_page_link = subtitle.get_subtitles_page_link(movies, movie_number-1)
    subtitles_node = subtitle.get_subtitles_node(subtitles_page_link)

    LANGUAGES = [
        'Farsi',
        'Arabic',
        'English',
        'French',
        'Indonesian',
        'Norwegian',
        'Romanian'
    ]

    subtitles_fa = subtitle.get_subtitles_node_lang(subtitles_node, lang=LANGUAGES[0])
    subtitle.show_subtitles_node(subtitles_fa)
    subtitle_number = int(input("enter what do you want be downloaded ? : "))

    subtitle_name = subtitle.get_subtitle_name(subtitles_fa[subtitle_number-1])
    subtitle_page_link = subtitle.get_subtitle_page_link(subtitles_fa, subtitle_number-1)

    subtitle_link = subtitle.get_subtitle_link(subtitle_page_link)
    filePath = "/home/bahram/Desktop/"
    connection = requests.get(subtitle_link).content

    file = open(filePath+subtitle_name+".zip","wb")
    file.write(connection)
    file.close()
    #Download(connection, subtitle_name+".zip",filePath)
    print(subtitle_page_link)
if __name__ == '__main__':
    main()
