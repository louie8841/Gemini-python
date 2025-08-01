import urllib.request
import json

api_key = "your api key"  #you can get your api key on here "https://ai.google.dev/gemini-api/docs?hl=en" 
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

while True:
    user_input = input("Enter question:")

    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }

    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(api_url, data=json_data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            text_response = result["candidates"][0]["content"]["parts"][0]["text"]
            print("Gemini:", text_response)

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode()}")

    except Exception as e:
        print(f"Error: {e}")
