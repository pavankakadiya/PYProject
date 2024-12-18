# PYProject - Environmental Impact Assessment  

We present an easy-to-use web tool that lets users assess their environmental effect by examining personal information like energy use, garbage generation, and business travel. The program offers a thorough PDF report that lists all inputs and outputs.

## Features  
--Users can enter information including monthly bills, rubbish generated, and kilometers traveled in this user-friendly form.  
--Carbon Footprint Calculation: Using user input, the software determines CO2 emissions.  
--A comprehensive and expert report that summarizes user data and outcomes is produced in PDF format.  
--Smooth operation on desktop and mobile devices is a feature of responsive design.  

---

## Tools and Technologies  
--Frontend: a user-centric design created with HTML and CSS.
--Backend: Flask was used to implement it, utilizing Python's web framework capabilities.
--PDF Generation: Creates reports using the FPDF library.

---

## How to Use  

### 1. Prerequisites  
- Install Python 3.7 or higher.  
- Install the following Python libraries:  
  bash
  pip install flask fpdf
  

### 2. Steps to Run the App  
1. Clone the Project:  
   bash
   git clone https://github.com/yourusername/environmental-impact-assessment.git  
   cd environmental-impact-assessment  
     
2. Run the App  
   bash
   python app.py  
     
3. Open in Browser:  
   Visit `http://127.0.0.1:5000/` in your web browser.  

---

## How It Works  
1.Enter your personal information on the form, including your city, the number of kilometers you drove for work, the quantity of waste you generate, and your energy expenses.  
2. Calculations: The application calculates and displays your CO2 emissions using basic calculations.  
3. Downloadable Report: You will receive a PDF report that includes all of the information and findings.  

---

## Formulas Used  
1. Energy Use:  
   
   (Electric Bill * 12 * 0.0005) + (Gas Bill * 12 * 0.0053) + (Fuel Bill * 12 * 2.32)
     
2. Waste:  
   
   (Waste Generated * 12 * (0.57 - (Recycled Waste / 100)))
     
3. Business Travel:  
   
   (Kilometers Traveled * (1 / Fuel Efficiency) * 2.31)
     

---

## Project Structure  
/static/         # Contains static files like CSS, JavaScript, and generated PDF reports.  
/templates/      # HTML templates used for rendering the web pages.  
app.py           # Main Python script for running the Flask web application.  
README.md        # Documentation file describing the project, features, and setup.  

---

## Contributing  
Are you willing to assist with this project? Once you have forked the repository and made your modifications, you are free to submit a pull request. Please make sure your code is logically sound, well-documented, and extensively tested.  

---

## Contact  
If you have any questions, feel free to reach out:  
- Email: kakdiyapavan@gmail.com  
- GitHub: [pavankakadiya](https://github.com/pavankakadiya)  
