import requests

url = "http://meta.vmfc.host:2095/api/playlist/videos/v1"

headers = {
    'Cookie': 'did=ec2c57610856;uid=114943;token=qZfQEorogY_RWJjGT2ahWCbGiNE3XqbMmZG6wdQn1lKS9XwEQ3EpXdO6TorPn_MzkTiyfVJe2zUfeJphFOMl3wHd5oebI0rvHk7QYHdrHJu3hmbSl19haMIgiL58qwDJUgso_TCJ3F18-gIHmIoom7Qee0pRtI1yo2uW2lImX4AL3Q8nLTimxOJa83vBeLQR7pFMkx5o2b5XW1yRqX50yrHyqqJe4hY0GXFRS1LfY6hj95mKgI5zvg0_6xpxdX8g',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '383',
    'Host': 'meta.vmfc.host:2095',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/2.7.2',
}

param = {
    'v': 4,
    'm': '3bgJScHT6AD0jGD32lPxhlNqZ3ERlwodON31XzSD4HbphtDlg1Ajhd1nPg4r2zL0UVkykDZ%2Bzkq5M7S0y3YK1faj00%2BoQHAlC00mJMmAP67kf506TJeaTYtw3Bb0pTmC3r6wAiRVzZ5C4CpPtoq%2Ffh45txW29Pp9kn0SeRkhKEY7hNzIbcKZTOccmYY2sDzdq9n2QYS%2BkwCnPIpZGr2%2FA4mZuJH%2B4sm%2BbqBfBy9XwmUYOtFKxdhHTHeHWvkmGaoEjZizwXARXkIr9AjbJ0JfthqxZbQ7J7VZit4H9jMR47IQ4PbNP8IRyzyHqOsd9P5K',
    's': '3b1d68da36aa9ad9550d3cdb2c58363491b90e56'
}

response = requests.post(url, headers=headers, params=param)
print(response)
