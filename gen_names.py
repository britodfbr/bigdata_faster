from faker import Faker

def gen_names(filename, nlines=1000000):
    fake = Faker()

    with open(filename, 'w') as f:
        f.write('NAME\n')
        for i in range(nlines):
            f.write(f'{fake.name()}\n')
