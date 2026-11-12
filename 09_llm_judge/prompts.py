import logfire
from logfire import VariablesOptions
import os
from dotenv import load_dotenv

load_dotenv()

logfire.configure(
    api_key=os.environ["LOGFIRE_PROMPTS"],  # requires project:read_variables
    variables=VariablesOptions(),
)


def get_prompt(
    name: str, default: str = "be a jokey assistant", label: str = "production"
):
    prompt = logfire.var(
        name=f"prompt__{name}",
        type=str,
        default=default,
    )
    prompt.refresh_sync(force=True)
    resolved = prompt.get(label=label)
    print(resolved.version, resolved.label)
    return resolved.value


if __name__ == "__main__":
    print(get_prompt("coach_agent_instructions"))
