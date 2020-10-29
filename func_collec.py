def min_enclosing_rectangle(radius, x, y) :
    ''' (number,number,number)->(tupule)
        radius>0
        gets the radius of the circle, and co-ordinates of the middle of the circle
        it then returns the smallest length and width of a rectangle possible to fit in a circle
        '''
    if (radius<0):
        return None
    else:
        width=x-radius
        length=y-radius
        return (width,length)

def vote_percentage (results):
    '''(string)->number
        a function that counts the amount of no and yes in a string and returns the percentage of yes'''
    results=results.lower()
    yes=results.count("yes")
    no=results.count("no")
    total=yes+no
    return (yes/(total))

def vote():
    '''none->none
    calls a function that counts the amount of no and yes in a string and returns the percentage of yes
    then it generates the verdict of the voting'''

    votes=input("Enter the yes, no, abstained votes one by one and then press enter: ")
    answer=vote_percentage(votes)
    if answer==1:
        print("the proposal passes unanimously")
    elif answer>=2/3 and answer<1:
        print("the proposal passes with super majority")
    elif  answer>=1/2 and answer<2/3:
        print("the proposal passes by simple majority")
    else:
        print("the proposal does not pass")