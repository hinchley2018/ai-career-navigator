from crewai import Agent, Task, Crew
from crewai_tools import SeleniumScrapingTool
from langchain_cohere import ChatCohere
import os

# Set API keys as environment variables
os.environ["COHERE_API_KEY"] = 'PPxvWZZnTGFueJoI8gbiel23rheor7mSwIrJ2PI8'

class InterviewAssistant:
    def __init__(self, link_to_profile):
        self.link_to_profile = link_to_profile
        # Initialize the language model
        self.llm = ChatCohere()

        # Initialize agents for different tasks
        self.question_generator_agent = Agent(
            role="Interview Question Generator",
            goal="Generate relevant and challenging interview questions based on the job role.",
            backstory=("You are an expert in interview preparation, tasked with generating a list of interview questions "
                       "based on the job description and requirements provided by the user. Your questions should be insightful, "
                       "challenging, and relevant to the job role."),
            verbose=True,
            llm=self.llm
        )

        self.resume_agent = Agent(
            role="Resume Screener",
            goal="Analyze resumes and provide feedback on relevance to the job role.",
            backstory="You are an expert in resume screening, tasked with evaluating resumes and providing feedback on their relevance to the job role.",
            verbose=True,
            llm=self.llm
        )

        self.feedback_agent = Agent(
            role="Interview Feedback Specialist",
            goal="Provide constructive and detailed feedback on interview answers.",
            backstory=("You are an expert in interview feedback, responsible for reviewing and providing feedback on answers "
                       "submitted by candidates. Your feedback should be thorough, constructive, and help candidates improve their responses."),
            verbose=True,
            llm=self.llm
        )

        self.linkedin_optimizer_agent = Agent(
            role="LinkedIn Profile Optimizer",
            goal="Provide suggestions to optimize LinkedIn profiles based on industry standards and best practices.",
            backstory=("You are an expert in LinkedIn profile optimization, tasked with analyzing profiles and providing actionable suggestions "
                       "to enhance visibility, professionalism, and effectiveness in showcasing skills and experience."),
            verbose=True,
            llm=self.llm
        )

        self.problem_solver_agent = Agent(
            role="Technical Problem Solver",
            goal="Generate and solve technical problems, and provide solutions or suggestions.",
            backstory=("You are an expert in technical problem-solving, responsible for generating technical problems, solving them, "
                       "and providing detailed explanations or suggestions for improvement."),
            verbose=True,
            llm=self.llm
        )

        self.interview_question_flow_agent = Agent(
            role="Interview Question Flow Specialist",
            goal="Handle a complete interview question flow including generating questions, evaluating answers, and providing feedback.",
            backstory=("You are an expert in managing the interview question flow. This involves generating relevant interview questions, "
                       "evaluating candidate answers, and providing detailed feedback to enhance the interview process."),
            verbose=True,
            llm=self.llm
        )

        # Initialize tasks for different functionalities
        self.question_generation_task = Task(
            description=("Generate a set of interview questions based on the following job role and description:\n"
                          "{job_role}\n"
                          "{job_description}\n\n"
                          "Ensure that the questions are relevant, challenging, and tailored to the job role."),
            expected_output=("A list of interview questions that are relevant and challenging based on the provided job role and description. "
                              "The questions should cover various aspects of the role and test different skills and knowledge."),
            agent=self.question_generator_agent
        )

        self.resume_feedback_task = Task(
            description="Analyze the provided resume and job description, and provide feedback on the candidate's relevance to the role. Here is the resume data: {resume_data}",
            expected_output="A detailed analysis of the resume, highlighting strengths, weaknesses, and relevance to the job role.",
            agent=self.resume_agent
        )

        self.feedback_task = Task(
            description=("Review the submitted answer for the following interview question:\n"
                           "{interview_question}\n\n"
                           "Provide detailed and constructive feedback on the answer submitted by the candidate. "
                           "Focus on areas of improvement, strengths, and how the answer can be enhanced."),
            expected_output=("Constructive and detailed feedback on the submitted answer, including suggestions for improvement, strengths, and how "
                              "the candidate can enhance their response."),
            agent=self.feedback_agent
        )

        self.linkedin_optimization_task = Task(
            description="Analyze the LinkedIn profile and provide suggestions for optimization. Here is the profile data: {profile_data}",
            expected_output="Actionable suggestions for enhancing the LinkedIn profile, including improvements to content, structure, and visibility.",
            agent=self.linkedin_optimizer_agent
        )

        self.problem_solving_task = Task(
            description="Generate a technical problem based on the given criteria and provide a detailed solution. Here are the criteria: {criteria}",
            expected_output="A technical problem with a detailed solution or explanation based on the provided criteria.",
            agent=self.problem_solver_agent
        )

        self.interview_question_flow_task = Task(
            description=("Handle the complete interview question flow including:\n"
                           "1. Generating questions based on job role and description.\n"
                           "2. Evaluating candidate answers.\n"
                           "3. Providing detailed feedback on the answers.\n"
                           "Job Role: {job_role}\n"
                           "Job Description: {job_description}\n"
                           "Interview Question: {interview_question}\n"
                           "Candidate Answer: {candidate_answer}"),
            expected_output=("A comprehensive handling of the interview question flow, including generated questions, evaluation of answers, "
                              "and detailed feedback on the candidate's responses."),
            agent=self.interview_question_flow_agent
        )

    def review_linkedin_profile_and_provide_feedback(self):
        text = SeleniumScrapingTool(self.link_to_profile).run()
        profile_input = {
            "profile_data": text
        }
        self.crew = Crew(
            agents=[self.linkedin_optimizer_agent],
            tasks=[self.linkedin_optimization_task],
            verbose=False
        )
        return self.crew.kickoff(inputs=profile_input)

    def generate_interview_questions(self, job_role, job_description):
        question_inputs = {
            "job_role": job_role,
            "job_description": job_description,
        }
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
        self.crew = Crew(
            agents=[self.feedback_agent],
            tasks=[self.feedback_task],
            verbose=False
        )
        return self.crew.kickoff(inputs=feedback_inputs)

    def solve_technical_problem(self, criteria):
        problem_inputs = {
            "criteria": criteria
        }
        self.crew = Crew(
            agents=[self.problem_solver_agent],
            tasks=[self.problem_solving_task],
            verbose=False
        )
        return self.crew.kickoff(inputs=problem_inputs)

# Example usage:
# assistant = InterviewAssistant("https://www.linkedin.com/in/example/")
# assistant.review_linkedin_profile_and_provide_feedback()
