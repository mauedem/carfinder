from adapters.psql_database.accounts.tables import AccountsTable
from core.accounts.entities import Account, PersonalData


def present_account(account_table: AccountsTable) -> Account:
    return Account(
        email=account_table.email,
        personal_data=PersonalData(
            first_name=account_table.personal_data.first_name,
            last_name=account_table.personal_data.last_name,
        )
    )
