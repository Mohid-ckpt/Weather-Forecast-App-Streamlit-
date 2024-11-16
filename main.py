# Imports:

import streamlit as st
import plotly.express as px
from backend import get_data

# Frontend:
st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=15,
                 help="Select the number of days forecasted")
option = st.selectbox("Select the data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}:")

if place:
    try:
        # Get the required data:
        filtered_data = get_data(place,days)

        if option.lower() == 'temperature':
            # Filter the Data:
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            temperatures = [temperature/10 for temperature in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create the temperature plot:
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        elif option == 'Sky':
            # Filter the data:
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            images = {'Clear':'images/clear.png','Clouds':'images/cloud.png',
                      'Rain':'images/rain.png','Snow':'images/snow.png'}
            image_list = [images[condition] for condition in sky_conditions]
            # Viewing the sky data:
            st.image(image_list, width=115)
    except:
        st.write("Please enter a valid place")