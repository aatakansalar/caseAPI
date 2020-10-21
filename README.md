# CaseAPI

*Summarify Case Study Projesi*

Hazır bir transformer modelini* kullanarak Türkçe metinleri olumlu - olumsuz
olarak etiketleyen bir API 

#### Docker Build 
Docker Image'ini oluşturmak için `docker build -t caseAPI .` komutu kullanılabillir. Image'imiz oluşturulacak, sonrasında da bir container olarak çalıştırılacaktır.

Image'den bir container oluşturup arkaplanda çalıştırmak için ise
`docker run --publish 8000:8080 --detach caseAPI` komutu kullanılabilir.  

Sonrasında `http://localhost:8000` adresinden API'ımıza ulaşılabilir, `http://localhost:8000/docs` adresindense dokümantasyonu görülebilir.  

Ayrıca bu image `docker pull aatakansalar/caseapi` komutuyla indirilebilir.  


---
#### API Kullanımı

##### Status
CaseAPI'ın çalıştığından emin olmak için, `http://localhost:8000/status` adresine
bir `get` isteği atılabilir. 

##### Değerlendirme Operasyonları
CaseAPI ile bir metni değerlendirmek için `http://localhost:8000/argument`
adresine bir `post` sorgusu yapılmalı. Sorguda etiketlenmesini istediğimiz
metni de parametre olarak eklemeliyiz. Bu parametremizin biçimi de `{"body": "Metin..."}` 
şeklinde bir dictionary olmalıdır.

Bunu bir python betiğinde şu şekilde yapabiliriz:
```` python
import requests
argument = {"body": "Bu film hayatımda izlediğim en kötü filmdi."}
response = requests.post("http://localhost:8000/argument", json = argument)

print(response.status_code) 
# Çıktı: 200

print(response.json()) 
# Çıktı: {'body': 'Bu film hayatımda izlediğim en kötü filmdi.', 'evaluation': {'label': 'negative', 'score': 0.9983533024787903}}
````

Birbirinden bağımsız birden çok metni tek bir sorguyla değerlendirmek için ise 
`http://localhost:8000/arguments` adresine yine bir `post` sorgusu yapılmalı. Sorgumuzda 
etiketlenmesini istediğimiz metinlerimizi de sorgumuzla iliştirmeliyiz. Bu parametrenin biçimi de
`{"argList": [{"body":"Metin..."},{"body":"Metin..."},{"body":"Metin..."}]}` şeklinde 
olmalıdır.

Bunu bir python betiğinde şu şekilde yapabiliriz:

```` python
import requests
arguments = {
    "argList": [
        {"body": "Bu film hayatımda izlediğim en kötü filmdi."},
        {"body": "Ne kadar güzel bir kitaptı."},
        {"body": "Servis çok kötüydü, yemekler soğumuştu."},
    ]
}
response = requests.post("http://3.131.38.243:8080/arguments", json = arguments)
print(response.status_code)
# Çıktı: 200

print(response.json())
# Çıktı: {'evaluations': [{'body': 'Bu film hayatımda izlediğim en kötü filmdi.', 'evaluation': {'label': 'negative', 'score': 0.9983533024787903}}, {'body': 'Ne kadar güzel bir kitaptı.', 'evaluation': {'label': 'positive', 'score': 0.9754379391670227}}, {'body': 'Servis çok kötüydü, yemekler soğumuştu.', 'evaluation': {'label': 'negative', 'score': 0.9993332028388977}}]}
````  

###### Kullanılan Transformer Modeli
- https://huggingface.co/savasy/bert-base-turkish-sentiment-cased
