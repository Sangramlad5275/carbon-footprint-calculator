
import streamlit as st
import pandas as pd
import pdfkit
from calculator import calculate_footprint

st.title("🌱 Carbon Footprint Calculator (Basic)")

st.sidebar.header("Your Inputs")
electricity_kwh = st.sidebar.number_input("Annual electricity consumption (kWh)", min_value=0, value=3000)
heating_kwh = st.sidebar.number_input("Annual heating consumption (kWh)", min_value=0, value=5000)
heating_type = st.sidebar.selectbox("Heating type", options=['gas', 'oil', 'electricity'])
car_km = st.sidebar.number_input("Annual car travel (km)", min_value=0, value=8000)
flights_km = st.sidebar.number_input("Annual flights (km)", min_value=0, value=2000)
diet_type = st.sidebar.selectbox("Diet type", options=['omnivore', 'vegetarian', 'vegan'])

inputs = {
    'electricity_kwh': electricity_kwh,
    'heating_kwh': heating_kwh,
    'heating_type': heating_type,
    'car_km': car_km,
    'flights_km': flights_km,
    'diet_type': diet_type
}

results = calculate_footprint(inputs)

st.subheader("Your Results")
st.metric("Total Annual CO₂ Emissions", f"{results['total']:.2f} tons CO₂e")

breakdown = {
    'Electricity': results['electricity'],
    'Heating': results['heating'],
    'Car': results['car'],
    'Flights': results['flights'],
    'Diet': results['diet']
}
df = pd.DataFrame.from_dict(breakdown, orient='index', columns=['Tons CO₂e'])
df.loc['Total'] = results['total']

csv = df.to_csv().encode('utf-8')
st.download_button("Download results as CSV", data=csv, file_name='carbon_footprint_results.csv', mime='text/csv')

html_string = """
<html>
<head>
<style>
body { font-family: Arial, sans-serif; }
h1 { color: #2e7d32; }
</style>
</head>
<body>
<h1>Carbon Footprint Report</h1>
<p><strong>Total Emissions:</strong> {:.2f} tons CO₂e</p>
<h2>Breakdown</h2>
<ul>
<li>Electricity: {:.2f} tons CO₂e</li>
<li>Heating: {:.2f} tons CO₂e</li>
<li>Car: {:.2f} tons CO₂e</li>
<li>Flights: {:.2f} tons CO₂e</li>
<li>Diet: {:.2f} tons CO₂e</li>
</ul>
<h2>Suggestions</h2>
<p>- Switch to renewable electricity.<br>
- Improve insulation.<br>
- Reduce flights.<br>
- Shift diet.<br>
- Use electric vehicles.</p>
</body>
</html>
""".format(results['total'], results['electricity'], results['heating'], results['car'], results['flights'], results['diet'])

if st.button("Generate and Download PDF"):
    pdfkit.from_string(html_string, "carbon_footprint_report.pdf")
    with open("carbon_footprint_report.pdf", "rb") as f:
        st.download_button("Click to download PDF", f, file_name="carbon_footprint_report.pdf")
