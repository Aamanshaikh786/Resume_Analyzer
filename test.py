import google.generativeai as genai

genai.configure("enter your api key")


for model in genai.list_models():
    print(model.name, "-", model.display_name)