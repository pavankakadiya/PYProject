# PYProject - Environmental Impact Assessment  

Introducing an intuitive web application that enables users to evaluate their environmental impact by analyzing personal data such as energy consumption, waste production, and business travel. The application provides a comprehensive PDF report detailing all inputs and results.

---

## Features  
- Easy-to-Use Form: Users can enter details such as monthly bills, waste generated, and kilometers traveled.  
- Carbon Footprint Calculation: The app calculates CO2 emissions based on user input.  
- PDF Report: A professional and detailed report is generated, summarizing user data and results.  
- Responsive Design: Works smoothly on both desktop and mobile devices.  

---

## Tools and Technologies  
--Frontend: Developed using HTML and CSS, featuring a user-centric design.
--Backend: Implemented with Flask, leveraging Python's web framework capabilities.
--PDF Generation: Utilizes the FPDF library for creating reports.


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
1. Data Input: Fill out the form with your own details like your energy bills, waste generated, and kilometers traveled for business and your City.  
2. Calculations: The app uses simple formulas to calculate your CO2 emissions and give you result.  
3. Downloadable Report: A PDF report is created with all the details and gives you results.  

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
Interested in contributing to this project? You're welcome to fork the repository, implement your improvements, and submit a pull request. Please ensure your code is well-documented, thoroughly tested, and logically sound.  

---

## Contact  
If you have any questions, feel free to reach out:  
- Email: kakdiyapavan@gmail.com  
- GitHub: [pavankakadiya](https://github.com/pavankakadiya)  
