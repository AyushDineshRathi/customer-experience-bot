from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Retail Store Master Policy & Operations', 0, 1, 'C')

def create_dummy_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    text = """
    1. CONTEXTUAL PROMOTIONS (WEATHER):
    - Cold/Snow: Offer "Winter Warmer Bundle" ($15 Scarf+Coffee).
    - Rain: Offer Free Umbrella rental (Deposit $5).
    - Hot/Sunny: Suggest Iced Lemonade at the Cafe (Zone A).

    2. RETURN & EXCHANGE POLICY:
    - Electronics (e.g., iPhones, Headphones): Returnable within 14 days if sealed.
    - Clothing: 30 days with tags.
    - Clearance Items: Final Sale (No returns).
    - No Receipt? Store credit only.

    3. STORE NAVIGATION & ZONES:
    - Zone A: Entrance, Cafe, Men's Wear.
    - Zone B: Electronics, Starbucks, Escalator.
    - Zone C: Kids section, Restrooms, "Lost & Found".

    4. MEMBERSHIP TIERS:
    - Silver: 2% cashback.
    - Gold: 5% cashback + Free Coffee.
    - Platinum: 10% cashback + Personal Shopper.

    5. CRISIS PROTOCOLS:
    - Lost Child: Escort to "Lost & Found" (Zone C) immediately. Alert Security.
    - Spill/Mess: Call maintenance on channel 4. Block area.
    """
    
    # Write text
    pdf.multi_cell(0, 10, text)
    pdf.output("store_policy.pdf")
    print("✅ Expanded 'store_policy.pdf' created.")

if __name__ == "__main__":
    create_dummy_pdf()