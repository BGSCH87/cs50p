from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        # We pass the name in here so it's ready for the header or body
        super().__init__(orientation="P", unit="mm", format="A4")
        self.username = name

    def header(self):
        # 1. Set font for the Title
        self.set_font("helvetica", style="B", size=30)
        # 2. Add the title text
        self.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)
        
        # 3. Add the Shirt Image
        # To "fill" A4, we set width (w) to 210mm. 
        # Position (x=0, y=60) moves it down so it doesn't overlap the title.
        self.image("shirtificate.png", x=10, y=60, w=190)

# --- Execution Block ---

# 1. Get the name first
user_name = input("What is your name: ")

# 2. Instantiate the class (don't remove this!)
pdf = PDF(user_name)

# 3. Add a page (this automatically triggers the header() method)
pdf.add_page()

# 4. Overlay the text on the shirt
# We use set_y to move the "cursor" to the middle of the shirt image
pdf.set_y(120)
pdf.set_font("helvetica", size=28)
pdf.set_text_color(255, 255, 255) # White text for the shirt
pdf.cell(0, 10, f"{pdf.username} took CS50", align="C")

pdf.set_y(160)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(255, 255, 255) # White text for the shirt
pdf.cell(0, 10, f"And {pdf.username} loved Regex!", align="C")




# 5. Output
pdf.output("shirtificate.pdf")