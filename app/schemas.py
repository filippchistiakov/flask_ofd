from marshmallow import Schema, fields, EXCLUDE, pre_load
from datetime import datetime
# Схемы Json зефирки
# Кастомные поля
class FieldCustomDatetime(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        elif isinstance(value, int):
            value = datetime.utcfromtimestamp(value)
            return value
        elif isinstance(value, datetime):
            return value
        else:
            return ValidationError

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return ""
        elif isinstance(value, int):
            value = datetime.utcfromtimestamp(value)
            return value
        elif isinstance(value, datetime):
            return value
        else:
            raise


class Receipt(Schema):
    fiscal_datetime = FieldCustomDatetime(
        data_key="dateTime"
    )  # fields.DateTime(tzinfo=pytz.utc, data_key="dateTime") #Дата чека
    company_inn = fields.Str(
        data_key="userInn"
    )  # ИНН компании
    company_name = fields.Str(
        data_key="user"
    )  # наименование компании
    kktregid = fields.Str(
        data_key="kktRegId"
    )  # регистрационный номер ККТ, выданный ФНС России или * если нет группировки по кассам
    shiftnumber = fields.Int(
        data_key="shiftNumber"
    )  # номер смены
    requestnumber = fields.Int(
        data_key="requestNumber"
    )  # номер чека за смену
    fiscaldrivenumber = fields.Str(
        data_key="fiscalDriveNumber", required=True
    )  # заводской номер фискального накопителя
    fiscalsign = fields.Int(
        data_key="fiscalSign"
    )  # фискальный признак документа
    fiscaldocumentnumber = fields.Int(
        data_key="fiscalDocumentNumber", required=True
    )  # порядковый номер фискального документа
    cashtotalsum = fields.Int(
        data_key="cashTotalSum"
    )  # форма расчета - наличными, в копейках
    ecashtotalsum = fields.Int(
        data_key="ecashTotalSum"
    )  # сумма уплаченная электронными средствами платежа, в копейках
    totalsum = fields.Int(
        data_key="totalSum"
    )  # ИТОГ, в копейках
    nds18 = fields.Int(
        data_key="nds18"
    )  # НДС итога чека со ставкой 18%
    nds10 = fields.Int(
        data_key="nds10"
    )  # НДС итога чека со ставкой 10%
    nds0 = fields.Int(
        data_key="nds0"
    )  # НДС итога чека со ставкой 0%
    ndsno = fields.Int(
        data_key="ndsNo"
    )  # НДС не облагается
    ndscalculated18 = fields.Int(
        data_key="ndsCalculated18"
    )  # НДС итога чека с рассчитанной ставкой 18%, в копейках
    ndscalculated10 = fields.Int(
        data_key="ndsCalculated10"
    )  # НДС итога чека с рассчитанной ставкой 10%, в копейках
    addresstocheckfiscalsign = fields.Str(
        data_key="addressToCheckFiscalSign"
    )  # адрес сайта для проверки ФП
    receiptcode = fields.Int(
        data_key="receiptCode"
    )  # код документа "Кассовый чек" (всегда равен 3)
    bsocode = fields.Int(
        data_key="bsoCode"
    )  # код документа "БСО" (всегда равен 4)
    bankagentoperation = fields.Str(
        data_key="bankAgentOperation"
    )  # операция банковского агента
    banksubagentoperation = fields.Str(
        data_key="bankSubagentOperation"
    )  # операция банковского субагента
    operationtype = fields.Int(
        data_key="operationType"
    )  # признак расчета
    taxationtype = fields.Int(
        data_key="taxationType"
    )  # применяемая система налогообложения
    bankagentphone = fields.Str(
        data_key="bankAgentPhone"
    )  # телефон банковского агента
    paymentagentphone = fields.Str(
        data_key="paymentAgentPhone"
    )  # телефон платежного агента
    operatorphonetotransfer = fields.Str(
        data_key="operatorPhoneToTransfer"
    )  # телефон оператора по переводу денежных средств
    operatorinn = fields.Str(
        data_key="operatorInn"
    )  # ИНН оператора по переводу денежных средств
    bankagentremuneration = fields.Int(
        data_key="bankAgentRemuneration"
    )  # размер вознаграждения банковского агента (субагента)
    paymentagentremuneration = fields.Int(
        data_key="paymentAgentRemuneration"
    )  # размер вознаграждения платежного агента (субагента), в копейках
    operator = fields.Str(data_key="operator")  # кассир
    operatorname = fields.Str(
        data_key="operatorName"
    )  # наименование оператора по переводу денежных средств
    banksubagentphone = fields.Str(
        data_key="bankSubagentPhone"
    )  # телефон банковского субагента
    paymentsubagentphone = fields.Str(
        data_key="paymentSubagentPhone"
    )  # телефон платежного субагента
    senderaddress = fields.Str(
        data_key="senderAddress"
    )  # адрес отправителя
    operatorphonetoreceive = fields.Str(
        data_key="operatorPhoneToReceive"
    )  # телефон оператора по приему платежей
    retailplaceaddress = fields.Str(
        data_key="retailPlaceAddress"
    )  # адрес (место) расчетов
    operatoraddress = fields.Str(
        data_key="operatorAddress"
    )  # адрес оператора по переводу денежных средств
    buyeraddress = fields.Str(
        data_key="buyerAddress"
    )  # адрес покупателя

    @pre_load
    def normalize_str(self, in_data):
        try:
            in_data["userInn"] = (
                in_data["userInn"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        try:
            in_data["user"] = (
                in_data["user"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        return in_data

    class Meta:
        unknown = EXCLUDE


class Openshift(Schema):
    company_inn = fields.Str(
        data_key="userInn"
    )  # ИНН компании
    company_name = fields.Str(
        data_key="user"
    )  # наименование компании
    operator = fields.Str(data_key="operator")  # кассир
    retailplaceaddress = fields.Str(
        data_key="retailPlaceAddress"
    )  # адрес (место) расчетов
    open_datetime = FieldCustomDatetime(
        data_key="dateTime"
    )  # дата, время
    shiftnumber = fields.Int(
        data_key="shiftNumber"
    )  # номер смены
    kktregid = fields.Str(
        data_key="kktRegId"
    )  # регистрационный номер ККТ, выданный ФНС России или * если нет группировки по кассам
    fiscaldrivenumber = fields.Str(
        data_key="fiscalDriveNumber", required=True
    )  # заводской номер фискального накопителя
    fiscaldocumentnumber = fields.Int(
        data_key="fiscalDocumentNumber", required=True
    )  # порядковый номер фискального документа
    fiscalsign = fields.Int(
        data_key="fiscalSign"
    )  # фискальный признак документа

    @pre_load
    def normalize_str(self, in_data):
        try:
            in_data["userInn"] = (
                in_data["userInn"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        try:
            in_data["user"] = (
                in_data["user"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        return in_data

    class Meta:
        unknown = EXCLUDE


class Closeshift(Schema):
    company_inn = fields.Str(
        data_key="userInn"
    )  # ИНН компании
    company_name = fields.Str(
        data_key="user"
    )  # наименование компании
    operator = fields.Str(data_key="operator")  # кассир
    close_datetime = FieldCustomDatetime(
        data_key="dateTime"
    )  # дата, время
    shiftnumber = fields.Int(
        data_key="shiftNumber"
    )  # номер смены
    receiptsquantity = fields.Int(
        data_key="receiptsQuantity"
    )  # количество кассовых чеков за смену
    documentsquantity = fields.Int(
        data_key="documentsQuantity"
    )  # количество фискальных документов за смену
    nottransmitteddocumentsquantity = fields.Int(
        data_key="notTransmittedDocumentsQuantity"
    )  # кол-во неподтвержденных документов ФД
    nottransmitteddocumentsdatetime = FieldCustomDatetime(
        data_key="notTransmittedDocumentsDateTime"
    )  # дата и время первого из непереданных ФД
    ofdresponsetimeoutsign = FieldCustomDatetime(
        data_key="ofdResponseTimeoutSign"
    )  # признак превышения времени ожидания ответа ОФД
    fiscaldrivereplacerequiredsign = fields.Int(
        data_key="fiscalDriveReplaceRequiredSign"
    )  # признак превышения времени ожидания ответа ОФД
    kktregid = fields.Str(
        data_key="kktRegId"
    )  # регистрационный номер ККТ, выданный ФНС России или * если нет группировки по кассам
    fiscaldrivenumber = fields.Str(
        data_key="fiscalDriveNumber", required=True
    )  # заводской номер фискального накопителя
    fiscaldocumentnumber = fields.Int(
        data_key="fiscalDocumentNumber", required=True
    )  # порядковый номер фискального документа
    fiscalsign = fields.Int(
        data_key="fiscalSign"
    )  # фискальный признак документа

    @pre_load
    def normalize_str(self, in_data):
        try:
            in_data["userInn"] = (
                in_data["userInn"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        try:
            in_data["user"] = (
                in_data["user"].lower().strip()
            )
        except Exception:  # Поменять
            pass
        return in_data

    class Meta:
        unknown = EXCLUDE


class Document(Schema):
    receipt = fields.Nested(Receipt, data_key="receipt")
    openshift = fields.Nested(
        Openshift, data_key="openShift"
    )
    closeshift = fields.Nested(
        Closeshift, data_key="closeShift"
    )

    class Meta:
        unknown = EXCLUDE


class Platformaofd(Schema):
    document = fields.Nested(
        Document, data_key="document", required=True
    )

    class Meta:
        unknown = EXCLUDE

