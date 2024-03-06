import peewee

db = peewee.SqliteDatabase("craftyllamabot.db")


ADIMN_LIST = [
    "nyle_",
    "mclarz",
]


class User(peewee.Model):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField(unique=True)
    is_admin = peewee.BooleanField(default=False)

    class Meta:
        database = db


class Message(peewee.Model):
    id = peewee.PrimaryKeyField()
    user = peewee.ForeignKeyField(User, backref="messages")
    content = peewee.TextField()
    created_at = peewee.DateTimeField(
        constraints=[peewee.SQL("DEFAULT CURRENT_TIMESTAMP")]
    )

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([User, Message], safe=True)

    with db.atomic():
        for admin in ADIMN_LIST:
            _, created = User.get_or_create(username=admin, is_admin=True)
            if created:
                print(f"Created admin user: {admin}")
            else:
                print(f"Admin user: {admin}")


initialize_db()
