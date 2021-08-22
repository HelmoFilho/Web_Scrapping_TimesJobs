from bs4 import BeautifulSoup
import requests
import re

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

job = soup.find("li", class_ = "clearfix job-bx wht-shd-bx")

job_comp = job.find("h3", class_ = "joblist-comp-name").text
job_comp = re.sub(r"\s\s", "", job_comp)

job_skills = job.find("span", class_ = "srp-skills").text
job_skills = re.sub(r"\s\s", "", job_skills)
print(job_skills)