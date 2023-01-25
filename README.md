# Restaurant_Reviews_Sentimental_Analysis

#- In this project, we are going to perform Sentimental Analysis of food delivery Reviews.

Problem Statement: Scrape First N Restaurants and capture first N Dining Reviews and apply sentiment analysis to the data.

Libraries Used: pandas,selenium.webdriver.common.by ,selenium , webdriver_manager.chrome , selenium.webdriver.chrome.option , time , selenium.webdriver.support,selenium.webdriver.support.wait,nltk,seaborn,sklearn,matplotlib.pyplot,

Locators Used: CLASS_NAME , TAG_NAME , XPATH, LINK_TEXT.

Steps followed to Create a Dataset: A] Scrape User reviews: 1) Entered the location whichever area user needs (Dynamic). 2) Go to Dining out scrape that location restaurant names.As per user requires how many restaurants user needs to scrape and the Restaurant rated 3) Go to all the restaurants Scrape the Reviews, Reviewed by and Reviewed Text.

We are going to use <a href="https://www.mygreatlearning.com/blog/bag-of-words/"> Bag Of Words 

  Technique to predict positive and negative reviews. Vast amount of data is in text format which is highly unstructured in nature. In order to get necessary information from this kind of data, text mining and Natural Language Processing is important. NLP is part of Artificial Intelligence which deals with human languages.

In Jupyter notebook, I have explained steps to perform NLP using <a href="https://www.mygreatlearning.com/blog/bag-of-words/"> Bag of Words 
  
technique and I have predicted Positive and Negative reviews using Logistic Regression Algorithm and Naive Bayes Algorithm. The accuracy of the model is 88.21752265861026 % and F1 Score is 0.9197080291970803.

After doing sentiment analysis with NLP found that the data is Positive. 78% are Positive Reviews.

It has been observed that reviews rated as 3 are maximum Neutral.If required can be removed.
