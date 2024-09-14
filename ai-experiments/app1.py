from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from InterviewAssistant import InterviewAssistant  # Import the InterviewAssistant class
import logging
from typing import Any

app = FastAPI()

assistant = InterviewAssistant("https://www.linkedin.com/in/umermehmood2762/")

logging.basicConfig(level=logging.DEBUG)

def serialize(obj: Any):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()  
    elif isinstance(obj, dict):
        return obj  
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]  
    else:
        return {"error": f"Object of type {type(obj).__name__} is not JSON serializable"}

# Define request models for endpoints
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

# Route: generate-interview-questions
@app.post("/generate-interview-questions/")
async def generate_interview_questions(request: InterviewQuestionRequest):
    try:
        questions = assistant.generate_interview_questions(request.job_role, request.job_description)
        logging.debug(f"Generated questions: {questions}")
        return serialize(questions)
    except Exception as e:
        logging.error(f"Error generating interview questions: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while generating interview questions")

# Route: provide-feedback
@app.post("/provide-feedback/")
async def provide_feedback(request: FeedbackRequest):
    try:
        feedback = assistant.provide_feedback(
            request.job_role,
            request.job_description,
            request.interview_question,
            request.candidate_answer
        )
        logging.debug(f"Feedback generated: {feedback}")
        return serialize(feedback)
    except Exception as e:
        logging.error(f"Error providing feedback: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while providing feedback")

# Route: solve-technical-problem
@app.post("/solve-technical-problem/")
async def solve_technical_problem(request: SolveProblemRequest):
    try:
        problem_solution = assistant.solve_technical_problem(request.criteria)
        logging.debug(f"Problem solution: {problem_solution}")
        return serialize(problem_solution)
    except Exception as e:
        logging.error(f"Error solving technical problem: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while solving technical problems")

# Route: handle-interview-question-flow
@app.post("/handle-interview-question-flow/")
async def handle_interview_question_flow(request: FeedbackRequest):
    try:
        interview_flow = assistant.handle_interview_question_flow(
            request.job_role,
            request.job_description,
            request.interview_question,
            request.candidate_answer
        )
        logging.debug(f"Interview flow: {interview_flow}")
        return serialize(interview_flow)
    except Exception as e:
        logging.error(f"Error handling interview question flow: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during interview question flow")

# Route: review-linkedin-profile
@app.post("/review-linkedin-profile/")
async def review_linkedin_profile():
    try:
        linkedin_feedback = assistant.review_linkedin_profile_and_provide_feedback()
        logging.debug(f"LinkedIn feedback: {linkedin_feedback}")
        return serialize(linkedin_feedback)
    except Exception as e:
        logging.error(f"Error reviewing LinkedIn profile: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while reviewing the LinkedIn profile")

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logging.error(f"Unhandled exception: {exc}")
    raise HTTPException(status_code=500, detail="An unexpected error occurred. Please try again later.")

# To run the app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
