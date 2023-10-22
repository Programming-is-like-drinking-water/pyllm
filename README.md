# 🎈 Streamlit + LLM

## Overview of the App

This app showcases a growing collection of LLM.

Current examples include:

- Login
- File Q&A
- 🔎 Related Resource Search
- 🦜 Problem Quick-Solved
- 🔗 Personalize Learning Plan
- 📝 Chat with feedback
- 📝Social_Platfrom

### Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps, do the following:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API key into the text box as follows:

```
OPENAI_API_KEY='xxxxxxxxxx'
```

## Run it locally

virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Login.py
