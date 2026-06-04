# Movie Recommendation System

movies = [
    # ----------- ENGLISH MOVIES -----------

    # Action
    {"title": "Avengers: Endgame", "genre": "action", "lang": "english"},
    {"title": "John Wick", "genre": "action", "lang": "english"},
    {"title": "Mad Max: Fury Road", "genre": "action", "lang": "english"},
    {"title": "The Dark Knight", "genre": "action", "lang": "english"},
    {"title": "Gladiator", "genre": "action", "lang": "english"},
    {"title": "Mission Impossible", "genre": "action", "lang": "english"},
    {"title": "Die Hard", "genre": "action", "lang": "english"},

    # Comedy
    {"title": "The Hangover", "genre": "comedy", "lang": "english"},
    {"title": "Superbad", "genre": "comedy", "lang": "english"},
    {"title": "Home Alone", "genre": "comedy", "lang": "english"},
    {"title": "Deadpool", "genre": "comedy", "lang": "english"},
    {"title": "Step Brothers", "genre": "comedy", "lang": "english"},
    {"title": "Mask", "genre": "comedy", "lang": "english"},
    {"title": "Rush Hour", "genre": "comedy", "lang": "english"},

    # Romance
    {"title": "Titanic", "genre": "romance", "lang": "english"},
    {"title": "The Notebook", "genre": "romance", "lang": "english"},
    {"title": "La La Land", "genre": "romance", "lang": "english"},
    {"title": "Before Sunrise", "genre": "romance", "lang": "english"},
    {"title": "Me Before You", "genre": "romance", "lang": "english"},
    {"title": "The Fault in Our Stars", "genre": "romance", "lang": "english"},
    {"title": "Notting Hill", "genre": "romance", "lang": "english"},

    # Sci-Fi
    {"title": "Interstellar", "genre": "sci-fi", "lang": "english"},
    {"title": "Inception", "genre": "sci-fi", "lang": "english"},
    {"title": "The Matrix", "genre": "sci-fi", "lang": "english"},
    {"title": "Gravity", "genre": "sci-fi", "lang": "english"},
    {"title": "Blade Runner 2049", "genre": "sci-fi", "lang": "english"},
    {"title": "Avatar", "genre": "sci-fi", "lang": "english"},
    {"title": "Arrival", "genre": "sci-fi", "lang": "english"},

    # Horror
    {"title": "The Conjuring", "genre": "horror", "lang": "english"},
    {"title": "It", "genre": "horror", "lang": "english"},
    {"title": "Insidious", "genre": "horror", "lang": "english"},
    {"title": "A Quiet Place", "genre": "horror", "lang": "english"},
    {"title": "The Nun", "genre": "horror", "lang": "english"},
    {"title": "Annabelle", "genre": "horror", "lang": "english"},
    {"title": "The Ring", "genre": "horror", "lang": "english"},

    # ----------- TAMIL MOVIES -----------

    # Action
    {"title": "Vikram", "genre": "action", "lang": "tamil"},
    {"title": "Kaithi", "genre": "action", "lang": "tamil"},
    {"title": "Master", "genre": "action", "lang": "tamil"},
    {"title": "Theri", "genre": "action", "lang": "tamil"},
    {"title": "Mersal", "genre": "action", "lang": "tamil"},
    {"title": "Sarkar", "genre": "action", "lang": "tamil"},
    {"title": "Anjaan", "genre": "action", "lang": "tamil"},

    # Comedy
    {"title": "Boss Engira Bhaskaran", "genre": "comedy", "lang": "tamil"},
    {"title": "OK OK", "genre": "comedy", "lang": "tamil"},
    {"title": "Kalakalappu", "genre": "comedy", "lang": "tamil"},
    {"title": "Varuthapadatha Valibar Sangam", "genre": "comedy", "lang": "tamil"},
    {"title": "Thillu Mullu", "genre": "comedy", "lang": "tamil"},
    {"title": "Soodhu Kavvum", "genre": "comedy", "lang": "tamil"},
    {"title": "Panchathanthiram", "genre": "comedy", "lang": "tamil"},

    # Romance
    {"title": "96", "genre": "romance", "lang": "tamil"},
    {"title": "Vinnaithaandi Varuvaayaa", "genre": "romance", "lang": "tamil"},
    {"title": "OK Kanmani", "genre": "romance", "lang": "tamil"},
    {"title": "Minnale", "genre": "romance", "lang": "tamil"},
    {"title": "Alaipayuthey", "genre": "romance", "lang": "tamil"},
    {"title": "Raja Rani", "genre": "romance", "lang": "tamil"},
    {"title": "Remo", "genre": "romance", "lang": "tamil"},

    # Sci-Fi
    {"title": "Enthiran", "genre": "sci-fi", "lang": "tamil"},
    {"title": "2.0", "genre": "sci-fi", "lang": "tamil"},
    {"title": "Indru Netru Naalai", "genre": "sci-fi", "lang": "tamil"},
    {"title": "24", "genre": "sci-fi", "lang": "tamil"},
    {"title": "Maanaadu", "genre": "sci-fi", "lang": "tamil"},
    {"title": "Tik Tik Tik", "genre": "sci-fi", "lang": "tamil"},
    {"title": "Dasavathaaram", "genre": "sci-fi", "lang": "tamil"},

    # Horror
    {"title": "Aranmanai", "genre": "horror", "lang": "tamil"},
    {"title": "Kanchana", "genre": "horror", "lang": "tamil"},
    {"title": "Demonte Colony", "genre": "horror", "lang": "tamil"},
    {"title": "Pizza", "genre": "horror", "lang": "tamil"},
    {"title": "Maya", "genre": "horror", "lang": "tamil"},
    {"title": "Aval", "genre": "horror", "lang": "tamil"},
    {"title": "Yaamirukka Bayamey", "genre": "horror", "lang": "tamil"},
]

print("\n ------- WELCOM TO MOVIE RECOMMENDATION SYSTEM ------- \n")

language = input("Choose Language (Tamil/English): ").lower()
genres_input = input("Enter Preferred Genres : ").lower()

user_genres = [g.strip() for g in genres_input.split(",")]

recommendations = []

# Scoring logic
for movie in movies:
    score = 0

    if movie["lang"] == language:
        score += 2   # language match

    if movie["genre"] in user_genres:
        score += 3   # genre match

    if score > 0:
        recommendations.append((movie["title"], score))

# Sort by score (highest first)
recommendations.sort(key=lambda x: x[1], reverse=True)

# Output
if recommendations:
    print("\nTOP RECOMMENDATIONS:\n")
    for movie, score in recommendations[:10]:
        print(f" {movie} (Score: {score})")
else:
    print(" NO RECOMMENDATIONS FOUND!")