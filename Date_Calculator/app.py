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
    col1, col2, col3 = st.columns(3)
    with col1:
        years = st.number_input('Years', min_value=0, value=0, step=1)
        months = st.number_input('Months', min_value=0, value=0, step=1)
    with col2:
        weeks = st.number_input('Weeks', min_value=0, value=0, step=1)
        days = st.number_input('Days', min_value=0, value=0, step=1)
    with col3:
        hours = st.number_input('Hours', min_value=0, value=0, step=1)
        minutes = st.number_input('Minutes', min_value=0, value=0, step=1)
    seconds = st.number_input('Seconds', min_value=0, value=0, step=1)

    if st.button('Calculate Date', on_click=None):
        original_date, new_date = add_time_to_date(years, months, weeks, days, hours, minutes, seconds)
        st.markdown(f"**Original Date and Time:** `{original_date.strftime('%Y-%m-%d %H:%M:%S')}`")
        st.markdown(f"**New Date and Time:** `{new_date.strftime('%Y-%m-%d %H:%M:%S')}`")


if __name__ == '__main__':
    main()

