from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.schema import UniqueConstraint
from flask_app.database import Base
from datetime import datetime
# Модели таблиц БД
class ReceiptModel(Base):
    __tablename__ = "receipts"
    id = Column(BigInteger, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone="UTC"), default=datetime.utcnow
    )
    fiscal_datetime = Column(TIMESTAMP(timezone="UTC"))
    company_inn = Column(String)
    company_name = Column(String)
    kktregid = Column(String)
    shiftnumber = Column(BigInteger)
    requestnumber = Column(BigInteger)
    fiscaldrivenumber = Column(String)
    fiscalsign = Column(BigInteger)
    fiscaldocumentnumber = Column(BigInteger)
    cashtotalsum = Column(BigInteger)
    ecashtotalsum = Column(BigInteger)
    totalsum = Column(BigInteger)
    nds18 = Column(BigInteger)
    nds10 = Column(BigInteger)
    nds0 = Column(BigInteger)
    ndsno = Column(BigInteger)
    ndscalculated18 = Column(BigInteger)
    ndscalculated10 = Column(BigInteger)
    addresstocheckfiscalsign = Column(String)
    receiptcode = Column(BigInteger)
    bsocode = Column(BigInteger)
    bankagentoperation = Column(String)
    banksubagentoperation = Column(String)
    operationtype = Column(BigInteger)
    taxationtype = Column(BigInteger)
    bankagentphone = Column(String)
    paymentagentphone = Column(String)
    operatorphonetotransfer = Column(String)
    operatorinn = Column(String)
    bankagentremuneration = Column(BigInteger)
    paymentagentremuneration = Column(BigInteger)
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


class OpenshiftModel(Base):
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


class CloseshiftModel(Base):
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


