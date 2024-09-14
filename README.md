# Sentiment Analysis Web Application

## Overview

The **Sentiment Analysis Web Application** is a sophisticated tool for analyzing textual sentiment using advanced NLP techniques. Built with Flask and integrated with the BERT-based sentiment analysis API, this project provides real-time emotional insights into user-provided text. It showcases the ability to develop scalable, responsive web applications that leverage machine learning models for real-world applications.

## Features

- **Real-Time Sentiment Analysis**: Detects and evaluates emotions in text, including positive, negative, and neutral sentiments.
- **User-Friendly Interface**: An intuitive web interface built with HTML and Bootstrap for easy interaction and clear presentation of results.
- **Robust Backend**: Flask-based API endpoint for processing sentiment analysis requests and handling responses.
- **Error Handling and Logging**: Comprehensive error handling and logging for tracking and debugging issues.
- **Unit Testing**: Includes test cases to ensure accurate sentiment classification and robustness of the application.

## Technology Stack

- **Backend**: Flask, Python
- **Sentiment Analysis**: BERT-based NLP API
- **Frontend**: HTML, Bootstrap, JavaScript
- **Testing**: unittest

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/InfectedDuck/emotion-detection-system.git
    cd emotion-detection-system
    ```

2. **Install Dependencies**:
    Ensure you have `Python 3.7+` and `pip` installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask App**:
    ```bash
    python app.py
    ```

4. **Run Unit Tests**:
    ```bash
    python -m unittest discover
    ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the text you want to analyze in the provided textarea.
3. Click on **"Run Sentiment Analysis"** to get the sentiment results.
4. View the sentiment label and score displayed on the results page.

## Code Structure
- **app.py**: Flask application configuration and routes.
- **sentiment_analyzer.py**: Sentiment analysis logic interacting with the BERT-based API.
- **index.html**: User interface for text input and displaying results.
- **tests.py**: Unit tests for validating sentiment analysis functionality.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details. <br>
This project is made as a part of IBM Course.
