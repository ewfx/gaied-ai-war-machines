import openai

client = openai.OpenAI(api_key="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")


models = client.models.list()

for model in models:
    print(model.id)
