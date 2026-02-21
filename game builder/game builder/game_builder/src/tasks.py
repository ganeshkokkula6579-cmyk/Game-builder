from textwrap import dedent
from crewai import Task


class GameTasks:
    def code_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are a Senior Software Engineer tasked with creating a game in Python.

                Instructions
                ------------
                {game}

                Requirements
                ------------
                - Write clean, efficient, and well-structured Python code.
                - Include all necessary imports.
                - Do not add explanations or comments in the final output.
                - Output ONLY the full Python code, nothing else.
                """
            ),
            agent=agent,
            expected_output="Full working Python code for the game",
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are a QA Engineer reviewing Python game code.

                Instructions
                ------------
                {game}

                Review Criteria
                ---------------
                - Fix any syntax errors, logic errors, or runtime issues.
                - Add any missing imports or variable declarations.
                - Fix mismatched brackets and indentation errors.
                - Check for basic security vulnerabilities.
                - Ensure the game runs without crashing.

                Your final answer must be the corrected Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Reviewed and corrected Python game code",
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are the Chief QA Engineer ensuring the Python game is production-ready.

                Instructions
                ------------
                {game}

                Evaluation Criteria
                -------------------
                - Verify the code is complete and functional.
                - Confirm it meets the described mechanics.
                - Ensure no missing parts (imports, variables, functions).
                - Output ONLY the final, correct Python code with no extra explanations.

                """
            ),
            agent=agent,
            expected_output="Final validated Python game code",
        )
