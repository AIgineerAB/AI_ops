# Dockerize RAG

<a href="" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/ai_engineering/.png?raw=true" alt="dockerize rag" width="600">
</a>

## Setup 

We take the base code from 11_rag but put it into two different packages so that we can separate installations for respective docker containers. 

Start up a new project and then create two packages 

```bash
uv init --no-package --python 3.13
uv init --package backend 
uv init --package frontend
```

Then add the dependencies in each of the `pyproject.toml`. You can take a look at the different pyprojects of this lecture. When that is done do 

```bash
uv sync --all-packages
```

## Logfire

To setup logfire 
1. create a project called ragbit
2. run this 
  
```bash
uv run logfire projects use ragbit
```

3. install logfire for fastapi 

```bash
uv add "logfire[fastapi]"
```

4. You also need to get a write token in logfire. Go into security and access -> write tokens -> new write token
5. Add it to your .env, which your docker-compose.yaml will inject into the running container. You need to name it LOGFIRE_TOKEN for logfire.configure() to automatically pick up

```bash
LOGFIRE_TOKEN=<your write token>
```
