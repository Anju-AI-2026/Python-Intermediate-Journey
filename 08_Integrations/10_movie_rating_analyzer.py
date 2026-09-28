# Store movie information
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "Titanic", "genre": "Romance", "rating": 7.9},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Coco", "genre": "Animation", "rating": 8.4},
    {"title": "Joker", "genre": "Drama", "rating": 8.1}
]


# Transform movie information
movie_records = list(
    map(
        lambda movie: {
            **movie,
            "category": (
                "Excellent" if movie["rating"] >= 8.5
                else "Good" if movie["rating"] >= 7.5
                else "Average"
            )
        },
        movies
    )
)


# Find movies rated 8.5 or above
top_rated_movies = list(
    filter(
        lambda movie: movie["rating"] >= 8.5,
        movie_records
    )
)


# Find movies belonging to the Sci-Fi genre
scifi_movies = list(
    filter(
        lambda movie: movie["genre"].lower() == "sci-fi",
        movie_records
    )
)


# Calculate average movie rating
average_rating = round(
    sum(movie["rating"] for movie in movie_records)
    / len(movie_records),
    2
)


# Find the highest-rated movie
highest_rated = max(
    movie_records,
    key=lambda movie: movie["rating"]
)


# Display all movies
print("\n" + "=" * 60)
print("             🎬 MOVIE RATING ANALYZER")
print("=" * 60)

print("\n📋 ALL MOVIES")
print("-" * 60)

for movie in movie_records:
    print(
        f"{movie['title']:<20} "
        f"{movie['genre']:<12} "
        f"Rating: {movie['rating']:<5} "
        f"{movie['category']}"
    )


print("\n🌟 TOP-RATED MOVIES (8.5 AND ABOVE)")
print("-" * 60)

for movie in top_rated_movies:
    print(f"{movie['title']:<25} {movie['rating']}")


print("\n🚀 SCI-FI MOVIES")
print("-" * 60)

for movie in scifi_movies:
    print(f"{movie['title']:<25} {movie['rating']}")


# Display summary
print("\n📊 MOVIE SUMMARY")
print("-" * 60)
print(f"Total movies       : {len(movie_records)}")
print(f"Top-rated movies   : {len(top_rated_movies)}")
print(f"Sci-Fi movies      : {len(scifi_movies)}")
print(f"Average rating     : {average_rating}")
print(f"Highest-rated movie: {highest_rated['title']}")
print(f"Highest rating     : {highest_rated['rating']}")
print("=" * 60)