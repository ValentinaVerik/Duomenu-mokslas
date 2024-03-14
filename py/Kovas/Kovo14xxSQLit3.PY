import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# #sukursime lentele
# c.execute("""CREATE TABLE people(
#     id INTEGER PRIMARY KEY,
#     name text,
#     age int)
#     """)
#
# names = [('1', 'Jonas', '34'), ('2', 'Antanas', '35'), ('3', 'Migle', '23')]
# c.executemany('INSERT INTO people VALUES (?, ?, ?)', names)
#
# c.execute("SELECT * FROM people")
#
# result = c.fetchall()
# for row in result:
#     print(row)
# conn.commit()
# conn.close()



#sukursime lentele
# c.execute("""CREATE TABLE jobs(
#     id INTEGER PRIMARY KEY,
#     job_title text,
#     person_id INTEGER,
#     FOREIGN KEY(person_id) REFERENCES people(id))
#     """)
#
# jobs = [('1', 'inzinierius', '1'), ('2', 'Programuotojas', '2'), ('3', 'Analitikas', '3')]
# c.executemany('INSERT INTO jobs VALUES (?, ?, ?)', jobs)

# c.execute("""SELECT people.name, jobs.job_title from people
#     JOIN jobs on people.id = jobs.person_id
#     """)
# result = c.fetchall()
# print(result)
#
# conn.commit()
# conn.close()
"""
1. Sukurkite naują lentelę hobbies su trimis stulpeliais: id (sveikasis skaičius ir pagrindinis raktas),
 hobby (tekstas), ir person_id (sveikasis skaičius), kuris yra foreign key, susiejantis pomėgį
  su asmeniu iš people lentelės.
"""
conn = sqlite3.connect('test.db')
c = conn.cursor()


# c.execute("""CREATE TABLE hobbies(
#      id INTEGER PRIMARY KEY,
#      hobby text,
#      person_id INTEGER,
#      FOREIGN KEY(person_id) REFERENCES people(id))
#      """)


hobbies = [('1', 'Muzika', '1'),
           ('2', 'Daile', '2'),
           ('3', 'Dviraciai', '3')
           ]
additional_hobbies = [('sokti', '1'),
                      ('dainuoti', '1')]

# c.executemany('INSERT INTO hobbies(hobby, person_id) VALUES (?,?)', additional_hobbies )
c.execute("""SELECT people.name, hobbies.hobby from people
     JOIN hobbies on people.id = hobbies.person_id
     WHERE people.name = 'Jonas'
     """)

curs.execute("""
    SELECT * FROM 

    (SELECT people.name as vardas, COUNT(hobbies.hobby) as hobiu_skaicius
    FROM people    
    JOIN hobbies ON hobbies.person_id = people.id 
    GROUP BY people.id)

    WHERE hobiu_skaicius > 1;
    """)
ans4 = curs.fetchall()
print(ans4)

result = c.fetchall()
print(result)

# c.executemany('INSERT INTO hobbies VALUES (?, ?, ?)', hobbies)
# c.execute('''
#     UPDATE hobbies SET hobby = 'zvejyba' WHERE person_id = (SELECT id from people WHERE name = 'Jonas')
#     and hobby = 'Muzika'
# ''') # kaip pakeisti hobby
# c.execute("SELECT * FROM hobbies")
# c.execute("""SELECT people.name, hobbies.hobby from people
#      JOIN hobbies on people.id = hobbies.person_id
#      """)
#
# result = c.fetchall()
# print(result)

conn.commit()
conn.close()

"""
2. Įterpkite duomenis į hobbies lentelę. Pavyzdžiui, Jonas mėgsta žvejoti, Ona - skaityti, o Petras - programuoti.

"""
"""
3. Parašykite SQL užklausą, kuri naudoja JOIN operaciją, kad gautumėte visų žmonių vardus kartu su jų pomėgiais.
"""
"""
4. Parašykite SQL užklausą, kuri grąžintų visus asmenis, turinčius daugiau nei vieną pomėgį, 
įskaitant jų vardus ir pomėgius.
"""

# c.execute("""CREATE TABLE hobbies(
#      id INTEGER PRIMARY KEY,
#      hobby text,
#      person_id INTEGER,
#      FOREIGN KEY(person_id) REFERENCES people(id))
#      """)
#
# hobbies = [('1', 'Muzika', '1'),
#            ('2', 'Daile', '2'),
#            ('3', 'Dviraciai', '3')
#            ]
# c.executemany('INSERT INTO hobbies VALUES (?, ?, ?)', hobbies)
#
# # c.execute("SELECT * FROM hobbies")
# c.execute("""SELECT people.name, hobbies.hobby from people
#      JOIN hobbies on people.id = hobbies.person_id
#      """)
#
# result = c.fetchall()
# print(result)
#
# conn.commit()
# conn.close()
