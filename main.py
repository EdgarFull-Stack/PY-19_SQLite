import sqlite3
#
# conn = sqlite3.connect('pavyzdys.db')
# c = conn.cursor()
#
# c.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS studentai (
#                 vardas TEXT,
#                 pavarde TEXT,
#                 klase INTEGER)
#     '''
# )
#
# conn.commit()
# conn.close()

def append_to_studentai(vardas, pavarde, klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO studentai (vardas, pavarde, klase) VALUES (?,?,?)',(vardas, pavarde, klase))
def print_all_studentai_rows():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM studentai'):
            print(row)

def print_all_studentai_names():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute('SELECT vardas FROM studentai'):
            print(row)

def print_all_studentai_by_klase(klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM studentai WHERE klase = ?',(klase,)):
            print(row)

# append_to_studentai('Edgar', 'Lip',12)
# append_to_studentai('John', 'John',10)
print_all_studentai_rows()
print_all_studentai_names()
print_all_studentai_by_klase(10)
