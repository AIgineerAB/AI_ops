# Exercise 1 - PydanticAI, FastAPI 

In this exercise, you get to work with fastapi to serve PydanticAI models to different endpoints and then consume these endpoints. 

## 0. PydanticAI fundamentals

Make a PydanticAI model that can take an input of a location and then it should suggest 5 restaurants nearby that place. The restaurant model should have

- name
- type of food (cuisine)
- price level
- rating
- short description
- opening hours
- location

It's okay if your model is making up a restaurant that doesn't exist

## 1. FastAPI to serve PydanticAI

Now make a fastapi with a post endpoint in natural language to prompt for a location and what type of food. Based on these it should generate a restaurant and store it in a duckdb database.

Also implement a get endpoint for showing all restaurants in the database. Implement a simple frontend in for example streamlit to consume this API.

## 2. A pedagogical programming bot

Create a chatbot that is specialized in helping out with programming tasks. It should answer shortly, so not spoonfeeding with long answers, and it should be socratic, that is always ask follow up questions rather than giving the answer.


## Theory questions

a) What problem does PydanticAI solve when using LLMs?

b) Why is schema validation critical in LLM-based systems?

c) What risks exist if retries are unlimited?

d) How can FastAPI be used to serve PydanticAI? Give an example



## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology          | explanation |
| -------------------- | ----------- |
| tools                |             |
| dependencies         |             |
| output_type          |             |
| dependency injection |             |
| request body         |             |
| response model       |             |
| pydantic model       |             |
| Agent                |             |
| output_type          |             |
| model                |             |
| run                  |             |
| system prompt        |             |
| retry loop           |             |
| tool call            |             |
| messages             |             |
