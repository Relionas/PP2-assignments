import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_tracks()

        self.index = 0
        self.is_playing = False

    def load_tracks(self):
        files = []
        for f in os.listdir(self.music_folder):
            if f.endswith((".mp3", ".wav")):
                files.append(os.path.join(self.music_folder, f))
        return files

    def load_current(self):
        pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        if not self.playlist:
            return
        if not self.is_playing:
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.load_current()
        pygame.mixer.music.play()

    def previous(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.load_current()
        pygame.mixer.music.play()

    def get_current_track(self):
        return os.path.basename(self.playlist[self.index])

    def get_pos(self):
        return pygame.mixer.music.get_pos() // 1000