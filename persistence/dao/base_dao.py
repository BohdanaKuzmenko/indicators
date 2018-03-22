from contextlib import contextmanager

from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from persistence.connection.connection_manager import ConnectionManager


class BaseDAO(object):
    _ACTIVE_STATUS = 'active'
    _ALLOWED_TITLES = ['Associate', 'Counsel', 'Partner']

    def __init__(self):
        self._engine = ConnectionManager.create_db_engine()
        self.Session = sessionmaker(bind=self._engine, expire_on_commit=False)

        @event.listens_for(self._engine, "engine_connect")
        def ping_connection(connection, branch):
            if branch:
                return
            save_should_close_with_result = connection.should_close_with_result
            connection.should_close_with_result = False
            try:
                connection.scalar(select([1]))
            except exc.DBAPIError as err:
                if err.connection_invalidated:
                    connection.scalar(select([1]))
                else:
                    raise
            finally:
                connection.should_close_with_result = save_should_close_with_result

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


