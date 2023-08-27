from django.shortcuts import render,HttpResponse
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

player_data = pd.read_csv('static\data\FIFA22_official_player_data.csv')

def Player_Score(team):
    data = player_data[player_data['Nationality']==team]
    data = data.loc[:,'Crossing':'DefensiveAwareness'].select_dtypes(exclude = 'object')
    score = 0
    for index, row in data.iterrows():
        player_score = row.sum()
        score = score + (player_score/3400)
    score = score / data.shape[0]
    return round(score * 50,2)
def index(request):
    context = {
        'variable': "this is sent",
        'variable2': "this is sent 2"
    }
    return render(request, 'index.html', context)


from django.shortcuts import render

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
            TeamAScore = 0
            for row in teamA_inputs.iterrows():
                ps = Player_Score(row['Name'])
                TeamAScore+=ps
            TeamBScore = 0
            for row in teamB_inputs.iterrows():
                ps = Player_Score(row['Name'])
                TeamBScore+=ps
            if (TeamAScore > TeamBScore):
                output = "Team A Wins"
            elif (TeamAScore < TeamBScore):
                output = "Team A Wins"
            else:
                output = "Draw"
            return render(request, 'custom_team.html', {'team_prediction': output})
    else:
        return render(request, 'custom_team.html',{'team_prediction': 'Select Players'})

def Leaderboard(request):
    return render(request,'Leaderboard.html')
def Prediction(request):
    return render(request,'Prediction.html')
def MatchScore(request):
    return render(request,'matchscore.html')
