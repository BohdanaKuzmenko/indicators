from datetime import datetime
from .date_utils import DateUtils


class ProzorroRequestUrlCreator(object):
    @staticmethod
    def create_tender_url(base_url: str, tender_id: str) -> str:
        return base_url + '/' + tender_id

    @staticmethod
    def create_tenders_url(base_url: str, date: datetime) -> str:
        return ProzorroRequestUrlCreator.create_tenders_url(base_url, date, 1000)

    @staticmethod
    def create_tenders_url(base_url: str, date: datetime, page_limit: int) -> str:
        return "{}?limit={}&mode=_all_&offset={}".format(base_url, page_limit, DateUtils.zoned_date_time_to_str(date))
