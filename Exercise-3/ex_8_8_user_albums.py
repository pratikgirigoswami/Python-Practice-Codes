# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:40:15 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5

"""
def make_album(artist, album):
    artist_album_dict = {
        'artist': artist.title(),
        'title': album.title(),
        }
    if songs:
        artist_album_dict['songs'] = songs
        
    return artist_album_dict

print("Enter 'quit' to stop and exit.")

while True:
    album = input("Enter the album's name:")
    if album == 'quit':
        break
    
    artist = input("Enter the artist's name:")
    if artist == 'quit':
        break

    ar_al = make_album(artist, album)
    print(ar_al)