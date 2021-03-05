from typing import Optional

from core.accounts.tokenizers import IAccessTokenizer


class AccessTokenizer(IAccessTokenizer):
    
    def encode(self, account_data: dict) -> str:
        pass

    def decode(self, token: str) -> Optional[dict]:
        pass