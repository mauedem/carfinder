from core.errors import CoreError, ErrorCodes
from core.accounts.repos import IAccountsRepo
from core.accounts.schemas import AccountSchema
from core.accounts.serializers import serialize_account
from core.accounts.tokenizers import IPasswordTokenizer, IAccessTokenizer


class AccountsService:
    accounts_repo: IAccountsRepo
    
    password_tokenizer: IPasswordTokenizer
    access_tokenizer: IAccessTokenizer
    
    
    def register(self, account_data: dict) -> dict:
        schema = AccountSchema()
        validation_errors = schema.validate(account_data)
        if validation_errors:
            raise CoreError(ErrorCodes.ACCOUNT_IS_NOT_A_VALID, validation_errors)
        
        password_hash = self.password_tokenizer.encode(account_data['password'])
        account = self.accounts_repo.create(
            email=account_data['email'],
            password_hash=password_hash,
            first_name=account_data['personal_data']['first_name'],
            last_name=account_data['personal_data']['last_name'],
        )
        
        return serialize_account(account)

    def authorize(self, email: str, password: str) -> str:
        password_hash = self.password_tokenizer.encode(password)
        account = self.accounts_repo.authorize(email, password_hash)
        
        if not account:
            raise CoreError(ErrorCodes.BAD_CREDENTIALS)
        
        token = self.access_tokenizer.encode(serialize_account(account))
        
        return token
    
    def authenticate(self, token: str) -> dict:
        token_data = self.access_tokenizer.decode(token)
        if not token_data:
            raise CoreError(ErrorCodes.NOT_AUTHORIZED)
        
        account_email = token_data['email']
        
        account = self.accounts_repo.get_by_email(account_email)
        
        return serialize_account(account)
