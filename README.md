🧠 AI-Powered Slogan Generator using OpenAI & Google Cloud Functions
This project demonstrates how to build and deploy a serverless slogan generator for businesses using OpenAI's GPT-3.5-turbo model and Google Cloud Functions. By sending a business description via POST request, the deployed function returns a tailored slogan in real-time.

🚀 Key Features:
Google Cloud Function setup using functions_framework

Integration with OpenAI's Chat Completions API

Deployed endpoint accessible for external API calls (e.g., Postman)

JSON input/output for easy integration into frontends or automation workflows

📦 Tech Stack:
Python 3.12

OpenAI API (gpt-3.5-turbo)

Google Cloud Run (Serverless)

Postman for testing

📌 Example Use Case:
Send:
{
  "name": "A company that is a veterinarian-designed pet-wellness assistant..."
}

Get:

{
  "slogan": "Pawsitively proactive care for your furry friend."
}