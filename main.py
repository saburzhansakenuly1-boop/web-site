# numbers = list(map(int, input().split()))

# for i in range(1, len(numbers)):
#     if numbers[i] <= numbers[i - 1]:
#         print("NO")
#         break
# else:
#     print("YES")    


# numbers = list(map(int, input().split()))
# for i in range(1,len(numbers)):
#     if numbers[i] <= numbers[i - 1]:
#         print("NO")
#         break
#     else:
#         print("YES")


# менің керек затым

# git add .
# git commit -m "любой коментарий жазу "
# git push

# datetime библиотека 
# dt кличка по который хранить в себе значение 
# now переменная которая хранит  в себе значения
# now() метед который опеределяет нам текущее время 
# переменная тайм которая харанит в себе текущее время и выводит из него день то есть date()
# from datetime import date
# import datetime as dt 
# now=dt.datetime.now()
# time=now.date()
# today=date.today()
# print(time, today)


# today внутри готовый вариант 
# dt.datetime.now(),now.date()

# import datetime 
# timeobj=datetime.time(8,48,56)
# print(timeobj)



# import datetime
# date_obj=datetime.datetime(2020,10,17)
# h1=date_obj.datetime.time(12,34,56)
# print(h1)






# from datetime import timedelta
# td_object=date_obj.timedelta(days=8,seconds=0,microseconds=5,milliseconds=0,minutes=8,hours=0,weeks=0)
# print(td_object)



import pytz
import datetime 
tz_berlin=pytz.timezone("Europe/Berlin")
dt_berlin=datetime.datetime.now(tz_berlin)
print(dt_berlin)