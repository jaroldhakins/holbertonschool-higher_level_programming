#!/usr/bin/python3
''' Create a class list
'''


class MyList(list):
    ''' created MyList
    '''

    def print_sorted(self):
        '''
        prints the list sorted
        '''
        print(sorted(self))
