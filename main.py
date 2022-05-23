sec = int(input('Введите кол-во секунд = '))

if sec >= 60 :
  minutes = sec // 60
  print(minutes, 'мин', sec % 60, 'сек')
if sec >= 3600 :
  hours = sec // 3600
  print(hours, 'часов', minutes % 60, 'мин', sec % 60, 'сек')
if sec >= 86400 :
  days = sec // 86400
  print(days, 'дней', hours % 3600, 'часов', minutes % 60, 'мин', sec % 60, 'сек') 
    


