from src.pickle_demo import load_pickle
from src.pickle_demo import A

data = load_pickle("pickle_test.pkl")
print(data)
print("given data list: ", [str(dat) for dat in data])
