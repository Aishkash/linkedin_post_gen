# LinkedIn Post Generator

## Project Overview
This project is designed to help users create professional posts for LinkedIn, utilizing automation to streamline the process.

## Features
* AI-generated LinkedIn posts
* Topic-based generation
* English / Hinglish support
* Short / Medium / Long formats
* Custom prompt input
* Beautiful Streamlit UI

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API / LLM
* JSON Dataset

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Aishkash/linkedin_post_gen.git
   ```
2. Navigate to the project directory:
   ```bash
   cd linkedin_post_gen
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```
## Environment Variables

### Create .env
```bash
   GROQ_API_KEY=your_api_key_here
   ```
### To start the application, run:
   ```bash
   npm start
   ```
- Follow the on-screen instructions to create and manage your LinkedIn posts.

## folder Structure
```bash
linkedin_post_gen/
│── main.py
│── ui.py
│── styles.css
│── post_generator.py
│── few_shot.py
│── llm_help.py
│── preprocess.py
│── README.md
│── requirements.txt
│── .gitignore
│── .env
│
├── Data/
│   ├── raw_post.json
│   └── processed_posts.json
│
└── __pycache__/
   ```

## Dependencies
- React
- Axios
- Express
- dotenv
- cors

---