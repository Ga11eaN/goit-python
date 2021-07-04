from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, query
from sqlalchemy.sql.expression import select

Base = declarative_base()

engine = create_engine('sqlite:///personal-helper.db', echo=True)

session = Session(bind=engine)


class Contact(Base):

    __tablename__ = 'contacts'

    def __init__(self, name, phone='', address='', mail='', birthday='', note=''):
        self.name = name[:40]
        self.phone = phone[:12]
        self.address = address[:40]
        self.mail = mail[:20]
        self.birthday = birthday[:10]
        self.note = note[:200]

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    phone = Column(String(12), nullable=True)
    address = Column(String(40), nullable=True)
    mail = Column(String(20), nullable=True)
    birthday = Column(String(10), nullable=True)
    note = Column(String(200), nullable=True)


Base.metadata.bind = engine

# new_contact = Contact('Petro', '0936541553', 'Kyiv, Franka 55',
#                      'petro@gmail.com', '13.02.2008', 'hello world!!!')
# session.add(new_contact)
# session.commit()

for contact in session.query(Contact).all():
    print(contact.id, contact.name, contact.phone)


sel = select(Contact.address).where(Contact.address == 'Kyiv, Franka 55')
print(session.connection().execute(sel).fetchall())

for contact in session.query(Contact).filter(Contact.address.contains('Kyiv')):
    print(contact.id, contact.name, contact.phone, contact.address)

session.close()
