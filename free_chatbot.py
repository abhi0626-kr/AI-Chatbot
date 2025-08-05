import sys
import re

try:
    from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
except ImportError:
    print("Transformers library not found. Please install it with:\n  pip install transformers")
    sys.exit(1)

class FreeChatbot:
    def __init__(self, name="Jarvis", model_name="facebook/blenderbot-400M-distill"):
        self.name = name
        print(f"Loading model '{model_name}'... (this may take a minute the first time)")
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
        print(f"{self.name} is ready to chat!")

    def ask(self, user_message):
        # Normalize input: lowercase, remove punctuation, strip spaces
        normalized = re.sub(r'[^\w\s]', '', user_message.lower()).strip()
        # List of possible name-related question keywords/phrases
        name_keywords = [
            "what is your name",
            "whats your name",
            "who are you",
            "your name",
            "may i know your name",
            "tell me your name",
            "can you tell me your name",
            "do you have a name"
        ]
        # Check if any keyword is present in the normalized input
        if any(keyword in normalized for keyword in name_keywords):
            return f"My name is {self.name}."
        # Otherwise, use the model's response
        inputs = self.tokenizer([user_message], return_tensors="pt")
        reply_ids = self.model.generate(**inputs, max_new_tokens=100)
        response = self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        return response.strip()

def main():
    print("\nWelcome to your Jarvis AI! (type 'exit' or 'quit' to end)")
    chatbot = FreeChatbot(name="Jarvis")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"\n{chatbot.name}: Goodbye! Have a great day!")
                break
            response = chatbot.ask(user_input)
            print(f"\n{chatbot.name}: {response}")
        except KeyboardInterrupt:
            print(f"\n{chatbot.name}: Session ended by user")
            break

if __name__ == "__main__":
    main()