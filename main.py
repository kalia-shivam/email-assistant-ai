import functions_framework
import os
from flask import jsonify, Request
from openai import OpenAI

# Load env vars locally (ignored on Google Cloud)
load_dotenv()

@functions_framework.http
def get_message(request: Request):
    request_json = request.get_json(silent=True)

    if not request_json or 'email' not in request_json:
        return jsonify({'error': 'Missing "email" in request'}), 400

    email = request_json['email']

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that creates replies to emails "
                    "that politely say no to the request you have been asked to perform. "
                    "Only return the reply to the email, nothing else."
                )
            },
            {
                "role": "user",
                "content": email
            }
        ],
        temperature=1.41,
        max_tokens=1066,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=3
    )

    result = {
        'choice_1': response.choices[0].message.content,
        'choice_2': response.choices[1].message.content,
        'choice_3': response.choices[2].message.content
    }

    return jsonify(result)
