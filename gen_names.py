from faker import Faker

def gen_names(filename, nlines=1000000):
    fake = Faker()

    with open(filename, 'w') as f:
        print(f'creating {filename} ')
        f.write('NAME\n')
        for i in range(nlines):
            f.write(f'{fake.name()}\n')
