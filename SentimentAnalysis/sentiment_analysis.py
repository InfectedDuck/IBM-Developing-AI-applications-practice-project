import requests


def sentiment_analyzer(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Constructing the request payload in the expected format
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Custom header specifying the model ID for the sentiment analysis service
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Sending a POST request to the sentiment analysis API
        response = requests.post(url, json=myobj, headers=header)
        # Check if the response status code is not 200 (success)
        if response.status_code != 200:
            return {'label': None, 'score': None}

        # Parsing the JSON response from the API
        formatted_response = response.json()

        # Extracting sentiment label and score from the response
        label = formatted_response.get(
            'documentSentiment', {}).get(
            'label', None)
        score = formatted_response.get(
            'documentSentiment', {}).get(
            'score', None)

        # Return the results as a dictionary
        return {'label': label, 'score': score}

    except Exception as e:
        # Handle unexpected errors
        print(f"Error during sentiment analysis: {e}")
        return {'label': None, 'score': None}
