from flask import Flask, render_template, request, jsonify
from SentimentAnalysis import sentiment_analyzer
import logging

# Create the Flask application instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def render_index_page():
    logger.debug('Rendering index page')
    return render_template('index.html')

@app.route('/sentimentAnalyzer', methods=['POST'])
def sent_analyzer():
    data = request.get_json()
    text_to_analyze = data.get('textToAnalyze', '')
    logger.debug(f'Received text to analyze: {text_to_analyze}')
    
    if not text_to_analyze:
        logger.warning('No text provided in the request')
        return jsonify({'result': "Invalid input! Try again."}), 400

    try:
        # Perform sentiment analysis
        result = sentiment_analyzer(text_to_analyze)
        logger.debug(f'Sentiment analysis result: {result}')
        
        # Check if the result is valid
        if result['label'] is None or result['score'] is None:
            logger.error('Sentiment analysis returned invalid results')
            return jsonify({'result': "Invalid input! Try again."}), 500
        
        # Format and return the response
        response = f"The given text has been identified as {result['label']} with a score of {result['score']}."
        logger.info('Sentiment analysis successful')
        return jsonify({'result': response})
    
    except Exception as e:
        # Handle unexpected errors
        logger.error(f'Error during sentiment analysis: {e}')
        return jsonify({'result': "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    # Run the Flask application on port 5000 with debug mode enabled
    app.run(port=5000, debug=True)
