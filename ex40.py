class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

first_song = ["Happy birthday to you",
"I don't want to get sued",
"So I stop right here"]

happy_bday = Song(first_song)

second_song = ["They rally around tha family", "With pocketes full of shells"]

bulls_on_parade = Song(second_song)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
