#libraries import
from django.shortcuts import render,HttpResponse
import pandas as pd
from django.shortcuts import render

# data set Import
df=pd.read_csv('static\data\international_matches.csv')
df1=pd.read_csv('static\data\FIFA - 2022.csv')

player_data = pd.read_csv('static\data\FIFA22_official_player_data.csv')

def GK_Score(Name):
    data = player_data[player_data['Name'] == Name]
    data = data.loc[:, 'GKDiving':'GKReflexes'].select_dtypes(exclude='object')
    score = data.sum().sum()
    return round(score/5, 2)

def Player_Score(Name):
    data = player_data[player_data['Name']==Name]
    data = data.loc[:,'Crossing':'SlidingTackle'].select_dtypes(exclude = 'object')
    score = data.sum().sum()
    return round(score/29,2)

def index(request):
    context = {
        'variable': "this is sent",
        'variable2': "this is sent 2"
    }
    return render(request, 'index.html', context)

def predictor_working():
    teams = df['home_team'].unique()    

    team_stats = []

    for team in teams:
        
        result = df[(df['home_team']==team) & ((df['tournament']== 1)|(df['tournament']== 0))]
        
        total_matches = len(df[(df['home_team'] == team) | (df['away_team'] == team)])
        total_wins = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Win')]) + len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Lose')])
        total_draws = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Draw')]) + len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Draw')])
        total_losses = total_matches - total_wins - total_draws
        
        home_wins = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Win')])
        home_draws = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Draw')])
        home_losses = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Lose')])
        
        away_wins = len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Lose')])
        away_draws = len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Draw')])
        away_losses = len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Win')])
        
        win_percentage = (total_wins / total_matches) * 100 if total_matches > 0 else 0
        draw_percentage = (total_draws / total_matches) * 100 if total_matches > 0 else 0
        loss_percentage = (total_losses / total_matches) * 100 if total_matches > 0 else 0
        
        home_win_percentage = (home_wins / (home_wins + home_draws + home_losses)) * 100 if (home_wins + home_draws + home_losses) > 0 else 0
        home_draw_percentage = (home_draws / (home_wins + home_draws + home_losses)) * 100 if (home_wins + home_draws + home_losses) > 0 else 0
        home_loss_percentage = (home_losses / (home_wins + home_draws + home_losses)) * 100 if (home_wins + home_draws + home_losses) > 0 else 0
        
        away_win_percentage = (away_wins / (away_wins + away_draws + away_losses)) * 100 if (away_wins + away_draws + away_losses) > 0 else 0
        away_draw_percentage = (away_draws / (away_wins + away_draws + away_losses)) * 100 if (away_wins + away_draws + away_losses) > 0 else 0
        away_loss_percentage = (away_losses / (away_wins + away_draws + away_losses)) * 100 if (away_wins + away_draws + away_losses) > 0 else 0
        
        # Calculate average rank, rank difference, point difference, and won previous matches
        avg_rank = (df[df['home_team'] == team]['home_team_fifa_rank'].mean() + df[df['away_team'] == team]['away_team_fifa_rank'].mean()) / 2
        rank_diff = df[df['home_team'] == team]['home_team_fifa_rank'].mean() - df[df['away_team'] == team]['away_team_fifa_rank'].mean()
        point_diff = df[df['home_team'] == team]['home_team_total_fifa_points'].mean() - df[df['away_team'] == team]['away_team_total_fifa_points'].mean()
        won_previous_matches = len(df[(df['home_team'] == team) & (df['home_team_result'] == 'Win')]) + len(df[(df['away_team'] == team) & (df['home_team_result'] == 'Win')])
        
        team_stats.append([team, total_matches, total_wins, total_draws, total_losses, home_wins, home_draws, home_losses, away_wins, away_draws, away_losses, win_percentage, draw_percentage, loss_percentage, home_win_percentage, home_draw_percentage, home_loss_percentage, away_win_percentage, away_draw_percentage, away_loss_percentage, avg_rank, rank_diff, point_diff, won_previous_matches,result])

        # Create DataFrame
    columns = ['Team', 'Total', 'Win', 'Draw', 'Lose', 'Home Win', 'Home Draw', 'Home Lose', 'Away Win', 'Away Draw', 'Away Lose', 'Win %', 'Draw %', 'Lose %', 'Home Win %', 'Home Draw %', 'Home Loss %', 'Away Win %', 'Away Draw %', 'Away Loss %', 'avg_rank', 'rank_diff', 'point_diff', 'won_previous_matches','result']
    team_stats_df = pd.DataFrame(team_stats, columns=columns)

        # Display the DataFrame
        # Filter the team_stats_df DataFrame
    filtered_team_stats_df = team_stats_df

        # Display the filtered DataFrame
    filtered_team_stats_df

    sorted_team_stats_df = filtered_team_stats_df.sort_values(by='Win %', ascending=False)

        # Reset the index of the sorted DataFrame and add 1 to each index value
    sorted_team_stats_df.reset_index(drop=True, inplace=True)
    sorted_team_stats_df.index = sorted_team_stats_df.index + 1

        # Display the sorted and indexed DataFrame
    return(sorted_team_stats_df['Team'].head(1).iloc[0])




def Custom(request):

    if request.method == 'POST':
        teamA_gk = request.POST.get('teamA_gk')
        teamA_back1 = request.POST.getlist('teamA_back1')
        teamA_back2 = request.POST.getlist('teamA_back2')
        teamA_back3 = request.POST.getlist('teamA_back3')
        teamA_back4 = request.POST.getlist('teamA_back4')
        teamA_mid1 = request.POST.getlist('teamA_mid1')
        teamA_mid2 = request.POST.getlist('teamA_mid2')
        teamA_mid3 = request.POST.getlist('teamA_mid3')
        teamA_mid4 = request.POST.getlist('teamA_mid4')
        teamA_fwd1 = request.POST.getlist('teamA_fwd1')
        teamA_fwd2 = request.POST.getlist('teamA_fwd2')

        teamA_inputs = [teamA_gk]+teamA_back1+teamA_back2+teamA_back3+teamA_back4+teamA_mid1+teamA_mid2+teamA_mid3+teamA_mid4+teamA_fwd1+teamA_fwd2
        
        teamB_gk = request.POST.get('teamB_gk')
        teamB_back1 = request.POST.getlist('teamB_back1')
        teamB_back2 = request.POST.getlist('teamB_back2')
        teamB_back3 = request.POST.getlist('teamB_back3')
        teamB_back4 = request.POST.getlist('teamB_back4')
        teamB_mid1 = request.POST.getlist('teamB_mid1')
        teamB_mid2 = request.POST.getlist('teamB_mid2')
        teamB_mid3 = request.POST.getlist('teamB_mid3')
        teamB_mid4 = request.POST.getlist('teamB_mid4')
        teamB_fwd1 = request.POST.getlist('teamB_fwd1')
        teamB_fwd2 = request.POST.getlist('teamB_fwd2')

        teamB_inputs = [teamB_gk]+teamB_back1+teamB_back2+teamB_back3+teamB_back4+teamB_mid1+teamB_mid2+teamB_mid3+teamB_mid4+teamB_fwd1+teamB_fwd2



        if ("" in teamA_inputs) or ("" in teamB_inputs):
            return render(request, 'custom_team.html', {'team_prediction': 'Players Not Selected'})
        else:
            TeamAScore = GK_Score(teamA_inputs[0])
            for row in teamA_inputs[1:]:
                ps = Player_Score(row)
                TeamAScore+=ps
            TeamBScore = GK_Score(teamB_inputs[0])
            for row in teamB_inputs[1:]:
                ps = Player_Score(row)
                TeamBScore+=ps
            if (TeamAScore > TeamBScore):
                output = "Team A Wins"
            elif (TeamAScore < TeamBScore):
                output = "Team B Wins"
            else:
                output = "Draw"
            return render(request, 'custom_team.html', {'team_prediction': output})
    else:
        return render(request, 'custom_team.html',{'team_prediction': 'Select Players'})

def Leaderboard(request):
    return render(request,'Leaderboard.html')
def Prediction(request):
    output = predictor_working()
    return render(request,'Prediction.html',{'team_prediction': output})
def MatchScore(request):
    return render(request,'matchscore.html')
