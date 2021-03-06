#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Shrek Adventure
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

# sets up count variable
count = 0

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Shrek\'s House' : {
                  'south' : 'Swamp 1',
                  'east'  : 'Swamp 7',
                  'ogre'  : 'Shrek',
                  'item' : 'sign',
                  'north' : 'Swamp 5',
                  'west' : 'Swamp 2',
                },

            'Swamp 1' : {
                  'north' : 'Shrek\'s House',
                },
            'Swamp 7' : {
                  'west' : 'Shrek\'s House',
                  'south': 'Swamp 8',
                  'item' : 'potion',
                  'north' : 'Swamp 6',
               },
            'Swamp 8' : {
                  'north' : 'Swamp 7'
               },
            'Swamp 6' : {
                  'south' : 'Swamp 7',
                  'item' : 'donkey',
               },
            'Swamp 2' : {
                  'east' : 'Shrek\'s House',
                  'item' : 'Thing',
                  'north' : 'Swamp 3',
                  'south' : 'Swamp 4',
               },
            'Swamp 3' : {
                  'south' : 'Swamp 2',
               },
            'Swamp 4' : {
                  'north' : 'Swamp 2',
               },
            'Swamp 5' : {
                  'south' : 'Shrek\'s House',
                  'item' : 'another item',
               },

         }

#start the player in the Hall
currentRoom = 'Swamp 1'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Swamp 8' and 'donkey' in inventory and 'potion' in inventory:
      print('You escaped the swamp!!! But your journey has only begun... YOU WIN!')
      break

  ## If a player enters Swamp 5 and get 'another item', they lose
  elif currentRoom == 'Swamp 5' and 'another item' in inventory:
      print('The swamp begins to swallow you whole...you will never esacpe')
      break

  # don't mess with Shrek
  elif currentRoom == 'Shrek\'s House':
      count += 1
      if count == 5:
          print("Shrek has eaten you. You should have gotten out of his swamp.")
          break
