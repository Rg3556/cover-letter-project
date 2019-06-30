import datetime


## user profile
user_name = "Ruolin Gou"
user_status = "Master's student"
user_major = "Social and Consumer Psychology Program"

## STARTING
# March, 30th, 2019
today = datetime.date.today()
F_today = today.strftime("%B, %d, %Y")
# print(F_today)

company_name = "Phoenix Marketing International"
company_address_1 = "1430 Broadway, 19th Floor" 
company_address_2 = "New York, NY 10018"

start = f""" 
{F_today}

{company_name}
{company_address_1}
{company_address_2}
"""
print(start)

## CONTENTS
job_title = "Market research Intern"
skill_1 = "analytical" # = filtered_1 
skill_2 = "market reserch" # = filtered_2 
skill_3 = "communication" # = filtered_3 
print("Dear HR Manager:")
print("")
print(f"I want to express my immense interest in the opportunity of the {job_title} at {company_name}. I am a {user_status.lower()} in the {user_major} at NYU graduating in 2020. For this {job_title} position, I am excited to apply my market research and consumer behavior knowledge to real-world situations and learn valuable experience from industry professionals. I believe that my qualifications and educational pursuits are a great fit with the kind of candidate you company is looking for. Given my passion and knowledge, I would be able to contribute to this role immediately.")
print("")
print(f"The value I will bring to your organization includes a strong skill set which I have developed through my academic experiences. I know a {job_title} position requires strong {skill_1}, {skill_2}, and {skill_3} skills, and my previous research experiences strongly supported my competence. I worked as a research assistant in two labs at Willamette University for three years. I was actively engaged in both data collection and analysis processes. My communication skills got good practice on understanding the purpose of my supervisors and transmitting correct information to experiment participants and staff to gain expected and unbiased results. Additionally, the data analysis processes, including data coding, cleaning, analysis, visualization, and interpretation, gave me opportunities to apply my statistical knowledge and strengthen my analytical skills. I feel comfortable working with basic Microsoft office products, such as Excel and PPT, and analytical software, such as SYSTAT and R. I also developed the ability to multitask through balancing my schedule of different research projects, leadership position, and coursework. From my current master program, I am trained to apply psychological theories to the marketing industry and be familiar with qualitative research and analysis as well.")
print("")
print(f"Additionally, my prior experience of running an international student council gave me the excellent practice of both my communication skills and leadership and provided me a global perspective. I also developed the ability to multitask through balancing my schedule of different research projects, leadership position, and coursework.")
print("")
print(f"I feel strongly that my analytical and communication skills, consumer psychology background, and past research experience will make me an excellent fit for the role of Marketing Intern. My global cultural perspective can also contribute to this position. I would welcome the opportunity to discuss the position in further interview. Thank you for your time and consideration.")
## ENDING
end = f"""
Sincerely,
{user_name}
"""
print(end)
