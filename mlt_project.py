import pandas as p

match = p.read_csv('IPL_Matches_2008_2022.csv')
match.rename(columns = {'ID' : 'Match_Id'} , inplace = True)
# print(match.head(3))

match_data = p.read_csv('IPL_Ball_by_Ball_2008_2022.csv')
match_data.rename(columns = { 'ID' : 'Match_Id' , 
                              'innings' : 'Innings' , 
                              'overs' : 'Over' , 
                              'ballnumber' : 'Ball' ,  
                              'batter' : 'Batsman' ,
                              'bowler' : 'Bowler' ,  
                              'non_striker' : 'NonStriker' ,
                              'extra_type' : 'Extra_Type' ,
                              'batsman_runs' : 'Batsman_Run' , 
                              'extra_run' : 'ExtraRun' , 
                              'total_run' : 'Total_Run' ,
                              'non_boundary' : 'Non_Boundary' ,
                              'isWicketDelivery' : 'Is_Wicket_Delivery' ,
                              'player_out' : 'Player_Dismissed' ,
                              'kind'  : 'Dismissal_Kind' ,
                              'fielders_involved' : 'Fielder' , 
                              'BattingTeam ' : 'BattingTeam'} , inplace = True)
# print(match_data.head(3))

data = match_data.groupby(['Match_Id' , 'Innings']).sum()['Total_Run'].reset_index() #reset_index , it allows you reset the index back to the default 0, 1, 2 etc indexes.
# print(data.head(10))

data = data[data['Innings'] == 1]
# print(data.head())

final_data = match.merge(data[['Match_Id' , 'Total_Run']] , left_on = 'Match_Id' , right_on = 'Match_Id')
# print(final_data['Team1'].unique())
# print(final_data.head(10))

teams = [
    'Sunrisers Hyderabad' ,
    'Mumbai Indians' ,
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders' ,
    'Delhi Capitals' ,
    'Kings XI Punjab',
    'Chennai Super Kings', 
    'Rajasthan Royals'
]

final_data['Team1'] == final_data['Team1'].str.replace('Delhi Daredevils' , 'Delhi Capitals')
final_data['Team2'] == final_data['Team2'].str.replace('Delhi Daredevils' , 'Delhi Capitals')

final_data['Team1'] == final_data['Team1'].str.replace('Deccan Chargers' ,  'Sunrisers Hyderabad')
final_data['Team2'] == final_data['Team2'].str.replace('Deccan Chargers' ,  'Sunrisers Hyderabad')

final_data = final_data[final_data['Team1'].isin(teams)]
final_data = final_data[final_data['Team2'].isin(teams)]

final_data = final_data[['Match_Id' , 'City' , 'WinningTeam' , 'Total_Run']]
delivery_data = final_data.merge(match_data , on = 'Match_Id')
delivery_data = delivery_data[delivery_data['Innings'] == 2]

delivery_data = delivery_data.sort_values(by=['Match_Id', 'Innings'])
# print(type(delivery_data.Player_Dismissed))
delivery_data['Current_Score'] = delivery_data.groupby('Match_Id').apply(p.Series.cumsum)['Total_Run_y']

# cumulative_sum = []
# cum_sum = 0
# for index, row in delivery_data.iterrows():
#     cum_sum += row['Total_Run_y']
#     cumulative_sum.append(cum_sum)
# delivery_data['Current_Score'] = cumulative_sum

delivery_data['Runs_Left'] = delivery_data['Total_Run_x'] - delivery_data['Current_Score']
delivery_data['Balls_Left'] = 120 - (delivery_data['Over'] * 6 + delivery_data['Ball'])
delivery_data['Player_Dismissed'] = delivery_data['Player_Dismissed'].fillna('0')
delivery_data['Player_Dismissed'] = delivery_data['Player_Dismissed'].apply(lambda x:x if x == '0'  else '1')
delivery_data['Player_Dismissed'] = delivery_data['Player_Dismissed'].astype('int')
wickets = delivery_data.groupby('Match_Id').apply(p.Series.cumsum)['Player_Dismissed'].values
delivery_data['Wickets_Left'] = 10 - wickets

# cumulative_wicket = []
# cum_wicket = 10
# for index, row in delivery_data.iterrows():
#     if not p.isnull(row['Player_Dismissed']):  # Checking if a player is dismissed
#         cum_wicket -= 1  # Incrementing wicket count if a player is dismissed
#         cumulative_wicket.append(cum_wicket)

# delivery_data['Wickets_Left'] = cumulative_wicket
# delivery_data['Wickets_Left'] = 10 - wicket



