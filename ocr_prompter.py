import os
import dotenv
import re
import json
import time
import openai

from ocr_parser import extract_text_from_pdf
from openai_requests import ask_GPT


class OCRPrompter(object):
    def __init__(self, job_description):
        self.desc = "Uses text extracted from OCR to prompt OpenAI models"
        self.job_description = job_description

    def extract_text_from_pdf(self, pdf_path):
        # FULL PATH
        text = extract_text_from_pdf(pdf_path)
        return text

    def ask_GPT(self, prompt):
        try:
            response = ask_GPT(prompt, "gpt-4o-mini")
        except Exception as e:
            print("Error on ask_GPT. Possible rate limit.")
            return None
        return response



    def __ai_eval_candidate(self, pdf_path, instructions):
        # Depreciated due to bad dependency / factoring of functionality... unused in project
        text = self.extract_text_from_pdf(pdf_path)
        print("text extracted from candidate pdf-------------------------------------->")
        print(text)
        
        EVAL_PROMPT = """
{INSTRUCTIONS}

Job Description:
``````
{JOB_DESCRIPTION}
``````

Candidate Information:
``````
{CANDIDATE_INFORMATION}
``````
"""
        EVAL_PROMPT = re.sub("{INSTRUCTIONS}", instructions, EVAL_PROMPT)
        EVAL_PROMPT = re.sub("{JOB_DESCRIPTION}", self.job_description, EVAL_PROMPT)
        EVAL_PROMPT = re.sub("{CANDIDATE_INFORMATION}", text, EVAL_PROMPT)
        #prompt = re.sub("{EXTRACTED_TEXT}", text, )
        prompt = EVAL_PROMPT

        try:
            response = ask_GPT(prompt, "gpt-4o-mini")
        except Exception as e:
            print("Error on ask_GPT. Possible rate limit.")
            return None
        

        return response

