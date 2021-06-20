def act3():
    print('As you await for your execution, you hear a roar come from the skies above.')
    print('You pay no heed, untill your name is called up for execution when a dragon appears.')
    print('As mass panic ensues you hear a voice shout out for you to come and follow them, do you listen?')
    
    answer= input(">").lower()

    if "y" in answer:
        act4()
    else:
        print('The dragon torches you and all surrouding alive\nGAMEOVER')

def act2():

    print('Lokir: D**n you Stormcloaks. Skyrim was fine until you came along.')
    print('lokir: Empire was nice and lazy. If they hadnt been looking for you')
    print('Lokir: I could’ve stolen that horse and been half way to Hammerfell')
    print('Lokir: You there. You and me — we shouldnt be here. It’s these Stormcloaks')
    print('Lokir: the Empire wants.')
    print('Guard: Be quiet back there you scum')
    print('the other Guard: We are at the keep, prepare your necks')
    print('Lokir: wait i shouldnt be here, i have no idea who this stormcloak man is')
    print('As Lokir runs away from the execution site he gets shot down by a nearby archer')
    print('do you wish to stay and await execution, or attempt to run away')

    answer= input(">").lower()

    if "run" in answer:
       print('as you run away from the cart, y ou to are shot down with an arrow\nGAME OVER')

    if "stay" in answer:
        act3()
def game():
    print('Hey, you. Youre finally awake')
    
    answer= input(">").lower()
    
    if "h" in answer:
        print ('Ralof; you were trying to cross the border right? walked right into that Imperal ambush, same as us, and that thief over there.')
        act2()
    else:
        print('Ralof; oh, guess ye arnt the dragonborn')
game()     
