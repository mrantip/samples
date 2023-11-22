# для хрома

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# для файерфокса
fp = webdriver.FirefoxProfile()

fp.set_preference("intl.accept_languages", user_language)

актуальном считается вот это:

from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference("intl.accept_languages", user_language)
driver_browser = webdriver.Firefox(options=options)