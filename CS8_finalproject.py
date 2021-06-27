# Sarah Liang, CS 8 (S21)

def read_configuration(filename):
    '''
    Takes a filename as input and returns a list,
    where every line from file is a list
    (each white-separated value as its element).
    '''
    file=open(filename,'r')     #opens file to read
    content=file.readlines()    #reads file as list of strings

    grid=[]                     #creates grid
    for string in content:
        string=string.split()   #splits each line into list by the whitespace
        grid.append(string)     #adds list to grid
    return grid                 #returns grid

    file.close()                #closes file




import copy

def next_day(grid):
    '''
    Takes 2D grid of city, returns new 2D grid
    representing state of city the next day.
    '''
    new_grid = copy.deepcopy(grid)  #makes copy of grid
    
    if len(grid)==0:        #returns empty list if grid is empty
        return []
    #returns same grid if it contains a single list w/ just 1 element in it
    if len(grid)==1:
        return grid
    
    #creates a new list to document positions of existing vampires
    vamp_coord = []
    for row in range(len(new_grid)):
        for col in range(len(new_grid[row])):
            if new_grid[row][col]==1:               #checks if position is a vamp
                vamp_coord.append((row,col))    #if it is, adds it to list
    
    #uses vampirize helper function
    for (row,col) in vamp_coord:        #uses vampire positions to vampirize
        new_grid=vampirize(new_grid,(row,col)) #gets city grid after one day of vampirization

    return new_grid



def vampirize(grid, position):
    '''
    Takes in a grid of a city and a vampire's position as a tuple.
    For the position, updates adjacent cells to be vampires,
    returns new grid.
    '''

    #returns -1 if the grid is empty or contains a single list w/ just 1 element
    if len(grid)==0 or (len(grid)==1 and len(grid[0])==1):
        return -1
                                                            
    new_grid = copy.deepcopy(grid)      #makes copy of grid

    row=position[0]
    col=position[1]
    #returns None if the position coordinates are outside of grid
    if row>=len(grid) or col>=len(grid[0]):
        return None 
        
    if row<(len(new_grid)-1):               #if a vamp is in the rows except for the bottom row
        if new_grid[row+1][col]==0:         #and a human is below it
            new_grid[row+1].pop(col)            #removes that human
            new_grid[row+1].insert(col,1)       #inserts a vamp in that space

    if row>0:                               #if a vamp is in the rows except for the top row
        if new_grid[row-1][col]==0:         #and a human is above it
            new_grid[row-1].pop(col)            #removes that human
            new_grid[row-1].insert(col,1)       #inserts a vamp in that space

    if col<(len(new_grid[row])-2):          #if a vamp is in the columns except for the 2 rightmost ones
        if new_grid[row][col+1]==0:         #and a human is to the right of it
            new_grid[row].pop(col+1)            #removes that human
            new_grid[row].insert(col+1,1)       #inserts a vamp in that space

    if col==(len(new_grid[row])-2):         #if a vamp is in the second to rightmost column
        if new_grid[row][col+1]==0:         #and a human is to the right of it
            new_grid[row].pop(col+1)            #removes that human
            new_grid[row].append(1)             #inserts a vamp in that space

    if col>0:                               #if a vamp is in the columns except for the leftmost one
        if new_grid[row][col-1]==0:         #and a human is to the left of it
            new_grid[row].pop(col-1)            #removes that human
            new_grid[row].insert(col-1,1)       #inserts a vamp in that space

    return new_grid



def days_remaining_1(grid):
    '''
    Given a grid of a city, returns the shortest number of days
    after which there are no humans left in town.
    '''

    orig_grid=copy.deepcopy(grid)       #makes copy of grid

    #returns -1 if the grid is empty or contains a single list w/ just 1 element
    if len(grid)==0 or (len(grid)==1 and len(grid[0])==1):
        return -1

    num_days=0      #start on day 0
    show_city_each_day(orig_grid,num_days)   #visualize grid on day 0
    next_grid=next_day(grid)                 #take grid for next day
    
    while next_grid!=orig_grid:     #loop while next day's grid is different from the original grid
        num_days+=1
        show_city_each_day(next_grid,num_days)  #visualize grid on next day
        orig_grid=next_grid                     #orig_grid is set to the previous day's grid
        next_grid=next_day(orig_grid)           #take the grid for the next day
        

    return num_days #returns num_days when all humans are vamps (no changes in the grid)

    


def show_city_each_day(grid, num_days):
    '''
    Takes a 2D grid (a nested list) that represents the city
    and the number of day it is. Returns that day from the function.
    Prints the grid w/ 'H' for humans, 'V' for vampires, 'W' for walls,
    and 'P' for healers.
    '''
    if len(grid)==0:        #returns -1 if the grid is empty
        return -1

    new_grid=copy.deepcopy(grid)        #makes copy of grid
    
    print('Day {}:\n'.format(num_days))     #prints day w/ grid on that day
    for row in range(len(new_grid)):
        for n in range(len(new_grid[row])):
            if new_grid[row][n]==1:
                new_grid[row].pop(n)
                new_grid[row].insert(n,'V') #insert 'V' for vamps
            elif new_grid[row][n]==0:
                new_grid[row].pop(n)
                new_grid[row].insert(n,'H') #insert 'H' for humans
            elif new_grid[row][n]==2:
                new_grid[row].pop(n)
                new_grid[row].insert(n,'W') #insert 'W' for walls
            elif new_grid[row][n]==3:
                new_grid[row].pop(n)
                new_grid[row].insert(n,'P') #insert 'P' for potion
        print(' '.join(new_grid[row]))
    print('')                               #end with new line after each grid
    return num_days         #returns day
    


def days_remaining_2(grid):
    '''
    Given a grid of a city, returns the shortest number of days
    after which there are no humans left in town, or returns -1
    if not all people will turn into vampires.
    '''
    
    orig_grid=copy.deepcopy(grid)       #makes copy of grid

    #returns -1 if the grid is empty or contains a single list w/ just 1 element
    if len(grid)==0 or (len(grid)==1 and len(grid[0])==1):
        return -1

    num_days=0      #start on day 0
    show_city_each_day(orig_grid,num_days)   #visualize grid on day 0
    next_grid=next_day(grid)                 #take grid for next day

    while next_grid!=orig_grid:      #loop while next day's grid is different from the orig
        num_days+=1
        show_city_each_day(next_grid,num_days)   #visualize grid on next day
        orig_grid=next_grid                      #orig_grid is set to the previous day's grid
        next_grid=next_day(orig_grid)            #take the grid for the next day

    for row in range(len(next_grid)):
        for col in range(len(next_grid[row])):
            if next_grid[row][col]==0:       #returns -1 if there's at least 1 human left
                return -1

    return num_days     #returns day when all humans are vamps (no changes in the grid after a day)



def cure(grid, position):
    '''
    Takes in a grid of a city and a healer's position as a tuple.
    For the healer's position, updates all adjacent cells and diagonals
    in the grid to be human, returns new grid based on
    input grid and position of healer w/ the potion
    '''

    new_grid=copy.deepcopy(grid)    #makes copy of grid

    #returns -1 if the grid is empty or contains a single list w/ just 1 element
    if len(grid)==0 or (len(grid)==1 and len(grid[0])==1):
        return -1

    row=position[0]
    col=position[1]
    #return None if the healer position coordinates are outside of the grid
    if row>=len(grid) or col>=len(grid[0]):
        return None

    if row<(len(grid)-1):               #if the healer is in the rows except for the bottom row
        new_grid[row+1].pop(col)            #removes coordinate below it
        new_grid[row+1].insert(col,0)       #inserts a human in that space

    if row>0:                           #if the healer is in the rows except for the top row
        new_grid[row-1].pop(col)            #removes coordinate above it
        new_grid[row-1].insert(col,0)       #inserts a human in that space

    if col<(len(grid[row])-2):          #if the healer is in the columns except for the 2 rightmost ones
        new_grid[row].pop(col+1)            #removes coordinate to the right of it
        new_grid[row].insert(col+1,0)       #inserts a human in that space

    if col==(len(grid[row])-2):         #if the healer is in the second to rightmost column
        new_grid[row].pop(col+1)            #removes coordinate to the right of it
        new_grid[row].append(0)             #inserts a human in that space

    if col>0:                           #if the healer is in the columns except for the leftmost one
        new_grid[row].pop(col-1)            #removes coordinate to the left of it
        new_grid[row].insert(col-1,0)       #inserts a human in that space

    if row>0 and col>0:                 #if the healer is NOT in the left col and top row
        new_grid[row-1].pop(col-1)          #removes coordinate in the healer's top left
        new_grid[row-1].insert(col-1,0)     #inserts a human in that space

    #if the healer is in the columns except for the 2 rightmost ones and not in top row
    if row<(len(grid)-1) and col<(len(grid[row])-2):
        new_grid[row-1].pop(col+1)          #removes coordinate in the healer's top right
        new_grid[row-1].insert(col+1,0)     #inserts a human in that space

    #if the healer is in the second to rightmost column and not in top row
    if row<(len(grid)-1) and col==(len(grid[row])-2):
        new_grid[row-1].pop(col+1)          #removes top right coordinate
        new_grid[row-1].append(0)           #inserts a human in that space

    if row<(len(grid)-1) and col>0:         #if the healer is NOT in the left column and bottom row
        new_grid[row+1].pop(col-1)          #removes coordinate in the healer's bottom left
        new_grid[row+1].insert(col-1,0)     #inserts a human in that space

    #if the healer is in the columns except for the 2 rightmost ones and is not in the bottom row
    if row<(len(grid)-1) and col<(len(grid[row])-2):
        new_grid[row+1].pop(col+1)          #removes bottom right coordinate
        new_grid[row+1].insert(col+1,0)     #inserts a human in that space

    #if the healer in second to right most col and not in bottom row
    if row<(len(grid)-1) and col==(len(grid[row])-2):
        new_grid[row+1].pop(col+1)          #removes bottom right coordinate
        new_grid[row+1].append(0)           #inserts a human in that space

    return new_grid



def days_remaining_3(grid):
    '''
    Given a grid of a city, returns the shortest number of days
    after which there are no humans left in town or returns -1 if not
    all people will turn into vampires. Calls cure function after
    vampires are done w/ vampirization at the end of night.
    '''

    orig_grid=copy.deepcopy(grid)       #makes copy of grid

    #returns -1 if the grid is empty or contains a single list w/ just 1 element
    if len(grid)==0 or (len(grid)==1 and len(grid[0])==1):
        return -1

    #Note that the town can have more than one healer. So, keep healer positions in list.
    healer_coord = []
    for row in range(len(orig_grid)):
        for col in range(len(orig_grid[row])):
            if orig_grid[row][col]==3:            #checks if position is a healer
                healer_coord.append((row,col))    #if it is, adds it to list

    num_days=0      #start on day 0
    show_city_each_day(orig_grid,num_days)   #visualize grid on day 0
    next_grid=next_day(grid)                 #takes vampirized grid for next day

    while next_grid!=orig_grid:
    #loops while next day's grid is different from the orig
                    
        #use cure function
        for (row,col) in healer_coord:            #uses healer(s) positions to cure
            next_grid=cure(next_grid,(row,col))   #healer(s) cure after vampirization

        num_days+=1
        #visualize grid (after 1 vampirization and 1 cure) on next day
        show_city_each_day(next_grid,num_days)
        orig_grid=next_grid          #orig_grid is set to the previous day's grid
        next_grid=next_day(orig_grid)         #take the grid for the next day

        if num_days==30:        #stops after 30 days
            break

    #returns -1 if there's at least 1 human left after 30 days
    for row in range(len(next_grid)):
        for col in range(len(next_grid[row])):
            if next_grid[row][col]==0:
                return -1

    return num_days   #returns day when there are no humans left (no changes in the grid after a day)


print(days_remaining_3([[1,1,1,0,1,2,3],[2,1,0,1,0,2,2],[0,0,0,0,1,0,0],[0,1,0,0,0,1,0]]))
