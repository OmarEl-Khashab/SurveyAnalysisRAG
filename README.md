# SAT-RAG: Survey Analysis Tool using RAG

##  Description
SAT-RAG is a survey analysis tool powered by Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).
It is a web application that utilizes LLM models from OpenAI 
to process and analyze user queries related to two survey datasets provided by Bounce Insights Company, 
for market research purposes. The tool provides valuable insights to clients by 
leveraging the capabilities of RAG and LangChain.

The project comprises the following components::

- **Backend:** The question-and-answer chat feature is developed using the OpenAI GPT model and LangChain to implement Retrieval-Augmented Generation (RAG) for extracting insights. The backend connection is facilitated by a FastAPI-based service that processes user queries and interactions.


- **Frontend:** A simple HTML/CSS interface that allows for an interactive user experience.



The datasets provided by Bounce Insights include:

- **Dataset 1:** Sustainability Research Results, which contains client responses on how sustainability influences their choices.
  
- **Dataset 2:** Christmas Research Results, detailing client responses regarding how Christmas marketing strategies affect their purchasing decisions.


## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Instructions](#Instructions)
- [API Documentation](#api-documentation)
- [Acknowledgement](#Acknowledgement)

## Tool Features

- **LLM-Generated Analysis:** Utilizes OpenAI’s LLM models through retrieval-augmented generation (RAG) in LangChain for accurate and insightful answers based on survey data.
- **Easy Query Interface:** Intuitive interface allows users to ask questions about survey datasets, making it accessible for the user.
- **Simple UI:** User-friendly question-answer interface designed for seamless interaction, enhancing user experience and engagement.

## Prerequisites

- **Python:** Required programming language; ensure version 3.9 or later is installed.
- **LangChain:** Library for building LLM applications.
- **FastAPI:** Framework for building APIs.
- **OpenAI:** For interacting with OpenAI models.
- **Conda Virtual Environment (optional):** To manage dependencies for running python packages.

## Installation and Setup

1. **Clone the Repository:**

	```sh
	git clone https://github.com/elcaiseri/Survey-Analysis-RAG-System.git
	cd SurveyAnalysisRAG
	```

2. **Install the required packages** 

	```sh
	pip install -r requirements.txt
	```

3. **Add your Data Paths :**

	Add your dataset path and path of the embeddings store:
	```
	data_path = "/SurveyAnalysisRAG/Data"
	embeddings_dir = "/SurveyAnalysisRAG/Data/{Name of the file}"
	```

4. **Start the App:**

	Run the main code to start the survey experience in the UI:

	```sh
	python main.py
	```


## How to use:

1. **Access the Application:**

	- Open your browser and go to `http://127.0.0.1:8000`.


2. **Interact with the Application:**

	- Enter a question in the input field (e.g., “Define how important is sustainability to consumers?”).
	- Select the related survey dataset from the dropdown (Sustainability Survey or Christmas Survey).
	- Click **Generate Insights** to input the query.


3. **View Results:**
	- The LLM will generate a response the  displayed in the screen.
## API Documentation

The backend exposes a POST endpoint for querying datasets.

- **Endpoint:** `/query`
- **Method:** POST
- **Description:** Processes a user query and returns AI-generated insights.

**Request Body:**

```json
{
  "query": "Define how important is sustainability to consumers?",
  "source": "Dataset 1 (Sustainability Research Results)"
}
```

**Response:**

```json
{
  "answer": "Sustainability is highly important to consumers, with many prioritizing brands' sustainability credentials in purchasing decisions, influencing around 60-70% of shoppers."
}
```

**Error Handling:**

- If the request fails, the API returns an appropriate HTTP status code and an error message.

## Web Application Interface



<p align="center">
  <img src="/SAT.png" alt="My Image" width="700"/>
</p>

## Acknowledgement

This is a big thanks for the Bounce Insights Company for sharing this dataset to complete this Machine learning awesome Project

Feel free to contribute reach out for the project by opening issues or submitting pull requests. If you have any questions, contact me at omar_khashab11@hotmail.com
