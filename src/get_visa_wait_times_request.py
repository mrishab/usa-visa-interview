from typing import List
from get_visa_wait_time_request import GetVisaWaitTimeRequest


class GetVisaWaitTimesRequest:
    def __init__(self, city_configs: dict) -> None:
        self.city_configs = city_configs

    def get(self, city_name: str) -> GetVisaWaitTimeRequest:
        return self.city_config[city_name]

    def get_all(self) -> List[GetVisaWaitTimeRequest]:
        return self.city_configs.values()


def from_dict(data: dict) -> GetVisaWaitTimesRequest:
    city_configs = {}
    for city_name, config in data.items():
        city_config = GetVisaWaitTimeRequest(city_name=city_name, cid=config['cid'])
        city_configs[city_name] = city_config

    return GetVisaWaitTimesRequest(city_configs)
