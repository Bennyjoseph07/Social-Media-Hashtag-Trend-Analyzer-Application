# Social Media Hashtag Trend Analyzer Application

This project contains scripts for accessing the AWS Lambda, AWS Dynamodb, AWS API gateway.
## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Scripts](#scripts)
   - app.py
   - aws_lambda_funtion.py
5. [Contact](#contact)

## Introduction

The task is to develop a Streamlit application that allows users to compose and publish posts, same as popular social media platforms. 
This application will integrate with AWS Lambda and DynamoDB to facilitate post processing and hashtag analysis.


## Installation

To set up this project, clone the repository and install the necessary dependencies:

# Clone the repository
git clone https://github.com/Bennyjoseph07/Social-Media-Hashtag-Trend-Analyzer-Application.git

# Navigate to the project directory
cd Social-Media-Hashtag-Trend-Analyzer-Application

# Install dependencies
pip install -r requirements.txt

## Usage

Need to create 1 AWS Lambda function with the file 
aws_lambda_funtion.py

We need to create 2 dynamodb tables 
1. twitter_post with key as twitter_post
2. twitter_hashtag with key as treanding_tag

For the created Lambda funtion, we need to create AWS API gateway in POST method

## Scripts
 - To run the streamlit application 
 - Copy the API Gateway POST methord URL link and change in app.py
- app.py
- streamlit run app.py
- This code is a Streamlit-based web application for analyzing social media trends. 
   It allows users to post messages and retrieve trending hashtags via API calls, displaying the results in a chat interface or as a DataFrame and bar chart. 
   The app's layout includes title, image, and input options for user interaction.


## Contact
Created by Your Name - Benny Joseph

Project Link: https://github.com/Bennyjoseph07/Social-Media-Hashtag-Trend-Analyzer-Application
