from google import genai

client = genai.Client(api_key="AIzaSyDYh_H5V3Cu5s4jngkkq553LMWq13SfKls")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["How does AI work?"]
)
print(response.text)