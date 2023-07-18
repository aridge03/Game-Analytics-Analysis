
import streamlit as st
import pandas as pd
import plotly.express as px

# Make the title setup 
st.title ('Game Information Dashboard')
st.write('Visualization of video game analytics last updated December 2020.')
st.write('Checkout [Data Visualization Options] to begin')

# Select the allowed columns to read from CSV
allowed_columns = ['name','playtime','achievements_count','ratings_count','suggestions_count','game_series_count','reviews_count']

# Choose possible column values for Y-axis
possible_y = ['playtime','achievements_count','ratings_count','suggestions_count','game_series_count','reviews_count']
df = pd.read_csv('first_40_lines.csv', usecols= allowed_columns,  nrows=25)
st.sidebar.header('Data Visualization Options')
st.sidebar.write('Game Analytics Bar Chart')

#Dropdown option for Bar Chart
selected_columns = st.sidebar.multiselect('Select columns for Bar Chart', possible_y)
if 'name' not in selected_columns:
    selected_columns.append('name')
if selected_columns:
    chart_data = df[selected_columns].set_index('name')
    chart_data_sorted = chart_data.sort_values(by=selected_columns[0], ascending=False)
    st.bar_chart(chart_data_sorted, use_container_width=True)
    # Display descriptions of chosen column
    if "playtime" in selected_columns:
        st.sidebar.write('Playtime: Hours needed to complete the game')
    if "achievements_count" in selected_columns:
        st.sidebar.write('Achievements Count: Number of achievements in game')
    if "ratings_count" in selected_columns:
        st.sidebar.write('Ratings Count: Number of RAWG users who rated the game')
    if "suggestions_count" in selected_columns:
        st.sidebar.write('Suggestions Count: Number of RAWG users who suggested the game')
    if "game_series_count" in selected_columns:
        st.sidebar.write('Game Series Count: Number of games in the series')
    if "reviews_count" in selected_columns:
        st.sidebar.write('Reviews Count: Number of games in the series')
    
else:
    st.write('Please select columns to display the bar chart.')

#Dropdown option for Bubble Chart
st.sidebar.write('Game Analytics Bubble Chart')
selected_column_bubble = st.sidebar.selectbox('Select a column for Bubble Chart', possible_y)
if selected_column_bubble:
    if selected_column_bubble != 'name':
        fig = px.scatter(df, x='name', y=None, size=selected_column_bubble, size_max=40,
                     color=selected_column_bubble, hover_name='name', hover_data=[selected_column_bubble])

        # Plot the bubble chart
        fig.update_layout(
        xaxis_title='Name',
        yaxis_title='Bubble Size',
        title=f"Bubble Chart - Bubble Size based on '{selected_column_bubble}'" )
        st.plotly_chart(fig)
    else:
        st.write("Please choose a Y-axis column other than 'name' for the Bubble Chart.")

# Display the DataFrame in a table
st.write('Original DataFrame:')
st.write(df)
