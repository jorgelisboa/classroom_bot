import calendar
from datetime import datetime
import webbrowser

#Dictionary to classes that I will have
#Matérias, mude conforme for as suas
subjects = {    'MONDAY' : ['FISICA_IV', 'BIO_2', 'QUIMICA','INTERVALO', 'HISTORIA', 'FISICA_I', 'QUIMICA'],
                'TUESDAY' : ['FISICA_II', 'HISTORIA', 'REDACAO', 'INTERVALO', 'MAT_V', 'BIO_1', 'MAT_III'],
                'WEDNESDAY' : ['GEOGRAFIA', 'HISTORIA', 'GEOGRAFIA', 'INTERVALO', 'LITERATURA', 'BIO_3', 'GRAMATICA'],
                'THURSDAY' : ['FILOSOFIA', 'BIO_4', 'SOCIOLOGIA', 'INTERVALO', 'INTER_TEXT_I', 'MAT_I', 'MAT_IV'],
                'FRIDAY' : ['QUIMICA', 'QUIMICA', 'INGLES', 'INTERVALO', 'FISICA_III', 'INTER_TEXT_II', 'MAT_II'],
                'SATURDAY' : ['QUIMICA', 'QUIMICA', 'INGLES', 'INTERVALO', 'FISICA_III', 'INTER_TEXT_II', 'MAT_II'],
                'SUNDAY' : ['QUIMICA', 'QUIMICA', 'INGLES', 'INTERVALO']
              }
#LINKS para as aulas
classes = {     'BIO_1' : 'https://meet.google.com/lookup/b6zwqo5ruy',
                'BIO_2' : 'https://meet.google.com/lookup/cuia6uszyp',
                'BIO_3' : 'https://meet.google.com/lookup/b6zwqo5ruy',
                'BIO_4' : 'https://meet.google.com/lookup/cuia6uszyp',
                'INTERVALO' : '',
                'FISICA_I' : 'https://meet.google.com/lookup/cuwsa7yj5p',
                'FISICA_II' : 'https://meet.google.com/lookup/cuwsa7yj5p',
                'FISICA_III' : 'https://meet.google.com/lookup/achfdgxduf',
                'FISICA_IV': 'https://meet.google.com/lookup/achfdgxduf',
                'QUIMICA' : 'https://meet.google.com/lookup/d742626utl',
                'HISTORIA'	: 'https://meet.google.com/lookup/bqpswzpo62',
                'REDACAO' :	'https://meet.google.com/lookup/gape5zehkb',
                'MAT_I' : 'https://meet.google.com/lookup/hucgtjsvzb',
                'MAT_II' : 'https://meet.google.com/lookup/coe65kvl6l',
                'MAT_III' : 'https://meet.google.com/lookup/gdjy7po4dc',
                'MAT_IV' : 'https://meet.google.com/lookup/gdjy7po4dc',
                'MAT_V' : 'https://meet.google.com/lookup/hucgtjsvzb',
                'GEOGRAFIA' : 'https://meet.google.com/lookup/c3sjd6irj5',
                'GRAMATICA' : 'https://meet.google.com/lookup/b5bhscdkze',
                'LITERATURA' : 'https://meet.google.com/lookup/c4t6ulqiq3',
                'FILOSOFIA' : 'https://meet.google.com/lookup/dlfhtmsyzm',
                'SOCIOLOGIA' : 'https://meet.google.com/lookup/a7led2onz4',
                'INTER_TEXT_I' : 'https://meet.google.com/lookup/fku7lacuqa',
                'INTER_TEXT_II' : 'https://meet.google.com/lookup/bcsz6cnocf',
                'INGLES' : 'https://meet.google.com/lookup/hzspyufdf2'
          }

#Creating a def to know the day
def find_day():#Return to me a day in a array (0 == Monday ... 6 == Sunday)
    date_and_time = datetime.now()#Put "datetime.now()" in a variable 
    #print(date_and_time) #Return Y-M-D and Hours
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    #print(date) #Return Day/Month/Year 
    date = datetime.strptime(date, '%d %m %Y').weekday()
    #print(date) #Return the day based on a array (.weekday())
    day = calendar.day_name[date]
    return day.upper()

#print(find_day())

# def to return the classes from the day
def find_classes():
    subs = []
    day = find_day()
    classes = subjects[day]
    if day != 'SATURDAY' and day != 'SUNDAY':
        timings = ['07:30 am - 08:05 am','08:20 am - 08:55 am', '9:10 am - 09:45 am', '9:46 - 10:00', '10:10 am - 10:55 am', '11:10 am - 11:50 am', '11:55 am - 12:35 am']
        for i in range(6):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    if day == 'SATURDAY':
        print('SEM AULA')
    if day == 'SUNDAY':
        print('SEM AULA')
    return subs
print(find_classes())
def classes_today():
    subs = find_classes()
    for i in subs:
        time = datetime.now().time()
        time = str(time).split(":")
        if time[0] == i[0:2] and time[1] >= i[3:5]:
            print('\n' + '\t' + i,' <-- Present Session')
        elif time[0] == i[11:13] and time[1] < i[14:16]:
            print('\n' + '\t' + i,' <-- Present Session')
        else:
            print('\n' + '\t' + i)

def help_menu():
    print('\n' + '\t' + 'class [-a or automate] To automate')
    print('\n' + '\t' + 'class [-h or help] To see this menu')
    print('\n' + '\t' + 'class [subject_name] To open subject_name\'s link')
    print('\n' + '\t' + 'class [-t or today] To see today\'s classes')

def open_link(url):
    webbrowser.open(url)
    print('opened requested page')