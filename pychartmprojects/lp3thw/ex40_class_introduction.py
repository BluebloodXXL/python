class Song(object):
    # Inheriting the object class
    # Making a Class named Song that is-a object
    # Python 3 does not need extending the object class
    def __init__(self, lyrics):
        # Class Song has a __init__ that takes self and lyrics parameters
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # Class Song has a sing_me_a_song function
        # that takes self parameter and act on
        # class's lyrics parameter
        for line in self.lyrics:
            print(line)


class MyStuff:

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM A CLASSY APPLE!")


happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"
                        ])

objThing = MyStuff()

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

objThing.apple()
print(objThing.tangerine)
objThing.tangerine = "This is going to be different."
print(objThing.tangerine)
