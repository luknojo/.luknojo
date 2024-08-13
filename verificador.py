import requests

def verificar_sql_injection(url):
    payloads = ["'", '"', "or 1=1", "or 'a'='a"]
    for payload in payloads:
        nova_url = url + payload
        resposta = requests.get(nova_url)
        if "SQL" in resposta.text or "syntax" in resposta.text:
            print(f"Vulnerabilidade de SQL Injection detectada com o payload: {payload}")
        else:
            print(f"Não vulnerável ao payload: {payload}")

if __name__ == "__main__":
    url = input("Digite a URL a ser verificada: ")
    verificar_sql_injection(url)
