# Experiment Log

## Stage 1: Data Collection

1. Create a Reddit Application to get OAuth2 keys. [SUCCESS]
2. Creating the Python script which will be used to parse data. [SUCCESS]
    2.1. Getting Reddit and Subreddit instances. [SUCCESS]
    2.2. Parsing and Downloading the data [SUCCESS]

## Stage 2: Exploratory Data Analysis

1. Create a Jupyter Notebook for EDA [SUCCESS]

## Stage 3: Flair Detection

1. Clean the data - Removing punctuations and stopwords. [SUCCESS]
2. Removing the `r/` tag from the flairs.
    2.1. Using a higher order function approach. [FAILURE]
    2.2. Using `.replace()` to replace a certain predefined list of bad-characters with empty string. [SUCCESS]
3. Splitting the dataset into training and test. [SUCCESS]
4. TFIDF Vectorization [SUCCESS]

## Stage 4: Web Application

1. Load Flask app template. [SUCCESS]
2. Render basic HTML elements. [SUCCESS]