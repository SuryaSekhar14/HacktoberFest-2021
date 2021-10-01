# Inshorts-NLP

![Scraping](https://github.com/codekhal/Inshorts-NLP/blob/master/img/scraping.png)

Analysed syntax and Semantics of Corpus of Text Documents Retrived from Web Scraping of News articles from Inshorts and followed the Standard NLP Workflow of the CRISP-DM model.

![WorkFlow](https://github.com/codekhal/Inshorts-NLP/blob/master/img/workflow.png)

[*Credits*](https://towardsdatascience.com/@dipanzan.sarkar)


[![Open Issues](https://img.shields.io/github/issues-raw/codekhal/Inshorts-NLP?style=for-the-badge)](https://github.com/codekhal/Inshorts-NLP/issues)
[![Forks](https://img.shields.io/github/forks/codekhal/Inshorts-NLP?style=for-the-badge)](https://github.com/codekhal/Inshorts-NLP/network/members)
[![Stars](https://img.shields.io/github/stars/codekhal/Inshorts-NLP?style=for-the-badge)](https://github.com/codekhal/Inshorts-NLP/stargazers)

![Maintained](https://img.shields.io/maintenance/yes/2020)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python)  
![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative)  
![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi)


## :ledger: Index

- [Index](#index)
- [About](#about)
- [Usage](#usage)
- [Commands](#commands)
  - [Installation](#installation)
- [File Structure](#file-structure)
- [Brief Description](#brief-description)
- [Info Gallery](#gallery)
- [Guidelines](#guideline)
- [Resources](#resources)
- [Present Contributors](#contributors)
- [License](#license)

## :beginner: About
A NLP based Project which scraps the news articles of mainly 3 categories:
- Technology
- Sports
- World

from InShorts using website urls.
Finally after numerous preprocessing steps like Text Wrangling, Removing accented characters, Removing html tags, Lemmatization, Stemming, build a text normalizer to create dataset for applying sentiment analysis.


Sentiment analysis is perhaps one of the most popular applications of NLP.

The key aspect of sentiment analysis is to analyze a body of text for understanding the opinion expressed by it. Typically, quantifying this sentiment with a positive or negative value, called polarity.

- [Usage](#usage)

This project can be used to create following key features:

- Building Text summarizer using RNNs and LSTM
- Gain only particular sentiment be it positive or negative.
- Emojifier: Building appropriate reaction emojis from the extracted sentiments.
- Building a tone detector as Grammarly (Beta) provides us.

Build this project to learn the nuances of NLP of handling Text Data.

## :electric_plug: Installation

### :package: Commands

#### Packages which should be imported:

- **Pandas**
- **Numpy**
- **Seaborn**
- **nltk**
- **Afinn**
- **TextBlob**
- **Beautiful Soup**
- **requests**
- **Spacy Language Models**

**Note**: Spacy may give lot of errors, one should make sure to proper install it. 
Further more refer to the [*requirements.txt*](https://github.com/codekhal/Inshorts-NLP/blob/master/requirements.txt)

Just want to run the project on your local machine:
Make sure you install all the packages mentioned in requirements.txt.

- Clone the repository

```bash
$ git clone https://github.com/codekhal/Inshorts-NLP 

```

- Install dependencies.

```bash
$ cd Inshorts-NLP
```

- Now in your terminal, using appropriate conda env 

```bash
$ run jupyter or any other preferable editor
```  
## :open_file_folder: File Structure

- File structure with the basic details about files and directories.

```bash

.__Inshorts-NLP__
├── contractions.py
├── img
│   ├── scraping.png
│   ├── Sentiment_Score_News_Category.png
│   ├── sentiments.png
│   ├── stemming.png
│   ├── Visualizing_Sentiments_Box_Plot.png
│   └── workflow.png
├── LICENSE
├── news.csv
├── NLP_main.ipynb
├── __pycache__
│   └── contractions.cpython-35.pyc
├── README.md
└── requirements.txt

2 directories, 13 files

```

# - Brief Description

Built a web scraper which had scraped news articles from Inshorts website urls. 
Then using numerous text-preprocessing techniques, cleaned the data for further processing.
After this, turn came for sentiment analysis on the data.
Various popular lexicons are used for sentiment analysis, including the following.

- AFINN lexicon
- Bing Liu’s lexicon
- MPQA subjectivity lexicon
- SentiWordNet
- VADER lexicon
- TextBlob lexicon

Used NLTK, AFINN and TextBlob library. 
Using both data visualization tools and pandas dataframe techniques to show results of the dataset.

## :camera: Info Gallery

The sentiment score of different genres of news category is shown with the help of the following plots.

![Box Plot](https://github.com/codekhal/Inshorts-NLP/blob/master/img/Visualizing_Sentiments_Box_Plot.png)

Lastly, the count of three sentiments in different genres of news articles is depicted with the help of factor or bar plot.

![Factor Plot](https://github.com/codekhal/Inshorts-NLP/blob/master/img/Sentiment_Score_News_Category.png)

## :scroll: Guidelines

- __Contribution Guidelines__

**Future Work that could be done**:

- *Flask/Flask App Deployment* -​ ​ Deploy the app so that couldbe efficiently used.

- *Use of Deep Learning* -​ One may try and use deep learning for building a text summurizer and tone detector.


Kindly follow the [*Contributions Guildlines*](https://gist.github.com/PurpleBooth/b24679402957c63ec426) before you create any pull requests or issues. Though feel free to contribute in any form. <br> Open Source <3


##  :page_facing_up: Resources

- [Text Summarization](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/)
- [Data Retrieval with Web Scraping](https://www.kdnuggets.com/2018/07/practitioners-guide-processing-understanding-text-1.html)

## :star2: Present Contributors
[![Contributors](https://img.shields.io/github/contributors/codekhal/Inshorts-NLP?style=plastic)](https://github.com/codekhal/Inshorts-NLP/graphs/contributors)

### Want to share your ideas

`Feel free to reach out to me`

[![Telegram](https://img.shields.io/badge/Telegram-Chat-yellowgreen)](https://telegram.me/codekhal)

## :lock: License
[![License](https://img.shields.io/github/license/codekhal/Inshorts-NLP?style=plastic)](https://github.com/codekhal/Inshorts-NLP/blob/master/LICENSE)