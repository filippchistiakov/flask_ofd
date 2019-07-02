from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, Integer
from main_app import db

######## Кастомные поля

###Модели таблиц БД
class ReceiptModel(db.Model):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone='UTC'), default=datetime.utcnow
    )
    fiscal_datetime = Column(TIMESTAMP(timezone='UTC'))
    company_inn = Column(String)
    company_name = Column(String)
    kktregid = Column(String)
    shiftnumber = Column(Integer)
    requestnumber = Column(Integer)
    fiscaldrivenumber = Column(String)
    fiscalsign = Column(Integer)
    fiscaldocumentnumber = Column(Integer)
    cashtotalsum = Column(Integer)
    ecashtotalsum = Column(Integer)
    totalsum = Column(Integer)
    nds18 = Column(Integer)
    nds10 = Column(Integer)
    nds0 = Column(Integer)
    ndsno = Column(Integer)
    ndscalculated18 = Column(Integer)
    ndscalculated10 = Column(Integer)
    addresstocheckfiscalsign = Column(String)
    receiptcode = Column(Integer)
    bsocode = Column(Integer)
    bankagentoperation = Column(String)
    banksubagentoperation = Column(String)
    operationtype = Column(Integer)
    taxationtype = Column(Integer)
    bankagentphone = Column(String)
    paymentagentphone = Column(String)
    operatorphonetotransfer = Column(String)
    operatorinn = Column(String)
    bankagentremuneration = Column(Integer)
    paymentagentremuneration = Column(Integer)
    operator = Column(String)
    operatorname = Column(String)
    banksubagentphone = Column(String)
    paymentsubagentphone = Column(String)
    senderaddress = Column(String)
    operatorphonetoreceive = Column(String)
    retailplaceaddress = Column(String)
    def __init__(self, **kwargs):
        for arg in kwargs:
            self.arg = kwargs[arg]


class OpenshiftModel(db.Model):
    __tablename__ = 'openshift'
    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone='UTC'), default=datetime.utcnow
    )
    company_inn = Column(String)
    company_name = Column(String)
    operator = Column(String)
    retailplaceaddress = Column(String)
    open_datetime = Column(TIMESTAMP(timezone='UTC'))
    shiftnumber = Column(Integer)
    kktregid = Column(String)
    fiscaldrivenumber = Column(String)
    fiscaldocumentnumber = Column(Integer)
    fiscalsign = Column(Integer)
    def __init__(self, **kwargs):
        for arg in kwargs:
            self.arg = kwargs[arg]


class CloseshiftModel(db.Model):
    __tablename__ = 'closeshift'
    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone='UTC'), default=datetime.utcnow
    )
    company_inn = Column(String)
    company_name = Column(String)
    operator = Column(String)
    close_datetime = Column(TIMESTAMP(timezone='UTC'))
    shiftnumber = Column(Integer)
    receiptsquantity = Column(Integer)
    documentsquantity = Column(Integer)
    nottransmitteddocumentsquantity = Column(Integer)
    nottransmitteddocumentsdatetime = Column(TIMESTAMP(timezone='UTC'))
    ofdresponsetimeoutsign = Column(TIMESTAMP(timezone='UTC'))
    fiscaldrivereplacerequiredsign = Column(Integer)
    kktregid = Column(String)
    fiscaldrivenumber = Column(String)
    fiscaldocumentnumber = Column(Integer)
    fiscalsign = Column(Integer)
    def __init__(self, **kwargs):
        for arg in kwargs:
            self.arg = kwargs[arg]