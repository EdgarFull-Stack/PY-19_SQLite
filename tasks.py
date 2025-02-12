import sqlite3

conn = sqlite3.connect('mokykla.db')
c = conn.cursor()

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS mokykla (
                pavadinimas TEXT,
                adresas TEXT,
                mokiniu_skaicius INTEGER)
    '''
)

conn.commit()
conn.close()