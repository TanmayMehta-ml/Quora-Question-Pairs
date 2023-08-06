# Quora Question Pairs App - Model Training and Feature Engineering


---




This Jupyter Notebook documents the process of training a machine learning model to predict whether a pair of questions on Quora are duplicate or not. The goal of this project is to develop a web application that allows users to input two questions and get predictions about whether they are duplicate or not.

## Introduction

Quora is a popular platform where users can ask questions and get answers from the community. The task in this project is to determine whether a given pair of questions are duplicate or not. For this purpose, we will train a machine learning model using a dataset of labeled question pairs.

## Data Preprocessing

Data preprocessing is an essential step to clean and prepare the text data for feature extraction and modeling. The following preprocessing steps are performed:

- Removing special characters and decontracting words.
- Removing HTML tags using BeautifulSoup.
- Removing punctuation and tokenizing the text.

## Basic Feature Engineering

In this step, we extract basic features from the preprocessed text. The basic features include:

1. **q1_len**: The length of the first question in terms of the number of words.
2. **q2_len**: The length of the second question in terms of the number of words.
3. **q1_words**: A list of words in the first question after tokenization.
4. **q2_words**: A list of words in the second question after tokenization.
5. **words_common**: The number of words that are common between the two questions.
6. **words_total**: The total number of unique words in both questions combined.
7. **word_share**: The ratio of words_common to words_total, indicating the extent of word overlap between the questions.

## Advanced Feature Engineering

To capture more nuanced patterns and similarities between the questions, we create advanced features. The advanced features include:

1. **Token Features**:
   - **cwc_min**: Ratio of common words to the length of the smaller question.
   - **cwc_max**: Ratio of common words to the length of the larger question.
   - **csc_min**: Ratio of common stop words to the smaller stop word count among the two questions.
   - **csc_max**: Ratio of common stop words to the larger stop word count among the two questions.
   - **ctc_min**: Ratio of common tokens to the smaller token count among the two questions.
   - **ctc_max**: Ratio of common tokens to the larger token count among the two questions.
   - **last_word_eq**: 1 if the last word in the two questions is the same, 0 otherwise.
   - **first_word_eq**: 1 if the first word in the two questions is the same, 0 otherwise.

2. **Length Based Features**:
   - **mean_len**: Mean length of the two questions (number of words).
   - **abs_len_diff**: Absolute difference between the length of the two questions (number of words).
   - **longest_substr_ratio**: Ratio of the length of the longest common substring among the two questions to the length of the smaller question.

3. **Fuzzy Features**:
   - **fuzz_ratio**: fuzz_ratio score from fuzzywuzzy.
   - **fuzz_partial_ratio**: fuzz_partial_ratio from fuzzywuzzy.
   - **token_sort_ratio**: token_sort_ratio from fuzzywuzzy.
   - **token_set_ratio**: token_set_ratio from fuzzywuzzy.

## Exploratory Data Analysis (EDA)

EDA is performed to understand the distribution of features, their relationship with the target variable, and to identify any potential patterns or insights.

## Model Training

Two machine learning models, XGBoost and Random Forest, are trained using the basic and advanced features as inputs.

## Model Evaluation

The models are evaluated using a confusion matrix to compare their performance. The best performing model is selected for deployment.

## Saving the Model

The Random Forest model is pickled and saved to be used later for predictions in the web application.

## Function Definitions for Feature Extraction

The notebook includes function definitions for preprocessing the text data and extracting both basic and advanced features from the question pairs.

## References

- Quora Question Pairs Dataset: [Kaggle](https://www.kaggle.com/c/quora-question-pairs/data)
- Streamlit Documentation: [Streamlit](https://docs.streamlit.io/)
- Scikit-Learn Documentation: [Scikit-Learn](https://scikit-learn.org/stable/documentation.html)
- FuzzyWuzzy Documentation: [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)
- NLTK Documentation: [NLTK](https://www.nltk.org/)

Note: The final trained model (Random Forest) is saved as a pickle file named "model.pkl" for later use in the web application.
