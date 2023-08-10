import requests
from get_visa_wait_time_request import GetVisaWaitTimeRequest
from get_visa_wait_time_response import GetVisaWaitTimeResponse
from visa_wait_time import GetVisaWaitTimeUnit, VisaType, VisaWaitTime


class TravelClient:
    def __init__(self, host: str = "https://travel.state.gov") -> None:
        self.host = host

    def get_visa_wait_time(self, get_visa_wait_time_request: GetVisaWaitTimeRequest) -> GetVisaWaitTimeResponse:
        path = "/content/travel/resources/database/database.getVisaWaitTimes.html?cid={cid}&aid=VisaWaitTimesHomePage".format(cid=get_visa_wait_time_request.cid)
        url = "{}{}".format(self.host, path)
        res = requests.get(url=url)
        res.raise_for_status()
        intervals = res.text.strip().split("|")
        if len(intervals) < 3:
            raise Exception("Expected array of length 3, received: {}".format(intervals))
        visitor_visa = intervals[0].split(" ")
        student_visa = intervals[1].split(" ")
        other_non_immigrant_visa = intervals[2].split(" ")

        wait_times = [
            VisaWaitTime(visa_type=VisaType.VISITOR, unit=GetVisaWaitTimeUnit[visitor_visa[1]], value=visitor_visa[0]),
            VisaWaitTime(visa_type=VisaType.STUDENT_EXCHANGE_VISTOR, unit=GetVisaWaitTimeUnit[student_visa[1]], value=student_visa[0]),
            VisaWaitTime(visa_type=VisaType.OTHER_NONIMMIGRANT, unit=GetVisaWaitTimeUnit[other_non_immigrant_visa[1]], value=other_non_immigrant_visa[0]),
        ]
        return GetVisaWaitTimeResponse(get_visa_wait_time_request.city_name, wait_times=wait_times)
