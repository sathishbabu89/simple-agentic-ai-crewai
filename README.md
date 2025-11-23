# simple-agentic-ai-crewai
A simple Streamlit app that demonstrates how Agentic AI can break down tasks into manageable subtasks, aimed at helping new learners understand the basics of Agentic AI.

### 1. **GitHub Repository Setup**

### 2. **README.md**

````markdown
# Simple Agentic AI Task Decomposition

## Overview
This is a simple **Agentic AI** powered app built using **Streamlit** and **CrewAI** to demonstrate how tasks can be broken down into smaller, actionable steps. This app is perfect for anyone who wants to understand the basics of how Agentic AI works and how it can be applied to real-world tasks.

### Features:
- Input a high-level task.
- See how **Agentic AI** breaks down the task into smaller steps or subtasks.
- View the raw response directly from the **DeepSeek** LLM model.

## Requirements
To run the app locally, you need to have the following installed:
- Python 3.7 or above
- Streamlit
- CrewAI
- DeepSeek API key

### Installation Steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/simple-agentic-ai-task-decomposition.git
   cd simple-agentic-ai-task-decomposition
````

2. **Install dependencies:**

   Ensure you have a Python virtual environment (optional but recommended). Then install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   You need to create a `.env` file with the following keys:

   ```bash
   DEVZERO_LLM_MODEL=deepseek-chat
   DEEPSEEK_API_KEY=your_deepseek_api_key
   DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
   DEVZERO_TEMPERATURE=0.3
   ```

   Replace `your_deepseek_api_key` with your actual DeepSeek API key.

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at `http://localhost:8501`.

## Usage

* Enter a task (e.g., "Explain Kafka") in the text input box.
* Click the "Decompose Task" button.
* View the raw response showing how the task has been broken down into subtasks.

## Example Input & Output

### Input:

**Task**: Explain Kafka

### Output:

**Decomposed Subtasks (Raw Response):**

```
1. Establish the Core Problem & Analogy
2. Define Kafka's Core Purpose and Architecture
3. Deep Dive into Key Concepts & Terminology
4. Demonstrate Core Capabilities with a Simple Example
5. Discuss the Broader Ecosystem & Use Cases
6. Summarize and Provide a Final Takeaway
```

## Contributing

Feel free to fork the repository, make improvements, and create pull requests. Contributions are always welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

* [Streamlit](https://streamlit.io/)
* [CrewAI](https://www.crewai.com/)
* [DeepSeek](https://www.deepseek.com/)

````

### 3. **Other Files to Include**

- **requirements.txt**: This file will include the dependencies for your project.

```text
streamlit
crewai
requests
````

* **.gitignore**: To ignore unnecessary files such as `.env` and virtual environment folders.

```text
*.pyc
__pycache__/
.env
venv/
```

### 4. **Repository Setup**:

1. Create the repository on GitHub.
2. Clone the repository to your local machine.
3. Add your files (`app.py`, `README.md`, `requirements.txt`, `.gitignore`).
4. Commit and push the changes to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-username>/simple-agentic-ai-task-decomposition.git
git push -u origin master
```

---

Let me know if you'd like to adjust any part of this setup or need further assistance with the GitHub repository!

