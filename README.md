## 📧 Email Assistant – Generate Polite Email Responses with OpenAI

This is a lightweight Python-based serverless API that uses OpenAI's GPT-4 to **generate polite, context-aware email replies** that say "no" to requests in a respectful manner.


### 🔧 Features

* 🧠 Powered by **OpenAI GPT-4**
* ☁️ Deployed on **Google Cloud Run**
* 🔒 API key secured via environment variables
* 🔁 Accepts an email request in JSON and returns a polite rejection response
* ⚡ Fast and scalable using serverless architecture

---

### 🗂️ Tech Stack

* Python 3.12
* Flask + Functions Framework
* Google Cloud Run
* OpenAI API

---

### 📦 API Endpoint

`POST /`

**Request Body:**

```json
{
  "email": "Can you work on this urgent task tonight?"
}
```

**Response:**

```json
{
  "choice_1": "Hi, thank you for reaching out. I’d love to help, but I’m unable to take this on at the moment..."
}
```

---

### 📁 Files

* `main.py` – main API logic
* `requirements.txt` – dependencies
* `.gitignore`, `README.md` – basic project files

