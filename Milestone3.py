# import needed libraries
import streamlit as st
import openai
import os
import requests
import time
import json
import tiktoken
import numpy as np
from collections import defaultdict

# create variable for OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# path to the .json file
data_path = "career_assistant.json"

# load the dataset
with open(data_path, 'r', encoding='utf-8') as f:
    dataset = json.load(f)  

# initial dataset stats
print("Number of Examples:", len(dataset))
print("First Example:")
for key, value in dataset[0].items():  
    print(f"{key}: {value}")

# convert JSON to JSONL before uploading
json_file_path = "career_assistant.json"
jsonl_file_path = "career_assistant.jsonl"

# read JSON file
with open(json_file_path, "r", encoding = "utf-8") as f:
    dataset = json.load(f)  # load JSON file 

# convert to JSONL format
with open(jsonl_file_path, "w", encoding = "utf-8") as f:
    for entry in dataset:
        f.write(json.dumps(entry) + "\n")  # write each dictionary as a new line

print(f"Converted {json_file_path} to {jsonl_file_path}")

# load the old dataset (prompt-completion format)
input_file = "career_assistant.json" 
output_file = "career_assistant_chat.jsonl"

with open(input_file, "r", encoding = "utf-8") as f:
    old_data = json.load(f)

# convert to chat format
new_data = []
for entry in old_data:
    chat_entry = {
        "messages": [
            {"role": "system", "content": "You're a chatbot that helps users with creating career development plans."},
            {"role": "user", "content": entry["prompt"]},
            {"role": "assistant", "content": entry["completion"]}
        ]
    }
    new_data.append(chat_entry)

# save as a JSONL file
with open(output_file, "w", encoding = "utf-8") as f:
    for entry in new_data:
        f.write(json.dumps(entry) + "\n")

print(f"Converted dataset saved as {output_file}")

jsonl_file_path = "career_assistant_chat.jsonl"

with open(jsonl_file_path, 'r', encoding = 'utf-8') as f:
    for line in f:
        json.loads(line)  # will raise an error if the format is incorrect
print("Dataset is valid JSONL")

# upload JSONL file to OpenAI
headers = {"Authorization": f"Bearer {openai.api_key}"}

with open(jsonl_file_path, "rb") as f:
    response = requests.post(
        "https://api.openai.com/v1/files",
        headers = headers,
        files = {"file": f},
        data = {"purpose": "fine-tune"}
    )

# print response
print(response.json())

response = requests.post(
    "https://api.openai.com/v1/fine_tuning/jobs",
    headers = headers,
    json = {"training_file": "file-Bqi94DbzZYzC97TXnTh87Q", "model": "gpt-3.5-turbo"}
)
print(response.json())

training_job_id = "ftjob-sYMWQtdeRY4Z6NVA2w8UvYno"

# endpoint to check the status of the training job
url = f"https://api.openai.com/v1/fine_tuning/jobs/{training_job_id}"

# polling loop
while True:
    response = requests.get(url, headers = headers)
    
    if response.status_code == 200:
        data = response.json()
        status = data.get("status", "Unknown")
        print("Training Job Status:", status)
        
        # check if the training is complete
        if status in ["succeeded", "failed"]:
            print("Training finished with status:", status)
            if status == "succeeded":
                print("Trained Model Name:", data.get("fine_tuned_model", "Not Available"))
            break
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    # wait for 30 seconds before polling again
    print("Waiting for 30 seconds before the next poll...")
    time.sleep(30)

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers = headers,
    json = {
        "model": "ft:gpt-3.5-turbo-0125:personal::AzCXzj45",
        "messages": [{"role": "system", "content": "You're a chatbot that helps users with creating career development plans."},
                     {"role": "user", "content": "How can I become a data scientist?"}
                    ]
    }
)
print(response.json())

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers = headers,
    json = {
        "model": "ft:gpt-3.5-turbo-0125:personal::AzCXzj45",
        "messages": [{"role": "system", "content": "You're a chatbot that helps users with creating career development plans."},
                     {"role": "user", "content": "What certifications do I need to become an HR coordinator?"}
                    ]
    }
)
print(response.json())

# define the fine-tuned model ID
fine_tuned_model = "ft:gpt-3.5-turbo-0125:personal::AzCXzj45"

# make a chat completion request
response = openai.ChatCompletion.create(
    model = fine_tuned_model,
    messages = [
        {"role": "system", "content": "You're a chatbot that helps users with creating career development plans."},
        {"role": "user", "content": "What skills do I need to be an AI engineer?"}
    ],
    max_tokens = 200
)

# print the response
print(response["choices"][0]["message"]["content"])

url = f"https://api.openai.com/v1/fine_tuning/jobs/{training_job_id}"

response = requests.get(url, headers = headers)

if response.status_code == 200:
    job_details = response.json()
    print("Fine-Tuning Job Details:")
    print(job_details)
else:
    print(f"Error retrieving job details: {response.status_code}, {response.text}")

# fine-tuning job events endpoint
events_url = f"https://api.openai.com/v1/fine_tuning/jobs/{training_job_id}/events"

response = requests.get(events_url, headers = headers)

if response.status_code == 200:
    events = response.json().get("data", [])
    for event in events:
        print(event["message"])
else:
    print(f"Error retrieving events: {response.status_code}, {response.text}")