


def classmates(name):
    my_dict = {'David' : "Meet me after class",
            'Andrew' : 'Meet me after class',
            'Felix' : 'Do more codewars',
            'Jessica' : 'Do more codewars',
            'Robert' : 'Finish your homework',
            'William' : 'Finish your homework',
            'John' : 'Finish your homework',
            'Apollo' : 'You are good to go',
            'Cole' : 'You are good to go',
            'Dereck' : 'You are good to go',
            'Saed' : 'You are good to go',
            'Tony' : 'You are good to go',
            }
          
    return my_dict.get(name.title(), 'Get out of my class, ' + name.title())
print(classmates('william'))