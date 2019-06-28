import os
from pprint import pprint
from dotenv import load_dotenv
from linkedin_v2 import linkedin
import webbrowser

load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

#PERMISSIONS = linkedin.PERMISSIONS.enums.values() # trying to use all these permissions leads to errors
#> dict_values(['rw_company_admin', 'r_basicprofile', 'r_fullprofile', 'r_emailaddress', 'r_network', 'r_contactinfo', 'rw_nus', 'rw_groups', 'w_messages'])
PERMISSIONS = ["r_emailaddress", "r_liteprofile", "w_member_social"] # ["r_basicprofile"]

def user_get_token():
    #
    # GET AN AUTH CODE
    #
    CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "OOPS")
    CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "OOPS")
    REDIRECT_URL = os.environ.get("LINKEDIN_REDIRECT_URL", "http://localhost:8000")
    #print(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)

    auth = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, PERMISSIONS)
    #print(type(auth)) #> <class 'linkedin_v2.linkedin.LinkedInAuthentication'>
    #print(auth.authorization_url)

    webbrowser.open_new(auth.authorization_url)
    # login, grant permissions, then you'll be redirected to a localhost url.
    # ... observe the "code" parameter, and enter it below
    # ... making sure to remove the "state" parameter part of the url, which might come at the end
    auth_code = input("The auth code was:")

    auth.authorization_code = auth_code

    #
    # GET AN ACCESS TOKEN
    #

    access_token = auth.get_access_token() # this is an AccessToken object with a access_token property, which should be stored in the env var

    return access_token

if __name__ == "__main__":

    print("----------------")
    print("GETTING TOKEN...")
    if LINKEDIN_ACCESS_TOKEN:
        token = LINKEDIN_ACCESS_TOKEN
    else:
        token = user_get_token()
    print(token) # store in environment variable!

    print("----------------")
    print("INITIALIZING APP...")
    client = linkedin.LinkedInApplication(token=token)
    print(type(client))

    print("----------------")
    print("GETTING PROFILE...")
    profile = client.get_profile()
    pprint(profile)

    #>{
    #>    'firstName': {
    #>        'localized': {'en_US': 'Polly'},
    #>        'preferredLocale': {'country': 'US', 'language': 'en'}
    #>    },
    #>    'id': '987zyx',
    #>    'lastName': {
    #>        'localized': {'en_US': 'Professor'},
    #>        'preferredLocale': {'country': 'US', 'language': 'en'}
    #>    },
    #>    'localizedFirstName': 'Polly',
    #>    'localizedLastName': 'Professor',
    #>    'numConnections': 0,
    #>    'profilePicture': {'displayImage': 'urn:li:digitalmediaAsset:456plk'}
    #>}