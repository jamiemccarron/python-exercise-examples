import json
import sys

gold_bar = 0
print("you will start with a swoard")
print("your goal is to collectec 5 gold bars")


def UserChoice(travlerchoice):
    while True:
        user_answer = int(input("entre in you choice"))
        if user_answer <= 0:
            print("Invalid choice try again")
        elif user_answer > travlerchoice:
            print("Invalid choice out of range")
        else:
            return user_answer


game = {
    'StartingPosition': 'room1',

    "room1": {
        "description": "you are in a room and you can go north,south,west and east",
        "choices": [
            {
                "user_answer": "go north",
                "nextroom": "room2"
            },
            {
                "user_answer": "go south",
                "nextroom": "room3"

            },
            {
                "user_answer": "go east",
                "nextroom": "room4",
            },

            {
                "user_answer": "go west",
                "nextroom": "room5"

            },
        ]
    },
    "room2": {
        "description": "there is a troll in the room about to acctack you",
        "choices": [
            {
                'user_answer': '1: Fight',
                'result': 'you have killed the troll',
                'nextroom': 'room7',

            },
            {
                'user_answer': '2: Run Away',
                'result': 'you have ran back to the starting room',
                'nextroom': 'room1'
            }
        ]
    },
    "room3": {
        "description": "there is an empty room with with furthanter in it",
        "choices": [
            {
                "user_answer": "1 search the room",
                "nextroom": "room1"
            },
            {
                "user_answer": "2 go to the starting room",
                "nextroom": "room1"
            }
        ]
    },
    "room4": {
        "description": "there is an empty room with with furthanter in it",
        "choices": [
            {
                "user_answer": "1 search the room",
                "1": "you found a gold bar",
                'nextroom':"room1"

            },

            {
                'user_answer': '2 go back to the starting room',
                'nextroom': 'room1'
            },
        ],
    },
    "room7": {
        "description": "you kill the troll and see a securet door. Do you go in",
        "choices": [
            {
                "user_answer": "1 yes",
                "nextroom": "room6"
            },
            {
                "user_answer": "2 no",
                "result": "you will go back to the starting room",
                "nextroom": "room1"
            }
        ]
    },
    "room5": {
        "description": "there is an empty room with with furthanter in it",
        "choices": [
            {
                "user_answer": "1 search the room",
                'nextroom': "room1"
            },
        ],

    },
    "room6": {
        "description": "you are in a room with a giant spider which is about to acctack",
        "choices": [
            {
                "user_answer": "1 kill the spider run",
                "result": "you get 1 gold bar form killing the spider and retrun to the starting room",
                "nextroom": "room1"
            },
            {
                "user_answer": "2 retrun to the frist room",
                "nextroom": "room1"
            }
        ]
    }
}


def runRoom(room):
    print(room['description'])

    if len(room['choices']) == 0:
        sys.exit()

    for i in room['choices']:
        print(i['user_answer'])

    user_answer = UserChoice(len(room['choices']))

    return room['choices'][user_answer - 1]['nextroom']
    return room['choices'][user_answer - 1]["result"]


def main():
    print("starting the game")

    startingRoom = game['StartingPosition']
    roomKey = startingRoom
    while True:
        room = game[roomKey]
        roomKey = runRoom(room)


if __name__ == "__main__":
    with open('game.json', 'w') as fd:
        fd.write(json.dumps(game, indent=4))
    main()
