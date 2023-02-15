from faker import Faker
# Меныем локализацию на привычную
fake = Faker(['ru_RU'])
# Посмотрим что сгенерировл .profile()
for field in fake.profile().items():
    print(field)

