with open('the_fellowship_of_the_ring.txt') as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
            count += 1
print(count)
