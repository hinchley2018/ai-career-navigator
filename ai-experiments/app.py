from fastapi import FastAPI
from pydantic import BaseModel
from InterviewAssistant import InterviewAssistant  # Import the InterviewAssistant class

app = FastAPI()

# Initialize the InterviewAssistant with a LinkedIn profile or any other required data
assistant = InterviewAssistant("https://www.linkedin.com/in/umermehmood2762/")

# Request Models
class InterviewQuestionRequest(BaseModel):
    job_role: str
    job_description: str

class FeedbackRequest(BaseModel):
    job_role: str
    job_description: str
    interview_question: str
    candidate_answer: str

class SolveProblemRequest(BaseModel):
    criteria: str


# Route: Generate interview questions
@app.post("/generate-interview-questions/")
def generate_interview_questions(request: InterviewQuestionRequest):
    questions = assistant.generate_interview_questions(
        request.job_role,
        request.job_description
    )
    return {"result": questions}


# Route: Provide feedback for candidate's answer
@app.post("/provide-feedback/")
def provide_feedback(request: FeedbackRequest):
    feedback = assistant.provide_feedback(
        request.job_role,
        request.job_description,
        request.interview_question,
        request.candidate_answer
    )
    return {"result": feedback}


# Route: Solve a technical problem based on given criteria
@app.post("/solve-technical-problem/")
def solve_technical_problem(request: SolveProblemRequest):
    solution = assistant.solve_technical_problem(request.criteria)
    return {"result": solution}


# Route: Handle interview question flow
@app.post("/handle-interview-question-flow/")
def handle_interview_question_flow(request: FeedbackRequest):
    interview_flow = assistant.handle_interview_question_flow(
        request.job_role,
        request.job_description,
        request.interview_question,
        request.candidate_answer
    )
    return {"result": interview_flow}


# Route: Review LinkedIn profile and provide feedback
@app.post("/review-linkedin-profile/")
def review_linkedin_profile():
    linkedin_feedback = assistant.review_linkedin_profile_and_provide_feedback()
    return {"result": linkedin_feedback}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
