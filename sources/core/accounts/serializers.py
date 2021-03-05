from core.accounts.entities import Account


def serialize_account(account: Account) -> dict:
    return dict(
        email=account.email,
        personal_data=dict(
            first_name=account.personal_data.first_name,
            last_name=account.personal_data.last_name,
        ),
        confirmed=account.confirmed,
    )
