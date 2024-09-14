from flask import Flask, request, jsonify
from InterviewAssistant import InterviewAssistant  # Import the InterviewAssistant class from your module

app = Flask(__name__)

# Initialize the InterviewAssistant with a dummy LinkedIn profile
assistant = InterviewAssistant("https://www.linkedin.com/in/umermehmood2762/")

@app.route('/generate-interview-questions', methods=['POST'])
def generate_interview_questions():
    data = request.json
    questions = assistant.generate_interview_questions(data['job_role'], data['job_description'])
    return jsonify(questions)

@app.route('/provide-feedback', methods=['POST'])
def provide_feedback():
    data = request.json
    feedback = assistant.provide_feedback(
        data['job_role'],
        data['job_description'],
        data['interview_question'],
        data['candidate_answer']
    )
    return jsonify(feedback)

@app.route('/solve-technical-problem', methods=['POST'])
def solve_technical_problem():
    data = request.json
    problem_solution = assistant.solve_technical_problem(data['criteria'])
    return jsonify(problem_solution)

@app.route('/handle-interview-question-flow', methods=['POST'])
def handle_interview_question_flow():
    data = request.json
    interview_flow = assistant.handle_interview_question_flow(
        data['job_role'],
        data['job_description'],
        data['interview_question'],
        data['candidate_answer']
    )
    return jsonify(interview_flow)

@app.route('/review-linkedin-profile', methods=['POST'])
def review_linkedin_profile():
    data = request.json
    linkedin_feedback = assistant.review_linkedin_profile_and_provide_feedback()
    return jsonify(linkedin_feedback)

if __name__ == '__main__':
    app.run(debug=True)
