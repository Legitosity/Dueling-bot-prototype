from random import *

'''
BCL Battle-Bot V0.1
'''

player_one_health = 100
computer_health = 100

player_one_attack = 0
computer_turn = 1
player_turn = 1
computer_move_attack = 0
computer_damage = 0
p1_controlled_att = 0
cp_controlled_att = 0
p1_att_var = 0
cp_att_var = 0
replay = True


while replay == True:
    player_turn = 1
    computer_turn = 1
    while player_one_health > 0 and computer_health > 0:

        # players turn

        if player_turn == 1:
            player_one_action = input("Do you want to attack or move? ")
            if player_one_action == "attack":
                p1_att_var = randint(1,100)
                if p1_att_var <= 10:
                    print("Player One has MISSED their attack!")
                    player_turn = 0
                    computer_turn = 1
                elif p1_att_var >= 11 and p1_att_var <= 95:
                    player_one_attack = p1_att_var
                    computer_health = max(computer_health - player_one_attack, 0)
                    print(f'Player One has dealt {str(player_one_attack)} damage to the Computer!')
                    print("")
                    print(f'Player One has {str(player_one_health)} health left')
                    print(f'The Computer has {str(computer_health)} health left')
                    player_turn = 0
                    computer_turn = 1
                else:
                    print(f'Player One has done CRITICAL damage of {player_one_attack} to the computer killing it instantly!!!')
                    computer_health = 0
                    print("")
                    print(f'Player One has {str(player_one_health)} health left')
                    print(f'The Computer has {str(computer_health)} health left')
                    player_turn = 0
                    computer_turn = 1

                if computer_health <= 0:
                    computer_turn = 0
                    computer_health = 0
                    print("")
                    print("")
                    print("@@@@@@@@@")
                    print("YOU WIN!!")
                    print("@@@@@@@@@")
                    print("")
                    print("")

                else:
                    print("")
            elif player_one_action == "move":
                print("Player One chose to move instead of attack!")
                print("")
                player_turn = 0
                computer_turn = 1
            else:
                print("That's not an option!")

        #  computers turn

        if computer_turn == 1:
            computer_move_attack = randint(1, 100)
            if computer_move_attack >= 25:
                print("The Computer moves to attack!")
                computer_damage = randint(1, 100)
                if computer_damage <= 10:
                    print(f'The Computer\'s attack missed!')
                    print("")
                    player_turn = 1
                    computer_turn = 0
                elif computer_damage >= 11 and computer_damage <= 90:
                    print(f'The Computer dealt {str(computer_damage)} damage to Player One!')
                    player_one_health = max(player_one_health - computer_damage, 0)
                    print("")
                    player_turn = 1
                    computer_turn = 0
                else:
                    print(f'The computer has done CRITICAL DAMAGE to you for {computer_damage} killing you instantly!!!')
                    print("")
                    player_one_health = 0
                    print(f'Player One has {str(player_one_health)} health left')
                    print(f'The Computer has {str(computer_health)} health left')
                    player_turn = 1
                    computer_turn = 0

                if player_one_health <= 0:
                    print("")
                    print("###########")
                    print("YOU LOSE!!")
                    print("###########")
                    print("")
                    print("")
                else:
                    print(f'The Player has {str(player_one_health)}  health left')
                    print(f'The Computer has {str(computer_health)} health left')
                    print("")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("The Computer chose to move!")
                print("")
                print(f'The Player has {str(player_one_health)}  health left')
                print(f'The Computer has {str(computer_health)} health left')
                print("")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                player_turn = 1
                computer_turn = 0


    game_again = input("Do you want to play again? yes or no: ")
    if game_again == "yes":
        replay = True
        player_one_health = 100
        computer_health = 100
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~NEW GAME~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")
    elif game_again == "no":
        replay = False
    else:
        print("\"yes\" or \"no\" please!")
        game_again = input("Do you want to play again? yes or no: ")



