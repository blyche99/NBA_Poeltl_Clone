import pandas as pd
from tabulate import tabulate
import math

data = pd.read_csv('poeltl_data/clean_tot.csv')


def main(df):
    target_player = select_player(df)

    x = target_player.iloc[0]['Player']

    guess_count = 0
    total_guess=8
    correct = False

    print(x)

    while (guess_count < total_guess) and (correct == False):
        val = guess(guess_count, x, data)
        correct=val

        guess_count+=1



def player_comp(p1, p2, df):
    out_tuple = [False, False, False, False, False, 1, 1, 1] #0 correct, 1 target higher, 2 target lower

    player1 = df[df['Player'] == p1]
    player2 = df[df['Player'] == p2]

    Name1 = player1.iloc[0]['Player']
    Name2 = player2.iloc[0]['Player']


    if Name1 == Name2:
        out_tuple[0]=True

    Tm1 = player1.iloc[0]['Tm']
    Tm2 = player2.iloc[0]['Tm']

    if Tm1 == Tm2:
        out_tuple[1]=True

    Conf1 = player1.iloc[0]['Conf']
    Conf2 = player2.iloc[0]['Conf']

    if Conf1 == Conf2:
        out_tuple[2] = True

    Div1 = player1.iloc[0]['Div']
    Div2 = player2.iloc[0]['Div']

    if Div1 == Div2:
        out_tuple[3] = True

    H1 = player1.iloc[0]['Ht']
    H2 = player2.iloc[0]['Ht']
    dif_H = H1-H2

    if dif_H == 0:
        out_tuple[5]=0
    elif dif_H>0:
        out_tuple[5]=2
    else:
        out_tuple[5]=1

    Pos1 = player1.iloc[0]['Pos']
    Pos2 = player2.iloc[0]['Pos']

    if Pos1 == Pos2:
        out_tuple[4] = True

    Age1 = player1.iloc[0]['Age']
    Age2 = player2.iloc[0]['Age']
    dif_age = Age1-Age2
    if dif_age == 0:
        out_tuple[6]=0
    elif dif_age>0:
        out_tuple[6]=2
    else:
        out_tuple[6]=1

    No1 = player1.iloc[0]['No.']
    No2 = player2.iloc[0]['No.']
    dif_no = No1-No2
    if dif_no == 0:
        out_tuple[7]=0
    elif dif_no>0:
        out_tuple[7]=2
    else:
        out_tuple[7]=1

    return out_tuple


def guess(guess_count, target, data, total_guess=8):
    #guess = input(f'Guess {guess_count+1} of {total_guess}:')
    i=0
    while i==0:
        try:
            guess = input(f'Guess {guess_count + 1} of {total_guess}:')
            player2 = data[data['Player'] == guess]
            Name2 = player2.iloc[0]['Player']
            i=1
        except IndexError:
            print('Please enter a valid player')


    output=False

    results = player_comp(guess, target, data)

    if results[0] == True:
        print(f'{guess} is Correct!')
        output=True
    else:
        print(f'{guess} is not correct.')
        outputter(results, guess, data)
    return output


def outputter(results, player_name, data):
    guess_res = [guess, 2, 3, 4, 5, 6, 7, 8]
    guess_data=data[data['Player']==player_name]
    guess_res[0] = guess_data.iloc[0]['Player']
    guess_res[1] = guess_data.iloc[0]['Tm']
    guess_res[2] = guess_data.iloc[0]['Conf']
    guess_res[3] = guess_data.iloc[0]['Div']
    guess_res[4] = guess_data.iloc[0]['Pos']
    guess_res[5] = convert_feet1(guess_data.iloc[0]['Ht'])
    guess_res[6] = guess_data.iloc[0]['Age']
    guess_res[7] = int(guess_data.iloc[0]['No.'])

    results[0] = ''

    i=0
    for res in results[:5]:
        if res==False:
            results[i]='Incorrect'
        elif res==True:
            results[i]='Correct'
        i+=1

    if results[5]==0:
        results[5]='Correct Height'
    elif results[5]==2:
        results[5]='Player is shorter'
    else:
        results[5]='Player is taller'

    if results[6]==0:
        results[6]='Correct Age'
    elif results[6]==1:
        results[6]='Player is older'
    else:
        results[6]='Player is younger'

    if results[7]==0:
        results[7]='Correct Number'
    elif results[7]==1:
        results[7]="Player's number is higher"
    else:
        results[7]="Player's number is lower"


    to_print=[guess_res, results]
    print(tabulate(to_print, headers=['Player', 'Team', 'Conf', 'Div', 'Pos', 'Ht', 'Age', '#']))


def convert_feet1(float_h):
    floor = math.floor(float_h)
    decimal = int(12*(float_h - floor))

    return(f"{floor}'{decimal}\"")


def select_player(df):
    target_player = df.sample()
    return target_player

if __name__ == "__main__":
    main(data)
