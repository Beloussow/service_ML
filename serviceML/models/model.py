import pickle


with open('model.pickle', 'rb') as f:
    model = pickle.load(f)


if __name__ == '__main__':
    print(model.predict([[1., 168., 88., 29., 0., 35., 0.905, 52.]]))