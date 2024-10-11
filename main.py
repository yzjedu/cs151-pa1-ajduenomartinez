


print("You wake up in an elevator, with no memory of how you got there. As you stand up, \nyou begin to try and retrace your steps, but"
      "you cannot remember how you came to be \ninside the elevator. You begin to ask yourself questions to try and jog your memory.")
name=str(input("What is your name?: "))
while name == "":
    print("Did you forget your name or something? Try again")
    name=str(input("Actually try this time: "))
print('You begin to look around, and you ask yourself: what you should do now? You wonder \nif you should leave the elevator, or stay in '
      'it and wait to see what happens.')
input('Leave elevator?: ')
print('It seems that no matter what you thought to do, you could only decide if you thought \nof a number when trying to decide what to do... '
      'That certainly IS strange. You ask \nyourself again if you should (1) Leave the elevator, or (2) stay in the elevator. ')
intro=str(input('Leave elevator?:' ))
while intro not in ('1', '2') and intro != '':
    print('Okay', name,', I tried explaining it in the context of the story but it seems you still \ndont get it so I guess Ill have to be straight up'
          ' about it. For the options in this game, you have to enter the \nactual DIGIT next to an option. Not the WORD of the number.'
          ' Ex. enter 1, not One. Got it? OK, lets try this again.')
    intro = str(input('Leave elevator?:'))
if intro == '2':
    print('You have decided to stay in the elevator. Going outside frightens you, and the \nsmall, cozy elevator brings you comfort. '
          'You decide to never leave the elevator, as the thought of even stepping outside \nthe elevator absolutely petrifies you.\nTHE END. (Try Again!) ')
    exit()

print('You have decided to leave the elevator. It was getting cramped in here anyway. You see three buttons on the elevator.')
elevator_floor=str(input("What floor?: "))
while elevator_floor not in ('1', '2', '3') and elevator_floor != '':
    print("You try to press a button that isn't there, so you don't actually go anywhere. You wonder why you tried doing that.")
    elevator_floor = str(input("What floor?: "))


if elevator_floor=='1':
     print("The elevator doors open to reveal a dark, narrow, stony hallway. Due to a lack of \nany other option, you begin to "
           "walk down the hallway. After what feels like hours of walking,\n you eventually reach a light at the end of the tunnel,"
           "and see a small underground city populated \nby giant worms and moles. There seems to be one nearby. Will you (1) Approach it,"
           "or walk past it?")
     talk_mole=str(input('Talk to the mole?: '))
     while talk_mole not in ('1', '2') and talk_mole != '':
         print('You awkwardly stare at the mole.')
         talk_mole = str(input('Will you stop staring awkwardly at the mole and talk to it?: '))
     if talk_mole == '1':
         print('Mole: Hello traveler! Welcome to our humble little village! There isnt much to see, \nbut we hope you enjoy your '
               'stay! If you need somewhere to rest, you can go to the local inn. \nIf you want to leave, youd have to go through '
               'the old mineshaft, but its easy to get lost in there.\n Either way, I wish you luck on your endeavors!')

     if talk_mole == '2':
         print('You keep walking into the village, walking past families of worms and moles. \nYou think its nice but also kinda gross.'
           'As you keep walking, you take notice of an old abandoned mineshaft. \nMaybe there is an exit in there somewhere. You also see'
           'an In; you wonder if perhaps you should rest before continuing. Will you (1) go to the mines, or (2) go to the Inn?')
     if talk_mole == '1':
        print('Will you heed the advice of the friendly mole and (1) go to the mines, or (2) go to the Inn?')
     cave_decision=str(input('Where will you go?: '))
     while cave_decision not in ('1', '2') and cave_decision != '':
         print('You stand idly, not really doing anything.')
         cave_decision=str(input('Will you make up your mind?: '))
     if cave_decision== '2':
         print('You decide to go to the inn. Its a small, homey place, and you feel at ease there.\n After getting the keys to your'
               'room, you decide to turn in for the night. Then you realize you dont\n even know what time of day it is because '
               'you are underground. You shrug it off, and swiftly fall asleep.\n You wake up after a delightful nap, feeling refreshed, '
               'and ready to go to the mines. \nWill you (1) Leave the inn, or (2) Stay?')
         inn_decision= str(input('What will you do?: '))
         while inn_decision not in ('1', '2') and inn_decision != '':
             print('You stay lying in the bed, staring at the ceiling.')
             inn_decision= str(input('Will you roll out of bed?: '))
         if inn_decision == '2':
             print('Against all odds, you decide to stay in the inn, and fall asleep again. However, when you awaken, \nyou are in your bed,'
                   ' and realize it was all a dream. What a lame ending.'
                   '\nTHE END (Try again!)')
             exit()
     print('You make your way to the mines. You approach the old-looking entrance to the mines, \nand you reluctantly walk inside. '
             'After walking for a while, you arrive to a fork in the road, with three possible paths. \n'
           'Will you go (1) Left, (2) Middle, or (3) Right.')
     while True:
         mines_choice = input('Where do you go?: ')
         if mines_choice == '':
             print('You stare at the different pathways, unable to make a choice.')
             continue
         try:
             mines_choice = int(mines_choice)
             if mines_choice == 1:
                print('You walk into a dead end. There is a note on the floor: "This is a dead end"')
             elif mines_choice == 2:
                print('You walk through the middle path, and after walking a while, you wind up in the exact same room you \n'
                'were in. It’s unmistakable. These mines do not follow the \nlaws of physics. You spare yourself the headache, and '
                'decide to just pick another path.')
             else:
                 print('You stare at the different pathways, unable to make a choice.')
         except ValueError:
             print('You stare at the different pathways, unable to make a choice.')
         if mines_choice == 3:
             break
     print('You walk into the right path. You have a good feeling about this one. As you walk further in, \nyou see a light'
           'at the end of the tunnel. You make your way to the end of the tunnel, and on the other side is... \nThe exit. \nTHE END')
     exit()


elif elevator_floor=='2':
    print("The elevator doors open, and you see what seems to be a foggy forest. \nYou are unsettled, but you proceed."
          "You reach a river long enough that you cannot walk across. \nThere appears to be a bridge a bit farther upstream. "
          "Will you (1) Try walking through the river or (2) Go to the bridge?")
    forest_choice = str(input('What do you do?: '))
    while forest_choice not in ('1', '2') and forest_choice != '':
        print('You stand by the river, doing nothing.')
        forest_choice = str(input('What do you do?: '))
    if forest_choice == '1':
        print('You decide that bridges are for weaklings and try to walk through the river. \nUnfortunately, you forgot you are not'
              'actually able to "walk" through a river, so you \nare taken by the strong current and are taken away, never to be seen again. \n'
              'THE END (Try again!)')
        exit()
    if forest_choice == '2':
        print('You make your way to the bridge. Before you can cross it, a gnome stops you. \nGnome: "Halt! You must pay the '
              'Gnome bridge tariff before crossing the gnome bridge!" \nYou realize you happened to have a bag filled with '
              'twenty dollars in pennies. You are befuzzled \nas to how you did not notice this extremely heavy bag of coins on your person. '
              'You decide to give the gnome some money. \nHow many pennies will you give it? (Hint: write your answer in "00.00", like '
              'actual money)')
        while True:
            try:
                gnome_money = float(input('How much money will you give the gnome?: '))

                if gnome_money <= 0.0:
                    print('The gnome yells at you: \nGnome: "You cant just not pay the gnome bridge tariff! Fork over the cash, bub!"')
                else:
                    break
            except ValueError:
                print('The gnome yells at you: \nGnome: "You cant just not pay the gnome bridge tariff! Fork over the cash, bub!"')

        if gnome_money <= 4.99:
            print('You give the gnome a small amount of money. The gnome reluctantly lets you pass.')
        elif 5.00 <= gnome_money <= 9.99:
            print('You give the gnome a decent amount of money. The gnome lets you pass.')
        elif 10.00 <= gnome_money <= 14.99:
            print('You give the gnome a large amount of money. The gnome happily lets you pass.')
        elif 15.00 <= gnome_money <= 19.99:
            print('You give the gnome a huge amount of money. The gnome is too busy literally jumping for joy to \ncare if you '
                  'cross the bridge, so you just cross the bridge.')
        elif gnome_money >= 20.00:
            print('The gnome passes out due to your extreme generosity and sheer amount of money he just recieved. \nYou cross'
                  'the bridge.')
    print('As you walk deeper into the forest, you see a witches hut. You know you probably shouldnt even consider it, \n'
          'but you think about walking in. Will you (1) Be reasonable and walk past the witches hut, or (2) walk into the'
          'witches hut?')
    witch_hut = str(input('What do you do?: '))
    while witch_hut not in ('1', '2') and witch_hut != '':
        print('You get a good look at the witches hut. you hear cackling coming from inside.')
        witch_hut = str(input('What do you do?: '))
    if witch_hut == '2':
        print('You very recklessly decide to walk into the witches hut. Unsurprisingly, there is a witch inside.\n'
              'Witch:"', name, ', what are you doing here?!, Get out of my witches hut!!" \nIt seems the witch somehow'
              'knew your name likely because of her evil witch magic. \nThe witch then raises her evil magic staff and waves '
              'it at you, warping you outside her hut. \nYou appear to be unscathed, so you keep walking. As you keep walking, you '
              'begin to feel \n strange, and you suddenly transform into a frog. It seems you are now destined to live '
              'as a frog. How unfortunate?? \nTHE END (Try again!)')
        exit()
    print('You very sensibly decide to walk past the witches hut. After walking a while, you eventually \nreach a fountain'
          'with a large statue of a fairy. You dont really see \nanywhere else to walk after this so you sit by the fountain.'
          'You feel exhausted from walking so much. \nWill you (1) Drink water from the fountian, or (2) fall asleep by the fountain? ')
    fairy_fountain = str(input('What do you do?: '))
    while fairy_fountain not in ('1', '2') and fairy_fountain != '':
        print('You cant decide on what to do, so you do both. As you fall asleep after drinking fairy water, \nyou have wicked dreams, '
              'from which you are destined to never wake up from. How unfortunate. \nTHE END (Try again!)')
        exit()
    if fairy_fountain == '1':
        print('You decide to take a sip of the fairy fountain water. You feel incredibly soothed. \nBut then you notice that '
              'your body is starting to fade away. You panic, but nothing \nyou do seems to make it stop. When youve completely'
              'vanished, you wake up on the sidewalk \nof your childhood home. You are so happy to be back that you cannot care'
              'to think of how this \nhappened. \nTHE END')
        exit()
    if fairy_fountain == '2':
        print('As you fall asleep, you see the statue start to move and wave her wand at you. \nYou wake up in the alley behind your favorite'
              'restaurant. You figure you might as well grab a bite while youre there. \nTHE END')
        exit()



elif elevator_floor=='3':
    print("The elevator doors open up to the 57th floor of what appears to be an office \nbuilding. You wonder how you wound up"
          "on the 57th floor even though there are only \nthree buttons on the elevator. You shrug it off and walk into the office. "
          "You look around, \nbut you cant seem to see or hear anybody or any movement whatsoever. Huh. There are only two paths you can see. "
          "\nYou can either (1) Go to the bathroom, or (2) Open the unmarked door in front of you.")
    bathroom = str(input('What do you do?: '))
    while bathroom not in ('1', '2') and bathroom != '':
        print("You stand in the boring, hardly decorated room, doing nothing.")
        bathroom = str(input('What do you do?: '))
    if bathroom == '1':
        print('You walk into the bathroom. You dont really need to use the stalls, so you just wash your face. \nDo you (1) Leave the bathroom'
              'or (2) Stay? ')
        bathroom_2 = str(input('What do you do?: '))
        while bathroom_2 not in ('1', '2') and bathroom_2 != '':
            print('You stare at yourself in the mirror. Despite everything, its still you.')
            bathroom_2 = int(input('What do you do?: '))
            if bathroom_2 == '2':
                print('You stay in the bathroom and wash your face again. And again. And again. You cant \nseem to stop washing your face. You'
                      'wash your face so much that your skin washes off and now \nyour face is just a skull with eyeballs. You start to really freak out,'
                      'but then you realize: today is halloween! \nNobody is going to notice your skullface! You confidently walk out of the bathroom.')
            if bathroom_2 == '1':
                print('You walk out of the bathroom with a freshly washed face.')
    print('You walk past the bathroom and into the unmarked door. You walk into another room, very similar to the one \nyou were just in,'
          'except now there are two doors, a left and a right one. The left door seems to be calling to you. \nWill you walk into the (1) left'
          'door, or the (2) right door?')
    doors_choice = str(input('What door do you pick?: '))
    while doors_choice not in ('1', '2') and doors_choice != '':
        print('You stare at the doors, unable to make a choice.')
        doors_choice = str(input('Will you pick a door already?: '))
    if doors_choice == '2':
        print('Although everything in you was telling you to walk through the left door, you ignore your intuiton, \nand walk through'
              'the right door. On the other side of the door was the office \nbreak room. It was a truly magnificent break room.'
              'You really had to sit down and let it \nsink in. The realization that every break room you see after this will be'
              'absolutely\n horrible began to sink in, and you started to feel an inkling of despair. You decided it was time to leave '
              '\nthe break room. It was an incredibly difficult choice, but you simply could not \nstay there any longer. You turned around,'
              ' walked out of the break room, and back into the left door. \nYou dont know how youll be able to move on after what just occured.')
    print('After walking through the left door, you realize it really wasnt as interesting as you thought it would be. All you see are two sets of stairs. '
          'One goes up and the other goes down. Will you go (1) Down the stairs, or (2) Up the stairs?')
    stairs_choice = str(input('Where will you go?'))
    while stairs_choice not in ('1', '2') and stairs_choice != '':
        print('You stare at the stairs, unable to make a choice.')
        stairs_choice = str(input('Where will you go?'))
    if stairs_choice == '1':
        print('You begin to walk down the stairs. You arrive at a parking garage. You wander the \nparking garage for a bit, and then realize'
              ' that the way you came in is no longer there. You freak out and\n start frantically looking for an exit. You are destined to forever'
              'roam the parking garage. \nTHE END (Try again?!)')
        exit()
    if stairs_choice == '2':
        print('You begin to walk up the stairs. You reach a really big office with many decortaions, and a door that says "CEO" on it. At this point,'
              ' you dont think there is much of a reason to not walk through the door.')
        try:
            bathroom_2
        except NameError:
            bathroom_2 = '1'
        if bathroom_2 == '2':
            print('You walk through the door. The CEO of the company is sitting at his desk. He swivels \nhis chair around to '
                  'look at who just entered his office. To his horror, was you, \na person with a skull for a face. He began to scream'
                  'at security to get you out of his office. \nAs security carries you out of the building, you wonder why he was so shocked'
                  ' to see you. It is only\n then that you come to the terrifying realization: today ISNT halloween. Its April 23rd. You have '
                  'literally\n no idea how you arrived to the conclusion that it was halloween. You are thrown out of the building. \nYou escaped, but now '
                  'you have to live a skullface instead of a normal person face. \nTHE END')
            exit()
        if bathroom_2 == '1':
            print('You walk through the door. The CEO of the company is sitting at his desk. He swivels \nhis chair around to '
                  'look at who just entered his office. He begins to yell at you, \nsaying something about you interrupting a really important call?'
                  'You cant hear him clearly over how hard he is yelling. \nHe calls security to escort you out of the building. You finally escape the office building. '
                  '\nGood job. \nTHE END')
            exit()