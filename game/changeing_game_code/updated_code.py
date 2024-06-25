#!/usr/bin/env python
a=0
import sys
import random
def exit_code():
    print("GAME OVER")
    sys.exit()
a=random.randint(1,2)

def UserChoice(traverleschoice):
    while True:
        user_answer=int(input("enter your choice"))
        if user_answer==0:
            return "invalid answer"
        elif user_answer > traverleschoice:
            return "invalid answer"
        else:
            return user_answer
def action1():
    print("you are a travller walking through a mysterious twon and all of a sudden you see a car")
    print("you see the cars door open")
    print("what do you do")
    print("(1) steal the car")
    print("(2)protect the car from being stolen")
    print("(3)walk away and forget about the car")
    user_answer=UserChoice(3)

    if user_answer==1:
        return 2
    elif user_answer==2:
        return 10
    else:
        return 12
def action2():
    print("you sprit towards the car and drive off")
    print("but all of a sudden you hear the police behind you")
    print("what do you do")
    print("(1)pull over")
    print("(2)drive faster away")
    user_answer=UserChoice(2)
    if user_answer==1:
        return 3
    else:
        return 4
def action3():
    print("you pull over for the police and are arrested")
    print("you are sent jail for 5 years")
    exit_code()

def action4():
    print("you drive away faster and faster until you see a police barracade")
    print("what do you do")
    print("(1) drive through the barracade")
    print("(2)stop and get arressed by the police")
    print("(3)get out of the car and run away from the police")
    user_answer=UserChoice(3)
    if user_answer==1:
        return 5
    elif user_answer==2:
        return 6
    else:
        return 7
def action5():
    print("you drive throught the barrcade and your car flips and explodes")
    print("you die")
    exit_code()
def action6():
    print("you get out of you car and the police arrsted you and you are snet to jail for 5 years")
    exit_code()
def action7():
    print("you get out of the car and run away from the police")
    print("the police yell for you to stop")
    print("what do you do")
    print("(1)keep running")
    print("(2)stop and get arrsted")
    user_answer=UserChoice(2)
    if user_answer==1:
        return 8
    else:
        return 9
def action8():
    print(" you keep running but you are tazered and fall to the ground")
    print("you are arrseted and sent to jail for 10 years")
    exit_code()
def action9():
    print("you stop running and are tackled to the ground")
    print("you are arresed and sent to jail for 10 years")
    exit_code()
def action10():
    print("you stand by the car for about 10 mins and wait for the owner to get back")
    print("when he get back he offer you pay you money for protecting his car")
    print("what do you do")
    print("(1) take the money")
    print("(2) leave and not take the money")
    user_answer=UserChoice(2)
    if user_answer==1:
        return 11
    else:
        return 12
def action11():
    print(" you take the money and walk off")
    return 12
def action12():
    print("walking down the road you see the car you where just at speeding round a conoer")
    print("just as it goes out of your sight you hear a massive bang and you know that the car carshed")
    print("you run to make sure everyone is ok and you hear someone stuck inside the car")
    print("the car is on fire")
    print("what do you do")
    print("(1)help the person stuck in the car")
    print("(2) walk away")
    user_answer=UserChoice(2)
    if user_answer==1:
        return 13
    else:
        return 15
def action13():
    print("you run over to the car and start to help the person out of the")
    print("as you start to help the person out of the car you smell pertrol")
    print("(1) help the person out of the car risking you own life")
    print("(2) walk away and save you own life")
    user_anwser=UserChoice(2)
    if user_anwser==1 and a==1:
        print("the car blow up you died")
        exit_code()
    elif user_anwser==1 and a==2:
        return 14
    else:
        return 16
def action14():
    print("you get the person out of the car and run")
    print("while you run you hear the car blow up behide you")
    print("you get up and start walking down the road again")
    return 16
def action15():
    print("as you are walking away you hear and explostion behind you but you still carry on walking down the street")
    return 16
def action16():
    print("you start walking down the street and you hear some one crying for help")
    print("you notice that someone has just stolen someones phone")
    print("you notice that the robber is running towards you")
    print("(1) stop the robber and get back the phone")
    print("(2) get out of the way and allow the robber to get past")
    user_answer=UserChoice(2)
    if user_answer==1 and a==2:
        return 17
    elif user_answer==1 and a==1:
        return 18
    else:
        return 21
def action17():
    print("you stop the robber and pick up the phone")
    print("you hand the phone back to the owner and they give you a £10 reward")
    print("you countine to walk down the street")
    return 21
def action18():
    print("you stop the robber and the phone falls to the ground and smashes")
    print("you hand the phone back to the owner")
    print("the owner blames you for breaking your phone and demands for you to say sorry")
    print("what do you do")
    print("(1) say sorry")
    print("(2) walk away")
    user_answer=UserChoice(2)
    if user_answer==1:
        return 19
    else:
        return 20
def action19():
    print("you say sorry and the owner of the phone walks away")
    return 21
def action20():
    print("you walk away and igonor the owner of the phone yelling at you")
    return 21
def action21():
    print("you walk down the street")
    exit_code()

user_action=[action1,action2,action3,action4,action5,action6,action7,action8,action9,action10,action11,action12,action13,action14,action15,action16,action17,action18,action19,action20,action21]
def main():
    print("starting the game")

    index = 0
    while True:
        action = user_action[index]
        nextaction = action ()
        index = nextaction - 1


if __name__ == "__main__":
    main()
