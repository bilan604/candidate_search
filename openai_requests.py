import os
import time
from dotenv import load_dotenv
load_dotenv()

import openai


openai.api_key = os.environ.get("OPENAI_API_KEY")


def ask_GPT(query, model="gpt-4o-mini"):
    ans = None
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}]
        )
        ans = response.choices[0].message.content.strip()
    except Exception as e:
        print("\nError Occured when making request to OpenAI:")
        print(e)
        print("<----------------------------------------------")
        print("Sleeping for 10 seconds due to error")
        time.sleep(10)
    return ans

