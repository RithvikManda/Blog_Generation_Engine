# Blog Generator and Tourist Assistant

This project uses **LangChain**, **Streamlit**, and **Llama3** to build a blog generation and tourism assistant application. The app allows users to generate unique blogs on specified topics and provides recommendations for top tourist places.

---

## Features

- **Blog Generation:** Enter a topic and specify the word count to generate a blog post.
- **Tourist Assistance:** Provides recommendations for top tourist destinations.
- **Interactive UI:** Built with **Streamlit** for a user-friendly interface.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/blog-generator.git
   cd blog-generator
2. **Set up a Virtual Environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Linux/MacOS
   myenv\Scripts\activate     # For Windows
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
4.**Set up the .env File:**


  1. Create a `.env` file in the project root directory.

  2. Add your LangChain API key to the file:
    
    ```bash 
    LANGCHAIN_API_KEY="your_api_key_here"
##Usage
1. **Run the Streamlit App:**
   ```bash
   streamlit run llama.py
2. **Enter Input:**
   Blog Generator: Enter a topic and the desired word count to generate a blog.
   Tourist Assistant: The assistant can provide recommendations for tourist destinations (customizable via prompts).
   
##Project Structure
-> llama.py: Main application script.
-> .env: File for storing the API key (excluded from Git using .gitignore).
-> requirements.txt: File listing all dependencies.

## Example Prompt

### Blog Generation:

- **Input:**  
  `"Enter a topic for the blog: Technology"`  
  **Number of words:**  
  `500`  

- **Output:**  
  A unique 500-word blog about "Technology."

---

### Tourist Assistance:

- **Input:**  
  A location  

- **Output:**  
  Top 10 tourist destinations near the specified location.


## Requirements

- Python 3.7+
- Streamlit
- LangChain
- Llama3 Model (via Ollama)



### Explanation of the Sections:

1. **Project Description:** Brief overview of what the project does.
2. **Features:** Lists the key functionalities of the app.
3. **Installation:** Step-by-step instructions to set up the project locally.
4. **Usage:** Instructions on running the app and interacting with the UI.
5. **Project Structure:** Overview of the main files and their purposes.
6. **Example Prompt:** Demonstrates typical input and output for the app’s main features.
7. **Requirements:** Lists the software dependencies.


Make sure to replace `your_api_key_here` with your actual API key and `your-username` with your GitHub username in the instructions.


