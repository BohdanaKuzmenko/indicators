from sqlalchemy import func
from sqlalchemy.ext import baked

from persistence.dao.base_dao import BaseDAO
from persistence.entities.tender import Tender


class TenderDAO(BaseDAO):
    def get_tender_by_id(self, tender_id: int):
        with self.session_scope() as session:
            bakery = baked.bakery()
            bq = bakery(lambda s: session.query(Tender))
            bq += lambda q: q.filter(Tender.id == tender_id)
            result = bq(session).params(tender_id=tender_id).all()
        return result

    def get_tenders(self):
        with self.session_scope() as session:
            bakery = baked.bakery()
            bq = bakery(lambda s: session.query(Tender))
            bq += lambda q: q.limit(10)
            result = bq(session).params().all()
        return result

    def get_last_modified_date(self):
        with self.session_scope() as session:
            bakery = baked.bakery()
            max_date_modified = func.max(Tender.date_modified).label('tesr')
            bq = bakery(lambda s: session.query(max_date_modified))
            print(bq)
            result = bq(session).params().one()
        return result