import streamlit as st
import random
import time

st.title("🏥 Hospital Sensor Live Monitor")
st.write("### Live sensor data: Heart Rate, Temperature, and Oxygen Level")

# Patient list
patients = ["Harini", "Kamaraj", "Malathi", "Rajendiran", "Akash"]

# Function to generate simulated sensor readings
def sensor_data_stream():
    while True:
        data = []
        for p in patients:
            reading = {
                "patient": p,
                "heart_rate": random.randint(60, 100),
                "temperature": round(random.uniform(97.0, 100.0), 1),
                "oxygen_level": random.randint(90, 100),
            }
            data.append(reading)
        yield data
        time.sleep(1)

# --- Streamlit UI setup ---
placeholders = {}
for p in patients:
    st.subheader(f"👤 {p}")
    placeholders[p] = {
        "heart_rate_bar": st.progress(0),
        "temperature_bar": st.progress(0),
        "oxygen_bar": st.progress(0),
        "heart_rate_text": st.empty(),
        "temperature_text": st.empty(),
        "oxygen_text": st.empty(),
    }

# --- Live data update loop ---
for readings in sensor_data_stream():
    for reading in readings:
        p = reading["patient"]
        hr = reading["heart_rate"]
        temp = reading["temperature"]
        ox = reading["oxygen_level"]

        # update progress bars (scaled %)
        placeholders[p]["heart_rate_bar"].progress(min(hr, 100))
        placeholders[p]["temperature_bar"].progress(int((temp - 97) / 3 * 100))
        placeholders[p]["oxygen_bar"].progress(ox)

        # update text display
        placeholders[p]["heart_rate_text"].text(f"❤️ Heart Rate: {hr} bpm")
        placeholders[p]["temperature_text"].text(f"🌡️ Temperature: {temp} °F")
        placeholders[p]["oxygen_text"].text(f"🫁 Oxygen Level: {ox}%")

    time.sleep(1)
