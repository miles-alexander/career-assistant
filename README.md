# Career Assistant Chatbot 🤖

**Author:** [@miles-alexander](https://github.com/miles-alexander)  

---

## Project Overview

The Career Assistant Chatbot is an AI-powered tool designed to assist users with career planning and development. It provides guidance on career paths, essential skills, relevant certifications, and personalized career advice. The chatbot uses OpenAI’s fine-tuned GPT-3.5 model to deliver tailored responses based on user input.

---

## Features

* **Career Advice:** Get personalized recommendations for career paths and skills.
* **Skill Guidance:** Discover which skills are essential for your desired role.
* **Certification Suggestions:** Learn about industry-recognized certifications relevant to your field.
* **Interactive Chat Interface:** Easy-to-use chat interface built with Streamlit.
* **Fine-Tuned Model:** Uses a custom fine-tuned model for more accurate responses.

---

## Technology Stack

* **Python:** Backend and data processing
* **Streamlit:** Interactive front-end for chatbot interaction
* **OpenAI API:** Powered by a fine-tuned GPT-3.5 model
* **JSON:** Data format for training and response storage

---

## Example Interactions

**User:** "What skills do I need to be a data scientist?"

**Assistant:** "To become a data scientist, you should focus on Python, machine learning, SQL, and data visualization."

**User:** "What certifications should I get to be an HR Coordinator?"

**Assistant:** "To be an HR Coordinator, consider certifications like SHRM-CP, PHR, or HR Analytics."

---

## Run Locally

To run this project on your own machine:

**Clone the Repository**:

```bash
git clone https://github.com/miles-alexander/career-assistant.git
```

**Go to the Project Directory**:

```bash
cd career-assistant
```

**Install the Required Libraries**:

```bash
pip install streamlit openai
```

**Set Up OpenAI API Key**:

Replace `your_openai_api_key` with your actual OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key  # On Windows: set OPENAI_API_KEY=your_openai_api_key
```

**Run the Chatbot**:

```bash
streamlit run app.py
```

* Open the URL provided by Streamlit (usually `http://localhost:8501/`) in your browser.
* Start interacting with the chatbot.

---

## Milestone3.py: Fine-Tuning Summary

The file `Milestone3.py` contains the process used to fine-tune the GPT-3.5 model specifically for career guidance.

### Summary of the Fine-Tuning Process:

**Data Preparation:**

   * Converted the career guidance dataset from JSON to JSONL format.
   * Structured data into prompt-completion pairs for training.

**Fine-Tuning the Model:**

   * Uploaded the formatted dataset to OpenAI using the API.
   * Fine-tuned the GPT-3.5 model to generate career advice based on user queries.

**Model Usage:**

   * Loaded the fine-tuned model in the Streamlit app to respond to career-related questions.

**Note:**

* The fine-tuning process was completed separately, and the chatbot directly uses the resulting model.
* You do not need to repeat the fine-tuning process to use the chatbot.
* The `Milestone3.py` script is shared for reference and documentation purposes.

---

## Future Enhancements

* **Enhanced Personalization:** Incorporate user profiles for more tailored advice.
* **Industry-Specific Modules:** Add more targeted advice for different career fields.
* **Platform Integration:** Connect with LinkedIn for job suggestions and resume insights.

---
