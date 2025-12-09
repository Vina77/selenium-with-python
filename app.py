from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="msedgedriver.exe")
navegador = webdriver.Edge(service=service)

try:
    navegador.get("https://www.bing.com")

    try:
        botao_cookies = WebDriverWait(navegador, 5).until(
            EC.element_to_be_clickable((By.ID, "bnp_btn_accept"))
        )
        botao_cookies.click()
    except:
        pass

    elemento_busca = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    elemento_busca.send_keys("Cotação Dólar")
    elemento_busca.send_keys(Keys.RETURN)

    primeiro_resultado = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.b_focusTextSmall.curr_totxt"))
    )

    print("-" * 30)
    print(f"Cotação: {primeiro_resultado.text}")
    print("-" * 30)

    time.sleep(5)
except Exception as e:
    print("Erro detectado:", e)
finally:
    navegador.quit()