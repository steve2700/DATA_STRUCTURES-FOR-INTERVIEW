class Human:
    def sayhello(self, name=None):
        if name is not None:
            print('hello' ' ' + name)
        else:
            print('hello')

x = Human()
x.sayhello()
print(x)
x.sayhello('Stewart')
print(x)