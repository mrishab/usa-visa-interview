from multiprocessing.connection import wait
from typing import List
from get_visa_wait_time_response import GetVisaWaitTimeResponse

class GetVisaWaitTimesResponse:
    def __init__(self, wait_times: List[GetVisaWaitTimeResponse]) -> None:
        self.wait_times = wait_times
        self._sort()


    def get_all(self) -> List[GetVisaWaitTimeResponse]:
        return self.wait_times

    def _sort(self) -> None:
        # Note: Sort ignores the unit of the value.
        self.wait_times.sort(key = lambda wait_time: wait_time.get_visitor_visa_wait_time().value)

    def __str__(self) -> str:
        return self.get_all().__str__()