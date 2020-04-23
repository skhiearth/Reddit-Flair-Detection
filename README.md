# Reddit Flair Detection

In this pipeline, a Long Short Term Memory network – usually just called “LSTMs” – a special kind of RNN is used
to try and predict the flair of a Reddit post from the r/india subreddit. Reddit flair classification is a difficult task because of the wide variety and open nature of the platform. For prediction, please enter the complete URL of a Reddit post.

Advance users can use the automated endpoint in this web application: `automated_testing` to
predict the flair of multiple posts collectively. You can pass a .txt file to the endpoint with the URL of
each post in a line and the application returns a JSON object with the predictions for each post.
