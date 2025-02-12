import sqlite3

conn = sqlite3.connect('pavyzdys.db')
c = conn.cursor()

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS studentai (
                vardas TEXT,
                pavarde TEXT,
                klase INTEGER)
    '''
)

conn.commit()
conn.close()
