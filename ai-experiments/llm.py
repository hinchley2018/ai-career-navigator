from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama
import os
import chainlit as cl
from dotenv import load_dotenv

# Initialize the Ollama model
llm = ChatOllama(model="llama3.1", base_url="http://localhost:11434")

# Prompt template for generating interview questions
question_prompt_template = """
Generate a set of interview questions based on the following job role and description:
Job Role: {job_role}
Job Description: {job_description}

Ensure that the questions are relevant, challenging, and tailored to the job role.
"""

# Prompt template for providing feedback
feedback_prompt_template = """
Review the submitted answer for the following interview question:
Interview Question: {interview_question}
Candidate Answer: {candidate_answer}

Provide detailed and constructive feedback on the answer. Focus on areas of improvement, strengths, and how the answer can be enhanced.
"""

# Agent for generating interview questions
question_generator_agent = Agent(
    role="Interview Question Generator",
    goal="Generate relevant and challenging interview questions based on the job role.",
    backstory=(
        "You are an expert in interview preparation, tasked with generating a list of interview questions "
        "based on the job description and requirements provided by the user. Your questions should be insightful, "
        "challenging, and relevant to the job role."
    ),
    verbose=True,
    llm=llm  # Attach the Ollama model
)

# Agent for providing feedback on answers
feedback_agent = Agent(
    role="Interview Feedback Specialist",
    goal="Provide constructive and detailed feedback on interview answers.",
    backstory=(
        "You are an expert in interview feedback, responsible for reviewing and providing feedback on answers "
        "submitted by candidates. Your feedback should be thorough, constructive, and help candidates improve their responses."
    ),
    verbose=True,
    llm=llm  # Attach the Ollama model
)

# Task for generating interview questions
question_generation_task = Task(
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
    agent=question_generator_agent,
)

# Task for providing feedback on answers
feedback_task = Task(
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
    agent=feedback_agent,
)

# Initialize the Crew instance
crew = Crew(
    agents=[question_generator_agent],
    tasks=[question_generation_task],
    verbose=True
)

# Define inputs for generating interview questions
question_inputs = {
    "job_role": "Software Engineer",
    "job_description": "Responsible for developing and maintaining software applications, participating in code reviews, and collaborating with cross-functional teams."
}

# Generate interview questions
question_result = crew.kickoff(inputs=question_inputs)
print("Generated Interview Questions:\n", question_result)

# Define inputs for providing feedback on an answer
feedback_inputs = {
    "interview_question": "Describe a challenging project you worked on and how you overcame obstacles.",
    "candidate_answer": "I worked on a project where we had tight deadlines and limited resources. I overcame the obstacles by prioritizing tasks, working closely with the team, and finding creative solutions to manage the resources effectively."
}

# Provide feedback on the candidate's answer
feedback_result = crew.kickoff(task=feedback_task, inputs=feedback_inputs)
print("Feedback on the Submitted Answer:\n", feedback_result)

# Chainlit integration for interactive guidance
@cl.on_chat_start
async def main():
    # Sending a welcome message
    await cl.Message(content="Hello there, I am your guide for preparing interview questions and providing feedback. Ask me how to generate interview questions or provide feedback on answers, and I'll assist you. How can I help you today?").send()

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm)

@cl.on_message
async def on_message(message: cl.Message):
    # Extract the text from the message object
    user_message_text = message.content

    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")

    # Call the chain asynchronously
    res = await llm_chain.acall({"question": user_message_text}, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Extract the response text
    response_text = res["text"]

    # Send the response
    await cl.Message(content=response_text).send()
