# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\rodgo\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://eltiempo.es')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#inputSearch')))\
    .send_keys('Madrid')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon.icon-search')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon_weather_s.icon.icon-local')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/a')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')
texto_columnas = texto_columnas.text

tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

horas = list()
temp = list()
v_viento = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'V_viento(km_h)':v_viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()

