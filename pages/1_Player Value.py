from pages.functions.support_functions import read_csv
from pages.functions.plots import plot_scatter_player_points

import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Player Value Analyis")

filter_list = np.array(['Goalkeeper', 'Defender', 'Midfielder', 'Forward'])

goal_check = st.sidebar.checkbox('Goalkeeper', value=True)
def_check = st.sidebar.checkbox('Defender', value=True)
mid_check = st.sidebar.checkbox('Midfielder', value=True)
fow_check = st.sidebar.checkbox('Forward', value=True)
 
filter_index= np.array([goal_check, def_check, mid_check, fow_check])
position_filter = filter_list[filter_index]

budget_filter = st.sidebar.slider(label='Budget',
                          min_value=0.0, 
                          max_value=14.0, 
                          value=14.0, 
                          step=0.1)

tab1, tab2, tab3 = st.tabs(['Player Cost', 'Minutes Played', 'Player Popularity'])

player_data_df = player_data_df[player_data_df['position'].isin(position_filter)]
player_data_df = player_data_df[player_data_df['now_cost'] <= budget_filter]

with tab1:
    cost_to_points = plot_scatter_player_points(player_data_df, 'now_cost', 'Player Cost')
    st.plotly_chart(cost_to_points, use_container_width=True)

with tab2:
    minutes_to_points = plot_scatter_player_points(player_data_df, 'minutes', 'Minutes Played')
    st.plotly_chart(minutes_to_points, use_container_width=True)

with tab3:
    popularity_to_points = plot_scatter_player_points(player_data_df, 'selected_by_percent', 'Selected By (%)')
    st.plotly_chart(popularity_to_points, use_container_width=True)
