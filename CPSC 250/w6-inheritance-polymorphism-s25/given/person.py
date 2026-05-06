class Person:
    def __init__(self, first_name, last_name, id, second_last_name = None):
        self._first_name = first_name
        self._last_name = last_name
        self._second_last_name = second_last_name
        self._id = id

    def __str__(self):
        if self._second_last_name is None:
            return f"{self._last_name}, { self._first_name}"
        else:
            return f"{self._last_name}-{self._second_last_name}, {self._first_name}"

    def __eq__(self, other):
        return Person.__str__(self) == Person.__str__(other)

    def __gt__(self, other):
        return Person.__str__(self) > Person.__str__(other)

    def __lt__(self, other):
        return Person.__str__(self) < Person.__str__(other)


if __name__ == '__main__':
    person1 = Person("Manuel", "Pérez", "12345678A", "Quiñones")
    print(person1)