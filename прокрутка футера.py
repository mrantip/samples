# чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу.
# После выполнения кода элемент button должен оказаться в верхней части страницы.
# Подробнее о методе см https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView .

# Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")

# прям удалить
browser.element('footer').execute_script('element.remove()')
browser.element('#submit').perform(command.js.click)

# удалить рекламу
browser.execute_script('document.querySelector("#fixedban").remove()')
browser.element('footer').execute_script('element.remove()')

browser.element('#submit').execute_script('element.click()')