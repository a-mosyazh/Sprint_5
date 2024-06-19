from global_params import name, email


class ConstructorPage:  # Элементы страницы "Конструктор"
    bun_card = './/main//div[contains(@class, "menuContainer")]//ul[1]/a[1]/img'  # карточка первой булки в списке
    bun_tab = './/span[text()="Булки"]/parent::div'  # вкладка "Булки"
    sauce_tab = './/span[text()="Соусы"]/parent::div'  # вкладка "Соусы"
    filling_tab = './/span[text()="Начинки"]/parent::div'  # вкладка "Начинки"
    create_order_btn = './/button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    login_to_account_btn = './/button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт"


class LoginPage:  # Элементы страницы "Вход"
    login_link = './/a[text()="Войти"]'  # ссылка, ведущая на страницу "Вход"
    login_btn = './/button[text()="Войти"]'  # кнопка "Войти"
    password_field = './/form/fieldset[2]//input[@name="Пароль"]'  # поле "Пароль"
    email_field = './/form/fieldset[1]//input[@name="name"]'  # поле "Email"


class HeaderElement:  # Элементы хэдера страницы
    profile_btn = './/p[text()="Личный Кабинет"]'  # кнопка переходя в профиль
    constructor_btn = './/p[text()="Конструктор"]'  # кнопка "Конструктор"
    logo = '//*[contains(@class, "header__logo")]'  # лого


class ProfilePage:  # Элементы страницы Личный кабинет
    save_btn = './/button[text()="Сохранить"]'  # кнопка "Сохранить"
    logout_btn = './/button[text()="Выход"]'  # пункт "Выход"
    name_field = f'.//main//input[@value="{name}"]'  # поле "Имя"
    email_field = f'.//main//input[@value="{email}"]'  # поле "Логин"
    password_field = './/main//input[@type="password"]'  # поле "Пароль"


class RegistrationPage:  # Элементы страницы регистрации
    name_field = './/form/fieldset[1]//input[@name="name"]'  # поле "Имя"
    email_field = './/form/fieldset[2]//input[@name="name"]'  # поле "Email"
    password_field = './/form/fieldset[3]//input[@name="Пароль"]'  # поле "Пароль"
    register_btn = './/button[text()="Зарегистрироваться"]'  # кнопка "Зарегистрироваться"
