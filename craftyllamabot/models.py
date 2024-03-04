import peewee

db = peewee.SqliteDatabase("craftyllamabot.db")


class User(peewee.Model):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField(unique=True)
    email = peewee.CharField(unique=True)
    is_admin = peewee.BooleanField(default=False)

    class Meta:
        database = db
