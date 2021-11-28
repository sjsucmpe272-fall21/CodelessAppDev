import openai
openai.api_key = "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"

prompt="#create a flask route and method to check if a given string contains digits\n"

def get_flask_response(prompt):
    response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    temperature=0,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["#"]
    )
    resp=response.choices[0].text
    return resp
#print(get_flask_response(prompt))

