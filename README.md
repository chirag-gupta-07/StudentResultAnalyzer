# 📝 Student Result Analyzer

A Python project to analyze student marks using **Pandas** & **NumPy** and visualize results with **Matplotlib**.  
This project helps calculate totals, percentages, find subject toppers, and generate charts for better insights.

---

## ✨ Features
- Read student marks from a CSV file
- Calculate **total marks** and **percentage**
- Identify **subject toppers** and **overall topper**
- Generate **summary CSV file**
- Visualize results with **bar charts**

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chirag-gupta-07/StudentResultAnalyzer.git
   cd StudentResultAnalyzer
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   ```
   - Activate on **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - Activate on **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Prepare your dataset**  
   Example file: `students.csv`
   ```csv
   Name,Math,Science,English
   Amit,78,85,90
   Priya,92,80,88
   Rahul,60,70,65
   Sneha,85,95,89
   Karan,45,55,50
   ```

2. **Run the script**
   ```bash
   python main.py
   ```

3. **Output Includes**
   - Class averages per subject
   - Subject toppers & overall topper
   - New CSV file `results.csv` with total & percentage
   - Bar chart of student performance

---

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib

---

## 🚀 Future Enhancements
- Add a **Tkinter GUI** for user-friendly interaction
- Export results to **Excel** with formatting
- Add **subject-wise comparison graphs**

---

## 👨‍💻 Author
- **Chirag**  
- GitHub: [chirag-gupta-07](https://github.com/chirag-gupta-07)  
- LinkedIn: [Chirag Gupta](www.linkedin.com/in/chirag-gupta-aa3497379)

---
