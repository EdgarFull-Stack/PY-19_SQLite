import sqlite3
# Task 1
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
print('-'*40)
# Task 2
def append_to_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?,?,?)',(pavadinimas, adresas, mokiniu_skaicius))

# append_to_mokykla("Vilniausprogimnazija","Vilniausg.10",500)
# append_to_mokykla("Kaunogimnazija","Kaunog.5",800)
# Task 3
def print_all_mokykla_rows():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM mokykla'):
            str(row)
            print(f'Mokykla: {row[0]}, Adresas: {row[1]}, Mokiniu skaicius: {row[2]}')

print_all_mokykla_rows()


def print_mokykla_by_skaicius(mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM mokykla WHERE mokiniu_skaicius >= ?',(mokiniu_skaicius,)):
            print(row)
print(print_mokykla_by_skaicius(600))