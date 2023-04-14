import openai
openai.api_key = "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"
print(openai.Model.list())    
completion = openai.Completion.create(model="ada", prompt="Hello world")