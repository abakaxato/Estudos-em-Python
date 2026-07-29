import requests as rq

res = rq.get('https://cep.awesomeapi.com.br/json/50010-000')
print('\n Resposta da api :\n' , res.json())
print('\n Cidade :\n',res.json()['city'])
print('\n tipo do dado do res\n',type(res))