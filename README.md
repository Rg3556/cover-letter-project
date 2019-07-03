# cover-letter-project
 This project aim to allow users to automatically get an appropriate-formatted cover letter by input the website url of a LinkedIn job position.


## Prerequisites ##
- Anaconda 3.7    
- Python 3.7
- Pip
- Chromedriver 



## Setup ##

### Repo Setup/Installation

Visit the source code repository for the Rg3556's cover letter project [github source]: (https://github.com/Rg3556/cover-letter-project) and click "Fork" to copy the repo under your own control.

Then download (or "clone") your copy of the repo onto your local computer using GitHub Desktop or the command-line. Choose a familiar download location like the Desktop.
    
    https://github.com/Rg3556/cover-letter-project.git # this is the HTTP address, but you could alternatively use the SSH address
    

Then use your command line application (Mac Terminal or Windows Git Bash) to navigate to the location where you downloaded this repo.

    cd ~/Desktop/robo-advisor


Open the repo with your text editor (VS Code), and follow the instruction of the repo's "README.md" file to do the following setup.

### Chromedriver  Setup

Download chromedriver from http://chromedriver.chromium.org/downloads and replace the path (E:\Python scripts\chromedriver) with where you download it in the job.py.
  
    driver = webdriver.Chrome('E:\Python scripts\chromedriver')

### Environment Setup

Create and activate a new Anaconda virtual environment:

    
    conda create -n letter-env python=3.7 # (first time only)
    conda activate letter-env
    

From within the virtual environment, install Python package dependencies:
    
    pip install selenium
    pip install python-docx 
    pip install python-dotenv
    pip install pytest # (only if you'll be running tests)
    

## Usage ##

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

    python template.py

The system will ask you for a valid URL input. Please choose a random market-research related job or internship on LinkedIn, and copy and paste the job URL.

Then, you will get a cover letter created based on different key words filtered from the job description showing on the command-line screen. You will also automatically get a Microsoft version of this cover letter with additional header inside the cover letter, which named by the company's name.  

## Automated tests 

From within the virtual environment, run the Python script from the command-line:

    python test.py
