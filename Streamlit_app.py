import streamlit as st
import pandas as pd


coffee_data = pd.DataFrame({
    'Coffee Name': ['Ethiopian Yirgacheffe', 'Colombian Supremo', 'Guatemala Antigua', 'Sumatra Mandheling'],
    'Flavor Notes': ['Floral, Citrus, Tea', 'Nutty, Sweet, Chocolate', 'Spicy, Cocoa, Smooth', 'Earthy, Rich, Bold'],
    'Region': ['Ethiopia', 'Colombia', 'Guatemala', 'Indonesia'],
    'Roast Level': ['Light', 'Medium', 'Medium', 'Dark'],
    'Acidity': ['High', 'Medium', 'Low', 'Low'],
    'Body': ['Light', 'Medium', 'Medium', 'Full']
})

# Sidebar for user preferences
st.sidebar.header("Coffee Preferences")
preferred_flavor = st.sidebar.multiselect(
    "Flavor Notes",
    options=coffee_data['Flavor Notes'].unique(),
    help="Select flavor profiles you enjoy."
)
preferred_region = st.sidebar.selectbox(
    "Region",
    options=['Any'] + coffee_data['Region'].unique().tolist(),
    help="Choose a coffee-producing region."
)
preferred_roast = st.sidebar.radio(
    "Roast Level",
    options=['Any', 'Light', 'Medium', 'Dark'],
    help="Select your preferred roast level."
)
preferred_acidity = st.sidebar.radio(
    "Acidity",
    options=['Any', 'High', 'Medium', 'Low'],
    help="Choose your preferred acidity level."
)
preferred_body = st.sidebar.radio(
    "Body",
    options=['Any', 'Light', 'Medium', 'Full'],
    help="Select your preferred body level."
)

# Filter data based on preferences
filtered_data = coffee_data.copy()

if preferred_flavor:
    filtered_data = filtered_data[filtered_data['Flavor Notes'].isin(preferred_flavor)]
if preferred_region != 'Any':
    filtered_data = filtered_data[filtered_data['Region'] == preferred_region]
if preferred_roast != 'Any':
    filtered_data = filtered_data[filtered_data['Roast Level'] == preferred_roast]
if preferred_acidity != 'Any':
    filtered_data = filtered_data[filtered_data['Acidity'] == preferred_acidity]
if preferred_body != 'Any':
    filtered_data = filtered_data[filtered_data['Body'] == preferred_body]

# Main section
st.title("Green Coffee Recommendation Tool")
st.write("Select your preferences in the sidebar to see recommendations.")

if not filtered_data.empty:
    st.subheader("Recommended Coffees")
    st.dataframe(filtered_data)
else:
    st.warning("No coffees match your preferences. Try adjusting the filters.")