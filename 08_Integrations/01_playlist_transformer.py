# Store all song names
songs = []


# Get song names from the user
def new_songs(songs):

    # Keep asking until the song input process is completed
    while True:

        song_number = input("How many songs are there ? :")

        # Check whether the entered value contains only alphabets
        if song_number.isalpha():
            print("Please enter a valid number :")
            break

        song_number = int(song_number)

        # Repeat the process according to the number of songs
        for _ in range(0, song_number):

            while True:

                song_name = input("Enter a song name :")

                if song_name.isnumeric():
                    print("Song name should not be a number ")
                    break

                else:
                    songs.append(song_name)
                    break

        return


new_songs(songs)

# Display original song names
print("Before Song names :", songs)


# Capitalize song names using map()
def capital_name(name):
    return name.capitalize()


new_songs_name = list(map(capital_name, songs))

# Display transformed song names
print("After song name :", new_songs_name)