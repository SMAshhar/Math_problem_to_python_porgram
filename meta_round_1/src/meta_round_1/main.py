#!/usr/bin/env python
import sys
from crew import MetaRound1Crew
from maker.maker import statement_maker

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

problem_statement = ("""
    You realize there might be a solution which only requires (N-1) lines (each also having a (P%) chance of being typed correctly). However, instead of thinking about that, you could also just type out the (N)-line solution more carefully to increase (P). How much would $P$ have to increase to yield the same chance of success as needing to type one fewer line of code?
    # Constraints
    (1 leq T leq 100)
    (2 leq N leq 1000)
    (1 leq P leq 99)
    # Input Format
    Input begins with an integer (T), the number of test cases. Each case is a single line containing the integers (N) and (P).
    # Output Format
    For the (i)th test case, print "Case #i: " followed by how much higher (P) would need to be to make spending your time typing carefully be as successful as typing one line fewer with your original (P).
    Your answer will be accepted if it is within an absolute or relative error of (10^-6).
    # Sample Explanation
    In the first case, you initially need to type (2) lines. You can either type just (1) line with a (50%) success rate, or you could improve your typing accuracy to (sqrt(50%) $approx$ 70.710678%), at which point you'd have a (sqrt(50%)^2 = 50%) chance of successfully typing the original (2) lines. So you would need to increase (P) by (70.710678 - 50 = 20.710678) for both approaches to have an equal chance of success.
""")
# the following statement uses
# with open("src/meta_round_1/test.md", 'r') as f:
#     problem_statement_1 = f.read()
    # problem_statement_1=problem_statement_1.replace('{', '(')
    # problem_statement_1=problem_statement_1.replace('}', ')')

full_statement = ''

with open ("./maker/statement.txt", "r") as f:
    full_statement = f.read()

with open("./maker/sample_in.txt", "r") as f:
    full_statement += "\nsample_input"
    full_statement += f.read()

with open("./maker/sample_out.txt", "r") as f:
    full_statement += "\nsample_output"
    full_statement += f.read()


problem_statement_1=statement_maker(full_statement=full_statement)

def run():
    """
    Run the crew.
    """
    inputs = {
        'problem':problem_statement_1
    }
    MetaRound1Crew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MetaRound1Crew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MetaRound1Crew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MetaRound1Crew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# run()