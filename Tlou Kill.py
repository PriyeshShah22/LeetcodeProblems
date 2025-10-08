import random
import time

player_distance = 0
men_to_defeat = 1
man_distance = random.randint(1, 7)
caught = False

print("A man is coming towards you. You need to kill him before he reaches you and pass through!")

while not caught:
    print(f"\nThe man is {man_distance} meters away from you.")
    action = input("Type 'grab' to grab him or 'hold' to wait or 'headshot' to shoot: ").lower()

    if action == 'grab':
        if man_distance == 2 or man_distance == 1:
            print("\nYou grabbed and killed the man. You survived!")
            caught = True
        else:
            print("\033[36mThe man is too far to grab. You are spotted, chance to grab failed.\033[0m")
            if time_challenge():
                print("\nYou quickly escaped and killed the man with a melee!")
                caught = True
            else:
                print("\033[36m\nYou failed to escape and were overpowered.\033[0m")
    elif action == "headshot":
        if man_distance <= 1:
            print("\nYou shot him in head nice job. You survived!")
            caught = True
        else:
            print("\033[36mToo far. Your missed the shot. Your position is exposed.\033[0m")
            men_to_defeat += 2
            print("Two more enemies are in front of you play smart to win. Total 3 to kill.")
            smart = input("Type your strong move: ").lower()
            if smart == "moltov" or smart =="nailbomb" or smart == "shotgun":
                print("Big Brain you killed them.")
                caught = True
            else:
                print("\033[36mYou died. Be Smarter than how that.\033[0m")
                begging = input("If you beg you can get respawned.(Enter 'I beg'):")
                if begging == "I beg":
                   man_distance = random.randint(1, 7)
                   begging = ""
                else:
                    break
    elif action == 'hold':
        if man_distance > 0:
            times = int(input("\nHow many meters do you want to hold?: "))
            man_distance -= times
        else:
            man_distance -= 1
        if man_distance <= 0:
            print("\033[36mThe man reached you and killed you. You couldn't survive!\033[0m")
            begging = input("If you beg you can get respawned.(Enter 'I beg'): ")
            if begging == "I beg":
                man_distance = random.randint(1, 7)
                begging = ""
            else:
                break
    else:
        print("\nDumb action.You have been killed.""\nGame over. You Lost!")
        exit()

if caught:
    print("\033[32m\nGame Over. You won!\033[0m")
else:
    print("\033[31m\nGame Over. You lost!\033[0m")