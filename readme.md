# Travel Policy Assistant (RAG)

An intelligent **Travel Policy Assistant** built using **Django, LangChain, Mistral AI, FAISS, and HuggingFace Embeddings** that answers employee travel policy questions directly from company travel policy PDFs.

The system supports:

* Employee Login & Signup
* Band-based entitlement filtering
* Domestic & Foreign travel policy Q&A
* RAG (Retrieval-Augmented Generation)
* Smart policy-based inference
* Chat history
* Responsive modern UI

---

## Features

### Authentication System

* Employee Signup
* Employee Login
* Secure authentication
* Logout functionality

### Employee Band-Based Responses

Supports the following employee bands:

* **9/10**
* **7/8**
* **5/6**
* **1/2/3/4**

The assistant automatically filters responses according to the logged-in employee’s band.

Example:

If a **Band 5/6** employee asks:

> Can I travel to Jaipur by flight?

The assistant responds according to the **5/6 policy only**, without showing entitlements of other bands.

---

## RAG Pipeline

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline:

1. Load travel policy PDFs
2. Split documents into chunks
3. Create embeddings using HuggingFace
4. Store embeddings in FAISS vector database
5. Retrieve relevant chunks
6. Generate answers using Mistral LLM

---

## Tech Stack

### Backend

* Django 5
* Python 3.11+

### AI / RAG

* LangChain
* Mistral AI
* FAISS Vector Store
* HuggingFace Embeddings
* Sentence Transformers

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite3

---

## Project Structure

```bash
travel_policy_rag/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
├── chatbot/
│   ├── views.py
│   ├── rag.py
│   ├── qa_chain.py
│   ├── loaders.py
│   ├── splitter.py
│   ├── embeddings_store.py
│   ├── urls.py
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── chat.html
│
├── static/
│   ├── css/
│       ├── style.css
│
├── data/
│   ├── domestic_travel.pdf
│   ├── foreign_travel.pdf
│
├── .env
├── requirements.txt
├── manage.py
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/travel-policy-rag.git

cd travel-policy-rag
```

---

### 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

### 5. Add PDFs

Put travel policy PDFs inside:

```bash
data/
```

Required files:

```bash
domestic_travel.pdf
foreign_travel.pdf
```

---

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 7. Run Server

```bash
python manage.py runserver
```

Open:

```bash
http://127.0.0.1:8000/
```

---

## How It Works

### Signup

Employee enters:

* Name
* Employee ID
* Password
* Band

### Login

Employee logs in securely.

### Chat

User asks travel policy questions.

Example:

```text
Can I travel to Bangalore by flight?
```

The assistant:

1. Detects employee band
2. Retrieves relevant policy chunks
3. Generates final answer
4. Restricts response to user entitlement

---

## Answer Rules

The assistant follows these rules:

* Uses only uploaded travel policy documents
* Answers only for logged-in employee band
* Does not reveal other bands’ entitlements
* Shows calculation steps only when required
* Uses tables only if needed
* Gives one final answer
* If policy is unavailable:

```text
This information is not present in the travel policy documents.
```

---

## Future Improvements

* PDF Upload UI
* Chat Export
* Multiple Company Policies
* Role-based Access
* PostgreSQL Support
* Docker Deployment
* Chat Memory
* React Frontend

---

## Screenshots

### Login Page

<img width="1331" height="630" alt="image" src="https://github.com/user-attachments/assets/aff3e60d-d292-4df2-bada-7af3752e8f53" />


### Signup Page

<img width="1344" height="628" alt="image" src="https://github.com/user-attachments/assets/a1231ad7-b4f3-469a-a9b7-6c1ab7400ee1" />


### Chat UI

<img width="1339" height="628" alt="image" src="https://github.com/user-attachments/assets/929a3f39-2493-4ff3-8766-af23fca31b4b" />


---

## Author

**Suryanandan Kumar**

GitHub:
https://github.com/suryanandan1

---

## License

This project is for educational and internal enterprise use.
