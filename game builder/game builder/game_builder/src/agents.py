from textwrap import dedent
from crewai import Agent
from model import GEMINI_LLM
   # switched from WATSONX_LLM to GEMINI_LLM


class GameAgents:
    def senior_engineer_agent(self):
        return Agent(
            role="Senior Software Engineer",
            goal="Create software as needed",
            backstory=dedent(
                """\
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise in programming in Python, and you always try to
                produce perfect, clean, and efficient code."""
            ),
            llm=GEMINI_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def qa_engineer_agent(self):
        return Agent(
            role="Software Quality Control Engineer",
            goal="Create perfect code by analyzing the code that is given for errors",
            backstory=dedent(
                """\
                You are a software engineer that specializes in checking code
                for errors. You have an eye for detail and a knack for finding
                hidden bugs.
                You check for missing imports, variable declarations, mismatched
                brackets and syntax errors.
                You also check for security vulnerabilities and logic errors."""
            ),
            llm=GEMINI_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role="Chief Software Quality Control Engineer",
            goal="Ensure that the code does the job it is supposed to do",
            backstory=dedent(
                """\
                You feel that programmers often do only half the job,
                so you are very dedicated to making high-quality, reliable code."""
            ),
            llm=GEMINI_LLM,
            allow_delegation=True,
            verbose=True,
        )
