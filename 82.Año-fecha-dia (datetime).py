import datetime,os,time

x = datetime.date.today()
# la más sencilla que he encontrado es esta:
print(str(x))
print(x)
x.isoformat()
print(x)
#dia de la semana
print(time.strftime("%A"))
#una buena funcion
print(       datetime.date.__str__(x)   )   

# esta informacion puede ser importante
os.system("start https://mail.python.org/pipermail/python-es/2006-March/011826.html")

