class Messages:
    def __init__(self):
        self.content =  {
        "new year": "Happy new year 2024, I hope you will have the best upcoming year!! btw, how are you",
        "idul fitri": "Selamat idul fitrii yaa. Semoga berkahny terus berlimpah yaa!! btw, apa kabar lu?",
        "ngapain": "lagi ngapain?",
        "ngerjain apa hari ini": "ngerjain apa hari ini?"
    }

    def getMessages(self,occasion,peopleList):
        messages = []
        msg = self.content[occasion] if occasion in self.content else None
        if msg:
            for person in peopleList:
                messages.append(f"Hey {person.name}{person.name[-1]}, {msg}")
        return messages