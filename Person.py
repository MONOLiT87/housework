#*ЗАДАЧА 1:
#Реализовать класс Person, у которого должно быть два публичных поля: age и name.
#Также у него должен быть следующий набор методов: know(person), который позволяет
#добавить другого человека в список знакомых. И метод is_known(person),
#который возвращает знакомы ли два человека

class Person():
	age = None
	name = ''
	list_of_known_persons = {}
	def __init__ (self, name, age):
		self.name = name
		self.age = age

	def is_known(self, person):
		try: # в данном случае ловим KeyError, если персона не находится в словаре, думаю что описание исключения внутри метода класса уместнее.
			if self.list_of_known_persons[person.name] == person.age:
				return True
			else:
				return False
		except KeyError:
			return False
	def known(self, person):
		self.list_of_known_persons[person.name] = person.age

Alex = Person('Alexander',32)
Sergey = Person('Sergey', 30)
Nikita = Person('Nikita', 27)
Dima = Person('Dima', 25)

Alex.known(Sergey)
Alex.known(Nikita)

print("Check {}'s relationship with {} : {} \n ".format(Alex.name, Sergey.name, Alex.is_known(Sergey)))
print("Check {}'s relationship with {} : {} \n ".format(Alex.name, Nikita.name, Alex.is_known(Nikita)))
print("Check {}'s relationship with {} : {} \n ".format(Alex.name, Dima.name, Alex.is_known(Dima)))
