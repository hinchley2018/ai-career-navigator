from fastapi import FastAPI
from pydantic import BaseModel
from InterviewAssistant import InterviewAssistant  # Import the modified InterviewAssistant class
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Initialize the InterviewAssistant
assistant = InterviewAssistant()

# Request models for different functionalities
class FeedbackRequest(BaseModel):
    job_role: str
    job_description: str
    interview_question: str
    candidate_answer: str

class LinkedInProfileRequest(BaseModel):
    profile_link: str

class JobDescriptionRequest(BaseModel):
    job_role: str
    job_description: str

class TechnicalProblemRequest(BaseModel):
    criteria: str

# Route to provide feedback on interview questions
@app.post("/provide-feedback/")
def provide_feedback(request: FeedbackRequest):
    feedback = assistant.provide_feedback(
        request.job_role,
        request.job_description,
        request.interview_question,
        request.candidate_answer
    )
    return {"result": feedback}

# Route to optimize LinkedIn profiles
@app.post("/optimize-linkedin/")
def optimize_linkedin_profile(request: LinkedInProfileRequest):
    optimization = assistant.review_linkedin_profile_and_provide_feedback(request.profile_link)
    return {"result": optimization}

# Route to generate interview questions
@app.post("/generate-questions/")
def generate_interview_questions(request: JobDescriptionRequest):
    questions = assistant.generate_interview_questions(
        request.job_role,
        request.job_description
    )
    return {"result": questions}

# Route to solve technical problems
@app.post("/solve-problem/")
def solve_technical_problem(request: TechnicalProblemRequest):
    solution = assistant.solve_technical_problem(request.criteria)
    return {"result": solution}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
