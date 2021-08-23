from bs4 import BeautifulSoup
import requests
import re
from colorama import Fore, Style

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

print("Put some skills that you are not familiar with (comma or space separated)")
unfamiliar_skills = (input("> ").replace(",", " ")).split()

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

print(Fore.LIGHTRED_EX + "JOBS THAT APPEARED A FEW DAYS AGO:" + Style.RESET_ALL)

for job in jobs:

    job_date = job.find("span", class_ = "sim-posted").span.text
    job_date = re.sub(r"(\s\s|\n)", "", job_date)

    if "few" in job_date:
        
        job_skills = job.find("span", class_ = "srp-skills").text
        job_skills = re.sub(r"(\s\s|\n)", "", job_skills)

        for _ in unfamiliar_skills:
            if _ in job_skills:
                break            

        else:
            job_info = job.header.h2.a["href"]

            job_comp = job.find("h3", class_ = "joblist-comp-name").text
            job_comp = re.sub(r"\s\s", "", job_comp)

            message = f"""
Job Company:    {job_comp}
Skills necessary:   {job_skills}
More info:  {Fore.BLUE + job_info + Style.RESET_ALL}"""

            print(message)

print("\n")