#GitHub Social Graph Backend

This backend application uses the GitHub API to retrieve information about GitHub users, such as their followers and social graph connections. Follow the steps below to set up and run the project locally.

##Steps to Set Up the Application Locally

    1. Clone the Repository
Clone this repository to your local machine:
       git clone <repository_url>
       cd <repository_name>
       
    2. Create and Activate a Virtual Environment
Create a virtual environment and activate it:
       python -m venv venv
       source venv/bin/activate # On Windows: .\venv\Scripts\activate
       
    3. Install Dependencies
Install the required Python packages:
       pip install -r requirements.txt
       
    4. Set Up Environment Variables
Create an API token in Git and set it in the config
       GITHUB_API_TOKEN=<your_personal_access_token>
       
    5. Run the Server
Start the FastAPI server using the following command
       python -m uvicorn backend.main:app --reload --port 5000
       
    6. Access the API
Open your browser, command line or Postman and access the API at http://127.0.0.1:5000.


##Application Logic
Base URL: http://127.0.0.1:5000/api/v1
1. GET /github/{username}
    • Purpose: Retrieve the list of followers for a specific GitHub user.
    • Parameters:
        ◦ username (string, required): GitHub username.
    • Logic:
        ◦ Sends a request to the GitHub API to fetch the followers of the given username.
        ◦ Returns a list of followers, including their login and avatar URLs.
    • Example:
        ◦ Request:
GET http://127.0.0.1:5000/api/v1/github/pe4ka1234
        ◦ Response:
   
          [
              {
                  "login": "follower1",
                  "avatar_url": "https://avatars.githubusercontent.com/u/12345?v=4"
              },
              {
                  "login": "follower2",
                  "avatar_url": "https://avatars.githubusercontent.com/u/67890?v=4"
              }
          ]
   
3. GET /github/social_graph/{username}
    • Purpose: Build a social graph for a GitHub user up to a specified depth.
    • Parameters:
        ◦ username (string, required): GitHub username.
        ◦ depth (integer, optional, default: 1): Depth of the social graph.
    • Logic:
        ◦ Recursively retrieves the followers for the specified user.
        ◦ Builds a nested graph of followers and their followers up to the defined depth.
    • Example:
        ◦ Request:
GET http://127.0.0.1:5000/api/v1/github/social_graph/pe4ka1234?depth=2
        ◦ Response:
   
          {
              "login": "pe4ka1234",
              "followers": [
                  {
                      "login": "follower1",
                      "avatar_url": "https://avatars.githubusercontent.com/u/12345?v=4",
                      "followers": []
                  },
                  {
                      "login": "follower2",
                      "avatar_url": "https://avatars.githubusercontent.com/u/67890?v=4",
                      "followers": [
                          {
                              "login": "nested_follower",
                              "avatar_url": "https://avatars.githubusercontent.com/u/98765?v=4",
                              "followers": []
                          }
                      ]
                  }
              ]
          }
5. GET /github/hello/{name}
    • Purpose: A simple health check endpoint to verify server functionality.
    • Parameters:
        ◦ name (string, required): Your name.
    • Logic:
        ◦ Returns a greeting message.
    • Example:
        ◦ Request:
GET http://127.0.0.1:5000/api/v1/github/hello/John
        ◦ Response:
          {
              "message": "Hello John"
          }
## link to the workspace:
https://sdf333-4106.postman.co/workspace/sdf-Workspace~09359a82-6160-481f-b1d1-daca601dd886/collection/39826827-d9a49929-b947-441e-9168-8837a8176e4b?action=share&creator=39826827
