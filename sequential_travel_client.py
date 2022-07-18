from get_visa_wait_times_response import GetVisaWaitTimesResponse
from get_visa_wait_times_request import GetVisaWaitTimesRequest
from travel_client import TravelClient


class SequentialTravelClient:
    def __init__(self, travel_client: TravelClient):
        self.travel_client = travel_client

    def get_visa_wait_times(self, get_visa_wait_times_req: GetVisaWaitTimesRequest) -> GetVisaWaitTimesResponse:
        wait_times = [self.travel_client.get_visa_wait_time(get_visa_wait_time_req) for get_visa_wait_time_req in get_visa_wait_times_req.get_all()]
        return GetVisaWaitTimesResponse(wait_times=wait_times)