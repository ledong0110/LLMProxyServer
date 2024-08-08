import openai # openai v1.0.0+
client = openai.OpenAI(api_key="anything",base_url="http://localhost:8080") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="ollama_chat/<your_model_name>", messages = [
    {
        "role": "user",
        "content": "Let's write a poem"
    }
],
stream=False)

print(response)
# res = ""
# for chunk in response:
#     # print(chunk)
#     if chunk.choices[0].delta.content:
#         res += chunk.choices[0].delta.content
#         print(res)
#         print("****************")
