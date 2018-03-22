from enum import Enum


class ProzorroTenderUpdatesManager(object):
    TENDERS_SEARCH_URL = 'https://public.api.openprocurement.org/api/2.4/tenders'
    _service_status = "ENABLED"

    async def load_last_modified_tenders(self):
        dateOffset = tenderLoaderService.resolveDateOffset();

