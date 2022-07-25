import requests
from Github import Github

class App:
    def menu(self):
        github=Github()
        while True:
            secim=input("1-Kullanıcı bul\n2-Repoları getir\n3-Repo oluştur\n4-Çıkış\n")

            if secim=="4":
                break
            else:
                if secim=="1":
                    username=input("kullanıcı adı giriniz:")
                    response=github.findUser(username)
                    response=response["login"]+"\n"+response["created_at"]
                    print(response)
                elif secim=="2":
                    username=input("kullanıcı adı giriniz:")
                    repos=github.getRepositories(username)
                    for repo in repos:
                        print(repo["name"]) 
                elif secim=="3":
                    name=input("Repo adını giriniz")
                    description=input("Açıklama giriniz")
                    result=github.createRepository(name,description)
                    print(result)
                else:
                    print("Hatali giriş tekrar deneyin")

app=App()
app.menu()