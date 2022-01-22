from ..database.update import join_game, update_game
from ..database.create import create_game
from ..database.get import get
from ..classes.board import Board
from ..classes.vars import pos_tuple
import os
from time import sleep


def playing_loop(game_data, game_board, my_color, mode):
    game_board.print_board(my_color)
    while True:
        print("\nYour Color:", my_color)
        while True:
            from_pos = input("\nMove from: ")
            if from_pos in pos_tuple and game_board.position_dict[from_pos].piece is not None and game_board.position_dict[from_pos].piece.piece_color == my_color:
                valid_moves = game_board.position_dict[from_pos].piece.get_moves()
            else:
                print("\nInvalid Piece!")
                continue
            if valid_moves == []:
                print(f"\nThe piece at {from_pos} cannot move, choose a different piece.")
                continue
            change_piece = False
            while True:
                print(f"\nValid Moves for piece at {from_pos}:", *valid_moves)
                to_pos = input("\nMove to (leave empty to move a different piece): ")
                if to_pos == "":
                    change_piece = True
                    break
                if to_pos in pos_tuple and to_pos in valid_moves:
                    break
                print("\nInvalid Move!")
            if not change_piece:
                break
        
        game_board.play_move(f"{from_pos}_{to_pos}")
        
        res = get("games", f"id = {game_data[0]} and status = 'running'")
        if len(res) != 1:
            raise ValueError("Ivalid game")

        old_game_data = res[0]

        old_moves = old_game_data[4]

        new_moves = old_moves + f" {from_pos}_{to_pos}"
        status_tuple = game_board.is_game_over(my_color)
        if status_tuple[0]:
            new_status = 'ended'
            if status_tuple[1] == "won":
                if mode == "hosted":
                    new_result = "user1"
                else:
                    new_result = "user2"
            elif status_tuple[1] == "lost":
                if mode == "hosted":
                    new_result = "user2"
                else:
                    new_result = "user1"
            else:
                new_result = "stalemate"
        else:
            new_status = old_game_data[1]
            new_result = old_game_data[5]

        update_game(game_data[0], f"moves = '{new_moves}', status = '{new_status}', result = '{new_result}'")

        new_game_data = list(old_game_data)
        new_game_data[4] = new_moves
        new_game_data[1] = new_status
        new_game_data[5] = new_result
        break

    return tuple(new_game_data)

def waiting_loop(game_data, game_board, my_color, moves):
    os.system('cls' if os.name == 'nt' else 'clear')
    game_board.print_board(my_color)
    if my_color == "white":
        print(f"\nWaiting for {game_data[3]}'s move...")
    else:
        print(f"\nWaiting for {game_data[2]}'s move...")
    while True:
        res = get("games", f"id = {game_data[0]}")
        if len(res) != 1:
            raise ValueError("Ivalid game")

        new_game_data = res[0]

        if moves == new_game_data[4]:
            continue

        new_move_notation = new_game_data[4].replace(moves, '').strip()
        game_board.play_move(new_move_notation)
        break
    
    return new_game_data

def start_game(myuser):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        option = input(f"""Welcome {myuser.username}
Enter 1 to join a game
      2 to host a game
      3 to quit

> """)
        if option in ['1', '2', '3']:
            break

        print("\nInvalid option\n")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if option == '3':
        return
    
    if option == '1':
        print("Searching for games...")
        res = get("games", f"status = 'open' and user1 <> '{myuser.username}'")
        print("\tDone.")
        if len(res) == 0:
            print("No open public game found, try hosting one.")
            print("Returning to menu...")
            sleep(3)
            return start_game(myuser)
        else:
            sleep(1)

        game_data = res[0]
        print(f"Joining game with {game_data[2]}...")
        join_game(game_data[0], myuser)
        print("\tDone.")
        sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')

        game_board = Board()
        my_color = "black"
        moves = ''

        while True:
            game_data = waiting_loop(game_data, game_board, my_color, moves)
            moves = game_data[4]

            os.system('cls' if os.name == 'nt' else 'clear')

            game_board.print_board(my_color)
            if game_data[1] == 'ended':
                print()
                if game_data[5] == 'user2':
                    print("You won!")
                elif game_data[5] == 'user1':
                    print("You lost!")
                else:
                    print("The game was a draw!")

                input("Press Enter to continue\n")
                return start_game(myuser)

            os.system('cls' if os.name == 'nt' else 'clear')

            game_data = playing_loop(game_data, game_board, my_color, "joined")

            os.system('cls' if os.name == 'nt' else 'clear')

            game_board.print_board(my_color)
            moves = game_data[4]
            if game_data[1] == 'ended':
                print()
                if game_data[5] == 'user2':
                    print("You won!")
                elif game_data[5] == 'user1':
                    print("You lost!")
                else:
                    print("The game was a draw!")

                input("Press Enter to continue\n")
                return start_game(myuser)
    elif option == '2':
        print("Creating game...")
        game_id = create_game(myuser)
        print("\tDone.")
        sleep(0.5)

        game_board = Board()
        my_color = "white"
        moves = ''
        
        os.system('cls' if os.name == 'nt' else 'clear')

        game_board.print_board(my_color)
        print("\nWaiting for someone to join the game...")
        
        while True:
            res = get("games", f"id = {game_id}")
            game_data = res[0]
            if game_data[1] == 'running':
                break
            sleep(0.1)
        
        print("\tDone.")
        print(f"{game_data[3]} joined the game")
        print("Loading...")
        sleep(1)

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            game_data = playing_loop(game_data, game_board, my_color, "joined")

            os.system('cls' if os.name == 'nt' else 'clear')

            game_board.print_board(my_color)
            moves = game_data[4]
            if game_data[1] == 'ended':
                print()
                if game_data[5] == 'user1':
                    print("You won!")
                elif game_data[5] == 'user2':
                    print("You lost!")
                else:
                    print("The game was a draw!")

                input("Press Enter to continue\n")
                return start_game(myuser)

            os.system('cls' if os.name == 'nt' else 'clear')

            game_data = waiting_loop(game_data, game_board, my_color, moves)
            moves = game_data[4]

            os.system('cls' if os.name == 'nt' else 'clear')

            game_board.print_board(my_color)
            if game_data[1] == 'ended':
                print()
                if game_data[5] == 'user1':
                    print("You won!")
                elif game_data[5] == 'user2':
                    print("You lost!")
                else:
                    print("The game was a draw!")
                
                input("Press Enter to continue\n")
                return start_game(myuser)
