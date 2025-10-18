from flask import Flask, render_template, request
import PyPDF2
import google.generativeai as genai

# ---------------------------
# Configure Gemini Pro API
# ---------------------------
genai.configure(api_key="AIzaSyBvjjr7-GhAhvLN-hKfXMEswlb2x52m4_4")  
model = genai.GenerativeModel("gemini-pro-latest")

# ---------------------------
# Initialize Flask app
# ---------------------------
app = Flask(__name__)

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    file = request.files['resume']

    if not file or not file.filename.endswith('.pdf'):
        return render_template('result.html', analysis="❌ Please upload a valid PDF file.")

    # Extract text from PDF
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    if len(text.strip()) == 0:
        return render_template('result.html', analysis="❌ No readable text found in the PDF.")

    # Create prompt for Gemini AI
    prompt = f"""
    You are a professional HR and resume analyst.
    Analyze the following resume text and provide structured feedback:
    - Strengths
    - Missing skills or sections
    - Suggestions for improvement
    - Overall impression

    Resume text:
    {text}
    """

    # Call Gemini Pro API
    response = model.generate_content(prompt)
    ai_output = response.text

    return render_template('result.html', analysis=ai_output)

# ---------------------------
# Run the Flask app
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
