from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Chatbot closed")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user
    )

    print("AI:", response.text)