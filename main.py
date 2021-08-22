from bs4 import BeautifulSoup
import requests
import re

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

for job in jobs:

    job_comp = job.find("h3", class_ = "joblist-comp-name").text
    job_comp = re.sub(r"\s\s", "", job_comp)

    job_skills = job.find("span", class_ = "srp-skills").text
    job_skills = re.sub(r"(\s\s|\n)", "", job_skills)

    job_date = job.find("span", class_ = "sim-posted").span.text
    job_date = re.sub(r"(\s\s|\n)", "", job_date)

    message = f"""
Job Company: {job_comp}
Skills necessary: {job_skills}
Date of posting: {job_date}"""

    print(message)