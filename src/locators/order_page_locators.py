from selenium.webdriver.common.by import By

# Локаторы для страницы заказа
NAME_FIELD = (By.NAME, "* Имя")
SURNAME_FIELD = (By.NAME, "* Фамилия")
ADDRESS_FIELD = (By.NAME, "* Адрес: куда привести заказ")
STATION_FIELD = (By.NAME, "* Станция метро")
PHONE_FIELD = (By.NAME, "* Телефон: на него позвонит курьер")
SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")

# Локаторы для второй страницы (с датой и сроком аренды)
DATE_FIELD = (By.NAME, "* Когда привезти самокат")
DROPDOWN_FIELD = (By.NAME, "* Срок аренды")
COLOR_FIELD = (By.NAME, "Цвет самоката")
ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

# Локаторы для страницы подтверждения
ORDER2_BUTTON = (By.XPATH, "//button[text()='Да']")

# Локаторы для успешного сообщения
SUCCESS_MESSAGE = (By.XPATH, "//div[@class='success-message']")