from django.shortcuts import render,HttpResponse
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def team_score_prediction():
    player_data = pd.read_csv('static/data/FIFA22_official_player_data.csv')
    team_data = pd.read_csv('static/data/FIFA - 2022.csv')

    player_data = player_data.replace('United States', 'USA')
    player_data = player_data.replace('Korea Republic', 'South Korea')

    l1 = team_data['Team'].tolist()
    player_data_1 = player_data[player_data['Nationality'].isin(l1)]

    Team_Score = pd.DataFrame(columns=['Team_Name', 'Win_Loss_perc', 'Player_Score', 'Net_Score'])

    def Win_Loss_perc(team):
        data = team_data[team_data['Team'] == team]
        score = data['Win'] * 3 + data['Draw'] * 1
        score = score / (data['Games Played'] * 3)
        score = score * 50
        return score.iloc[0]

    def Player_Score(team):
        data = player_data_1[player_data_1['Nationality'] == team]
        data = data.loc[:, 'Crossing':'DefensiveAwareness'].select_dtypes(exclude='object')
        score = 0
        for index, row in data.iterrows():
            player_score = row.sum()
            score = score + (player_score / 3400)
        score = score / data.shape[0]
        return round(score * 50, 2)

    for index, row in team_data.iterrows():
        wl = Win_Loss_perc(row['Team'])
        ps = Player_Score(row['Team'])
        net_score = (wl + ps)
        new_entry = {'Team_Name': row['Team'], 'Win_Loss_perc': wl, 'Player_Score': ps, 'Net_Score': net_score}
        Team_Score.loc[index] = new_entry

    df = Team_Score.head(5)

    plt.style.use('ggplot')
    x = range(len(df['Team_Name']))
    plt.figure(figsize=(20, 12))
    plt.style.use('ggplot')


    x = range(len(df['Team_Name']))

    plt.figure(figsize = (20,12))
    plt.bar(x, df['Net_Score'], width=0.2, color='cyan', align='center', label='Total Team Score (max : 100)')
    plt.bar([i + 0.2 for i in x], df['Player_Score'], width=0.2, color='brown', align='center', label='All Team Player Stats basis Score (max : 50)')
    plt.bar([i + 0.4 for i in x], df['Win_Loss_perc'], width=0.2, color='red', align='center', label='Team Win, Loss, and Draw Score (max : 50)')

    plt.xlabel('Teams',fontsize=40)
    plt.ylabel('Scores',fontsize=40)
    plt.title('Score ranking of Team on the basis of Player Stats and Teams Win-Loss Ratio',fontsize=40)
    plt.xticks([i + 0.2 for i in x], df['Team_Name'],fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize = 15)


    # Save the plot to an image
    buffer = BytesIO()
    plt.savefig(buffer, format='jpg')
    buffer.seek(0)
    img_data = buffer.read()
    buffer.close()

    # Encode the image data to base64
    img_base64 = base64.b64encode(img_data).decode('utf-8')

    # Get the predicted winning team
    data1 = df.head(1)
    predicted_team = data1.loc[0, 'Team_Name']

    context = {
        'graph_base64': img_base64,
        'predicted_team': predicted_team,
    }
    print(img_base64)
    return render( 'index.html', context)
team_score_prediction()
def index(request):
    context = {
        'variable': "this is sent",
        'variable2': "this is sent 2"
    }
    return render(request, 'index.html', context)

def index(request):
    context = {
        'variable':"this is sent",
        'variable2':"this is sent 2"
    }
    return render(request,'Index.html', context)

def Custom(request):
    return HttpResponse('this is Custom')
def DashBoard(request):
    return HttpResponse('this is DashBoard')
def LiveMatch(request):
    return HttpResponse('this is LiveMatch')
def MatchScore(request):
    return HttpResponse('this is MatchScore')
