# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Killer Wolf Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the killer Wolf.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def player_stat():
    print("-" * 20)
    print('You are in the {}'.format(currentRoom))
    print("-" * 20)


def main():
    pass

expand_roon (rooms['Main Fair ground']["south"])
def expand_room (myTuple):
     roomName, listOfItems = myTuple


rooms = {
    'Main Fair ground': {'South': ('Food stand',['1LB of meat','item2'])a,
                         'North': ('Arcade',[]),
                         'item' : 'real sword',
                         'East': 'Corn field',
                         'item' : 'wolf repellent',
                         'West': 'Candy shop',
                         'item' : 'candy'},
    'Security': {'item': 'protective gear', 'East': 'Food stand'},
    'Gift shop': {'item': 'map', 'West': 'Arcade'},
    'Petting area': {'item': 'killer wolf', 'South': 'Corn field'}  # villain
}

currentRoom = 'Main Fair ground'
player_move = ''

while currentRoom != 'Exit':
    player_stat()
    player_move = input('Enter your move:\n').lower()
    if player_move in ['Exit', 'exit']:
        currentRoom = 'Exit'
        print('Play again soon')
        continue
try:
    currentRoom = rooms[currentRoom][player_move]
except Exception:
    print("invalid move")
    continue

if 'Petting' == currentRoom:
    print("Kill the wolf")