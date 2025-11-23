import streamlit as st
import os
from crewai import Agent, Task, LLM
from textwrap import dedent

# Configure the LLM (DeepSeek)
llm = LLM(
    model=os.getenv("DEVZERO_LLM_MODEL", "deepseek-chat"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
    temperature=float(os.getenv("DEVZERO_TEMPERATURE", "0.3")),
)

# Initialize a simple Agent for task decomposition
agent = Agent(
    role="Simple Task Decomposer",
    goal="Break down a task into smaller, manageable steps.",
    backstory=dedent("""\
        You are a task decomposer.
        Your job is to take a high-level task and break it down into smaller, manageable subtasks.
        For example, if the task is 'Make a cup of tea,' you will break it down into steps like 'Boil water,' 'Steep tea,' etc.
    """),
    llm=llm
)

# Function to decompose the task using LLM
def decompose_task(agent, task_name):
    # Create the task object with the required fields: description and expected_output
    task = Task(
        name=task_name,
        description=f"Break down the task '{task_name}' into smaller steps",
        expected_output="A list of subtasks that can be followed to complete the main task."
    )
    
    # Generate the prompt to decompose the task using the LLM
    prompt = f"Please break down the task '{task_name}' into smaller steps or subtasks."
    
    # Use the agent's LLM to get a response
    response = agent.llm.call(prompt)  # Correct method for LLM completion
    
    # Return the response from LLM, splitting by newlines to get subtasks
    if response:
        return response.split('\n')  # Assuming LLM returns subtasks as newline-separated
    else:
        return ["Task decomposition not available"]

# Streamlit UI for task input
st.title("Simple Agentic AI Task Decomposition App")
st.write("Provide a task, and see how Agentic AI breaks it down into smaller steps!")

# User input for task
task_name = st.text_input("Enter a task", "")

# Button to decompose the task
if st.button("Decompose Task"):
    if task_name:
        # Use the Agent to decompose the task using LLM
        subtasks = decompose_task(agent, task_name)

        # Display the task and its decomposed subtasks
        st.write(f"Task: **{task_name}**")
        st.write("Decomposed Subtasks:")
        
        # Display raw response text as output
        st.text("\n".join(subtasks))  # Display the subtasks list as raw text
        
        # Optionally, you could list each subtask if desired
        # for idx, subtask in enumerate(subtasks, 1):
        #     st.write(f"{idx}. {subtask}")
    else:
        st.warning("Please enter a task to decompose.")
