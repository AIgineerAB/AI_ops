# LLM introduction


**part 1 - General theory about LLM**

<a href="https://youtu.be/Ei66WLCs0aw" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/machine_learning/llm_theory.png?raw=true" alt="theory of how LLM works" width="600">
</a>


<br>


<br>

**part 2 - Working with OpenRouter API**

<a href="https://youtu.be/LiwYZ1wbjNk" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/ai_engineering/openrouter_intro.png?raw=true" alt="openrouter and pydanticai" width="600">
</a>

> [!NOTE]
> models come and go quite quickly in OpenRouter, some may change their billing, some could be rate limited upstreams or other reasons you can't use the models. The easiest solution here is to check for another model and use that instead

- OpenRouter
- LLM 


## Setup OpenRouter

Go into [openrouter.ai/pricing](https://openrouter.ai/pricing) and click "Get Started For Free" and follow the instructions to sign up.

<img src="https://github.com/kokchun/assets/blob/main/ai_engineering/openrouter_free.png?raw=true" alt="sign up for free" width="400">


You could use your github account or gmail to sign up. 

<img src="https://github.com/kokchun/assets/blob/main/ai_engineering/openrouter_api_key.png?raw=true" alt="getting API key" width="400">

Create an API key and remember to copy it directly as it will only show once for you.

Now create a .env and add the following line 

```
OPENROUTER_API_KEY=<your-api-key>
```

If you name it OPENROUTER_API_KEY, then pydanticai Agent that we'll use, will find it automatically. 


> [!important]
> make sure that .env is in your .gitignore so you don't push it to github



## Read more 👓

- [openrouter models free](https://openrouter.ai/models?order=pricing-low-to-high&max_price=0)