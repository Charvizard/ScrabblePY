letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in  zip(letters, points)}
letter_to_points[" "] = 0
player_to_words = {'player1':['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
player_to_points = {}

def score_word(word) : 
    point_total = 0
    for letter in word : 
        if letter in letter_to_points : 
            point_total += letter_to_points[letter] 
        else : 
            point_total += 0
    return point_total


def score_player() : 
    for player, words in player_to_words.items() : 
        player_points = 0
        for word in words : 
            player_points += score_word(word)
        player_to_points[player] = player_points


def play_word() : 
    print("Who is the player?")
    player = input()
    print("What was the word they played, in ALL CAPS")
    new_word = input().upper()
    try : 
        player_to_words[player].append(new_word)
    except KeyError : 
        print("That player does not exist")

def start_game() : 
    play_word()
    play_game()

def play_game() : 
    score_player()
    winnerPoints = 0
    winner_player = " "
    for player, points in player_to_points.items() : 
        if points > winnerPoints : 
            winner_player = player
            winnerPoints = points
        if points == winnerPoints : 
            if winner_player != winner_player : 
                winner_player = winner_player + " ," + player
    print("The winner so far is : " + winner_player + " at " + str(winnerPoints) + " points")
    next_play(winner_player)
    


def next_play(winner) : 
    print("Would you like to add another word? Y/N")
    play = input()
    if play == "Y" : 
        start_game()
    else : 
        conclude_game(winner)

def conclude_game(winner) : 
    print(winner + " congratulations on winning!")

start_game()