from sqlalchemy import BigInteger, Boolean, Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from persistence.base import Base
from .procuring_entity import ProcuringEntity


class Tender(Base):
    __tablename__ = 'tender'

    id = Column(name='id', type_=BigInteger, primary_key=True, autoincrement=True)
    outer_id = Column(name='outer_id', type_=String)
    tender_id = Column(name='tender_id', type_=String)
    indicator_checked = Column(name='indicator_checked', type_=Boolean)
    status = Column(name='status', type_=String)
    date = Column(name='date', type_=DateTime)
    date_modified = Column(name='date_modified', type_=DateTime)
    procurement_method_type = Column(name='procurement_method_type', type_=String)
    procurement_method = Column(name='procurement_method', type_=String)
    procuring_entity_id = Column('procuring_entity_id', BigInteger, ForeignKey('procuring_entity.id'))
    procuring_entity = relationship('ProcuringEntity')

    def __str__(self):
        return """
        id: {};
        outer_id: {};
        tender_id: {};
        indicator_checked: {};
        status: {};
        date: {};
        date_modified: {};
        procurement_method_type: {};
        procurement_method: {};
        procuring_entity_id:{};
        """.format(self.id, self.outer_id, self.tender_id, self.indicator_checked,  self.status, self.date,
                   self.date_modified, self.procurement_method_type, self.procurement_method, self.procuring_entity_id)
