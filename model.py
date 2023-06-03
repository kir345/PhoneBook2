class PhoneBook:

    def __init__(self, path: str = 'phone.txt'):
        self.phone_book: list[dict[str,str]] = []
        self.path = path
        self.last_id = 0

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            self.phone_book.append({'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]})
        

    def save(self):
        data = []
        for contact in self.phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    
    def load(self):
        return self.phone_book

    def add(self, new: dict[str, str]) -> str:
        self.last_id += 1
        new['id'] = str(self.last_id)
        self.phone_book.append(new)
        return new.get('name')

    def search(self, word: str) -> list[dict[str, str]]:
        res: list[dict[str, str]] = []
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    res.append(contact)
                    break
        return res


    def change(self, contact: dict, index: int | str) -> str:
        for contact in self.phone_book:
            if index == contact.get('id'):
                contact['name'] = contact.get('name', contact.get('name'))
                contact['phone'] = contact.get('phone', contact.get('phone'))
                contact['comment'] = contact.get('comment', contact.get('comment'))
                return contact.get('name')



