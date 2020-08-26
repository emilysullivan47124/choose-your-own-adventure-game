print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10


if age >= 18:
  print("You are old enough to play!")

  wants_to_play = input("Do you want to play? (yes/no) ").lower()
  if wants_to_play =="yes":
    print("Let's play! ")
    print("You are starting with ", health, "health.")

    left_or_right = input("First choice... Left or Right(left/right)? ").lower()
    if left_or_right == "left":
      across_or_around = input("You follow the path and reach a lake. Do you swim across or go around (across/around)? ").lower()
      if across_or_around == "around":
        print("You went around and reached the other side of the lake. ")
        hill_or_woods = input("Do you want to go up the hill or into the woods (hill/woods)? ").lower()
        if hill_or_woods == "hill":
          print("At the top of the hill you see a castle. ")
          front_or_back = input("Do you want to knock on the front door or go around back? (front/back)").lower()
          if front_or_back == "back":
            print("You see several people practicing with swords.  A beautiful young woman is watching them.  Suddently, a dragon swoops down and carries her away.  The king asks if anyone is willing to go rescue the princess. ")
            volunteer_yes_no = input("Do you volunteer? (yes/no) ").lower()
            if volunteer_yes_no == "yes":
              print("The king gives you a sword, armor, and a horse.  You head out after the dragon.  As you are riding, you come to a river. ")
              cross_or_ford = input("Do you cross here or look for a ford? (cross/ford) ").lower()
              if cross_or_ford == "ford":
                up_or_down_stream = input("You decide to look for a ford. Do you go up stream or down? (up/down) ").lower()
                if up_or_down_stream == "up":
                  print("You come to a ford, and the horse makes it across safely.  An old woman is on the other side.  She asks for you to help her cross the river so she doesn't get wet. ")
                  help_yes_no = input("Do you help her cross? (yes/no) ").lower()
                  if help_yes_no == "yes":
                    print("She thanks you and gives you directions to the dragon's cave.  You find the cave and leave your horse nearby. ")
                    straight_or_above = input("Do you go straight up to the cave or try to circle to approach from above? (straight/above) ").lower()
                    if straight_or_above == "straight":
                      print("Like the hero you ar, you march straight up to the cave.  You do not see the dragon or the princess. ")
                      challenge_or_sneak = input("Do you call out a challenge or sneak in? (challenge/sneak) ").lower()
                      if challenge_or_sneak == "sneak":
                        print("You sneak into the cave, which goes deep into the mountain.  You find the dragon and the princess sitting on a pile of gold. ")
                        attack_or_call = input("Do you attack or call to them? (attack/call) ").lower()
                        if attack_or_call == "call":
                          print("The princess greets you.  The king had arranged for the princess to marry a prince she didn't like. Instead, she had asked her friend the dragon to	come get her.  The dragon was going to take to a neighboring kingdom where she would be able to marry her true love.  You are glad you didn’t have to fight the dragon.  You win!")
                        elif attack_or_call == "attack":
                          print ("The princess screams a warning. The dragon lashes out with its tail and smashes you. You die. ")
                          health = 0
                        else:
                          print("That was not a valid answer. ")
                      elif challenge_or_sneak == "challenge":
                        attack_or_run = input("The dragon comes out of the cave with a roar. Do you attack or run? (attack/run) ").lower()
                        if attack_or_run == "attack":
                          print("You attack!  Before you get to the dragon, it lets out a blast of fire.  You die.")
                          health = 0
                        elif attack_or_run == "run":
                          print("You are not so heroic after all.  You run away and lose the game.")
                        else:
                          print("That was not a valid answer. ")
                      else:
                        print("That was not a valid answer. ")
                    elif straight_or_above == "above":
                      climb_left_right = input("Do you want to climb to the left or the right? (left/right) ").lower()
                      if climb_left_right == "left":
                        print("You climb to the left.  As you are climbing, you step on a snake and it bites you.  You die.")
                        health = 0
                      elif climb_left_right == "right":
                        print("You climb to the right. As you are climbing, the rocks start to slide.  You get crushed in a landslide and die.")
                        health = 0
                      else:
                        print("That was not a valid answer. ")
                    else:
                      print("That was not a valid answer. ")
                  elif help_yes_no == "no":
                    print("You don't want to cross the river again, so you keep going. You head in the direction you think the dragon went. A path leads up into the mountains. ")
                    horse_or_foot = input("Do you stay on your horse or go on foot? (horse/foot) ").lower()
                    if horse_or_foot == "horse":
                      print("You get to the dragon's lair and see it in the mouth of the cave. The dragon roars.  The horse rears and throws you.  You land on your head and die.")
                      health = 0
                    elif horse_or_foot == "foot":
                      print("You go on foot up the path.  By the time you reach the dragon's lair, there is no sign of the dragon - or the princess. You lose.")
                    else: 
                      print("That was not a valid answer. ")
                  else:
                    print("That was not a valid answer. ")
                elif up_or_down_stream == "down":
                  mountain_or_forest = input("You're across the river, but not sure where to go from here. Do you want to head for the mountain or head toward the forest? (mountain/forest) ").lower()
                  if mountain_or_forest == "mountain":
                    print("Your horse loses its footing on the path and you both fall.")
                    health = 0
                  elif mountain_or_forest == "forest":
                    print("As you pick your way through the forest, a howl spooks your horse and it bolts. You try to stay on, but it ducks under a tree branch which hits you in the head. You die.")
                    health = 0
                  else:
                    print("That was not a valid answer. ")
                else:
                  print("That was not a valid answer. ")
              elif cross_or_ford == "cross":
                hang_or_jump = input("You guide your horse into the river.  The water is too swift; it pulls the horse off its feet.  Do you hang onto the horse or jump off? (hang/jump) ").lower()
                if hang_or_jump == "hang":
                  print("The horse is swept over on top of you.  You drown.")
                  health = 0
                elif  hang_or_jump == "jump":
                  print("You are swept away and crash against rocks. You drown.")
                  health = 0
                else:
                  print("That was not a valid answer. ")
              else: 
                print("That was not a valid answer. ")
            elif volunteer_yes_no == "no":
              join_yes_no = input("A knight in shining armor volunteers.  Everyone cheers and gathers to see him off.  Do you join in? (yes/no) ").lower
              if join_yes_no == "yes":
                print("The crowd gathers to watch him set off.  There is not enough room for everyone who wants to see.  The crowd starts pushing.  You get knocked off your feet and get trampled by the mob. You die.")
                health = 0
              elif join_yes_no == "no":
                print("While everyone else gathers together, you head away from the castle.  At the gate, the knight comes galloping out.  You cannot get out of the way in time and he rides you over. You die. ")
                health = 0
              else:
                print("That was not a valid answer. ")
            else: 
              print("That was not a valid answer. ")
          elif front_or_back == "back":
            argue_or_side = input("You knock on the door, which is answered by the steward.  He looks you over with a sneer and sayst aht commoners need to go to the side door.  Do you argue or head to the side? (argue/side) ").lower()
            if argue_or_side == "argue":
              print("You try to argue that you are not a commoner and should be allowed in.  The steward sighs and calls the guards over.  You are arrested and thrown in prison for impersonating a noble. You lose.")
            elif argue_or_side == "side":
              print("You head for the side door.  As you walk down the road, a wagon comes barrelling along and runs you over. You die.")
              health = 0
            else:
              print("That was not a valid answer. ")
          else: 
            print("That was not a valid answer. ")
        elif hill_or_woods == "woods":
          berries_or_birds = input("YOu head into the woods.  As you travel, you get very hungry.  Some fat birds are eating berries off a bush.  Do you eat some berries or try to snare a bird? (berries/bird) ").lower()
          if berries_or_birds == "berries":
            print("The berries were poisonous.  You die.")
            health = 0
          elif berries_or_birds == "bird":
            print("You set a snare across the bush and try to catch a bird.  While you are waiting, a game warden comes by.  He arrests you for paoching and throws you in prison.  You lose.")
          else:
            print("That was not a valid answer. ")
        else: 
          print("That was not a valid answer. ")
      elif across_or_around == "across":
        print("You managed to swim across the lake, but were bit by a fish.  You lost 5 health. ")
        health -= 5
        in_or_continue = input("You are chilled through from your swim.  You see a house on the edge of the woods. Do you go in or continue on? (in/continue) ").lower()
        if in_or_continue == "in":
          sit_or_bed = input("The house looks empty. Do you sit in front of the fire or lay down on the bed? (sit/bed) ").lower()
          if sit_or_bed == "sit":
            stew_or_apple = input("You sit in front of the fire.  As you warm up, you start feeling hungry.  You look around and find a pot of stew on the stove and an apple in a cabinet. Do you eat the stew or eat the apple? (stew/apple) ").lower()
            if stew_or_apple == "stew":
              print("You dish out a big bowl of stew and eat it.  You start to feel better.  Gain 2 health. ")
              health += 2
              wash_or_search = input("Do you wash your dishes or search the house? (wash/search) ").lower()
              if wash_or_search == "wash":
                finger_or_pocket = input("The witch comes in to find you doing dishes.  She is so impressed she decides to reward you by giving you a gold ring. Do you put ring in your pocket or put ring on your finger? (finger/pocket) ").lower()
                if finger_or_pocket == "pocket":
                  woods_or_path = input("You say goodbye to the witch and leave the house.  Do you cut through the woods or follow the path? (woods/path) ").lower()
                  if woods_or_path == "path":
                    party_yes_no = input("At the end of the path is a troll who is having a birthday party.  He asks if you are coming to help him celebrate.  Do you say yes or no? (yes/no) ")
                    if party_yes_no == "yes":
                      ring_yes_no = input("The troll claps his hands for joy.  Do you give him the ring as a present? (yes/no) ")
                      if ring_yes_no == "yes":
                        print("You hand him the ring.  He puts it on his little finger and it starts to shrink, until it cuts off his finger.  He roars in pain and then beats you into a pulp with his good hand.  You die.")
                        health = 0
                      elif ring_yes_no == "no":
                        print("You sit down and he gives you a piece of cake. It is rock hard and tastes terrible.  You choke on the bite you took and die.")
                        health = 0
                      else: 
                        print("That was not a valid answer. ")
                    elif party_yes_no == "no":
                      print("The troll insists and says you are just in time for dinner.  Before you can try to move on, he throws you into a pot to cook.  You die. ")
                      health = 0
                    else:
                      print("That was not a valid answer. ")
                  elif woods_or_path == "woods":
                    print("You try to cut through the woods, but get lost.  From all around you, you hear howling.   Wolves surround you and eat you.  You die. ")
                    health = 0
                  else:
                    print("That was not a valid answer. ")                  
                elif finger_or_pocket == "finger":
                  print("You slip the ring on your finger. It starts to shrink.  You try to pull it off, but it shrinks down until it cuts off your finger.  The witch laughs as you bleed out.  You die.")
                  health = 0
                else:
                  print("That was not a valid answer. ")
              elif wash_or_search == "search":
                print("The witch comes home and finds you searching the house.  She turns you into a mouse.  You lose! ")
              else:
                print("That was not a valid answer. ")              
            elif stew_or_apple == "apple":
              print("The apple was poisoned!  You die. ")
              health = 0
            else:
              print("That was not a valid answer. ")
          elif sit_or_bed == "bed":
            print("You fall asleep.  You wake up suddenly to find a wolf next to you.  'Why grandma, you look different' it says right before it eats you up. ")
            health = 0
          else:
            print("That was not a valid answer. ")
        elif in_or_continue == "continue":
          print("You suffer from hypothermia and die.")
          health = 0
        else:
          print("That was not a valid answer. ")
      else:
        print("That is not a valid answer. ")
    elif left_or_right == "right":
      print("You fell off a cliff and died.")
      health = 0
    else:
      print("That was not a valid answer. ")
    
    print("Your final health was ", health, "points. ")
    if health == 0:
      print("You died. ")
    else:
      print("You survived! ")

  else:
    print("See you later! ")

else:
  print("You are not old enough to play. Try again when you are older!") 