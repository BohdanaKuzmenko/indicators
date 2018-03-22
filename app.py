from persistence.connection.connection_manager import ConnectionManager
from persistence.dao.tender_dao import TenderDAO

_engine = ConnectionManager.create_db_engine()

tender_dao = TenderDAO()
for i in tender_dao.get_tenders():
    print(i)

tender_dao.get_last_modified_date()

