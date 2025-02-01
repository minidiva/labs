# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def isAbove55(movie):
    for x in movies:
        if x["name"] == movie:
            if x["imdb"] > 5.5:
                return True
            else:
                return False
    return False
        
# print(isAbove55("We Two"))

def goodMovies():
    goodmovies = []
    
    for x in movies:
        if x["imdb"] > 5.5:
            goodmovies.append(x["name"])
        else:
            continue
    return goodmovies
    
# print(goodMovies())

def categoryFilter(category):
    filteredlst = []

    for x in movies:
        if x["category"] == category:
            filteredlst.append(x["name"])
        else:
            continue
    return filteredlst

# print(categoryFilter("Romance"))

def AVGIMDB(movie):
    AVG = 0
    for x in movie:
        AVG += x["imdb"]

    AVG /= len(movie)
    return AVG

# print(AVGIMDB(movies))

def AVGIMDB_category(category):
    AVG = 0
    n = 0
    for x in movies:
        if x["category"] == category:
            AVG += x["imdb"]
            n += 1

    AVG /= n
    return AVG

# print(AVGIMDB_category("Romance"))