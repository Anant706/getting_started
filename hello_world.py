from random import choice


class Person:
    def __init__(self, name):
        self.greeting = '<div>Hello {name}</div>'
        self.name = name

    def __str__(self):
        return self.getting_print()

    def getting_print(self):
        return self.greeting.format(name=self.name)


def main():
    people = [
        Person('Raju'),
        Person('John'),
        Person('Amit'),
        Person('Raj')
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()
