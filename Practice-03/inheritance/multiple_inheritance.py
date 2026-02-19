class Camera:
    def take_photo(self):
        print("Photo taken.")

class Player:
    def play_music(self):
        print("Music playing.")

class Phone(Camera, Player):
    pass

p = Phone()
p.take_photo()
p.play_music()