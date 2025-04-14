from selenium.webdriver.common.by import By

# Локаторы для страницы заказа
NAME_FIELD = By.CSS_SELECTOR, "input[placeholder='* Имя'"
SURNAME_FIELD = By.CSS_SELECTOR, "input[placeholder='* Фамилия']"
ADDRESS_FIELD = By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"
STATION_FIELD = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
PHONE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")

# Локаторы для второй страницы (с датой и сроком аренды)
DATE_FIELD = By.CSS_SELECTOR, "input[placeholder= '* Когда привезти самокат']"
DROPDOWN_FIELD = (By.XPATH, "//div[@aria-expanded='true']")
COLOR_SCOOTER_BLACK = By.ID, "black"
COLOR_SCOOTER_GREY = By.ID, "grey"
ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

# Локаторы для страницы подтверждения
ORDER2_BUTTON = (By.XPATH, "//button[text()='Да']")

# Локаторы для успешного сообщения
SUCCESS_MESSAGE = (By.XPATH, "//div[@class='success-message']")