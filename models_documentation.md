
# Models Documentation

## 1. `__init__.py`

### Description
This file initializes the SQLAlchemy instance used for database interaction in the Flask application.

### Attributes
- **db**: Instance of `SQLAlchemy`, responsible for handling database operations.

---

## 2. `cow.py`

### Description
Defines the `cows` model, representing the cow data in the dairy business.

### Attributes
- **animal_id**: Unique identifier for the cow (Primary Key).
- **cow_breed**: Breed of the cow.
- **gender**: Gender of the cow (e.g., male or female).
- **farmer_id**: Foreign key referencing the `farmers` table.
- **is_milking**: Boolean indicating if the cow is currently milking.
- **percent_fat**: Fat content percentage in the cow's milk.
- **percent_snf**: Solids-not-fat percentage in the cow's milk.
- **hygiene_rating**: Hygiene rating of the cow.
- **milking_performance**: Performance metrics for milking.

---

## 3. `dairyowner.py`

### Description
Defines the `dairy_owner` model, representing dairy owners and their attributes.

### Attributes
- **dairy_id**: Unique identifier for the dairy owner (Primary Key).
- **dairy_name**: Name of the dairy.
- **state**: State where the dairy is located.
- **taluka**: Taluka (sub-district) of the dairy's location.
- **district**: District where the dairy is located.
- **village**: Village where the dairy is situated.
- **created_at**: Date the dairy owner was created.
- **updated_at**: Date the dairy owner information was last updated.
- **deleted_at**: Date the dairy owner information was marked as deleted.

### Relationships
- **farmers**: One-to-many relationship with the `farmers` model.
- **supply**: One-to-many relationship with the `Supplies` model.
- **transactions**: One-to-many relationship with the `Transaction` model.

---

## 4. `farmer_bank.py`

### Description
Defines the `farmer_bank_details` model, representing the banking details of farmers.

### Attributes
- **farmer_id**: Foreign key referencing the `farmers` table.
- **account_no**: Unique account number of the farmer's bank account (Primary Key).
- **ifsc_code**: IFSC code of the farmer's bank.
- **bank_name**: Name of the farmer's bank.

---

## 5. `farmer.py`

### Description
Defines the `farmers` model, representing farmer data in the application.

### Attributes
- **farmer_id**: Unique identifier for the farmer (Primary Key).
- **dairy_id**: Foreign key referencing the `dairy_owner` table.
- **state**: State where the farmer resides.
- **name**: Name of the farmer.
- **contact_number**: Farmer's contact number.
- **address**: Address of the farmer.
- **taluka**: Taluka (sub-district) of the farmer's location.
- **district**: District where the farmer is located.
- **village**: Village where the farmer resides.
- **wallet_balance**: Current wallet balance of the farmer.
- **created_at**: Date the farmer was created.
- **updated_at**: Date the farmer information was last updated.
- **deleted_at**: Date the farmer information was marked as deleted.

### Relationships
- **cow**: One-to-many relationship with the `cows` model.
- **muster_by_name**: One-to-many relationship with the `muster` model by farmer name.
- **muster_by_id**: One-to-many relationship with the `muster` model by farmer ID.
- **farmer_bank**: One-to-many relationship with the `farmer_bank_details` model.
- **supply_transaction**: One-to-many relationship with the `SupplyTransaction` model.
- **transactions**: One-to-many relationship with the `Transaction` model.

---

## 6. `muster_data.py`

### Description
Defines the `muster` model, representing muster data related to farmers and their milk production.

### Attributes
- **farmer_id**: Foreign key referencing the `farmers` table.
- **milk_union**: Name of the milk union.
- **muster_id**: Unique identifier for the muster (Primary Key).
- **payment_period_start**: Start date of the payment period.
- **payment_period_end**: End date of the payment period.
- **district**: District where the farmer is located.
- **taluka**: Taluka (sub-district) of the farmer's location.
- **village**: Village where the farmer resides.
- **bulk_milk_supplier**: Name of the bulk milk supplier.
- **farmer_name**: Name of the farmer (Foreign key referencing `farmers.name`).
- **total_milk**: Total amount of milk produced.
- **percent_fat**: Fat percentage of the milk.
- **percent_snf**: SNF percentage of the milk.
- **amount**: Amount to be paid to the farmer.
- **deduction_amount**: Any deduction from the payment.
- **final_amount_after_deduction**: Final amount after deductions.
- **avg_rate_per_litre**: Average rate per litre of milk.

### Relationships
- **farmer**: Foreign key relationship with the `farmers` table.

---

## 7. `supplies.py`

### Description
Defines the `Supplies` model, representing different supplies available at the dairy.

### Attributes
- **supply_id**: Unique identifier for the supply (Primary Key).
- **dairy_id**: Foreign key referencing the `dairy_owner` table.
- **name**: Name of the supply.
- **price**: Price of the supply.

### Relationships
- **supply_transaction**: One-to-many relationship with the `SupplyTransaction` model.

---

## 8. `supply_transaction.py`

### Description
Defines the `SupplyTransaction` model, representing transactions related to supplies purchased by farmers.

### Attributes
- **supply_transaction_id**: Unique identifier for the supply transaction (Primary Key).
- **farmer_id**: Foreign key referencing the `farmers` table.
- **supply_id**: Foreign key referencing the `supplies` table.
- **quantity**: Quantity of the supply purchased.
- **total_amount**: Total amount for the transaction.

### Relationships
- **farmer**: Foreign key relationship with the `farmers` table.
- **supply**: Foreign key relationship with the `supplies` table.

---

## 9. `transactions.py`

### Description
Defines the `Transaction` model, representing transactions made by farmers.

### Attributes
- **transaction_id**: Unique identifier for the transaction (Primary Key).
- **farmer_id**: Foreign key referencing the `farmers` table.
- **dairy_id**: Foreign key referencing the `dairy_owner` table.
- **quantity**: Quantity of the product involved in the transaction.
- **price_per_unit**: Price per unit of the product.
- **total_amount**: Total amount for the transaction.

### Relationships
- **farmer**: Foreign key relationship with the `farmers` table.
- **dairy_owner**: Foreign key relationship with the `dairy_owner` table.
