from Person import Person


class People:
    def __init__(self):
        self.people = [
            Person("Febrian", "+19252358139", "bestie"),
            Person("Ronald", "+15104786156", "bestie"),
            Person("Felica","+15104786156","so"),
            Person("Ting","+15104786156", "bestie"),
            Person("yiyi cecil","+65 9839 6626", "aunt"),
            Person("gugu ajin", "uncle"),
            Person("mei", "+65 8123 2386","cousin"),
            Person("shar", "+6281938887918", ["dang"]),
            # Sharron Tania
            Person("shar", "+12067855179", ["dang"]),
            Person("pett", "+16264204061", ["eecs"]),
            Person("nate", "+16264999197", ["eecs"]),
        ]

    def getPersonDataFromName(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None

    def getPeopleDataFromTags(self, tags):
        people = []
        for person in self.people:
            if tags in person.tags:
                people.append(person)
        return people if len(people) > 0 else None

    def addPerson(self, person):
        self.people.append(person)