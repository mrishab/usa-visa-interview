from typing import List
from visa_wait_time import VisaType, VisaWaitTime


class GetVisaWaitTimeResponse:
    def __init__(self, city: str, wait_times: List[VisaWaitTime]) -> None:
        self.city = city
        self.wait_times = wait_times

    def get_visitor_visa_wait_time(self) -> VisaWaitTime:
        return self._get_wait_time_by_visa_type(VisaType.VISITOR)

    def get_student_visa_wait_time(self) -> VisaWaitTime:
        return self._get_wait_time_by_visa_type(VisaType.STUDENT_EXCHANGE_VISTOR)

    def get_other_visa_wait_time(self) -> VisaWaitTime:
        return self._get_wait_time_by_visa_type(VisaType.OTHER_NONIMMIGRANT)

    def _get_wait_time_by_visa_type(self, visa_type: VisaType) -> VisaWaitTime:
        matches = list(filter(lambda wait_time: wait_time.visa_type is visa_type, self.wait_times))
        if len(matches) > 1:
            raise Exception("Expected length 1, found: {}".format(matches))
        return matches[0]

    def __str__(self) -> str:
        wait_times = [
            "{visa_type}: {value} {unit}".format(
                visa_type=wait_time.visa_type,
                value=wait_time.value,
                unit=wait_time.unit
            ) for wait_time in self.wait_times
        ]
        return str(wait_times)