import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from .database import db


class Profile(db.Model):
    """Модель профиля пользователя.

    Vars:
        id (int): Идентификатор
        username (str): Имя пользователя.
        password (str): Пароль.
        name (str): Название компании.
        email (str): Почта.
        balance (int): Баланс.
        lines (obj): Подключенные к пользователю линии.
        calls (obj): Звонки пользователя.
        payment_accounts (obj): Счета пользователя.
        created_on (datetime): Дата регистрации.
    """
    __tablename__ = 'profiles'

    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    username = db.Column(
        db.String(32),
        index=True,
        unique=True
    )
    password = db.Column(
        db.String(128),
        nullable=False
    )
    name = db.Column(
        db.String(120),
        nullable=False
    )
    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True
    )
    balance = db.Column(
        db.Integer(),
        nullable=False
    )
    lines = db.relationship(
        'Lines',
        backref='profile',
        lazy='dynamic'
    )
    calls = db.relationship(
        'Calls',
        backref='profile',
        lazy='dynamic'
    )
    payment_accounts = db.relationship(
        'PaymentAccount',
        backref='profile',
        lazy='dynamic'
    )
    created_on = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )

    def __init__(
        self, username, password, name, email, balance,
    ):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.balance = balance

    def set_password(self, password):
        """Устанавливает и хэширует пароль пользователя.

        Args:
            password (str): Заданный пароль.
        Vars:
            password (str): Захэшированный пароль.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Проверяет введеннй пароль на соответствие устоновленному.

        Args:
            password (str): Пароль пользователя.

        Returns:
            (bool): Булеево значение совпадения паролей.
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<Profile %r>' % self.name


class Lines(db.Model):
    """Модель подключенных линий к пользователю.

    Vars:
        id (int): Идентификатор.
        profile_id (obj): Пользователь к которому подключена линия.
        type_of_line (int): Тип линии.
        cli (int): CLI.
        city (str): Город.
        tariff (str): Тариф.
    """
    __tablename__ = 'lines'

    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer(),
        db.ForeignKey('profiles.id'),
        nullable=False
    )
    type_of_line = db.Column(
        db.Integer(),
        nullable=False
    )
    cli = db.Column(
        db.Integer(),
        nullable=False
    )
    city = db.Column(
        db.String(120),
        nullable=False
    )
    tariff = db.Column(
        db.String(120),
        nullable=False
    )

    def __init__(
        self, profile_id, type_of_line, cli, city, tariff
    ):
        self.profile_id = profile_id
        self.type_of_line = type_of_line
        self.cli = cli
        self.city = city
        self.tariff = tariff

    def __repr__(self):
        return '<Lines %r>' % self.type_of_line


class Calls(db.Model):
    """Модель совершенных звонков.

    Vars:
        id (int): Идентификатор.
        profile_id (obj): Пользователь совершивший звонок.
        line_id (obj): Линия с которой был совершен звонок.
        direction (str): Направление звонка.
        date (datetime): Дата совершения звонка.
        duration (str): Продолжительность.
        cost (int): Стоимость.
    """
    __tablename__ = 'calls'

    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer,
        db.ForeignKey('profiles.id'),
        nullable=False
    )
    line_id = db.Column(
        db.Integer(),
        db.ForeignKey('lines.id'),
        nullable=False
    )
    direction = db.Column(
        db.String(120),
        nullable=False
    )
    date = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )
    duration = db.Column(
        db.Integer(),
        nullable=False
    )
    cost = db.Column(
        db.Integer(),
        nullable=False
    )

    def __init__(
        self, profile_id, line_id, direction, duration, cost
    ):
        self.profile_id = profile_id
        self.line_id = line_id
        self.direction = direction
        self.duration = duration
        self.cost = cost

    def __repr__(self):
        return '<Calls %r>' % self.direction


class PaymentAccount(db.Model):
    """Модель расчетных счетов пользователя.

    Vars:
        id (int): Идентификатор.
        profile_id (obj): Пользователь, которому выставлен счёт.
        account_number (int): Номер счета.
        service_name (str): Название услуги.
        date (datetime): Дата выставления счёта.
        adress (str): Адресс использования услуги.
        amount (int): Сумма счёта.
        status (bool): Статус, оплачен или нет.
    """
    __tablename__ = 'payment_accounts'

    id = db.Column(
        db.Integer(),
        primary_key=True
    )
    profile_id = db.Column(
        db.Integer(),
        db.ForeignKey('profiles.id'),
        nullable=False
    )
    account_number = db.Column(
        db.Integer(),
        nullable=False
    )
    service_name = db.Column(
        db.String(250),
        nullable=False
    )
    date = db.Column(
        db.DateTime(),
        default=datetime.datetime.now
    )
    adress = db.Column(
        db.Text(),
        nullable=False
    )
    amount = db.Column(
        db.Integer(),
        nullable=False
    )
    status = db.Column(
        db.Boolean(),
        nullable=False
    )

    def __init__(
        self, profile_id, account_number, service_name, adress, amount,
        status
    ):
        self.profile_id = profile_id
        self.account_number = account_number
        self.service_name = service_name
        self.adress = adress
        self.amount = amount
        self.status = status

    def __repr__(self):
        return '<PaymentAccount %r>' % self.account_number
