import streamlit as st 
import pandas as pd
import pickle
import requests
from sklearn.ensemble import RandomForestRegressor

from datetime import date
import datetime

Data = pickle.load(open("data.pkl","rb"))
RandomForest = pickle.load(open("RandomForest.pkl","rb"))


st.title("Flight Price")


select_Airline = st.selectbox(
    "Which Airline do you want",
    Data["Airline"].values
)

select_source = st.selectbox(
    "what is your source location",
    Data["Source"].values
)


select_Destination = st.selectbox(
    "what is your source ",
    Data["Destination"].values
)



import datetime

# Set default date
default_date = datetime.date.today()

# Create two columns for day and month inputs
col7, col8 = st.columns(2)

# Add day input to first column
journey_day = col7.number_input("Select the journey day", value=default_date.day, min_value=1, max_value=31)

# Add month input to second column
journey_month = col8.selectbox("Select the journey month", options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=default_date.month - 1)

# Convert month name to month number
month_number = datetime.datetime.strptime(journey_month, "%B").month

# Combine day and month inputs into a datetime object
journey_date = datetime.date(default_date.year, month_number, journey_day)

# Display the selected date
st.write("You selected Journey date:", journey_date.strftime("%B %d, %Y"))



# Set the default time to 12:00 PM
default_time = datetime.time(12, 0)

# Create two input columns for hours and minutes
col1, col2 = st.columns(2)

# Add a time input widget to the first column for selecting the hour
dep_hour = col1.time_input("Select the Departure Time", value=default_time)

# Add a time input widget to the second column for selecting the minute
dep_minute = col2.time_input("Select the Departure minute", value=default_time)

# Combine the selected hour and minute into a datetime object
dep_time = datetime.datetime.combine(datetime.date.today(), datetime.time(dep_hour.hour, dep_minute.minute))

# Display the selected time
st.write("Dep_Time:", dep_time.time())




default_time1 = datetime.time(10, 0)

col3, col4 = st.columns(2)

Arrival_hour = col3.time_input("Select the  Arrival hour", value=default_time)

Arrival_minute = col4.time_input("Select the Arrival minute", value=default_time)

Arrival_time = datetime.datetime.combine(datetime.date.today(), datetime.time(dep_hour.hour, dep_minute.minute))

# Display the selected time
st.write("You selected:", Arrival_time.time())

default_time2 = datetime.time(11, 0)
col5, col6 = st.columns(2)

Duration_hour = col5.time_input("Select the  Duration hour", value=default_time)

Duration_minute = col6.time_input("Select the Duration minute", value=default_time)

Duration_time = datetime.datetime.combine(datetime.date.today(), datetime.time(dep_hour.hour, dep_minute.minute))


if st.button("Predict"):
    prediction = RandomForest.predict([[select_Airline, select_source, select_Destination, journey_day, journey_month, dep_hour, dep_minute, Arrival_hour, Arrival_time, Duration_hour, Duration_minute]])

# Display the predicted result
st.title(prediction[0])








