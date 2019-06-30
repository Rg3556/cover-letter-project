import datetime
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

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

## BOBY CONTENTS
job_title = "Market research Intern"
skill_1 = "analytical" # = filtered_1 
skill_2 = "market reserch" # = filtered_2 
skill_3 = "communication" # = filtered_3 
intro_p = f"I want to express my immense interest in the opportunity of the {job_title} at {company_name}. I am a {user_status.lower()} in the {user_major} at NYU graduating in 2020. For this {job_title} position, I am excited to apply my market research and consumer behavior knowledge to real-world situations and learn valuable experience from industry professionals. I believe that my qualifications and educational pursuits are a great fit with the kind of candidate you company is looking for. Given my passion and knowledge, I would be able to contribute to this role immediately."
analytical_research = "I know this position requires strong analytical and research ability, and my previous research experiences strongly supported my competence. I worked as a research assistant in two psychology labs at Willamette University for three years and actively engaged in both experimental design and data analysis processes. The complicated experimental design procedure improved my skills of thorough design and organization and attention to details. The data analysis processes, including data coding, cleaning, analysis, visualization, and interpretation, gave me great opportunities to apply my statistical knowledge and strengthen my analytical skills. From my current master program, I have learned market research methods and design thinking, using interviews, focus groups, and other qualitative methods to achieve human-centered designs. I am trained to apply psychological theories to the marketing industry and be familiar with qualitative research and analysis as well."
communication = "Additionally, my communication skills gained good practice during my research experience. During the data collection, I have to understand the purpose of my supervisors and transmit correct information to experiment participants to gain expected and unbiased results. This training enhanced both my communication clarity and confidence."
global_leadership_communication = "My prior experience of running an international student council gave me an excellent exercise of both my communication skills and leadership, and provided me a global perspective."
software = "I feel comfortable working with Microsoft Office applications, such as Excel and Power Point, and analytical software, such as SPSS, SYSTAT and R."
multitasking = "I also developed the ability to multitask through balancing my schedule of different research projects, leadership position, and coursework."
ending_body = f"I feel strongly that my analytical and communication skills, consumer psychology background, and past research experience will make me an excellent fit for the role of Marketing Intern. My global cultural perspective can also contribute to this position. I would welcome the opportunity to discuss the position in further interview. Thank you for your time and consideration."
print("Dear HR Manager:")
print("")
print(intro_p)
print("")
# if "analytical" or "research" in job job_requirments:
#     print(analytical_research)
# print("")
# if "market" or "marketing" in job_requirments
#     
#     
#     print(f" During the data collection, I have to understand the purpose of my supervisors and transmit correct information to experiment participants to gain expected and unbiased results. This training enhanced both my communication clarity and confidence. My prior experience of running an international student council gave me an excellent exercise of both my communication skills and leadership, and provided me a global perspective. I feel comfortable working with Microsoft Office applications, such as Excel and Power Point, and analytical software, such as SPSS, SYSTAT and R. I also developed the ability to multitask through balancing my schedule of different research projects, leadership position, and coursework.")

print("")
print(ending_body)
## ENDING
end = f"""
Sincerely,
{user_name}
"""
print(end)


## Writing the output to a word document
### Attributed from: https://python-docx.readthedocs.io/en/latest/
doc = docx.Document()
# header = doc.add_heading(user_name, 0) 
header = doc.add_heading(user_name, 3)
header_contact = doc.add_heading("10 River rd, Apt 4N, New York, NY, 10044 | 646-243-0136 | rg@3556@nyu.edu", 8)
header.alignment = WD_ALIGN_PARAGRAPH.CENTER
header_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
# header_style = doc.styles['Normal']
# font = header_style.font
# font.name = 'Times New Roman'
# font.size = Pt(9)
# header_style_font = header_style.font
# header_style_font.name = 'Times New Roman'
# font.header_style_font = Pt(8)
# header_font = header.font
# header_font.size = Pt(10)
# header_font.name = 'Times New Roman'
# header_font.alignment = WD_ALIGN_PARAGRAPH.CENTER

p1 = doc.add_paragraph(start)
p2 = doc.add_paragraph("Dear HR Manager:")
p3 = doc.add_paragraph(intro_p)
p4 = doc.add_paragraph(ending_body)
# p4 = doc.add_paragraph(intro_p)
# p4 = doc.add_paragraph(intro_p)
# p4 = doc.add_paragraph(intro_p)
p4 = doc.add_paragraph(end)
doc.save(f'{company_name}-cover letter.docx')