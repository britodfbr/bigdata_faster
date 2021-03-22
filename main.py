import time
from pathlib import Path
from gen_names import gen_names

file = 'names.txt'

if not Path(file).is_file():
    gen_names(file)

with open(file) as f:
    names = f.readlines()[:1000000]
    names_set = set(names)

def in_names():
    ret = []
    for i in range(100):
        ret.append(str(i) in names)
    return ret


def in_names_set():
    ret = []
    for i in range(100):
        ret.append(str(i) in names_set)
    return ret


def run():
    s = time.time()
    in_names()
    print(f"""
    Running in_names ..
    Time taken: {time.time() - s}""")

    s = time.time()
    in_names_set()
    print(f"""
    Running in_names_set ..
    Time taken: {time.time() - s}""")    


if __name__ == "__main__":
    run()

    
