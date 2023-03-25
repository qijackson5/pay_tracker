# import time
#
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.total_pay = 0
#
#     def start(self):
#         pay_per_sec = self.salary / 12 / 2 / 80 / 3600
#
#         while True:
#             self.total_pay += pay_per_sec * 0.1
#             time.sleep(0.1)
#
#     def pay(self):
#         return self.total_pay
#



import time


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.total_pay = 0

    def start(self):
        pay_per_sec = self.salary / 12 / 2 / 80 / 3600

        while True:
            self.total_pay += pay_per_sec * 0.1
            time.sleep(0.1)

    def get_pay(self):
        return self.total_pay