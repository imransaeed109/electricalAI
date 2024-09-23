import streamlit as st

def main():
    st.title("Electrical Wire Selection App")

    # Inputs for Current, Voltage
    current = st.number_input("Enter Current (Amps)", min_value=0.0, format="%.2f")
    voltage = st.number_input("Enter Voltage (Volts)", min_value=0.0, format="%.2f")
    
    # Add any other inputs you may need like temperature, wire length
    ambient_temp = st.number_input("Ambient Temperature (°C)", min_value=-20, max_value=50)
    wire_length = st.number_input("Wire Length (meters)", min_value=0.0, format="%.2f")

    if st.button("Calculate Wire Size"):
        # Call your logic here
        suggest_wire(current, voltage, ambient_temp, wire_length)

def suggest_wire(current, voltage, temp, length):
    # Your logic for wire selection goes here
    # Example logic (simple, will need real standards to make accurate)
    if current <= 10:
        wire_type = "Copper"
        wire_diameter = "2.5 mm²"
        conductor_type = "Solid"
    elif current <= 20:
        wire_type = "Copper"
        wire_diameter = "4 mm²"
        conductor_type = "Stranded"
    else:
        wire_type = "Aluminum"
        wire_diameter = "6 mm²"
        conductor_type = "Stranded"

    st.write(f"Recommended Wire Type: {wire_type}")
    st.write(f"Wire Diameter: {wire_diameter}")
    st.write(f"Conductor Type: {conductor_type}")

if __name__ == "__main__":
    main()
