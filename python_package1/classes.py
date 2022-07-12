# Классы
class  Worker:
    """Класс, описывающий работника"""
    def __init__(self, name, pay):
        """Конструктор"""
        self.name = name
        self.pay = pay

    def lastname(self):
        """Выводит фамилию"""
        return self.name.split()[-1]

    def giverase(self, percent):
        """Увеличим зарплату"""
        self.pay *= (100 + percent) / 100

worker = Worker('Ігор Пастушенко', 10000)
print(worker.name)
print(worker.lastname())
print(worker.pay)
worker.giverase(50)
print(worker.pay)