import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import ast
# Page title
st.set_page_config(page_title='Price Right Explorer', page_icon='📊')
st.title('📊 Price Right Explorer')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the approximate price at which someone can mark their property.')
  st.markdown('**How to use the app?**')
  st.warning('Select/Provide some values to below fields related to your property.')
  
st.subheader('To provide a rough estimate for the place ($)')

# Load data
df = pd.read_csv('data/listings_detailed.csv')

locations = df.neighbourhood_group_cleansed
# Input widgets
location = st.text_input("Enter Street:")

# # Show suggestions based on user input
# filtered_suggestions_location = [sugg for sugg in locations if location.lower() in sugg.lower()]
# if filtered_suggestions_location:
#     st.write("Suggestions:")
#     selected_suggestion = st.selectbox("Select suggestion:", filtered_suggestions_location)
#     st.write("You selected:", selected_suggestion)

df.accommodates = df.accommodates.astype('int')
accomodates = df.accommodates.unique()
accomodates.sort()
accomodates_selection = st.selectbox('Select number of people', accomodates)

property_type = df.property_type.unique()
property_type_selection = st.selectbox('Property Type', property_type)

df.bedrooms = df.bedrooms.fillna(0).astype(int)
bedroom = df.bedrooms.unique()
bedroom.sort()
bedroom_selection = st.selectbox('Bedrooms', bedroom)

amenities = set()
for amenities_str in df.amenities:
    amn = amenities_str.replace('["','')
    amn = amn.replace('"]','')
    amn = amn.split('", "')
    for a in amn:
       amenities.add(a.strip())

amenities_list = list(amenities)
amenities_select = st.multiselect('Select amenities available', amenities_list);


#Display price
st.markdown("# The average price for your property would be $1500", unsafe_allow_html=True)

# df_selection = df[df.accommodates.isin(accomodates_selection)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# Display DataFrame
# df_columns =['name','description','property_type','room_type','bedrooms','amenities']
# df_editor = st.data_editor(df, height=212, use_container_width=True,num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# # Display chart
# chart = alt.Chart(df_chart).mark_line().encode(
#             x=alt.X('year:N', title='Year'),
#             y=alt.Y('gross:Q', title='Gross earnings ($)'),
#             color='genre:N'
#             ).properties(height=320)
# st.altair_chart(chart, use_container_width=True)
