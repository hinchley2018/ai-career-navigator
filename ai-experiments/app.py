from fastapi import FastAPI
from pydantic import BaseModel

# Assuming InterviewAssistant is a custom class you have defined in another module
from InterviewAssistant import InterviewAssistant  # Import the class

app = FastAPI()

# Initialize the InterviewAssistant with a LinkedIn profile or any other required data
assistant = InterviewAssistant("https://www.linkedin.com/in/umermehmood2762/")

class FeedbackRequest(BaseModel):
    job_role: str
    job_description: str
    interview_question: str
    candidate_answer: str

@app.post("/provide-feedback/")
def provide_feedback(request: FeedbackRequest):
    # Call the assistant's provide_feedback method and return the result
    feedback = assistant.provide_feedback(
        request.job_role,
        request.job_description,
        request.interview_question,
        request.candidate_answer
    )
    return {"result": feedback}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
