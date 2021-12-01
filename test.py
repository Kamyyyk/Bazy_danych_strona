from database import Database
from os import getenv

db = Database(getenv('DB'))
db.cursor.execute("SELECT login,funds FROM users")
query = db.cursor.fetchall()
print(query)

#
# miasto = ('Warszawa', 'Kraków', 'Wrocław')
#
# def test(**kwargs):
#     return ' and '.join([f'{kwarg}=?' for kwarg in kwargs]), tuple(miasto)
# # print(test(a='?'))
#
# def test_2(*args):
#     return ','.join(['?' for i in args])
#
#
# print(test_2("x",'d','d','d','d','d'))
