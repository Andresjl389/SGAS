from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from sqlmodel import SQLModel

from Dominio.Entidades.Usuario.usuario import Usuario
from Dominio.Entidades.Usuario.roles import Roles
from Dominio.Entidades.Usuario.estado_usuario import Estado_Usuario
from Dominio.Entidades.Sesion.sesion import Sesion
from Dominio.Entidades.Reserva.estado_reserva import Estado_Reserva
from Dominio.Entidades.Reserva.reserva import Reserva
from Dominio.Entidades.Registro.solicitud_registro import Solicitud_Registro
from Dominio.Entidades.Registro.estado_solicitud_registro import Estado_Solicitud_Registro
from Dominio.Entidades.Notificaciones.notificaciones import Notificaciones
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula

from Infraestructura.Configuracion.configuracion import URL
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", URL)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
