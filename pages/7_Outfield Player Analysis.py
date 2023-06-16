import streamlit as st

from pages.functions.support_functions import \
    read_csv

from pages.functions.plots import plot_player_points_bar

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

st.markdown("# Outfield Player Analyis")

position_radio = st.sidebar.radio(
    "Position",
    ('Defender', 'Midfielder', 'Forward'))

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Goals Scored', 'Assists', 'No. Starts', 
                                                    'Clean Sheets', 'Goals Conceded', 'Penalties Missed',
                                                    'Yellow Cards', 'Red Cards']) 

player_df = read_csv('data/players.csv')
player_df = player_df[player_df['position'] == position_radio]

with tab1:
    player_df_gs = player_df.sort_values(by=['goals_scored'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_gs, 'goals_scored', 'Goals')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    player_df_a = player_df.sort_values(by=['assists'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_a, 'assists', 'Assists')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    player_df_starts = player_df.sort_values(by=['starts'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_starts, 'starts', 'Starts')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    player_df_gc = player_df.sort_values(by=['clean_sheets'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_gc, 'clean_sheets', 'Clean Sheets')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    defender_df_gc = player_df.sort_values(by=['goals_conceded'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_gc, 'goals_conceded', 'Goals Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    player_df_pm = player_df.sort_values(by=['penalties_missed'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_pm, 'penalties_missed', 'Penalties Missed')
    st.plotly_chart(fig, use_container_width=True)

with tab7:
    player_df_yc = player_df.sort_values(by=['yellow_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_yc, 'yellow_cards', 'Yellow Cards')
    st.plotly_chart(fig, use_container_width=True)

with tab8:
    player_df_rc = player_df.sort_values(by=['red_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(player_df_rc, 'red_cards', 'Red Cards')
    st.plotly_chart(fig, use_container_width=True)