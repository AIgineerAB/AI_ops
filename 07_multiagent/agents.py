from pydantic_ai import Agent
from pydantic_ai import RunContext
from model import nvidia_model
from depdencies import ClientDeps
from datetime import datetime
from pathlib import Path

model = nvidia_model("nvidia/nemotron-3.5-super-vl-120b-a12b")

study_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a study expert. Give concrete study plans and learning techniques."
    ),
)

career_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a career advisor. Give practical advice on jobs, resumes, and career paths.",
    ),
)

coach_agent = Agent(
    model=model,
    deps_type=ClientDeps,
    instructions=(
        "You are a personal coach. Follow these steps IN ORDER:\n"
        "1. Call `ask_study_agent` for study questions.\n"
        "2. Call `ask_career_agent` for career questions.\n"
        "3. Combine the answers into ONE short, simple response.\n"
        "4. Call `export_report` with that final response as `text`.\n"
        "5. Reply to the user with the final response."
    ),
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