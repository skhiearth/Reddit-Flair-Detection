# Experiment Log

## Stage 1: Data Collection

1. Create a Reddit Application to get OAuth2 keys. [SUCCESS]
2. Creating the Python script which will be used to parse data. [SUCCESS]
    2.1. Getting Reddit and Subreddit instances. [SUCCESS]
    2.2. Parsing and Downloading the data [SUCCESS]
3. Use PRAW for downloading large amount of data. [FAILURE - API restriction]
4. Use PushShift for collecting Reddit data. [SUCCESS - More than 8 lakh entries collected.]

## Stage 2: Exploratory Data Analysis

1. Create a Jupyter Notebook for EDA [SUCCESS]
2. Evaluate class balance. [SUCCESS - We observed a very severe class imbalance in the dataset. Out of the hundreds of flairs, only top 5 had a significant number of entries compared to the total number of entries in the dataset. Due to already low performance of classic ML models, I am sticking to only predicting among the Top 5 flairs, because these are the most common. The dataset is following a very aggressive form of the Pareto Principle.]

## Stage 3: Flair Detection

1. Clean the data - Removing punctuations and stopwords. [SUCCESS]
2. Removing the `r/` tag from the flairs.
    2.1. Using a higher order function approach. [FAILURE]
    2.2. Using `.replace()` to replace a certain predefined list of bad-characters with empty string. [SUCCESS]
3. Splitting the dataset into training and test. [SUCCESS]
4. TFIDF Vectorization [SUCCESS]
5. Use classical ML models with complete dataset. [FAILURE - 50% Accuracy]
6. Use classical ML models with balanced data of most frequent class labels. [SUCCESS - 67% Accuracy without any optimizations and tuning]
7. Use classical ML models with complete data for frequent classes. [FAILURE - Not enough compute power to train on 3.5 Lakh rows and 50k coloumns.]
    7.1. Use Kaggle kernels for this task. [FAILURE - RAM bottleneck]
    7.2. Use Google Colab for this task. [FAILURE - RAM bottlenech]
    7.3. Create and use GCP Compute Engine instance for this task. []
8. Use ANNs with complete dataset. [FAILURE - 56% Accuracy, very high overfitting]
9. Use ANNs with most frequent class labels. [FAILURE - 64% Accuracy, very high overfitting]
10. Use LSTMs with balanced data for most frequent classes. [SUCCESS - 70% Accuracy, no/little overfitting before callback is triggered]
11. Use LSTMs with complete data for most frequent classes. [SUCCESS - 72% Accuracy, no/little overfitting before callback is triggered]

## Stage 4: Web Application

1. Load Flask app template. [SUCCESS]
2. Render basic HTML elements. [SUCCESS]
3. Predict flair from taking Reddit title + body from user. [SUCCESS - Trial for working of the model]
4. Predict flair from taking Reddit URL from user. [SUCCESS - Trial for working of the PRAW instance]
5. Predict flair from a text file containing URLs of multiple reddit posts. [SUCCESS]
6. Add instructions on web app usage to the landing page. [SUCCESS]

## Stage 5: Future Work

1. Use Feature Enginerring to improve classification accuracy [POSSIBLE FEATURE: Length of title, number of puncutations, direct occurences of certain words in the title (like Corona -> Coronavirus), etc. Unable to implement feature engineering due to computing constraints and time (Each epoch of Neural Network takes approximately 40 minutes to run)]
2. Build a more elegant UI/UX for the web application. [Unable to implement a more elegant UX due to lack of knowledge and practice in this domain.]
