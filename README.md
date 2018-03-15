# LinkedIn Profile Retriever

This project automates LinkedIn OAuth2 authentication process in a Python Flask Web App. It processes steps listed at https://developer.linkedin.com/docs/oauth2, to retrieve a user's LinkedIn profile information.

# Run the project locally

* Set the redirect uri in your LinkedIn application to https://localhost:5000/oauth/callback
* Download the project. 
  In index.html, change '{client_id}', '{redirect_uri}' and '{scope}' to what your LinkedIn application sets to. 
  In main.py, change {client_id}, {client_secret} to what your application sets to.
  Note if you need full profile info, your need to request r_fullprofile permission from LinkedIn Developers.
* Create an ssl cert. Place server.crt and server.key in a directory named "ssl" under the root directory. See reference http://www.daveoncode.com/2017/05/16/python-recipe-run-flask-app-locally-in-https/
* Run it by hitting F5 in Visual Studio, point your browser to https://localhost:5000

# Python Flask app on Azure App Service Web

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service Web.

This repository can directly be deployed to Azure App Service.

For more information, please see the [Python on App Service Quickstart docs](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python).

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
