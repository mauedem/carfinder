from core.accounts.tokenizers import IPasswordTokenizer


class PasswordTokenizer(IPasswordTokenizer):
    
    def encode(self, password: str) -> str:
        pass
