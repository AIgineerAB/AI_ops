# Exercise 0 - PydanticAI and OpenRouter

In this exercise, you get to work with data validation using Pydantic v2 and PydanticAI. Output in general from LLMs are unstructured and hard to work with, to get any value from it you need to structure the output and validate its contents. This can be done with Pydantic.

## 0. Summarize job ads

In the data folder, there are a few job ads taken from arbetsförmedlingen.se.

a) Read all the jobs ads into python

b) Create a function that uses PydanticAI agent to summarize a job ad. This function should take in an ad as its parameter and return a summary.

c) Now create and export markdown files for each job ad and its corresponding summary.

d) Try to take other job ads from arbetsförmedlingen.se and see how well your function performs.

e) Make the output structured using a pydantic model together with PydanticAI agent. The output from the agent should have the following fields:

- job_title
- description
- summary
- responsibilities
- words_in_article

## 1. Product extractor

In this task you will based on product descriptions, be able to extract out relevant information into structured format using pydantic model together with PydanticAI agent.

a) Read the `products.json` and store all of its descriptions into a list

b) Loop through this list and extract structured output from each of the descriptions. The structure should have the fields: name, price, category, in_stock and description

c) Now try to validate programmatically if the output fields are correct.

> [!NOTE]
> some of the fields might be straightforward as some others might require the use of another LLM agent

## 2. Sentiment analysis

You will use agent here to determine if a review is positive, negative or neutral for a set of reviews.

a) Read in `reviews.json` and extract all texts and store it in a list

b) Iterate your list and use an agent to give a sentiment.

For the tasks below, remember what you've learnt from classical machine learning on how to validate prediction against ground truth. Note that here you might need to calculate them yourself.

c) Now validate how many correct you got and compute the accuracy.

d) Also compute recall and precision.

e) Create a confusion matrix.

## 3. A grading assistant

Teachers in general have a lot of administrations to do and one of those things is grading. Can we create a simple grade assistant to assist a Swedish teacher in grading? This exercise focuses a lot in prompt engineering and afterwards to postprocess the output using Pydantic.

> [!NOTE]
> this task is easier if you know Swedish. If you don't know Swedish you could adapt it to other language, but need to find other data, or you could use LLM to translate the data into English.

a) [Go into this page with examples of students answers](https://www.uu.se/download/18.11971c6f1989761a6625867/1755009079925/Svsva%20Niv%C3%A5%201%20Del%20C%20Resonerande%20uppgift,%20matris,%20analys.pdf) to a particular question. Copy some example texts and paste it into files with names like `student_text_1.txt`, `student_text_2.txt`.

b) Read these data into python and tell your LLM to grade them.

c) Make structured output with fields proposed_grade, motivation and improvements.

d) Output a folder with the following txt files: proposed_grade.txt, motivation.txt and improvements.txt

e) In the data folder there is a file called svenska1_criterias.txt and copy "Betygskriterier" for "Svenska 1". These are the criterias for the different grades. Read these into Python and use them for f).

f) Now repeat b)-e) but with the criterias in your prompt as well. Can you see any differences in the outputs?

g) Can you improve the output quality by providing few shot examples?

## 4. Theory questions

a) Explain the primary purpose of Pydantic. What core problems does it solve for developers?

b) In Pydantic, what is the key difference between using model_validate() and model_validate_json()? When would you use each one?

c) How can you define a field in a Pydantic model that has a specific value constraint, such as a minimum or maximum number? Give an example.

d) Describe how Pydantic plays a role in PydanticAI agents

e) What is a computed field in Pydantic?

f) What are tokens in LLMs?

g) What are few shot examples?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology        | explanation |
| ------------------ | ----------- |
| few shot learning  |             |
| token              |             |
| context window     |             |
| pydantic           |             |
| BaseModel          |             |
| Field              |             |
| model_fields       |             |
| computed_field     |             |
| model_validate     |             |
| model_dump         |             |
| type hinting       |             |
| serialization      |             |
| deserialization    |             |
| prompt engineering |             |
| zero-shot learning |             |
| OpenRouter         |             |
| Agent              |             |
| system prompt      |             |
| agent.run          |             |
|                    |             |
