class Person:

    def __init__(self, first_name, patronymic, last_name, phones):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        if ('private' in self.phones):
            return self.phones['private']
        return None

    def get_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def get_work_phone(self):
        if ('work' in self.phones):
            return self.phones['work']
        return None

    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'

class Company:
    
    def __init__(self, name, type, phones, *persons):
        self.name = name
        self.type = type
        self.phones = phones
        self.persons = persons

    def get_phone(self):
        if ('contact' in self.phones):
            return self.phones['contact']

        for person in self.persons:
            phone = person.get_work_phone()
        if (phone != None):
            return phone

        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type}'

    def send_sms(*contacts):
        for contact in contacts:
            phone = contact.get_phone()

        if (phone != None):
            print(f'Отправлено СМС на номер {phone} с текстом: {contact.get_sms_text()}')

        else:
            print(f'Не удалось отправить сообщение абоненту: {contact.get_name()}')



