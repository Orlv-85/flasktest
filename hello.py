from flask import Flask
from flask import request

app = Flask(__name__)

spisok = {
101:['umnik', 'umnik@tut.by','Dwarf','2021-12-20T17:51:00'],
102:['vorchun', 'vorchun@tut.by','Gnome','2021-12-20T17:51:00'],
103:['veselchak', 'veselchak@tut.by', 'Dwarf','2021-12-20T17:51:10'],
104:['sonya', 'sonya@tut.by','Gnome','2021-12-20T17:51:15'],
105:['skromink', 'skromink@tut.by', 'Dwarf','2021-12-20T17:51:20'],
106:['chihun', 'chihun@tut.by','Gnome','2021-12-20T17:51:25'],
107:['prostak','prostak@tut.by', 'Dwarf','2021-12-20T17:51:30']
}

@app.route('/')
def start():
    return 'Здесь хранится список пользователей'

@app.route('/users', methods=['GET', 'POST'])
def users():

    username = request.args.get('username')
    departament = request.args.get('departament')

    if bool(username) == True:

        if bool(departament) == True:
            list_namedep_filter=[i[0] for i in list(spisok.values()) if departament in i[2]]
            list_name_filter=[i for i in list_namedep_filter if username in i]
            return (' '.join(list_name_filter))

        elif bool(departament) == False:
            list_name=[(i[0]) for i in list(spisok.values())]
            list_name_filter=[i for i in list_name if username in i]
            return (' '.join(list_name_filter))

    elif bool(username) == False:

        if bool(departament) == True:
            list_namedep_filter=[i[0] for i in list(spisok.values()) if departament in i[2]]
            return (' '.join(list_namedep_filter)

        elif bool(departament) == False:
            return (' '.join(str (i[0]) for i in list(spisok.values())))
