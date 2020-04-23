# Reddit Flair Detection

In this pipeline, a Long Short Term Memory network – usually just called “LSTMs” – a special kind of RNN is used
to try and predict the flair of a Reddit post from the r/india subreddit. Reddit flair classification is a difficult task because of the wide variety and open nature of the platform. For prediction, please enter the complete URL of a Reddit post.

Advance users can use the automated endpoint in this web application: `automated_testing` to
predict the flair of multiple posts collectively. You can pass a .txt file to the endpoint with the URL of
each post in a line and the application returns a JSON object with the predictions for each post.

There is a sample `test.py` file in the root directory of the project for testing purposes of the automated checkpoint.

All dependencies of the web app are in the `requirements.txt` file. Please use `pip install -r requirements.txt` to install dependencies. There may be additional dependencies in the Jupyter notebooks, which are listed in the first code cell (import) of every notebook.

The data files couldn't be uploaded to GitHub due to large size and unavailability of free space in GLFS.
