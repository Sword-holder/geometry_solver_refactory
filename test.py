def func(**dict):
    name = list(dict.keys())[0]
    print(name)
    print(type(name))
    
func(attr='hello')