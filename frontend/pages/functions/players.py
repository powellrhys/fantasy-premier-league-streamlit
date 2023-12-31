import requests
import pandas as pd
import os

from pages.functions.support_functions import read_csv

def collect_player_data():

    # Endpoint url
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Read in data from endpoint
    r = requests.get(url)
    json = r.json()

    # Create dataframe from endpoint components
    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])

    # List of variables to store in dataframe
    player_stats_of_interest = ['id', 'second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost',
                                'minutes', 'transfers_in', 'value_season', 'total_points', 'goals_scored',
                                'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
                                'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'starts']

    # Transform dataframe
    slim_elements_df = elements_df[player_stats_of_interest]
    slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
    slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
    slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
    slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

    # Add position variable to columns needed in final dataframe
    player_stats_of_interest.append('position')

    # Filter dataset
    slim_elements_df = slim_elements_df[player_stats_of_interest]

    # Write data to storage
    slim_elements_df.to_csv('data/players.csv')

def collect_unique_player_data(player_id, player_name, directory):

    # Read data from player endpoint
    url = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'
    r = requests.get(url)
    json = r.json()

    # Create pandas dataframe from player history data
    player_data_df = pd.DataFrame(json['history'])

    # Write data to storage
    player_data_df.to_csv(f'{directory}/{player_name}.csv')

def create_gameweek_df_for_team(metric, gameweeks, player_filter):

    # Collect list players in current team
    current_file_names = os.listdir('data_my_players')

    # Collect series of data with gameweek rounds
    rounds_series = read_csv(f'data_my_players/{current_file_names[0]}')['round']

    # Create gameweek pandas series
    df = pd.DataFrame(rounds_series)

    # Read my team player data
    for file in current_file_names:
        player_df = read_csv(f'data_my_players/{file}')
        df[file.replace('.csv', '')] = player_df[metric]

    # Create list of players
    players = df.columns.to_list()
    players.pop(0)

    # Filter my team player names by position filter
    columns = list(set(players) - set(player_filter))
    columns = list(set(players) - set(columns))
    columns.append('round')

    # Filter data by sidebar filters
    df = df[columns]
    df = df[(df['round'] >= gameweeks[0]) & (df['round'] <= gameweeks[1])]

    return df, columns
