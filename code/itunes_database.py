# Writing data from iTunes XML library to database


import sqlite3
import xml.etree.ElementTree as ET

db_filename = "final.sqlite"   # Database to write in
xml_lib  = "Library.xml"   		# iTunes Library


connection = sqlite3.connect(db_filename)
cur = connection.cursor()

# Deleting all old tables 
# And creating the new ones

cur.executescript("""
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Track;

	CREATE TABLE Artist ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE );
	CREATE TABLE Genre ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE ); 
	CREATE TABLE Album ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE );
	CREATE TABLE Track ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER );

	""")

# ---- printing XML ----
# file = open(xml_lib)
# for line in file:
# 	print line,

# search for exeact key in xml dict and returns it's value
def find_key(dict, key):
	found = False
	for item in dict:
		if found: return item.text
		if item.tag == "key" and item.text == key: found = True
	return None


xml_tree = ET.parse(xml_lib)
tracks = xml_tree.findall("dict/dict/dict")
print "There are", len(tracks), "tracks"

for track in tracks:
	artist = find_key(track, "Artist")
	genre = find_key(track, "Genre")
	album = find_key(track, "Album")
	track_name = find_key(track, "Name")
	length = find_key(track, "Total Time")
	rating = find_key(track, "Rating")
	count = find_key(track, "Total Time")

	if artist is None or genre is None or album is None or track_name is None:
		continue

		# Adding genre and artist name of the current track to DB
	cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre, ) )
	cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist, ) )
		# Getting artist_id from the Artist table
	cur.execute("SELECT id FROM Artist WHERE name = (?)", (artist, ) )
	
	artist_id = cur.fetchone()[0]
		# And adding it to the Album table along with the album name
	cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)", (album, artist_id) )
		# Forming the Track table the same way
	cur.execute("SELECT id FROM Genre WHERE name = (?)", (genre, ) )
	genre_id = cur.fetchone()[0]
	cur.execute("SELECT id FROM Album WHERE title = (?)", (album, ) )
	album_id = cur.fetchone()[0]
	cur.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ? ,?, ?, ?, ?)", (track_name, album_id, genre_id, length, rating, count) )




# for track in tracks:
	# print type(track)
# for item in itere: print item

connection.commit()
connection.close()

