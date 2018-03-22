from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import relationship

from persistence.base import Base


class ProcuringEntity(Base):
    __tablename__ = 'procuring_entity'

    id = Column(name='id', type_=BigInteger, primary_key=True, autoincrement=True)
    identifier_id = Column(name='identifier_id', type_=String(500))
    identifier_legal_name = Column(name='identifier_legal_name', type_=String(2000))
    identifier_scheme = Column(name='identifier_scheme', type_=String)
    tenders = relationship('Tender', back_populates='procuring_entity')

    def __str__(self):
        return """
        id: {};
        identifier_id: {};
        tender_id: {};
        indicator_checked: {};
        identifier_scheme: {}
        """.format(self.id, self.identifier_id, self.identifier_legal_name, self.identifier_scheme)
