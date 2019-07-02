from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, SmallInteger
from sqlalchemy.schema import UniqueConstraint
from flask_app.app import db

# Модели таблиц БД
class ReceiptModel(db.Model):
    __tablename__ = "receipts"
    id = Column(BigInteger, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone="UTC"), default=datetime.utcnow
    )
    fiscal_datetime = Column(TIMESTAMP(timezone="UTC"))
    company_inn = Column(String)
    company_name = Column(String)
    kktregid = Column(String)
    shiftnumber = Column(Integer)
    requestnumber = Column(Integer)
    fiscaldrivenumber = Column(String)
    fiscalsign = Column(Integer)
    fiscaldocumentnumber = Column(BigInteger)
    cashtotalsum = Column(BigInteger) #т.к. в значение в копейках, а чек может быть выше 21млн
    ecashtotalsum = Column(BigInteger)
    totalsum = Column(BigInteger)
    nds18 = Column(Integer)
    nds10 = Column(Integer)
    nds0 = Column(Integer)
    ndsno = Column(Integer)
    ndscalculated18 = Column(Integer)
    ndscalculated10 = Column(Integer)
    addresstocheckfiscalsign = Column(String)
    receiptcode = Column(SmallInteger)
    bsocode = Column(SmallInteger)
    bankagentoperation = Column(String)
    banksubagentoperation = Column(String)
    operationtype = Column(SmallInteger)
    taxationtype = Column(SmallInteger)
    bankagentphone = Column(String)
    paymentagentphone = Column(String)
    operatorphonetotransfer = Column(String)
    operatorinn = Column(String)
    bankagentremuneration = Column(SmallInteger)
    paymentagentremuneration = Column(SmallInteger)
    operator = Column(String)
    operatorname = Column(String)
    banksubagentphone = Column(String)
    paymentsubagentphone = Column(String)
    senderaddress = Column(String)
    operatorphonetoreceive = Column(String)
    retailplaceaddress = Column(String)
    __table_args__ = (
        UniqueConstraint(
            "fiscaldrivenumber",
            "fiscalsign",
            "fiscaldocumentnumber",
            name="_receipts_uniq",
        ),
    )


class OpenshiftModel(db.Model):
    __tablename__ = "openshift"
    id = Column(BigInteger, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone="UTC"), default=datetime.utcnow
    )
    company_inn = Column(String)
    company_name = Column(String)
    operator = Column(String)
    retailplaceaddress = Column(String)
    open_datetime = Column(TIMESTAMP(timezone="UTC"))
    shiftnumber = Column(BigInteger)
    kktregid = Column(String)
    fiscaldrivenumber = Column(String)
    fiscaldocumentnumber = Column(BigInteger)
    fiscalsign = Column(BigInteger)
    __table_args__ = (
        UniqueConstraint(
            "fiscaldrivenumber",
            "fiscalsign",
            "fiscaldocumentnumber",
            name="_openshift_uniq",
        ),
    )


class CloseshiftModel(db.Model):
    __tablename__ = "closeshift"
    id = Column(BigInteger, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone="UTC"), default=datetime.utcnow
    )
    company_inn = Column(String)
    company_name = Column(String)
    operator = Column(String)
    close_datetime = Column(TIMESTAMP(timezone="UTC"))
    shiftnumber = Column(BigInteger)
    receiptsquantity = Column(BigInteger)
    documentsquantity = Column(BigInteger)
    nottransmitteddocumentsquantity = Column(BigInteger)
    nottransmitteddocumentsdatetime = Column(
        TIMESTAMP(timezone="UTC")
    )
    ofdresponsetimeoutsign = Column(
        TIMESTAMP(timezone="UTC")
    )
    fiscaldrivereplacerequiredsign = Column(BigInteger)
    kktregid = Column(String)
    fiscaldrivenumber = Column(String)
    fiscaldocumentnumber = Column(BigInteger)
    fiscalsign = Column(BigInteger)
    __table_args__ = (
        UniqueConstraint(
            "fiscaldrivenumber",
            "fiscalsign",
            "fiscaldocumentnumber",
            name="_closeshift_uniq",
        ),
    )
