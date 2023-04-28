import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def chatgpt_response(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=200,
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response


# def chatgpt_conversation(conversation, model):
#     response = openai.Completion.create(
#         model=model,
#         messages=conversation
#     )
#     api_usage = response['usage']
#     print("Total token command: {0}".format(api_usage['total']))
#     # stop means complete

#     print(response["choices"][0].finish_reason)
#     print(response["choices"][0].index)
#     conversation.append({'role':response.choices[0].message.role, 'content'})
