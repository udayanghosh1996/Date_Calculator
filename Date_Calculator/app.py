from Realtive_Date_Calculator import *
from Date_Calcualtor import *
import streamlit as st

def main():

    # Styling
    st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            font-weight: bold;
        }
        .reportview-container .main .block-container{
            padding-top: 5rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
        </style>
        """, unsafe_allow_html=True)

    # Streamlit UI components
    st.title('Date and Time Calculator')

    # Layout

    col1, col2 = st.columns(2)
    with col1:
        st.header('Initial Date and Time')
        ini_year = st.number_input('Initial Year', min_value=0, value=0, step=1)
        ini_month = st.number_input('Initial Month', min_value=0, value=0, step=1)
        ini_day = st.number_input('Initial Day', min_value=0, value=0, step=1)
        ini_hour = st.number_input('Initial Hour', min_value=0, value=0, step=1)
        ini_minute = st.number_input('Initial Minute', min_value=0, value=0, step=1)
        ini_second = st.number_input('Initial Second', min_value=0, value=0, step=1)

    with col2:
        st.header('Duration to be added')
        years = st.number_input('Years', min_value=0, value=0, step=1)
        months = st.number_input('Months', min_value=0, value=0, step=1)
        weeks = st.number_input('Weeks', min_value=0, value=0, step=1)
        days = st.number_input('Days', min_value=0, value=0, step=1)
        hours = st.number_input('Hours', min_value=0, value=0, step=1)
        minutes = st.number_input('Minutes', min_value=0, value=0, step=1)
        seconds = st.number_input('Seconds', min_value=0, value=0, step=1)

    if st.button('Calculate Date', on_click=None):
        original_date, new_date = add_time_to_date(ini_year, ini_month, ini_day, ini_hour, ini_minute, ini_second,
                                                   years, months, weeks, days, hours, minutes, seconds)
        st.markdown(f"**Original Date and Time:** `{original_date.strftime('%Y-%m-%d %H:%M:%S')}`")
        st.markdown(f"**New Date and Time:** `{new_date.strftime('%Y-%m-%d %H:%M:%S')}`")


if __name__ == '__main__':
    main()

