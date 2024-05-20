import streamlit as st
import pandas as pd
from backend.dboperations import get_item_details
from helper_function.delivery_note import generate_delivery_note
from helper_function.barcode_scan import scan_barcode_opencv
# from fpdf import FPDF

# Title of the application
st.title("SCM Delivery Note Barcode")

# Session state to keep track of all entries
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Product ID', 'Product Name', 'Product Price', 'Product Stock'])

# Text input for barcode
barcode = st.text_input("Input for Barcode", help="Enter the barcode from Products table")

# Submit button for fetching data
if st.button("Submit"):
    item_details = get_item_details(barcode)
    if item_details:
        # Convert item_details to a DataFrame and append to session state
        new_entry = pd.DataFrame([item_details], columns=['Product ID', 'Product Name', 'Product Price', 'Product Stock'])
        st.session_state['data'] = pd.concat([st.session_state['data'], new_entry], ignore_index=True)
    else:
        st.error("No details found for the entered barcode.")

st.write('OR')

if st.button("scan barcode"):
    barcode = scan_barcode_opencv()
    item_details = get_item_details(barcode)
    if item_details:
        # Convert item_details to a DataFrame and append to session state
        new_entry = pd.DataFrame([item_details], columns=['Product ID', 'Product Name', 'Product Price', 'Product Stock'])
        st.session_state['data'] = pd.concat([st.session_state['data'], new_entry], ignore_index=True)
    else:
        st.error("No details found for the entered barcode.")


# Display the table and total price
if not st.session_state['data'].empty:
    st.table(st.session_state['data'])
    total_price = st.session_state['data']['Product Price'].sum()
    st.write(f"Total Price: ${total_price}")

# Button to generate PDF
if st.button("Generate Delivery Note PDF"):
    generate_delivery_note(st.session_state['data'])