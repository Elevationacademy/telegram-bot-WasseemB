import pickle


def save_popular(a):
    with open('popular.pickle', 'wb') as handle:
        pickle.dump(a, handle)


def read_popular():
    with open('popular.pickle', 'rb') as handle:
        b = pickle.load(handle)
    return b.items()
