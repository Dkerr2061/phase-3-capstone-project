from models.artist import Artist
from models.album import Album

from models.__init__ import CURSOR, CONN

Artist.create_table()
Album.create_table()

CURSOR.execute("DELETE FROM artists")
CURSOR.execute("DELETE FROM albums")
CONN.commit()


Artist.create("Tool")
Artist.create("Pink FLoyd")
Artist.create("Flume")
Artist.create("Soda Stero")
Artist.create("Halsey")
Artist.create("Little Busters")
Artist.create("Yoko Kanno")
Artist.create("Ice Cube")
Artist.create("Dr. Dre")
Artist.create("Primus")
Artist.create("Residente")
Artist.create("Rage Against The Machine")