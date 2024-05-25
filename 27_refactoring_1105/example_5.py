# определим кортеж и распакуем его в переменные
http_response = (404, 'Page not found')
code, message = http_response
print(f'code: {code}, message: {message}')
