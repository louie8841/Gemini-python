# Gemini API Chatbot (Python)

This is a simple terminal-based chatbot using Google's **Gemini 1.5 Flash API**.  
It sends your input to the Gemini API and prints out the AI's response in real-time.

---

## Features

- Communicates with Gemini 2.0 Flash model
- Simple terminal interface (input/output)
- Handles HTTP errors gracefully
- Easy to understand and modify

---

## How to Use

1. **Get your API key:**  
   Visit [https://ai.google.dev/gemini-api/docs?hl=ko](https://ai.google.dev/gemini-api/docs?hl=en)  
   and sign up for a free API key.

2. **Insert your key:**  
   Replace `"your api key"` in the script with your actual key:
   ```python
   api_key = "YOUR_API_KEY"
