from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF
from datetime import datetime

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Environmental Impact Assessment", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def calculate_energy_use(a1, a2, a3):
    return (a1 * 12 * 0.0005) + (a2 * 12 * 0.0053) + (a3 * 12 * 2.32)

def calculate_waste(b1, b2):
    return b1 * 12 * (0.57 - b2 / 100)

def calculate_business_travel(c1, c2):
    return c1 * (1 / c2) * 2.31

def generate_pdf(user_name, user_city, questions_answers, results, pdf_file_name):
    pdf = PDF()
    pdf.add_page()

    # Set header font and add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Environmental Impact Assessment Report", ln=True, align='C')
    pdf.ln(10)

    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Add user details with date
    pdf.set_font("Arial", size=12)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, "User Details:", ln=False, fill=True, align='L')  # "User Details" aligned to the left
    pdf.cell(0, 10, f"Date: {current_date}", ln=True, align='R')  # Date aligned to the right
    pdf.ln(5)
    pdf.cell(0, 10, f"Name: {user_name}", ln=True)
    pdf.cell(0, 10, f"City: {user_city}", ln=True)
    pdf.ln(10)

    # Add questions and answers
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(0, 10, "Questions and Answers:", ln=True, fill=True, align='L')
    pdf.ln(5)

    for question, answer in questions_answers:
        pdf.set_font("Arial", style="B", size=10)
        pdf.cell(90, 10, question, border=1, align='L')
        pdf.set_font("Arial", size=10)
        pdf.cell(100, 10, str(answer), border=1, align='L')
        pdf.ln()

    pdf.ln(10)

    # Add results section
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, "Summary of Calculated Results:", ln=True, fill=True, align='L')
    pdf.ln(5)

    pdf.set_fill_color(180, 200, 240)
    pdf.cell(100, 10, "Category", border=1, fill=True, align='C')
    pdf.cell(90, 10, "Amount (kg CO2)", border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_font("Arial", size=10)
    pdf.set_fill_color(245, 245, 245)
    for idx, (category, amount) in enumerate(results):
        fill = (idx % 2 == 0)
        pdf.cell(100, 10, category, border=1, fill=fill, align='L')
        pdf.cell(90, 10, f"{amount:.2f}", border=1, fill=fill, align='L')
        pdf.ln()

    # Add final note
    pdf.ln(10)
    pdf.set_font("Arial", style="I", size=10)
    pdf.multi_cell(0, 10, "Note: All calculated values are approximate and presented for educational purposes.", align='C')

    # Add second page with calculation formulas
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "How Calculations Are Performed", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, 
        "Energy Use: \n"
        "Formula: (Monthly Electric Bill * 12 * 0.0005) + (Monthly Gas Bill * 12 * 0.0053) + (Monthly Fuel Bill * 12 * 2.32)\n\n"
        "Waste: \n"
        "Formula: (Total Waste Generated Per Month * 12 * (0.57 - (Waste Recycled / 100)))\n\n"
        "Business Travel: \n"
        "Formula: (Total Kilometers Traveled per year for business purposes * (1 / avg. Fuel Efficiency in L) * 2.31)"
    )
    pdf.ln(10)

    # Save the PDF to a file
    pdf.output("./Python/PY PROJECT /static/" + pdf_file_name)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods=['POST'])
def process_form():
    # Get user details
    user_name = request.form['user_name']
    user_city = request.form['user_city']

    # Get form inputs
    a1 = float(request.form['electric_bill'])
    a2 = float(request.form['gas_bill'])
    a3 = float(request.form['fuel_bill'])

    b1 = float(request.form['waste_generated'])
    b2 = float(request.form['waste_recycled'])

    c1 = float(request.form['business_km'])
    c2 = float(request.form['fuel_efficiency'])

    # Calculate results
    energy_result = calculate_energy_use(a1, a2, a3)
    waste_result = calculate_waste(b1, b2)
    travel_result = calculate_business_travel(c1, c2)

    # Prepare results for display
    questions_answers = [
        ("Average monthly electric bill", a1),
        ("Average monthly natural gas bill", a2),
        ("Average fuel bill for Transportation", a3),
        ("Waste generated per month (kg)", b1),
        ("Percentage of waste recycled or composted", b2),
        ("Kilometers traveled for business per year", c1),
        ("Average fuel efficiency (liters per 100 km)", c2),
    ]

    results = [
        ["Energy Use (kg CO2)", energy_result],
        ["Waste (kg CO2)", waste_result],
        ["Business Travel (kg CO2)", travel_result],
    ]

    # Generate PDF
    pdf_file_name = "results_summary.pdf"
    generate_pdf(user_name, user_city, questions_answers, results, pdf_file_name)

    return redirect(f"/static/{pdf_file_name}")



if __name__ == "__main__":
    app.run(debug=True)
