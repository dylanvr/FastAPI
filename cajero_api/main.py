from db import user_db
from db import transaction_db


def main():

    print(user_db.database_users)
    print(user_db.get_user("camilo24"))

if __name__ == '__main__':
    main()