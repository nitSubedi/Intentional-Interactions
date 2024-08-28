from openai import OpenAI


client = OpenAI(api_key="")

def geenerate_description(event_name):
    response = client.chat.completions.create(
        model=  "gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are an Resident Assistant in a university dorm. writing your intentional interactions with your residents"},
            {"role":"user", "content": "Write an intentional interaction with a resident about {event_name}" }       ],
        temperature=0.7,
    )
    description = response.choices[0].text.strip()
    print (description)


geenerate_description("upcoming final exams")
