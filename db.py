from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# custom convection for naming index, unique

convection = {
    'ix': 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convection)
db = SQLAlchemy(metadata=metadata)
