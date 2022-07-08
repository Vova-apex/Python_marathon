class Developer:
    def __init__(self):
        self.skill = "Python"
        self.rate = 1100


developer1 = Developer()
developer2 = Developer()
developer3 = Developer()

developer1.rate = 1300
total_rate = developer1.rate+developer2.rate+developer3.rate
print(total_rate)


class Developer:
    def __init__(self, name, phone):
        self.name = name
        self.city = 'Kyiv'
        self.skill = 'Python'
        self.rate = 1300
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.city} {self.skill} {self.rate} {self.phone}"


user = Developer('Vlad', '+380631234570')
out = f"{user.name} {user.city} {user.skill} {user.rate} {user.phone}"
print(out)


class Developer:
    def __init__(self):
        self.fields = []


developer = Developer()
developer.fields.append('name')
developer.fields.append('city')
developer.fields.append('developer_skill')
developer.fields.append('rate')
developer.fields.append('phone')

developer.fields[2] = 'skill'
developer.fields.pop(4)
developer.fields.pop(3)
out = f"{developer.fields[0]} {developer.fields[1]} {developer.fields[2]}"
print(out)


class Developer:
    def __init__(self):
        self.fields = []

    def __contains__(self, item: str):
        for f in self.fields:
            if item in f:
                return True
        return False

    def add(self, field_item):
        self.fields.append(field_item)

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        idx = int(idx)
        self.fields[idx] = value


out = ''
value = 'f'
try:
    value = float(value)
except ValueError:
    out = f"value {value} can't be converted to float"
    print(out)
