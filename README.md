# 🤖 AI Code Reviewer
AI Code Reviewer is a Streamlit-based application that uses Google's Generative AI API to review Python code. It identifies potential bugs, suggests fixes, and provides insights for code optimization.

🚀 Features
Bug Detection: Identifies syntax errors, logical flaws, and potential issues in your Python code.
Code Optimization: Suggests fixes and improvements to enhance the code.
Actionable Insights: Provides tips for writing better Python code.
Interactive UI: User-friendly interface for analyzing Python code in real time.
🛠️ Tech Stack
Frontend: Streamlit
Backend: Google Generative AI API (Gemini-1.5)
Language: Python
🎯 Prerequisites
Before running the application, ensure you have the following installed:

Python 3.8 or above
Pip (Python package manager)
A valid API key for Google Generative AI
🛑 Important
Install the required libraries before running the application.
Ensure your API key is active and correctly configured in the code.
📝 Installation and Setup
1. Clone the Repository
bash
Copy code: https://github.com/KaushikSatpute/Ai_Code_Reviewer/blob/main/aicode.py

2. Install Dependencies
Install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
3. Add Your API Key
Replace "put your key here" in the code with your Google Generative AI API key:

python
Copy code
genai.configure(api_key="your-api-key-here")
4. Run the Application
Launch the Streamlit app:

bash
Copy code:
streamlit run aicode.py
5. Access the App
Open your browser and navigate to:

arduino
Copy code
http://localhost:8501
🖥️ File Structure
bash
Copy code
.
├── aicode.py              # Main application script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
📚 Usage
Paste your Python code in the text box provided in the app.
Click the Review Code button.
View the analysis, bug reports, and optimization suggestions.
⚙️ Example Output
Bug Report: Identifies syntax errors and logical flaws.
Fixed Code: Provides corrected code snippets with explanations.
Code Insights: Offers tips for improving code readability and efficiency.
📸 Screenshots
Home Page:

Code Review Example:

🧑‍💻 Contributing
Contributions are welcome! To contribute:

Fork this repository.
Create a new branch (feature-name).
Commit your changes.
Create a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🌟 Acknowledgments
Streamlit for providing a robust platform for interactive web apps.
Google Generative AI for powering the AI code analysis.
