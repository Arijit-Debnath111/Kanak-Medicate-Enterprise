import streamlit as st
import pandas as pd
import requests

def main():
    st.title("Konak")

    # Add sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Patients", "Appointments"])

    # Display different pages based on user selection
    if page == "Home":
        show_home_page()
    elif page == "Patients":
        show_patients_page()
    elif page == "Appointments":
        show_appointments_page()

def show_home_page():
    st.write("A one stop medical solution!")

API_BASE_URL = "https://example.com/api/medical/"

def fetch_patient_info(patient_name):
    url = f"{API_BASE_URL}/patients"
    params = {"name": patient_name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching patient information: {response.text}")
        return None

def show_patients_page():
    st.write("Patients Page")
    st.write("Here you can view and manage patients.")

    # Input for patient name
    patient_name = st.text_input("Enter patient's name")

    if st.button("Search"):
        # Fetch patient information from the API
        patient_info = fetch_patient_info(patient_name)

        if patient_info:
            st.write("Patient Information:")
            st.write(patient_info)

def show_appointments_page():
    st.write("Appointments Page")
    st.write("Here you can schedule appointments.")

    # Appointment form
    st.subheader("Schedule Appointment")

    patient_name = st.text_input("Patient's Name")
    appointment_date = st.date_input("Date")
    appointment_time = st.time_input("Time")

    if st.button("Schedule"):
        # Save appointment to database or perform other actions
        st.write(f"Appointment scheduled for {patient_name} on {appointment_date} at {appointment_time}")

if __name__ == "__main__":
    main()
