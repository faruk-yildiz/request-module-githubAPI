import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token="" #Github access token alanı
    def findUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
    def createRepository(self,name,description):
        jsonData={
            "name":name,
            "description":description,
            "homepage":"https:github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        }
        response=requests.post(self.api_url+"/user/repos?access_token="+self.token,json=jsonData)
        return response.json()