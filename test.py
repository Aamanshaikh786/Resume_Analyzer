import google.generativeai as genai

genai.configure(api_key="AIzaSyBvjjr7-GhAhvLN-hKfXMEswlb2x52m4_4")


for model in genai.list_models():
    print(model.name, "-", model.display_name)