import csv
import os
import random

# Class to hold song information (songList) which holds a list of lists:
# Lists contain [song name, album name, album release date, and duration (in seconds)]
#

"""
Class 1:
    Make init method to hold:
    Song name
    Album name
    Album release date
    Duration (in seconds)

Class 2:

    Method 1:
        Reads information from the file and makes a list 
        Lists contain [song name, album name, album release date, and duration (in seconds)]
        Add all song lists into a main list with every song

    Method 2:
        Makes a dictionary that holds each different song from each album


@author Ryan Schatzberg
@version 2/27/2025
"""

class GetSong:
    def __init__(self, song_name, album_name, album_release, duration_ms):
        self.song_name = song_name
        self.album_name = album_name
        self.album_release = album_release
        self.duration_ms = duration_ms

    def __str__(self):
        return "{}, {}, {}, {}".format(self.song_name, self.album_name, self.album_release, float(self.duration_ms))

class GetAlbum:
    def __init__(self, filepath="data/taylor_all_songs.csv", shuffled=False, amount=5):
        self.filepath = filepath
        self.albums = self.read_csv()
        self.shuffle = shuffled
        self.album_dict = self.album_toDict()
        self.amount = amount
        self.shuffled = self.getRandom()

    def read_csv(self):
        album_list = []
        with open(self.filepath, 'rt') as fin:
            reader = csv.reader(fin, delimiter=",")
            next(reader, None)
            for read in reader:
                if read[23][0].isdigit():
                    time = float(int(read[23])/1000)
                else:
                    time = read[23]
                album_list.append([read[4],read[0],read[2],time])
        return album_list

    def album_toDict(self):
        album_dict = {}
        for album in self.albums:
            if album[1] not in album_dict:
                album_dict[album[1]] = []
            else:
                album_dict[album[1]].append(album)
        if not self.shuffle:
            for key in album_dict:
                album_dict[key] = sorted(album_dict[key], key=lambda album_list: album_list[0].lower())
        else:
            for key in album_dict:
                temp = []
                for i in range(len(album_dict[key])):
                    rando = random.randint(0,len(album_dict[key])-1)
                    temp.append(album_dict[key][rando])
                    album_dict[key].pop(rando)
                album_dict[key] = temp.copy()

        return album_dict

    def getRandom(self):
        song = self.album_dict
        allSongs = []
        for key in song:
            for value in song[key]:
                allSongs.append(value)
        shuffledSongs = []
        if not self.amount or self.amount <= 0:
            amount = 5
        for _ in range(self.amount):
            if allSongs:
                rando = random.randint(0,len(allSongs)-1)
                shuffledSongs.append(allSongs[rando])
                allSongs.pop(rando)
            else:
                return shuffledSongs
        return shuffledSongs


def read_song_data(filepath="data/taylor_all_songs.csv", shuffled=False):
    get_albumDict = GetAlbum(filepath, shuffled)
    return get_albumDict.album_dict

def main():
    album_dict = read_song_data()
    for key in album_dict:
        print(key)
    user_input = int(input("\n1. Get Album\n2. Get Shuffled Album\n3. Get Random Playlist\n\n"))
    if user_input == 1:
        user_input = input("Enter Album Name: ")
        if user_input in album_dict:
            finalString = f'\n{"Song":60}{"Album":40}{"Album Release":20}{"Duration"}'
            for album in album_dict[user_input]:
                finalString += f'\n{album[0]:60}{album[1]:40}{album[2]:20}{album[3]}'
            return finalString
        else:
            return "Album not found..."
    elif user_input == 2:
        user_input = input("Enter Album Name: ")
        album_dict = read_song_data("data/taylor_all_songs.csv",True)
        if user_input in album_dict:
            finalString = f'\n{"Song":60}{"Album":40}{"Album Release":20}{"Duration"}'
            for album in album_dict[user_input]:
                finalString += f'\n{album[0]:60}{album[1]:40}{album[2]:20}{album[3]}'
            return finalString
        else:
            return "Album not found..."
    elif user_input == 3:
        shuffle_amount = int(input("Enter amount of songs (default is 5): ") or 5)
        random_album = GetAlbum("data/taylor_all_songs.csv", False, shuffle_amount)
        random_songs = random_album.getRandom()
        finalString = f'\n{"Song":60}{"Album":40}{"Album Release":20}{"Duration"}'
        for song in random_songs:
            finalString += f'\n{song[0]:60}{song[1]:40}{song[2]:20}{song[3]}'
        return finalString
    else:
        return "Please enter valid number (1 - 3)"

print(main())








