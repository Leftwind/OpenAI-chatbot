import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, user_input):
        response = openai.completions.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5,
           
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a Joke about birds")
    print(response)        
        