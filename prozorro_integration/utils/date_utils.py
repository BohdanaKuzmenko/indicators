from datetime import datetime
import pytz


class DateUtils(object):
    ZONED_DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'

    @staticmethod
    def str_to_zoned_date_time(zoned_date_time_str: str)->datetime:
        utc = pytz.utc
        return datetime.strptime(''.join(zoned_date_time_str.rsplit(':', 1)), '%Y-%m-%dT%H:%M:%S.%f%z').astimezone(utc)

    @staticmethod
    def zoned_date_time_to_str(zoned_date_time: datetime)->str:
        return zoned_date_time.strftime(DateUtils.ZONED_DATE_TIME_FORMAT)
