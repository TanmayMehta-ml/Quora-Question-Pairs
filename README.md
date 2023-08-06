# Quora Question Pairs Web App
<p align="center">
  <img src="quora_logo.png" alt="Quora Logo" width="200" height="200">
</p>


This project showcases a web application that utilizes advanced Natural Language Processing (NLP) techniques and feature engineering to identify question pairs with the same intent. The web app allows users to input two questions and receive predictions on whether the questions have similar meanings or not.

## Project Overview
The main goal of this project is to build a model that can accurately determine if two questions on Quora have the same intent. The task is to predict which of the provided pairs of questions contain two questions with the same meaning. The ground truth labels were supplied by human experts, making this a subjective and challenging problem.

## My Approach and Implementation
I started by preprocessing the data to clean and normalize the text data. Then, I performed basic feature engineering, such as calculating the length of questions and computing word overlap. The real power lies in the advanced feature engineering, where I created token features and fuzzy features using NLP techniques.

The implementation of the project is documented in a Jupyter Notebook [here](https://github.com/TanmayMehta-ml/Quora-Question-Pairs/blob/main/Quora%20Question%20Pairs%20-%20Model%20Training.ipynb). In this notebook, each step is explained in detail, making it a valuable resource for understanding the feature engineering and model training process.

## Kaggle Competition
The techniques and methods used in this project draw inspiration from the Quora Question Pairs competition on Kaggle. Although this project is not a direct submission to the competition, I adopted similar approaches and learned from the Kaggle community's best practices.

For a detailed understanding of the project and its implementation, you can explore the Jupyter Notebook [here](https://github.com/TanmayMehta-ml/Quora-Question-Pairs/blob/main/Quora%20Question%20Pairs%20-%20Model%20Training.ipynb). Additionally, you can find more information about the original Kaggle competition [here](https://www.kaggle.com/c/quora-question-pairs).

The project demonstrates the significance of NLP and feature engineering in solving real-world challenges related to question similarity identification. I encourage you to explore the Jupyter Notebook and try out the web app to experience the power of NLP in action!
