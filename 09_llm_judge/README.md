# LLM Judge in Pydantic Logfire

<a href="https://youtu.be/5Vpf_PV2vA8" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/ai_engineering/llm_judge.png?raw=true" alt="llm judge" width="600">
</a>



## Setup

Create an account and sign into [logfire](https://logfire-eu.pydantic.dev/login?from=%2Fsignup)

```bash
uv add logfire
uv run logfire auth
uv add "logfire[variables]"
uv add "logfire[system-metrics]"
```

## Concepts

- span - most atomic unit of work (name, start and duration) e.g. http request, database question, internal calculation
- trace - tree of spans -> parent/child path for one request
- metric - value measured over time e.g. latency, CPU load, queue length
- log - timestamped record of a single event witn no duration

## Read more

From logfire documentation

- [send first trace](https://pydantic.dev/docs/logfire/get-started/first-trace/)
- [prompt management overview](https://pydantic.dev/docs/logfire/prompt-management/)
- [prompt management concepts](https://pydantic.dev/docs/logfire/prompt-management/concepts/)
- [use prompts in your applications](https://pydantic.dev/docs/logfire/prompt-management/concepts/)
