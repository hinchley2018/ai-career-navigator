from crewai import Agent, Task, Crew
from langchain_cohere import ChatCohere
import os

# Set API keys as environment variables
os.environ["COHERE_API_KEY"] = 'PPxvWZZnTGFueJoI8gbiel23rheor7mSwIrJ2PI8'

class InterviewAssistant:
    def __init__(self):
        # Initialize the language model
        self.llm = ChatCohere()
        
        # Initialize agents
        self.question_generator_agent = Agent(
            role="Interview Question Generator",
            goal="Generate relevant and challenging interview questions based on the job role.",
            backstory=(
                "You are an expert in interview preparation, tasked with generating a list of interview questions "
                "based on the job description and requirements provided by the user. Your questions should be insightful, "
                "challenging, and relevant to the job role."
            ),
            verbose=True,
            llm=self.llm
        )
        
        self.feedback_agent = Agent(
            role="Interview Feedback Specialist",
            goal="Provide constructive and detailed feedback on interview answers.",
            backstory=(
                "You are an expert in interview feedback, responsible for reviewing and providing feedback on answers "
                "submitted by candidates. Your feedback should be thorough, constructive, and help candidates improve their responses."
            ),
            verbose=True,
            llm=self.llm
        )
        
        # Initialize tasks
        self.question_generation_task = Task(
            description=(
                "Generate a set of interview questions based on the following job role and description:\n"
                "{job_role}\n"
                "{job_description}\n\n"
                "Ensure that the questions are relevant, challenging, and tailored to the job role."
            ),
            expected_output=(
                "A list of interview questions that are relevant and challenging based on the provided job role and description. "
                "The questions should cover various aspects of the role and test different skills and knowledge."
            ),
            agent=self.question_generator_agent
        )
        
        self.feedback_task = Task(
            description=(
                "Review the submitted answer for the following interview question:\n"
                "{interview_question}\n\n"
                "Provide detailed and constructive feedback on the answer submitted by the candidate. "
                "Focus on areas of improvement, strengths, and how the answer can be enhanced."
            ),
            expected_output=(
                "Constructive and detailed feedback on the submitted answer, including suggestions for improvement, strengths, and how "
                "the candidate can enhance their response."
            ),
            agent=self.feedback_agent
        )
        
    
    
    def generate_interview_questions(self, job_role, job_description):
        question_inputs = {
            "job_role": job_role,
            "job_description": job_description,
        }
            # Initialize Crew instance
        self.crew = Crew(
            agents=[self.question_generator_agent],
            tasks=[self.question_generation_task],
            verbose=False
        )
        return self.crew.kickoff(inputs=question_inputs)
    
    def provide_feedback(self, job_role, job_description, interview_question, candidate_answer):
        feedback_inputs = {
            "job_role": job_role,
            "job_description": job_description,
            "interview_question": interview_question,
            "candidate_answer": candidate_answer
        }
            # Initialize Crew instance
        self.crew = Crew(
            agents=[self.feedback_agent],
            tasks=[self.feedback_task],
            verbose=False
        )
        return self.crew.kickoff(inputs=feedback_inputs)

# Example usage
if __name__ == "__main__":
    assistant = InterviewAssistant()
    
    # Generate interview questions
    questions = assistant.generate_interview_questions(
        job_role="Software Engineer",
        job_description="Responsible for developing and maintaining software applications, participating in code reviews, and collaborating with cross-functional teams.",
    )
    print(questions)
    # Provide feedback on an answer
    feedback = assistant.provide_feedback(
        job_role="Software Engineer",
        job_description="Responsible for developing and maintaining software applications, participating in code reviews, and collaborating with cross-functional teams.",
        interview_question=str(questions),
        candidate_answer="I worked on a project where we had tight deadlines and limited resources. I overcame the obstacles by prioritizing tasks, working closely with the team, and finding creative solutions to manage the resources effectively."
    )
