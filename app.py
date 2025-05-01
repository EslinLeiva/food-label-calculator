import streamlit as st
import pandas as pd

# Sample data for demonstration
data = {
    "header_id": [1, 2, 3, 4],
    "line_id": [10, 20, 30, 40],
    "provider_id": ["A123", "B456", "C789", "D012"],
    "TEPRV": ["T1", "T2", "T3", "T4"],
    "claim_amount": [100, 200, 300, 400]
}
df = pd.DataFrame(data)

# Streamlit app
st.title("Custom Data Report")

# Selection for report level
report_level = st.selectbox("Select Report Level Data:", ["Header Level Data", "Line Level Data"])

# Input for provider ID or TEPRV search
provider_id_input = st.text_input("Enter Provider ID (leave blank if not applicable):")
teprv_input = st.text_input("Enter TEPRV (leave blank if not applicable):")

# Filter data based on user input
filtered_df = df.copy()

if provider_id_input:
    filtered_df = filtered_df[filtered_df["provider_id"] == provider_id_input]

if teprv_input:
    filtered_df = filtered_df[filtered_df["TEPRV"] == teprv_input]

# Display report based on selection
if report_level == "Header Level":
    st.header("Header Level Report")
    st.dataframe(filtered_df[["header_id", "provider_id", "TEPRV", "claim_amount"]])
elif report_level == "Line Level":
    st.header("Line Level Report")
    st.dataframe(filtered_df[["line_id", "provider_id", "TEPRV", "claim_amount"]])

# Run the app
if __name__ == "__main__":
    st.run()
