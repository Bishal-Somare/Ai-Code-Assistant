# 🧠 AI Code Assistant

A backend-powered **AI Code Assistant** built using **Hugging Face Transformers**, **LangChain**, and **Django**. This project allows users to input a coding problem and get AI-generated Python solutions using Hugging Face's `zephyr-7b-alpha` model.

---

## ⚙️ **Technologies Used**

| Tool / Library           | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| 🧠 **LangChain**          | Building prompts and managing interactions with LLM                     |
| 🤗 **Hugging Face API**   | Using the Zephyr model for generating Python code                       |
| 🛠️ **Django**             | Web backend for handling views, routing, and project structure          |
| 🔐 **python-decouple**    | Managing environment variables securely via a `.env` file               |
| 🐍 **Python**             | Core programming language used in the entire project                    |

---

## 🚧 **Installation Steps**

Follow the steps below to set up and run the project on your local machine:

---

### 🔹 **Step 1: Clone the Repository**

```bash
git clone https://github.com/Bishal-Somare/Ai-Code-Assistant.git
cd Ai-Code-Assistant


### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
```

### 3. Install All Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a file named `.env` in the root folder and add your Hugging Face API token like this:

```
HUGGINGFACEHUB_API_KEY=your_huggingface_token_here
```

Make sure not to share your token publicly.

---

## 🚀 Running the Project

```bash
python manage.py runserver
```

Once the server starts, go to:
🌐 `http://127.0.0.1:8000/` in your browser.

---

## ✅ How to Use

1. Make sure the `.env` file is configured with a valid Hugging Face API token.
2. The core logic resides in `langchain.py`, where:

   * The user's problem is passed to a LangChain prompt.
   * The prompt is processed by Hugging Face's `zephyr-7b-alpha` model.
   * The model returns a Python-based solution as a response.
3. Integrate or call `askProblem("your question here")` from your Django views or API endpoints to use the assistant.

---

## 🙌 Author

Made with ❤️ by **[Bishal Somare](https://github.com/Bishal-Somare)**

```


