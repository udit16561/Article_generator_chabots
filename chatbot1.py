
from transformers import pipeline


generator = pipeline('text-generation', model='google/flan-t5-xl')  

def generate_article(topic, length=100):
    """
    Generates an article on a given topic using the specified model.
    """
    prompt = f"Write an article about {topic}."
    generated_text = generator(prompt, max_length=length, num_return_sequences=1)
    article = generated_text[0]['generated_text']
    return article


topic = input("Enter Your favorable Topic")
article = generate_article(topic, length=300)  
print(article)

# Chatbot interaction loop
while True:
    user_input = input("Enter your topic or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break

    try:
        generated_article = generate_article(user_input)
        print(generated_article)

    except Exception as e:
        print(f"An error occurred: {e}")