# закрытие сообщения о том что браузер запущен в отладочном режиме
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])

# уменьшение размера изображения в 0.8 раза
browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.8)"')