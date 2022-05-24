# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:17:44 2021

@author    : Pratikgiri Goswami
@Student ID: C0806977
@Coding Exercise 5
"""

# Part-1
print("\n------without number of tracks------")
def make_album(artist, album):
    artist_album_dict = {
        'artist': artist.title(),
        'title': album.title(),
        }
    return artist_album_dict

print(make_album('alisha chinai','made in india'))
print(make_album('sonu nigam','deewana'))
print(make_album('michael jackson','dangerous'))

print("\n------with number of tracks------")
# Part-2
def make_album(artist, album,songs=0):
    artist_album_dict = {
        'artist': artist.title(),
        'title': album.title(),
        }
    if songs:
        artist_album_dict['songs'] = songs
        
    return artist_album_dict

print(make_album('alisha chinai','made in india'))
print(make_album('sonu nigam','deewana'))
print(make_album('michael jackson','dangerous',30))