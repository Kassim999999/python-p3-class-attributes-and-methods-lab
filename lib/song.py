class Song:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    count = 0

    @classmethod
    def add_song_to_count(self):
        self.count += 1

    genres = []

    @classmethod
    def add_to_genres(self, genre):
        if genre not in self.genres:
         self.genres.append(genre)

    artists = []

    @classmethod
    def add_to_artists(self, artist):
       if artist not in self.artists:
          self.artists.append(artist)


    genre_count= {}

    @classmethod
    def add_to_genre_count(self, genre):
       if genre in self.genre_count:
          self.genre_count[genre] += 1
       else:
          self.genre_count[genre] = 1

    artist_count= {}

    @classmethod
    def add_to_artist_count(self, artist):
       if artist in self.artist_count:
          self.artist_count[artist] += 1
       else:
          self.artist_count[artist] = 1

