from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.CLASS_NAME, 'name')
    PASSWORD = (By.CLASS_NAME, 'Пароль')
    #Кнопка личный кабинет
    LK_BUTTOM = (By.LINK_TEXT, 'Личный Кабинет')
    #Кнопка войти на главной старнице
    ENTER_BUTTON = (
    By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')
    #Кнопка войти из страницы авторизации
    ENT_BUTT_LOGIN = (
    By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')
    #ЛОГОТИП
    LOGO = (By.XPATH, '//a[@class = "active"]')
    #Кнопка конструктор
    BUTTON_CONSTR = (By.XPATH, '//li/a[@href = "/"]')
    #Кнопка Зарегистрироваться
    BUTTON_REGISTRATION = (By.XPATH, '//a[@href = "/register"]')
    #Поле ИМЯ
    INPUT_NAME_REG = (By.LINK_TEXT, 'Имя')
    #Поле емейл
    INPUT_EMAIL_REG = (By.LINK_TEXT, 'Email')
    #Поле пароль
    INPUT_PSW_REG = (By.CLASS_NAME, 'Пароль')
    #Кнопка восстановить пароль
    BUTTON_RECOV_PSW = (By.XPATH, '//a[@href = "/forgot-password"]')
    #Кнопка выход из ЛК
    BUTTON_EXIT = (By.CLASS_NAME, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive')
    #Хэдер Собирете бургер
    HEADER = (By.XPATH, '//main/section/h1')
    #Кнопка оформить заказ
    ORDER_BUTTON = (
    By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')
    #Хэдер Восстановление пароля
    HEADER_REC_PWD = (By.XPATH, '//div[@class= "Auth_login__3hAey"]/h2')
    # Хэдер Вход
    HEADER_ENT = (By.XPATH, '//div[@class= "Auth_login__3hAey"]/h2')
    #Поле с эмейлом в ЛК
    INPUT_LK = (By.XPATH, '//input[@type = "text" and @name = "name"]')
    #Уведомление о коротком пароле
    ATTENT_ERROR = (By.XPATH, '//p[@class = "input__error text_type_main-default"]')
    #Вкладка Начинки
    NACHINKA = (By.XPATH, '//section/div//div/span[text()="Начинки"]')
    #Вкладка Соусы
    SAUCE = (By.XPATH, '//section/div//div/span[text()="Соусы"]')
    #Вкладка Булки
    BULKA = (By.XPATH, '//section/div//div/span[text()="Булки"]')
    #Отображение начинки
    SECTION_NACHINKA = (By.XPATH,
                        '//section/div//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]')
    #Отображение соуса
    SECTION_SAUCE = (By.XPATH,
                     '//section/div//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]')
    #Отображение булок
    SECTION_BULKA = (By.XPATH,
                     '//section/div//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]')
