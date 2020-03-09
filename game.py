from hanoi_tower import *
import pdb

game_board = Board()
game_running = True

def print_towers(tower_stack):
    for disk in tower_stack:
        print(disk.size)
        print("**")

# def print_towers(tower):
#     if len(tower) > 0:
#         spaces = len(tower) - 1 
#         for disk in tower:
#             print(spaces * " " + disk.size * "_" + str(disk.size) + "_" * disk.size)
#             spaces -= 1
#     else:
#         print('''
#      0
#      0
#      0
#      0
# _____0_____
#         ''')
    # print(len(tower) * "_" + "^" + "_" * len(tower))
#     _1_
#    __2__
#   ___3___
#  ____4____
# _____5_____

def setup_game(disk_count=5):

    for i in range(3):
        game_board.list_of_towers.append(Tower(i))
        

    for i in range(disk_count, 0, -1):
        game_board.list_of_towers[0].stack.append(Disk(i))

# def player_action():
#     from_tower = int(input("From tower: ")) - 1
#     to_tower = int(input("To Tower: ")) - 1

# def change_place_disk(tower):
#     pass


def main():
    setup_game()
    global game_running
    moves_made = 0

    end_list = game_board.list_of_towers[0].stack.copy()

    # game_board.list_towers()
    for tower in game_board.list_of_towers:
        print_towers(tower.stack)

    while game_running:
        correct = False
        
        while not correct:
            print("Pick tower: [1 - 3]")
            from_tower = int(input("From tower: ")) - 1

            to_tower = int(input("To Tower: ")) - 1
            moves_made += 1

            if from_tower <= 2 and from_tower >= 0 and to_tower <= 2 and to_tower >= 0:
                correct = True

        if game_board.list_of_towers[to_tower].peek() == []:
            game_board.list_of_towers[to_tower].add_to_tower(game_board.list_of_towers[from_tower].remove_from_tower())
        elif game_board.list_of_towers[to_tower].peek().size < game_board.list_of_towers[from_tower].peek().size:
            print("\n********Wrong move**********")
        else:
            game_board.list_of_towers[to_tower].add_to_tower(game_board.list_of_towers[from_tower].remove_from_tower())


        print("\n")
        # game_board.list_towers()
        for tower in game_board.list_of_towers:
            print_towers(tower.stack)

        print("**************************************\n")


        if game_board.list_of_towers[2].stack == end_list:
            print("Congratulations! You won!")
            print(f"Total moves: {moves_made}")
            game_running = False
    
    # for tower in game_board.list_of_towers:
    #     print(tower.stack)
    
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame closed by user")