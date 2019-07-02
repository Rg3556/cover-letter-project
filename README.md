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
    # pip install requests
    pip install python-dotenv
    # pip install pandas
    # pip install -r requirements.txt #> (loads contents of the .env file into the script's environment, and for Mail # and SMS messages)
    pip install pytest # (only if you'll be writing tests)
    

## Usage ##

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

    python job.py

