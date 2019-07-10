# Neighborhood
### July 10th 2019
#### By **[Purity Sowayi]** (https://github.com/apwao)
## Description
This is a project that allows users to view various neighborhoods within their city and the businesses therein. The user creates a profile and then is allowed to post announcements such as new businesses and neighborhood activities. The user is also able to view announcements made by different people.
## User Stories:
* As a user, I would like to sign up and be authenticated.
* As a user, I would like to log into the application.
* As a user, I would like to create a profile.
* As a user, I would like to register a business.
* As a user, I would like to post an announcement. 
* As a user, I would like to view posts and businesses by other people
## BDD
|Behavior                      |Input                       |Output
|------------------------------|----------------------------|----------------------------------------
|User signs up                 | Enters details and submits | User's account is activated
|User logs into account        | Submits Login Information  | Redirected to homepage
|User registers a business     | Submits business details   | Business is registered under their neighborhood
|User creates a profile        | Submits profile form       | Creates a profile which they can view 
|User posts an announcement    |  Submits announcements     | Added to announcements 
## Setup/Installation Requirements
* Ensure git is intalled in your computer
* Use 'git clone' command to Clone and then unzip the repository from github, https://github.com/apwao/neighborhood.git
* Navigate to the cloned project through the terminal
* Create a virtual environment and install all dependencies in the requirements.txt file using the command 'pip install -r requirements.txt'
* Create a postgresql database
* Create an .env file in the root of the application and specify the environment variables required
* run migrations using the command 'python3.6 manage.py migrate'
* Run the command 'python3.6 manage.py runserver' to run the application
## Known Bugs
* No known bugs
## Technologies Used
* HTML
* CSS
* Git
* Django
* Bootstrap
* Heroku
## Support and contact details
Incase of any issues, ideas, questions or concerns, contact contributor at pasowayi@gmail.com.
In order to contribute to the code: Fork a copy of the repository, push changes to a branch called contributions. Issue a pull request to the contributor.
### License
Copyright (c) 2019 **Purity Sowayi**
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
