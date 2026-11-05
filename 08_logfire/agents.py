from pydantic_ai import Agent
from pydantic_ai import RunContext
from model import nvidia_model
from depdencies import ClientDeps
from datetime import datetime
from pathlib import Path

# from pydantic_ai_harness.logfire import ManagedPrompt
from prompts import get_prompt


model = nvidia_model("nvidia/nemotron-3.5-super-vl-120b-a12b")

study_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=get_prompt("study_agent_instructions"),
)

career_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=get_prompt("career_agent_instructions"),
)

coach_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=get_prompt("coach_agent_instructions"),
)


@study_agent.instructions
def study_name(ctx: RunContext[ClientDeps]) -> str:
    return f"Student's name is {ctx.deps.name}. Address them by name"


@career_agent.instructions
def career_name(ctx: RunContext[ClientDeps]) -> str:
    return f"Person you are advising is {ctx.deps.name}. Address them by name"


@coach_agent.instructions
def coach_name(ctx: RunContext[ClientDeps]) -> str:
    return f"Client you are advicing is {ctx.deps.name}. Address them by name"


# delegation tools
@coach_agent.tool
async def ask_study_agent(ctx: RunContext[ClientDeps], question: str) -> str:
    """ask study specialist for advice on learning and studying"""
    result = await study_agent.run(question, deps=ctx.deps, usage=ctx.usage)
    return result.output


@coach_agent.tool
async def ask_career_agent(ctx: RunContext[ClientDeps], question: str) -> str:
    """ask career specialist for advice on what to choose for a career"""
    result = await career_agent.run(question, deps=ctx.deps, usage=ctx.usage)
    return result.output


@coach_agent.tool
def export_report(ctx: RunContext[ClientDeps], text: str):
    """exports the text to specified path"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exports_dir = Path("exports")
    exports_dir.mkdir(exist_ok=True)
    path = exports_dir / f"{ctx.deps.name.casefold()}_{timestamp}.md"
    path.write_text(text)
