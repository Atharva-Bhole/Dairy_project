```
.
├── .gitignore
├── controllers_documentation.md
├── models_documentation.md
├── README.md
├── requirements.txt
├── run.py
└── app
    ├── .env
    ├── __init__.py
    ├── models
    │   ├── cow.py
    │   ├── dairyowner.py
    │   ├── farmer.py
    │   ├── farmer_bank.py
    │   ├── muster_data.py
    │   ├── supplies.py
    │   ├── supply_transaction.py
    │   ├── transactions.py
    │   └── __init__.py
    ├── templates
    │   ├── admin
    │   └── farmers
    │       ├── farmer_muster_data.html
    │       └── farmer_prof.html
    └── controllers
        ├── dairy_owner_controller.py
        ├── farmer_controller.py
        ├── muster_controller.py
        ├── transaction_controller.py
        ├── __init__.py
        ├── admin
        │   ├── dashboard
        │   └── profile
        ├── dairy_owners
        │   ├── daily_data
        │   ├── dashboard
        │   ├── muster_data
        │   └── profile
        ├── farmers
        │   ├── bank_details
        │   │   └── farmer_bank_controller.py
        │   ├── daily_data
        │   ├── dashboard
        │   └── profile
        ├── forms
        │   └── farmerform.py
        ├── muster
        │   └── muster_data
        ├── supplies
        │   ├── supply_data
        │   │   └── supplies_controller.py
        │   └── supply_transactions
        └── transaction
            ├── bank_transactions
            ├── farmer_transactions
            └── supply_transactions
                └── supplies_transaction_controller.py
```
