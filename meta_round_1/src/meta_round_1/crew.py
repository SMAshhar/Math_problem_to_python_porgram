from crewai import Agent, Crew, Process, Task
from crewai import LLM
from crewai.project import CrewBase, agent, crew, task


# from meta_round_1.utils import get_groq_api_key

# Uncomment the following line to use an example of a custom tool
# from meta_round_1.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# groq_ai_key = get_groq_api_key()

# llm = LLM(
#     model="llama-3.1-70b-versatile",
#     api_key=groq_ai_key,
#     base_url='https://api.groq.com',
#     temperature=0.7
# )

@CrewBase
class MetaRound1Crew():
	"""MetaRound1 crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def phd_mathematician(self) -> Agent:
		return Agent(
			config=self.agents_config['phd_mathematician'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def computer_scientist(self) -> Agent:
		return Agent(
			config=self.agents_config['computer_scientist'],
			verbose=True
		)
	@agent
	def computer_programmer(self) -> Agent:
		return Agent(
			config=self.agents_config['computer_programmer'],
			verbose=True
		)
	@agent
	def code_interpretor(self) -> Agent:
		return Agent(
			config=self.agents_config['code_interpretor'],
			verbose=True
		)

	@task
	def understand_problem_task(self) -> Task:
		return Task(
			config=self.tasks_config['understand_problem_task'],
		)

	@task
	def design_algorithm_task(self) -> Task:
		return Task(
			config=self.tasks_config['design_algorithm_task'],
			output_file='report.md'
		)

	@task
	def code_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['code_generation_task'],
		)

	@task
	def code_executor_taskk(self) -> Task:
		return Task(
			config=self.tasks_config['code_executor_taskk'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MetaRound1 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=False
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)