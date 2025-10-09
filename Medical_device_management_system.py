import streamlit as st

# ------------------------------
# Parent class
# ------------------------------
class MedicalDevice:
    def __init__(self, device_name):
        self.device_name = device_name

    def switch_on(self):
        return f"{self.device_name} is now switched on."


# ------------------------------
# Child classes
# ------------------------------
class HeartMonitor(MedicalDevice):
    def display_heart_rate(self, bpm):
        return f"Heart rate: {bpm} bpm"


class AdvancedHeartMonitor(HeartMonitor):
    def alert_irregular_heartbeat(self):
        return f"{self.device_name} alerts: Irregular heartbeat detected!"


class DeviceNetwork:
    def connect_network(self):
        return "Device connected to hospital network."


class SmartMedicalDevice(HeartMonitor, DeviceNetwork):
    def auto_update(self):
        return f"{self.device_name} software updated automatically."


class BloodPressureMonitor(MedicalDevice):
    def display_bp(self, systolic, diastolic):
        return f"Blood Pressure: {systolic}/{diastolic} mmHg"


class SmartAdvancedMonitor(SmartMedicalDevice, AdvancedHeartMonitor):
    def remote_monitoring(self):
        return f"{self.device_name} is now available for remote monitoring."


# ------------------------------
# Streamlit App
# ------------------------------
st.title("🏥 Smart Medical Device Management System")

device_name = st.text_input("Enter Device Name")
device_type = st.selectbox(
    "Select Device Type",
    [
        "Heart Monitor",
        "Advanced Heart Monitor",
        "Blood Pressure Monitor",
        "Smart Medical Device",
        "Smart Advanced Monitor"
    ]
)

# Extra input for heart rate or blood pressure
bpm = st.number_input("Enter heart rate (BPM)", min_value=40, max_value=200, value=75)
systolic = st.number_input("Enter systolic pressure", min_value=80, max_value=200, value=120)
diastolic = st.number_input("Enter diastolic pressure", min_value=50, max_value=130, value=80)

if st.button("Activate Device"):
    if not device_name:
        st.warning("Please enter a device name!")
    else:
        features = {}

        # HEART MONITOR
        if device_type == "Heart Monitor":
            device = HeartMonitor(device_name)
            st.success(f"Heart Monitor Activated: {device.device_name}")
            features["Feature"] = [
                device.switch_on(),
                device.display_heart_rate(bpm)
            ]

        # ADVANCED HEART MONITOR
        elif device_type == "Advanced Heart Monitor":
            device = AdvancedHeartMonitor(device_name)
            st.success(f"Advanced Heart Monitor Activated: {device.device_name}")
            features["Feature"] = [
                device.switch_on(),
                device.display_heart_rate(bpm),
                device.alert_irregular_heartbeat()
            ]

        # BLOOD PRESSURE MONITOR
        elif device_type == "Blood Pressure Monitor":
            device = BloodPressureMonitor(device_name)
            st.success(f"Blood Pressure Monitor Activated: {device.device_name}")
            features["Feature"] = [
                device.switch_on(),
                device.display_bp(systolic, diastolic)
            ]

        # SMART MEDICAL DEVICE
        elif device_type == "Smart Medical Device":
            device = SmartMedicalDevice(device_name)
            st.success(f"Smart Medical Device Activated: {device.device_name}")
            features["Feature"] = [
                device.switch_on(),
                device.display_heart_rate(bpm),
                device.connect_network(),
                device.auto_update()
            ]

        # SMART ADVANCED MONITOR
        elif device_type == "Smart Advanced Monitor":
            device = SmartAdvancedMonitor(device_name)
            st.success(f"Smart Advanced Monitor Activated: {device.device_name}")
            features["Feature"] = [
                device.switch_on(),
                device.display_heart_rate(bpm),
                device.connect_network(),
                device.auto_update(),
                device.alert_irregular_heartbeat(),
                device.remote_monitoring()
            ]

        # Display results
        st.table(features)
