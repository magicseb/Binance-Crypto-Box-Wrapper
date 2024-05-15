from dataclasses import dataclass
from typing import Union


@dataclass
class Config:
    # ==================================================

    CHATS = [
        -1001610472708, 
        -1001813092752, 
        -1001515379979, 
        -1001644346269
    ]

    # ==================================================

    CLIENT_NAME: str = "ClientName"  # Client name | Can be left as now or changed
    API_ID: int = 21983845  # Telegram API ID
    API_HASH: str = "1da1fb20d6e39d45b6edaccdf91fcb95"  # Telegram API hash

    # ==================================================

    MAX_HOUR_REQUESTS: Union[int, float] = (
        100  # Maximum number of requests per hour (0 - unlimited)
    )

    # headers = {
    #     "User-Agent": "",  # Constant value if logged in from one device
    #     "bnc-uuid": "",  # Constant value
    #     "device-info": "",  # Constant value if logged in from one device
    #     "clienttype": "web",  # Constant value
    #     "csrftoken": "",
    #     "fvideo-id": "", # Constant value
    #     "fvideo-token": "",
    #     "x-trace-id": "",
    #     "x-ui-request-trace": "",
    #     "lang": "uk-UA",  # Constant value
    #     "Referer": "https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox",  # Constant value
    #     "Cookie": "",
    # }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "bnc-uuid": "857ee104-6478-444e-ba5c-90517c0b0de0",
        "device-info": "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZW4tVVMiLCJ0aW1lem9uZSI6IkdNVCswMzowMCIsInRpbWV6b25lT2Zmc2V0IjotMTgwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTI1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTI1LjAiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjZhMzY2OGExIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKE5WSURJQSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChOVklESUEsIE5WSURJQSBHZUZvcmNlIEdUWCA5ODAgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wKSwgb3Igc2ltaWxhciIsImF1ZGlvIjoiMzUuNzQ5OTcyMDkzODUwMzc0IiwicGxhdGZvcm0iOiJXaW4zMiIsIndlYl90aW1lem9uZSI6IkV1cm9wZS9LeWl2IiwiZGV2aWNlX25hbWUiOiJGaXJlZm94IFYxMjUuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6IjU3YmIzMmYxMmY2OGY5MTc4YTkyNDcwOTcyZTgxOGQwIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiLCJ9",
        "clienttype": "web",
        "csrftoken": "0d2ff28cfdb51f3b89d8db5fe3f49d02",
        "fvideo-id": "3345242808a5ab0885905ccbe9ededb49a539c62",
        "fvideo-token": "7Av7u8a3VDBn+illHVEdOQUB6I2BwooAT0cyhi06L+/T0oG+JPDIZ3qF+XfRJL7he7hbDj8sUwfSAaSygIL9ogA9WmA/8EJ9klSl3gaIAVRoLyf7DQbnq7eiCO0Mm6MZmdRwgfTExtT9AMmA2NkaY0n6+bsc9Z1s/YDxgY0Er/W9WqywV8EFGXXLBY3bDSCP8=1a",
        "x-trace-id": "1f15f0ac-27a2-40e6-b3c2-b4679a81426c",
        "x-ui-request-trace": "1f15f0ac-27a2-40e6-b3c2-b4679a81426c",
        "lang": "uk-UA",
        "Referer": "https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox",
        "Cookie": 'theme=dark; bnc-uuid=857ee104-6478-444e-ba5c-90517c0b0de0; source=Homepage_log_in; campaign=duckduckgo.com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22496344464%22%2C%22first_id%22%3A%2218de07474ed694-0311e8d2b3183b-e565623-2073600-18de07474ee600%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C…055717020c0ace63170ad5f6066813":{"date":1710514143189,"value":""}}; _ga_3WP50LGEEC=GS1.1.1708976615.6.1.1708978039.60.0.0; _ga=GA1.1.2117806244.1708883765; changeBasisTimeZone=; lang=uk-ua; se_sd=RJSBQQR5bRaUVICoLEhZgZZCwHRQHEVUlcSBdV0d1RSUgWlNWUJc1; cr00=529D8EBD8E8200C5DDF6D173AB3893B0; d1og=web.496344464.5EB82DB8FB781D69B2A36AAF8BC87282; r2o1=web.496344464.3D251940C1F2EAAC401245A1CC265833; f30l=web.496344464.A1A3B090E3D38945C213F51FF652665D; logined=y; p20t=web.496344464.C110552A84DF73235BB6E2530FA27A21',
    }

    def __getelement__(self, element: str) -> Union[int, float, bool, str]:
        return getattr(self, element, None)
