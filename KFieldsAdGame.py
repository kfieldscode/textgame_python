import random
import time

dog_breeds = (
    "Yorkie", "Husky", "Pug", "Poodle", "Great Dane", "German Shepard")
cat_breeds = (
    "Persion", "Tabby", "Munchkin", "Russian Blue", "Siamese", "Maine Coon")
cat = random.choice(cat_breeds)
dog = random.choice(dog_breeds)
choices = []


def print_pause(string):
    print(string)
#    time.sleep(3)


def intro():
    print_pause(
        "The year is 2050, the pet-zombie apocalypse "
        "just began 3 years ago.")
    print_pause(
        "You've managed to survive in an abandoned "
        "woodland cabin with your two beloved pets:")
    print_pause(f"A {cat} cat named Muzzie and a {dog} dog named Rocket.")
    print_pause(
        "Muzzie & Rocket are no match for the pet-zombies, "
        "they're just too cuddly.")
    print_pause("And you're no match for pet-zombies either,")
    print_pause("for they travel in massive hoards you cannot match!")
    print_pause(
        "In fact, there's an oncoming pet-zombie "
        "hoard heading your way tonight,")
    print_pause(
        "and your job is to keep Muzzie & Rocket safe "
        "from becoming pet-zombies!")
    print_pause("But unfortunately, your farm has failed this season, ")
    print_pause("and you and your pets are starving!")
    print_pause(
        "You will need to wait until tomorrow to "
        "retrieve more food & supplies.")
    print_pause(
        "With you & your pets starving, you scrumage through your stock pile,")
    print_pause("and behold, you only have one can of chicken left.")


def feed_question():
    answer = input(
        "Do you feed yourself or your pets? "
        "Please type either \"yourself\" or \"pets\"").lower()
    if answer == "yourself":
        choices.append("you")
        print_pause("You have decided to feed yourself over your pets.")
        print_pause(
            "Your pets quiver in hunger and relentlessly whine for food.")
        print_pause(
            "But now, at least you will have enough "
            "energy to prepare for the night,")
        print_pause(
            "but your pets may be uncooperative until they're fed tomorrow.")
    elif answer == "pets":
        choices.append("pets")
        print_pause(
            "You have decided to feed your pets over yourself, how generous!")
        print_pause(
            "Your pets will now be more cooperative throughout the night,")
        print_pause("but you are starting to feel weak from starvation.")
    else:
        print("Sorry, I don't understand.")
        feed_question()


def explain_choices():
    print_pause("Now it is time to make preparations for tonights hoard.")
    print_pause(
        "But time is running out, you see the sun "
        "slowly approaching nightfall.")
    print_pause(
        "You're brainstorming for ideas on how to protect your pets tonight.")
    print_pause("- You notice a deer carcass just beyond your front yard.")
    print_pause(
        "You can move it further away from your cabin to "
        "provide a distraction for the zombie hoard.")
    print_pause(
        "- You also have a set-up of wooden planks that"
        " you can use to board up your cabin,")
    print_pause(
        "which prevents zombies from coming in, "
        "or your pets from running out.")
    print_pause(
        "- Lastly, you remember the cellar deep within "
        "the basement of your cabin.")
    print_pause(
        "If you can manage to get your pets in there and "
        "lock them up, they may be protected for the night.")
    print_pause(
        "Unfortunately, there just isn't enough time "
        "to perform all these precautions.")
    print_pause("You only have enough time to do some.")


def first_question():
    first = input(
        "You have 3 choices, but you can only pick 2. Order doesnt matter."
        " \nPlease type the number for your pick. \n "
        "1. Provide distraction with deer carcass. \n "
        "2. Board house up. \n 3. Hide your pets in the cellar.")
    time.sleep(3)
    if first == "1":
        choices.append("distract")
        print_pause(
            "You have chosen to distract the zombies "
            "with the deer carcass first.")
        print_pause(
            "You head outside and drag the deer carcass "
            "further away from your cabin.")
    elif first == "2":
        choices.append("board")
        print_pause("You have chosen to board up your house first.")
        print_pause(
            "You head outside and build a protective "
            "layer of wood around your cabin.")
    elif first == "3":
        choices.append("hide")
        print_pause("You have chosen to hide your pets first.")
        print_pause(
            "You gather up your cat Muzzie & your dog "
            "Rocket and lock them in the cellar.")
    else:
        print("Sorry, I don't understand.")
        first_question()


def second_question():
    if "distract" in choices:
        second = input(
            "Time is running out, you now have 2 choices left."
            " You can only pick 1. \nPlease type the number for your pick. "
            "\n1. Board \n2. Hide \n")
        if second == "1":
            choices.append("board")
            print_pause("You have chosen to board up your house last.")
            print_pause(
                "You head outside and build a protective "
                "layer of wood around your cabin.")
            return
        elif second == "2":
            choices.append("hide")
            print_pause("You have chosen to hide "
                        "your pets in the cellar last.")
            print_pause("You gather up your cat Muzzie & your dog Rocket,")
            print_pause("then lock them in the cellar just before nightfall.")
            return
        else:
            print("Sorry, I don't understand.")
            second_question()
    if "board" in choices:
        second = input(
            "You have 2 choices. You can only pick 1. "
            "\nPlease type the number for your pick. "
            "\n1. Distract \n2. Hide \n")
        if second == "1":
            choices.append("distract")
            print_pause(
                "You have chosen to distract the zombies "
                "with the deer carcasss last.")
            print_pause(
                "You head outside and drag the deer "
                "carcass further away from your cabin.")
            return
        elif second == "2":
            choices.append("hide")
            print_pause("You have chosen to hide your "
                        "pets in the cellar last.")
            print_pause("You gather up your cat Muzzie & your dog Rocket,")
            print_pause("then lock them in the cellar just before nightfall.")
            return
        else:
            print("Sorry, I don't understand.")
            second_question()
    if "hide" in choices:
        second = input(
            "You have 2 choices. You can only pick 1. "
            "\nPlease type the number for your pick. "
            "\n1. Distract \n2. Board \n")
        if second == "1":
            choices.append("distract")
            print_pause(
                "You have chosen to distract the zombies "
                "with the deer carcasss last.")
            print_pause(
                "You head outside and drag the deer carcass "
                "further away from your cabin.")
            return
        elif second == "2":
            choices.append("board")
            print_pause("You have chosen to board up your house last.")
            print_pause(
                "You head outside and build a protective "
                "layer of wood around your cabin.")
            return
        else:
            print("Sorry, I don't understand")
            second_question()


def summary():
    print_pause("Just to summarize your actions so far, you have:")
    if "distract" and "hide" in choices:
        if "you" in choices:
            print_pause("- Fed yourself over your pets")
            print_pause(
                "- Provided a distraction for the zombies "
                "& hid your pets. But did not board your house.")
            return
        if "pets" in choices:
            print_pause("- Fed your pets over yourself.")
            print_pause(
                "- Provided a distraction for the zombies "
                "& hid your pets. But did not board your house.")
            return
    if "distract" and "board" in choices:
        if "you" in choices:
            print_pause("- Fed yourself over your pets.")
            print_pause(
                "- Provided a distraction for the zombies &"
                " boarded your cabin. But did not hide your pets.")
            return
        if "pets" in choices:
            print_pause("- Fed your pets over yourself.")
            print_pause(
                "- Provided a distraction for the zombies &"
                " boarded your cabin. But did not hide your pets.")
            return
    if "board" and "hide" in choices:
        if "you" in choices:
            print_pause("- Fed yourself over your pets.")
            print_pause(
                "- Boarded your house & hid your pets. You "
                "did not provide a distraction for the zombies.")
            return
        if "pets" in choices:
            print_pause("- Fed your pets over yourself.")
            print_pause(
                "- Boarded your house & hid your pets. You "
                "did not provide a distraction for the zombies.")
            return


def see_fate():
    go = input(
        "Are you ready to continue? Enter \"yes\" to see "
        "the fate of you & your pets.").lower()
    if go != "yes":
        print(
            "Sorry, I don't understand. There is no time to stall. "
            "It's time to see your pets fate!")
        see_fate()


def final_act():
    if "distract" and "hide" in choices:
        if "you" in choices:
            print_pause(
                "Since you weren't starving, you had enough "
                "energy to provide a proper distraction for the zombies,")
            print_pause(
                "they stayed far away from the cabin so "
                "there was no need to board up the house.")
            print_pause(
                "But your pets were extremely fussy since "
                "they had not eatened.")
            print_pause(
                "Luckily, your cellar was secure enough "
                "to hold in a hungry dog.")
            print_pause("But your cat Muzzie, unfortunately ... ")
            print_pause("was very uncooperative and curious "
                        "due to hunger ...")
            print_pause(
                "she managed to slip out of cracks "
                "unknown to you in the cellar...")
            print_pause(
                "since there were no boards, she "
                "easily pranced outside the cabin.")
            print_pause("towards the deer carcass you fed to the zombies!!!")
            print_pause(
                "Curiousity killed the cat, your Muzzie is now a ZOMBIE-CAT!")
            print_pause(
                "Your dog Rocket suvived, but your cat's been ZOMBIFIED.")
            print_pause(
                "Muzzie joins the pet-zombie hoard as a zombie now, you LOSE!")
            return
        if "pets" in choices:
            print_pause(
                "Since you were starving, you pass out "
                "from starvation in the cellar with your pets.")
            print_pause(
                "You were unconscious all night, therefore"
                " you weren't able to watch over your pets.")
            print_pause(
                "You wake up the next morning to your stomach grumbling...")
            print_pause("Only to find that... miraciously,")
            print_pause("your pets remained in the cellar and survived!")
            print_pause(
                "Since they weren't starving, they were "
                "content in their hiding spots.")
            print_pause(
                "You leave immediately to head to the "
                "nearby shelter for food.")
            print_pause("Both of your pets survived, "
                        "for they are not zombies!")
            print_pause("Congratulations, you WIN!")
            return
    if "distract" and "board" in choices:
        if "you" in choices:
            print_pause(
                "Since you weren't starving, you had enough "
                "energy to board up the cabin properly.")
            print_pause(
                "But both your pets were extremely fussy due to hunger.")
            print_pause("Smelling the deer carcass outside,")
            print_pause(
                "both your hungry pets try to escape to "
                "feed on the carcass.")
            print_pause("The board is strong enough to "
                        "hold in your fussy cat.")
            print_pause(
                "But despite your strong boards, your dogs "
                "hunger was able to overpower them.")
            print_pause(
                "Rocket gleefully runs to feed on the carcass, "
                "only to clash with the nearby zombies.")
            print_pause("So while your cat Muzzie survived,")
            print_pause("your dog unfortunately was ZOMBIFIED!")
            print_pause(
                "Rocket now joins the pet-zombie hoard as a"
                " dog-zombie :( You LOSE!")
            return
        if "pets" in choices:
            print_pause("As you were boarding the house up, ")
            print_pause("you began to feel lightheaded from starvation.")
            print_pause("Suddenly, you get dizzy and pass out!")
            print_pause("The pet-zombie hoard approaches,")
            print_pause("and as you were unconscious, ")
            print_pause("You become a snack for the pet-zombie hoard!")
            print_pause(
                "You never live another day to see the fate of your pets.")
            print_pause("Maybe they were pet-zombified,"
                        " who knows! You LOSE!")
            return
    if "board" and "hide" in choices:
        if "you" in choices:
            print_pause(
                "Since you weren't starving, you had enough "
                "energy to board up the cabin properly.")
            print_pause("You stay up overnight in the cellar with your pets.")
            print_pause("Muzzie & Rocket were both hungry & fussy,")
            print_pause(
                "but your cellar was secure enough to maintain your dog,")
            print_pause("and while Muzzy got curious & escaped the cellar...")
            print_pause(
                "she wasn't motivated enough to try and "
                "break through your secure boards.")
            print_pause("Therefore....")
            print_pause(
                "Both your cat Muzzie and your dog Rocket "
                "survived the pet-zombie hoard!")
            print_pause("Time to head to the local shelter "
                        "to feed your pets!")
            print_pause("Congratulations, you WIN!")
            return
        if "pets" in choices:
            print_pause(
                "Since you were starving, your boards "
                "around the cabin were weak,")
            print_pause(
                "but your pets were content with staying in "
                "the cellar since they were fed.")
            print_pause(
                "However, you pass out from starvation in "
                "the cabin with your pets.")
            print_pause(
                "Unconscious all night, you weren't able to"
                " watch over your pets.")
            print_pause(
                "You wake up the next morning to your "
                "stomach grumbling...")
            print_pause("Only to find that... unfortunately,")
            print_pause(
                "the zombies broke in your weak boards "
                "and pet-napped your pets.")
            print_pause(
                "You curse yourself for not providing the "
                "zombies a distraction.")
            print_pause(
                "Perhaps it MAY have spared your pets "
                "from being zombified.")
            print_pause(
                "Both Muzzie & Rocket become zombie-pets "
                "and join the hoard. You LOSE!")
            return


def play_again():
    choices.clear()
    again = input(
        "Would you like to play again? "
        "Please type \"yes\" or \"no\".").lower()
    if again == "yes":
        main()
    elif again == "no":
        print("Thanks for playing!")
    else:
        print("Sorry, I don't understand.")
        play_again()


def main():
    intro()
    feed_question()
    explain_choices()
    first_question()
    second_question()
    summary()
    see_fate()
    final_act()
    play_again()


if __name__ == '__main__':
    main()
