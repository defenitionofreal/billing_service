Billing web service
=====================
***

**Description**

The service provides 3 endpoints for account management:

1. Create an account.

Input parameters: name, overdraft flag (true - an unlimited minus move is possible).
Result: account ID.

2. Transfer money from account A to account B.

Input parameters: donor ID, recipient account ID, transfer amount.
Result: success or not

3. Request for account balance.

Input parameters: account ID. Result: sum

Account data and transactions must be stored in a relational DBMS.
Execute a DRF based service with postgresql DBMS.
Cover the code with autotests, unit tests

***

**Install:**

```
mkdir new_project
cd new_project
python3 -m venv venv
source venv/bin/activate
mkdir src
cd src
git clone https://github.com/defenitionofreal/ylab_test.git
pip install -r requirements.txt

# create db
createuser -dP Ylab
придумать пароль, у меня это 123
createdb -E utf8 -U Ylab Ylab

# settings.dev
make dev
# миграции
make migration
# load fixtures
make fixture
# runserver
make run
# run tests
make test
```


**API endpoints:**

```
# Create an account
http://127.0.0.1:8000/api/v1/billing/

# Transfer money
http://127.0.0.1:8000/api/v1/transfer/

# Request for account balance
http://127.0.0.1:8000/api/v1/billing/get_balance?id=1
```
