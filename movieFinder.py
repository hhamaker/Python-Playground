import urllib.request as urllib2
import ssl
import datetime
import json

class Movie(object):
    def __init__(self, Title, Year, Rated, Released, Runtime, Genre, Director, Writer, Actors, Plot, Language, Country, Awards, Poster, Ratings, Metascore, imdbRating, imdbID, Type, DVD, BoxOffice, Production, Website, Response):
        self.Title = Title
        self.Year = Year
        self.Released = Released
        self.Runtime = Runtime
        self.Genre = Genre
        self.Director = Director
        self.Writer = Writer
        self.Actors = Actors
        self.Plot = Plot
        self.Language = Language
        self.Country = Country
        self.Awards = Awards
        self.Poster = Poster
        self.Ratings = Ratings
        self.Metascore = Metascore
        self.imdbRating = imdbRating
        self.imdbID = imdbID
        self.Type = Type
        self.DVD = DVD
        self.BoxOffice = BoxOffice
        self.Production = Production
        self.Website = Website
        self.Response = Response
        
#makes a get call to robinhood quotes to get the stock info
def getMovie(movie):
    #don't use this too frequently as I am limited to 1000 callouts per month.
    credential = ''
    url = 'http://www.omdbapi.com/?i=' + credential + '=' + movie
    context = ssl._create_unverified_context()
    content = urllib2.urlopen(url, context=context).read()
    return content

def calculateYears(releaseYear):
    now = datetime.datetime.now()
    yearsSince = str(now.year - int(releaseYear))
    print ("That Movie is " +  yearsSince + " years old!")

movieName = 'FootLoose'
response = getMovie(movieName)
movie = json.loads(response)
year = movie["Year"]
calculateYears(year)