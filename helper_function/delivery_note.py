from fpdf import FPDF
import streamlit as st

def generate_delivery_note(product_data):
    pdf = FPDF()
    pdf.add_page()

    # Add the logo at the top of the PDF
    pdf.image('logo.png', x=10, y=8, w=40)  # Adjust x, y, w (width), h (height) as needed

    # Set title and fonts after the logo
    pdf.set_xy(0, 30)  # Reset position after logo; adjust y coordinate based on logo size
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Delivery Note", ln=True, align='C')

    # Add table headers
    pdf.cell(40, 10, "Product ID", border=1, ln=0)
    pdf.cell(100, 10, "Product Name", border=1, ln=0)
    pdf.cell(40, 10, "Product Price", border=1, ln=0)
    pdf.cell(40, 10, "Product Stock", border=1, ln=1)

    # Add table rows
    total_price = 0
    for _, row in product_data.iterrows():
        pdf.cell(40, 10, str(row['Product ID']), border=1, ln=0)
        pdf.cell(100, 10, str(row['Product Name']), border=1, ln=0)
        pdf.cell(40, 10, str(row['Product Price']), border=1, ln=0)
        pdf.cell(40, 10, str(row['Product Stock']), border=1, ln=1)
        total_price += row['Product Price']

    # Add total price at the end of the PDF
    pdf.cell(180, 10, "Total Price: $" + str(total_price), border=1, ln=1, align='C')

    # Output the PDF
    pdf.output("delivery_note.pdf")
    st.success('PDF generated successfully! PDF is saved in the server directory.')