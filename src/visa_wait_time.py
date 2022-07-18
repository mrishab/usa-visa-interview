from enum import Enum

class VisaType(Enum):
    VISITOR = "Visitor Visa"
    STUDENT_EXCHANGE_VISTOR = "Student/Exchange Visitor Visas"
    OTHER_NONIMMIGRANT = "All Other Nonimmigrant Visa"

class GetVisaWaitTimeUnit(Enum):
    Days = "Calendar Days"

class VisaWaitTime:
    def __init__(self, visa_type: VisaType, unit: GetVisaWaitTimeUnit, value: int) -> None:
        self.visa_type = visa_type
        self.unit = unit
        self.value = int(value)