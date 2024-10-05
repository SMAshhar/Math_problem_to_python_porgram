# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import CodeInterpreterTool
from langchain_groq import ChatGroq


from typing import List

# Tools
import os
from utils import get_openai_api_key, get_serper_api_key, get_groq_api_key

# search_tool = SerperDevTool(
#     search_url="https://google.serper.dev/scholar",
#     n_results=2,
# )
# scrape_tool = ScrapeWebsiteTool()

tools: List[object] = [CodeInterpreterTool()]

# environment variables
open_ai_key = get_openai_api_key()
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'
os.environ['SERPER_API_KEY'] = get_serper_api_key()

groq_ai_key = get_groq_api_key()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=groq_ai_key
)


# Agent 
understand_problem = Agent(
    role='Understand Problem',
    goal=("Understand the problem statement and identify the key components and list them down" 
          "for the next agent to work upon. The question will be given as an statement clearly defining"
          "the *constraints*, *Input Format*, *Output Format* and *Sample Explanation*. You are to break down"
          "all the needs of the problem and list down them in an understandable format."
          
          "Here is an example of the problem that will be given to you::"
          
          "You've found a solution to an implementation-heavy geometry problem that requires typing out \(N\) lines of code. Annoyingly, you only have a \(P\%\) chance of typing out any given line without a mistake, and your code will only be accepted if all \(N\) lines are correct. The chance of making a mistake in one line is independent of the chance of making a mistake in any other line."

"You realize there might be a solution which only requires \(N-1\) lines (each also having a \(P\%\) chance of being typed correctly). However, instead of thinking about that, you could also just type out the \(N\)-line solution more carefully to increase \(P\). How much would $P$ have to increase to yield the same chance of success as needing to type one fewer line of code?"

"# Constraints"
"\(1 \leq T \leq 100\)"
"\(2 \leq N \leq 1{,}000\)"
"\(1 \leq P \leq 99\)"

"# Input Format"
"Input begins with an integer \(T\), the number of test cases. Each case is a single line containing the integers \(N\) and \(P\)."

"# Example Input Format"
"4"
"3 10"
"2 50"
"13 37"
"950 95"

"# Output Format"
"For the \(i\)th test case, print `Case #i:`  followed by how much higher \(P\) would need to be to make spending your time typing carefully be as successful as typing one line fewer with your original \(P\)."

"Your answer will be accepted if it is within an absolute or relative error of \(10^{-6}\)."

"# Sample Explanation"
"In the first case, you initially need to type \(2\) lines. You can either type just \(1\) line with a \(50\%\) success rate, or you could improve your typing accuracy to \(\sqrt{50\%} $\approx$ 70.710678\%\), at which point you'd have a \(\sqrt{50\%}^2 = 50\%\) chance of successfully typing the original \(2\) lines. So you would need to increase \(P\) by \(70.710678 - 50 = 20.710678\) for both approaches to have an equal chance of success."
          
          ),
    backstory=(
                "You are a Phd level Mathematician whose approach to"
                "handling tough mathematical problems and identiifying the core underlying needs"
                "is unmatched. You have a keen eye for detail and a passion for understanding the"
                "underlying principles and the underlying forces that lead to a problem solution."
                "You have a deep understanding of the mathematical theory and have a good"
                "understanding of the underlying principles and the underlying forces that lead to a"
                "problem solution. You are also a good communicator and a great problem solver."),
    # tools=tools,
    llm=llm,
    verbose=True,
    allow_delegation=False
)

design_algotrithem = Agent(
    role='Design Algorithem',
    goal=("""Design an algorithm using the given 'understand_problem_analysis' that can solve the given problem. The algorithm should be able to
          solve the problem by considering all the needs of the problem and the constraints mentioned
          in the problem statement. The algorithm should be able to handle all the edge cases and
          provide a solution that is as accurate as possible.
          """),
    backstory=("""
                You are a brilliant computer scientist with a deep passion for designing efficient algorithms. Known for your precision and ability to solve the most complex problems, 
               you have a strong foundation in data structures, algorithms, and mathematical problem-solving. Your vast experience 
                allows you to approach each problem methodically, breaking it down into manageable parts and analyzing the best possible approach to ensure accuracy and efficiency.
                Your greatest strength lies in your ability to develop solutions that not only meet all constraints but also handle edge cases that others might overlook. With an
                eye for optimization and a commitment to delivering perfect solutions, you approach each challenge with a blend of creativity and rigor.
                Given the understand_problem_analysis from a top-tier mathematician, you leverage your knowledge to craft algorithms that can tackle any 
               input, regardless of complexity. You are driven by a desire to create solutions that are not only correct but also efficient, scalable, and future-proof.
               """),
    # tools=tools,
    llm=llm,
    verbose=True,
    allow_delegation=False
) 

code_generation = Agent(
    role='Code Generation',
    goal=("""Generate a code snippet using available data in python of the problem statement that can solve the given problem.
          The code should be able to handle all the edge cases and provide a solution that is as accurate as possible.
          The code should be efficient and scalable. The code should be able to handle all the constraints mentioned
          in the problem statement. The code should be able to handle all the edge cases and provide a solution
          that is as accurate as possible.
          """),
    backstory=("""
                You are a seasoned software engineer with a deep passion for creating efficient and scalable code solutions. Known for your precision and ability to solve the most complex problems,
                you have a strong foundation in programming languages, algorithms, and software development. Your vast experience allows you to approach each problem methodically, breaking it down into manageable parts and analyzing the best possible approach to ensure accuracy and efficiency.
                Your greatest strength lies in your ability to develop solutions that not only meet all constraints but also handle edge cases that others might overlook. With an
                eye for optimization and a commitment to delivering perfect solutions, you approach each challenge with a blend of creativity and rigor.
                Given the understand_problem_analysis from a top-tier software engineer, you leverage your knowledge to craft code snippets that can tackle any input, regardless of complexity. You are driven by a desire to create solutions that are not only correct but also efficient, scalable, and future-proof.
                """),
    # tools=tools,
    llm=llm,
    verbose=True,
    allow_delegation=False
)

code_executor = Agent(
    role='Code Executor',
    goal=("""Execute the generated code snippet and provide the output for the given problem statement.
          The code should be able to handle all the edge cases and provide a solution that is as accurate as possible.
          The code should be efficient and scalable. The code should be able to handle all the constraints mentioned
          in the problem statement. The code should be able to handle all the edge cases and provide a solution
          that is as accurate as possible.
          """),
    backstory=("""
                You are a seasoned software engineer with a deep passion for creating efficient and scalable code solutions. Known for your precision and ability to solve the most complex problems,
                you have a strong foundation in programming languages, algorithms, and software development. Your vast experience allows you to approach each problem methodically, breaking it down into manageable parts and analyzing the best possible approach to ensure accuracy and efficiency.
                Your greatest strength lies in your ability to develop solutions that not only meet all constraints but also handle edge cases that others might overlook. With an
                eye for optimization and a commitment to delivering perfect solutions, you approach each challenge with a blend of creativity and rigor.
                Given the understand_problem_analysis from a top-tier software engineer, you leverage your knowledge to craft code snippets that can tackle any input, regardless of complexity. You are driven by a desire to create solutions that are not only correct but also efficient, scalable, and future-proof.
                """),
    tools=[CodeInterpreterTool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)


# Task
understand_problem_task = Task(
    description="""
    Analyze the given {problem} statement to identify and extract all relevant components for the next stages of processing.
    You are required to:
    1. Parse the *constraints* provided in the {problem} to define the boundaries within which the solution must operate.
    2. Identify the *input format* specifications, including the types and structure of data that will be provided.
    3. Define the *output format* based on the {problem} requirements, ensuring that it aligns with the specified solution expectations.
    4. Break down the {problem} into key steps that will be handled in subsequent stages.
    5. Provide detailed explanations or clarifications on any ambiguities in the {problem} statement.
    6. Consider edge cases and potential issues that might arise in the solution process and document them for later agents.
    """,
    expected_output="""
    A well-structured and detailed breakdown of the {problem} that includes:
    1. A clear list of constraints.
    2. A description of the input format with examples.
    3. A description of the expected output format with examples.
    4. A list of steps for solving the {problem}, organized for further agents to implement.
    5. A list of edge cases and ambiguous areas to be addressed in future stages.
    6. A .md file carrying all this detail
    """,
    # tools=tasks['planning']['tools'],
    output_file="understanding.md",
    async_execution=False,  # Synchronous execution for better coordination
    agent=understand_problem  # Assigning the 'understand_problem' agent to execute this task
)


design_algorithm_task = Task(
    description="""
    Design an efficient algorithm that can solve the given problem based on the 'understand_problem_task'. 
    The task requires you to:
    1. Review the 'understand_problem_task' thoroughly and extract the key constraints, input/output format, and edge cases.
    2. Identify and define the core logic and steps necessary to solve the problem efficiently while adhering to the constraints.
    3. Ensure the algorithm can handle all edge cases and minimize the time and space complexity.
    4. Develop a solution that is scalable and works across varying input sizes, ensuring it provides accurate results under all possible scenarios.
    5. Optimize the algorithm by leveraging the appropriate data structures, mathematical models, and techniques.
    6. Provide an explanation of how the algorithm handles the different edge cases, constraints, and performs under typical as well as extreme conditions.
    """,
    expected_output="""
    A detailed algorithm that:
    1. Precisely addresses the problem using the 'understand_problem_task'.
    2. Includes pseudocode or a high-level flowchart of the core steps involved in solving the problem.
    3. A description of the chosen approach, including justifications for the data structures and optimization techniques used.
    4. A well-explained handling of edge cases and constraints.
    5. An analysis of the time and space complexity of the algorithm.
    6. A final Python implementation ready for testing and deployment.
    """,
    # tools=tasks['implementation']['tools'],  # Specify if particular tools are needed for implementation
    async_execution=False,  # Synchronous task execution
    context=[understand_problem_task],
    agent=design_algotrithem  # Linking the 'design_algorithm' agent to execute this task
)


code_generation_task = Task(
    description="""
    Generate a Python code solution for the problem statement using the data provided from the 'understand_problem_analysis' and 'design_algorithm'. The task requires you to:
    1. Review the 'understand_problem_analysis' and the algorithmic solution provided by the 'design_algorithm' agent.
    2. Translate the designed algorithm into an efficient and scalable Python code snippet.
    3. Ensure that the code is well-structured, adheres to best practices, and is easily understandable.
    4. Handle all edge cases as specified in the problem statement and ensure the solution works under the constraints.
    5. Optimize the code for performance, keeping the time and space complexity to a minimum.
    6. Provide inline comments to explain the logic behind critical sections of the code.
    7. Test the generated code against sample inputs and outputs to ensure correctness.
    """,
    expected_output="""
    A Python code solution that:
    1. Follows the algorithm designed in the 'design_algorithm' task.
    2. Is well-documented with comments and adheres to Pythonic conventions (PEP8).
    3. Efficiently handles all constraints and edge cases specified in the problem statement.
    4. Provides a clear and scalable solution that can handle large inputs effectively.
    5. Includes sample test cases to demonstrate the correctness of the code.
    """,
    # tools=tasks['testing']['tools'],  # Tools if necessary for testing or further integration
    async_execution=False,  # The code generation task is synchronous for accuracy
    context=[understand_problem_task, design_algorithm_task],
    agent=code_generation,  # Assigning the 'code_generation' agent to execute this task
    output_file="solution.py"
)


# Task
code_executor_task = Task(
    description="""
    Execute the Python code snippet generated by the 'code_generation' agent using the 'CodeInterpreterTool' and provide the results. The task involves:
    1. Loading the Python code provided by the 'code_generation' agent.
    2. Using the CodeInterpreterTool to run the code and capture the output.
    3. Ensure that the code handles all edge cases, constraints, and is scalable for larger input sizes.
    4. Evaluate the correctness of the code output based on the problem statement's expected results.
    5. Capture any errors or exceptions and return them as part of the output, with suggestions for potential debugging steps if necessary.
    """,
    expected_output="""
    1. The correct solution output for the problem, based on the inputs provided to the code.
    2. Error or exception details, if any, during the execution, with helpful insights on debugging.
    3. Performance statistics (optional) such as runtime and memory usage, if required.
    """,
    context=[code_generation_task],
    tools=[CodeInterpreterTool],  # Using the CodeInterpreterTool for execution
    async_execution=False,  # Task should be synchronous for accurate output
    agent=code_executor  # Assigning the 'code_executor' agent to execute this task
)

math_crew = Crew(
    agents=[understand_problem, design_algotrithem, code_generation, code_executor],
    tasks=[understand_problem_task, design_algorithm_task, code_generation_task, code_executor_task],
    verbose=True,
)

def solving_math (problem:str):
    return math_crew.kickoff(inputs=problem)
    
solving_math(
"""You’ve found a solution to an implementation-heavy geometry problem that requires typing out \(N\) lines of code. Annoyingly, you only have a \(P\%\) chance of typing out any given line without a mistake, and your code will only be accepted if all \(N\) lines are correct. The chance of making a mistake in one line is independent of the chance of making a mistake in any other line.

You realize there might be a solution which only requires \(N-1\) lines (each also having a \(P\%\) chance of being typed correctly). However, instead of thinking about that, you could also just type out the \(N\)-line solution more carefully to increase \(P\). How much would $P$ have to increase to yield the same chance of success as needing to type one fewer line of code?

# Constraints
\(1 \leq T \leq 100\)
\(2 \leq N \leq 1{,}000\)
\(1 \leq P \leq 99\)

# Input Format
Input begins with an integer \(T\), the number of test cases. Each case is a single line containing the integers \(N\) and \(P\).

# Output Format
For the \(i\)th test case, print "`Case #i:` " followed by how much higher \(P\) would need to be to make spending your time typing carefully be as successful as typing one line fewer with your original \(P\).

Your answer will be accepted if it is within an absolute or relative error of \(10^{-6}\).

# Sample Explanation
In the first case, you initially need to type \(2\) lines. You can either type just \(1\) line with a \(50\%\) success rate, or you could improve your typing accuracy to \(\sqrt{50\%} $\approx$ 70.710678\%\), at which point you'd have a \(\sqrt{50\%}^2 = 50\%\) chance of successfully typing the original \(2\) lines. So you would need to increase \(P\) by \(70.710678 - 50 = 20.710678\) for both approaches to have an equal chance of success.
"""
)