import re
import os
import time
from selenium_helper import SeleniumHelper
from ocr_prompter import OCRPrompter


def load_script(fn):
    with open(fn, 'r') as f:
        return "".join(f.readlines())

class MaiMaiHelper(SeleniumHelper):
    def __init__(self, phone: int, arguments):
        self.phone = phone
        self.arguments = arguments

    def start(self):
        self.load_driver()
        self.load_cookies()
        self.driver.get("https://maimai.cn/platform/login?to=https%3A%2F%2Fmaimai.cn%2Fent%2Fv41%2Frecruit%2Ftalents%3Ftab%3D1")

        done = input("Press Enter to continue once Logged...")
        self.save_cookies()

        done = input("Press Enter to begin scraping once search criteria has \nbeen added and search results are present...")
        ####
        #self.development()
        ####
        self.get_matching_candidates()
        ####

    def development(self):
        for i in range(25):
            fn = input("File name of script:").strip()
            params = input("Optional Parameters:").strip()
            if params and all([char in "0123456789" for char in params]):
                params = int(params)
            
            try:
                script = load_script("maimai_scripts/"+fn)
                resp = self.execute_script_with_params(script, params)
                print("---------------------->")
                print("Script Response:", resp)
            except Exception as e:
                print(e)

    def get_pdf_path(self, name):
        path = "/Users/lan/Downloads"
        try:
            os.listdir(path)
        except:
            path = "C:\\Users\\darkg\\Downloads"
            
        # Get full paths of all files in the directory
        full_paths = [os.path.join(path, f) for f in os.listdir(path)]

        # Sort by creation time
        files_sorted_by_ctime = sorted(full_paths, key=os.path.getctime)

        # Just the filenames (without full path), sorted
        filenames_sorted_by_ctime = [os.path.basename(f) for f in files_sorted_by_ctime]

        filename = filenames_sorted_by_ctime[-1]
        if "脉脉招聘" not in filename:
            return None
        if name not in filename:
            return None
        return filename

    def get_percentage(self, response: str) -> int:
        response = re.sub("\n", " ", response)
        words = response.strip().split(" ")
        words = [w.strip() for w in words if w.strip()]
        for w in words:
            if len(w) == 1:
                continue
            if not all([wi in "0123456789" for wi in w[:-1]]):
                continue
            return int(w[:-1])
        return None

    def get_match_percentage(self, name: str) -> int:
        pdf_path = self.get_pdf_path(name)

        ocr_prompter = OCRPrompter(self.arguments.job_description)
        print("About to extract text")
        text = ocr_prompter.extract_text_from_pdf(pdf_path)
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
        EVAL_PROMPT = re.sub("{INSTRUCTIONS}", self.arguments.instructions, EVAL_PROMPT)
        EVAL_PROMPT = re.sub("{JOB_DESCRIPTION}", self.arguments.job_description, EVAL_PROMPT)
        EVAL_PROMPT = re.sub("{CANDIDATE_INFORMATION}", text, EVAL_PROMPT)
        prompt = EVAL_PROMPT

        response = ocr_prompter.ask_GPT(prompt)
        print("\nAI response-------------------------->:")
        print(response)    
        if response == None:
            time.sleep(51)
            return None

        percentage = self.get_percentage(response)
        print(f"percentage: {str(percentage)}")
        if percentage == None:
            return None
        
        return percentage
            

    def get_matching_candidates(self):
        page = 1
        clicked_next_page = True
        while clicked_next_page == True:
            profile_count = self.execute_script_with_params_by_name("maimai_scripts/count_profiles.js", None)
            for i in range(profile_count):
                INSTRUCTIONS = self.load_script("maimai_scripts/INSTRUCTIONS.js")
                if INSTRUCTIONS.strip():
                    if "SLEEP10" in INSTRUCTIONS:
                        time.sleep(10)
                    if "SLEEP30" in INSTRUCTIONS:
                        time.sleep(30)
                    if "SLEEP60" in INSTRUCTIONS:
                        time.sleep(60)
                    if "RESTART" in INSTRUCTIONS:
                        inp = input("Press Enter when ready to restart:")
                        self.get_matching_candidates()
                        return
                    if "EXIT" in INSTRUCTIONS:
                        print("Exiting")
                        return
                    with open("maimai_scripts.js/INSTRUCTIONS.js", "w+") as f:
                        pass

                name = self.execute_script_with_params_by_name("maimai_scripts/get_name.js", i)
                if name == None:
                    raise Exception(f"Name was None for profile {str(i)}")
                
                print("clicking i'th profile")
                self.execute_script_with_params_by_name("maimai_scripts/click_profile.js", i)
                time.sleep(9)

                print("Downloading Resume")
                downloaded = self.execute_script_with_params_by_name("maimai_scripts/download_resume.js", None)
                time.sleep(4)
                
                if downloaded == False:
                    continue
                
                print("Switching to window 0")
                self.switch_to(0)
                time.sleep(4)
                
                match_pct = self.get_match_percentage(name)
                if match_pct == None:
                    print("Moving on to next candidate as match_pct is None")
                    continue

                if match_pct >= self.arguments.cutoff_pct:
                    print(f"About to add {name} with {str(match_pct)}% to {self.arguments.project_name}")
                    self.execute_script_with_params_by_name("maimai_scripts/click_folder.js", None)
                    time.sleep(3)

                    self.execute_script_with_params_by_name("maimai_scripts/click_project.js", None)
                    time.sleep(3)

                    self.execute_script_with_params_by_name("maimai_scripts/click_confirm.js", None)
                    time.sleep(3)

            clicked_next_page = self.execute_script_with_params_by_name("maimai_scripts/click_page.js", page)
            if clicked_next_page == False:
                print(f"clicked_next_page was false for {str(i)}")
                return 
            
            page += 1
            print(f"Setting page to {str(page)} and sleeping.")

            time.sleep(15)






