# PYProject 

# Environmental Impact Assessment Project
This repository contains a web application designed to calculate and evaluate environmental impacts, including energy use, waste, and business travel. The app calculates a user's carbon footprint and generates a detailed PDF report.

## Features
- User-Friendly Form: Collects personal and environmental data like monthly bills, waste generated, and business travel details.
- Carbon Footprint Calculator: Computes CO2 emissions based on provided data.
- PDF Report Generation: Automatically generates a professional report summarizing inputs and calculated results.
- Responsive Design: Optimized for desktops and mobile devices.

## Technologies Used
- Frontend: HTML, CSS (styled with a modern UI/UX approach)
- Backend: Flask (Python-based web framework)
- PDF Generation: FPDF (Python library)
- Deployment: Local development server for testing

## Installation

### Prerequisites
- Python 3.7 or higher
- Flask
- FPDF library

### Steps
1. Clone this repository:
   bash
   git clone https://github.com/yourusername/environmental-impact-assessment.git
   cd environmental-impact-assessment

2. Install the required dependencies:
   bash
   pip install flask fpdf


5. Run the Flask application:
   bash
   python app.py
   

6. Open your browser and navigate to:
   http://127.0.0.1:5000/
   

## How It Works
1. Input Data: Fill out the form with details such as energy bills, waste generated, and business travel.
2. Calculation: The backend computes CO2 emissions using predefined formulas.
3. PDF Report: A detailed report summarizing your inputs and the calculated environmental impact is generated and downloadable.

## Project Structure

/static/                 # Directory for static files, including the generated PDFs
/templates/              # HTML templates for the web app
app.py                   # Main Flask application script
README.md                # Project documentation

---

## Formulas Used
-Energy Use
  Energy = (Electric Bill * 12 * 0.0005) + (Gas Bill * 12 * 0.0053) + (Fuel Bill * 12 * 2.32)
-Waste
  Waste = (Waste Generated * 12 * (0.57 - (Recycled Waste / 100)))
-Business Travel
  Travel = (Kilometers Traveled * (1 / Fuel Efficiency) * 2.31)


## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests. Please adhere to the coding style and include tests for new functionality.

## Contact
For any questions or suggestions, feel free to reach out:
- Email: kakdiyapavan@gmail.com
- GitHub: [pavankakadiya](https://github.com/pavankakadiya)

