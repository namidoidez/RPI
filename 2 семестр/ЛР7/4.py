import time

class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket: ", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print("createDate: ", time.asctime(self.createDate))
        print("owner: ", self.owner)
        print("deadline: ", time.strftime("%d.%m.%Y", self.deadline))

# Создание объекта класса
ticket1 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))
# Вызов метода
ticket1.display()
# Получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
# Проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
setattr(ticket1, "owner", "Alexei Petrov")  # Установка значения атрибута
print("Owner(setattr): ", ticket1.owner)
delattr(ticket1, "owner")  # Удаления значения атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
del ticket1 # Удаление объекта

# Получение текущего времени и вывод на экран
current_time = time.localtime()
formatted_time = time.strftime("%d %b %Y %H:%M:%S", current_time)
print("Текущее время: ", formatted_time)