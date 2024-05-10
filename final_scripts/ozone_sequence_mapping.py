## Linhac 2024
## Fauzan Lodhi
## University of Waterloo

import pandas as pd
from scipy import stats
from functools import reduce

df = pd.read_csv("Linhac24_Sportlogiq.csv",encoding='UTF-8')


sequences = []

plays = len(df)


def new_ozone_poss(play_no):
    curr_team = df.loc[play_no, 'teaminpossession']
    if df.loc[play_no, 'xadjcoord'] >= 25 and curr_team > 0:
        if play_no > 0:
            prev_team = df.loc[play_no - 1, 'teaminpossession']
            prev_coord = df.loc[play_no - 1, 'xadjcoord']
            if prev_team == curr_team and prev_coord >= 25:
                return False
            else:
                return True
        else:
            return True
            
    else:
        return False

def ozone_continued(play_no, start_play):
    team = df.loc[start_play, 'teaminpossession']
    period = df.loc[start_play, 'period']
    game = df.loc[start_play, 'gameid']

    curr_team = df.loc[play_no, 'teaminpossession']
    curr_period = df.loc[play_no, 'period']
    curr_game = df.loc[play_no, 'gameid']
    curr_coord = df.loc[play_no, 'xadjcoord']
    curr_teamid = df.loc[play_no, 'teamid']

    if curr_game == game and curr_period == period and curr_team > 0 and curr_team == team:
        if curr_teamid == curr_team and curr_coord >= 25:
            return True
        
        elif curr_teamid != curr_team and curr_coord <= -25:
            return True
        
        else:
            return False
    else:
        return False


def icing_occurs(seq_end):
    
    is_icing = False
    
    team = df.loc[seq_end, 'teaminpossession']
    event = df.loc[seq_end, 'eventname']
    game = df.loc[seq_end, 'gameid']
    period = df.loc[seq_end, 'period']

    curr_team = team
    curr_event = event
    curr_game = game
    curr_period = period

    while seq_end < plays and curr_game == game and curr_period == period and curr_team == team and is_icing is False:
        if curr_event == 'icing':
            is_icing = True
        else:
            seq_end += 1
            curr_team = df.loc[seq_end, 'teaminpossession']
            curr_event = df.loc[seq_end, 'eventname']
            curr_game = df.loc[seq_end, 'gameid']
            curr_period = df.loc[seq_end, 'period']
    
    return is_icing



def add_sequence(seq, seq_start, seq_end):
    game = df.loc[seq_start, 'gameid']
    period = df.loc[seq_start, 'period']
    team = df.loc[seq_start, 'teaminpossession']
    start_time = df.loc[seq_start, 'compiledgametime']
    cmltv_time = df.loc[seq_end, 'compiledgametime'] - df.loc[seq_start, 'compiledgametime']
    manpower = df.loc[seq_start, 'manpowersituation']
    max_xG = 0
    cmltv_xG = 0
    fwd_time = 0
    dmen_time = 0
    penalties_drawn = 0
    puck_retrievals = 0
    shot_attempts = 0
    goals_scored = 0
    pass_attempts = 0
    slot_pass_attempts = 0
    icing = 0

    if df.loc[seq_end, 'gameid'] != game:
        if period == 3:
            cmltv_time = 3600 - start_time
        elif period == 4:
            cmltv_time = 3900 - start_time

    for i in seq:
        curr_xG = max(0, df.loc[i, 'xg_allattempts'])
        curr_team = df.loc[i, 'teamid']
        curr_time = df.loc[i, 'compiledgametime']
        curr_position = df.loc[i, 'playerprimaryposition']
        curr_event = df.loc[i, 'eventname']
        curr_period = df.loc[i, 'period']
        event_outcome = df.loc[i, 'outcome']
        if i < plays and curr_team == team:
            next_time = df.loc[i + 1, 'compiledgametime']
            next_game = df.loc[i + 1, 'gameid']
            
            if next_game != game:
                if curr_period == 3:
                    time_diff = 3600 - curr_time
                elif curr_period == 4:
                    time_diff = 3900 - curr_time
                    
            else:
                time_diff = next_time - curr_time
            
            if curr_position == 'F':
                fwd_time += time_diff
            
            elif curr_position == 'D':
                dmen_time += time_diff
        
        
        if curr_event == 'penalty' and curr_team != team:
            penalties_drawn += 1

        if curr_event == 'lpr' and event_outcome == 'successful' and curr_team == team:
            puck_retrievals += 1

        if curr_event == 'shot':
            shot_attempts += 1

        if curr_event == 'goal':
            goals_scored += 1
        
        if curr_event == 'pass':
            pass_attempts += 1
            if df.loc[i, 'type'] == 'slot':
                slot_pass_attempts += 1

        max_xG = max(max_xG, curr_xG)
        cmltv_xG += curr_xG
    
    if icing_occurs(seq_end) is True:
        icing = 1

    game_ids.append(game)
    periods.append(period)
    teams.append(team)
    start_times.append(start_time)
    cmltv_times.append(cmltv_time)
    manpowersituations.append(manpower)
    max_xgs.append(max_xG)
    cmltv_xgs.append(cmltv_xG)
    goals.append(goals_scored)
    shots.append(shot_attempts)
    passes.append(pass_attempts)
    slot_passes.append(slot_pass_attempts)
    fwd_times.append(fwd_time)
    dmen_times.append(dmen_time)
    penalties.append(penalties_drawn)
    retrievals.append(puck_retrievals)
    icings.append(icing)



game_ids = []
periods = []
teams = []
start_times = []
cmltv_times = []
manpowersituations = []
max_xgs = []
cmltv_xgs = []
goals = []
shots = []
passes = []
slot_passes = []
fwd_times = []
dmen_times = []
penalties = []
retrievals = []
icings = []



live_sequence = False
starting_play = 0
all_sequences = []
current_seq = []

for play in range(plays):
    if live_sequence is False:
        if new_ozone_poss(play) is True:
            live_sequence = True
            starting_play = play
            current_seq.append(play)
        else:
            continue
    else:
        if ozone_continued(play, starting_play) is True:
            current_seq.append(play)
        else:
            live_sequence = False
            all_sequences.append(current_seq)
            current_seq = []

for seq in all_sequences:
    first_play = seq[0]
    last_play = seq[-1]
    terminating_play = last_play + 1
    if terminating_play < plays:
        add_sequence(seq, first_play, terminating_play)
    else:
        add_sequence(seq, first_play, last_play)





sequence_results = {'game': game_ids, 'period': periods, 'team': teams, 'start time': start_times,  'ozone time': cmltv_times,'man power situation': manpowersituations, 'max xG': max_xgs, 'cumulative xG': cmltv_xgs, 'goals': goals, 'shots': shots, 'passes': passes, 'slot passes': slot_passes, 'fwd time': fwd_times, 'dmen time': dmen_times, 'penalties drawn': penalties, 'puck retrievals': retrievals, 'icings': icings}

results = pd.DataFrame(sequence_results)

results.to_csv("ozone_sequences.csv", sep=',', index=False, encoding='utf-8')
