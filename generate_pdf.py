from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Retail Store Internal Policy & Inventory', 0, 1, 'C')

def create_dummy_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    text = """
    1. COLD WEATHER PROTOCOL:
    If a customer mentions feeling cold, suggest hot beverages. 
    Current promotions:
    - 10% off Hot Cocoa at the in-store Starbucks (Zone B).
    - "Winter Warmer" bundle: Scarf + Coffee for $15.
    
    2. RAINY WEATHER PROTOCOL:
    If it is raining, offer:
    - Free umbrella rental with any purchase over $50.
    - Direction to the nearest covered parking (Zone A).

    3. STORE LOCATIONS:
    - Starbucks: 50m from entrance, Zone B.
    - Uniqlo: 2nd Floor, near the escalator.
    - Restrooms: Behind the customer service desk.
    
    4. RETURN POLICY:
    - Electronics: 15 days with receipt.
    - Clothing: 30 days with tags attached.
    - No returns on food items.
    """
    
    pdf.multi_cell(0, 10, text)
    pdf.output("store_policy.pdf")
    print("✅ 'store_policy.pdf' created successfully.")

if __name__ == "__main__":
    try:
        import fpdf
        create_dummy_pdf()
    except ImportError:
        print("Please run: pip install fpdf")