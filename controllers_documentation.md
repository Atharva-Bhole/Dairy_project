# Controllers Documentation

## Overview
This documentation outlines the various controllers used in the Flask application for managing a dairy business. Each controller handles specific routes and business logic related to farmers, dairy owners, bank details, supplies, transactions, and muster data.

### 1. **`__init__.py`**
This file initializes the controllers by importing the necessary blueprints from each controller module.

### 2. **`dairy_owner_controller.py`**
- **Blueprint Name**: `dairy`
  
- **Routes**:
  - **`/create_dairy_owner`** (POST)
    - Creates a new dairy owner using data from the request body.
    - **Response**: Success message.
    
  - **`/view_dairy_data`** (GET)
    - Retrieves a list of all dairy owners.
    - **Response**: JSON representation of all dairy owners.

### 3. **`farmer_bank_controller.py`**
- **Blueprint Name**: `bank_dets`
  
- **Routes**:
  - **`/get_farmer_bank`** (GET, POST)
    - Retrieves bank details for a specific farmer based on `farmer_id`.
    - **Response**: JSON containing bank details.
    
  - **`/add_farmer_bank`** (POST)
    - Adds a new bank detail for a farmer.
    - **Response**: JSON representation of the newly added bank detail.
    
  - **`/get_all_farmer_bank`** (GET)
    - Retrieves all farmer bank details.
    - **Response**: JSON containing all bank details.
    
  - **`/delete_farmer_bank`** (DELETE)
    - Deletes a farmer's bank detail based on `account_no`.
    - **Response**: Success message.

### 4. **`farmer_controller.py`**
- **Blueprint Name**: `farmers`
  
- **Routes**:
  - **`/test`** (GET)
    - Test route to verify connectivity.
    - **Response**: Test message.
    
  - **`/get_farmers`** (GET)
    - Retrieves a list of all farmers.
    - **Response**: JSON representation of all farmers.
    
  - **`/farmers`** (POST)
    - Creates a new farmer using data from the request body.
    - **Response**: JSON representation of the newly added farmer.
    
  - **`/farmer_profile`** (GET, POST)
    - Retrieves farmer details using a form.
    - **Response**: Renders a template with farmer details.
    
  - **`/get_farmer_muster_data`** (GET, POST)
    - Retrieves muster data for a specific farmer using a form.
    - **Response**: Renders a template with muster data.

### 5. **`muster_controller.py`**
- **Blueprint Name**: `muster_`
  
- **Routes**:
  - **`/get_muster_data`** (GET)
    - Retrieves muster data for a specific farmer based on `farmer_id`.
    - **Response**: JSON containing muster data.
    
  - **`/insert_muster_data`** (POST)
    - Inserts new muster data.
    - **Response**: JSON representation of the inserted muster data.
    
  - **`/get_all_muster_data`** (GET)
    - Retrieves all muster data.
    - **Response**: JSON containing all muster data.

### 6. **`supplies_controller.py`**
- **Blueprint Name**: `supplies`
  
- **Routes**:
  - **`/get_supplies`** (GET)
    - Retrieves supply details based on `supply_id`.
    - **Response**: JSON containing supply details.
    
  - **`/get_all_supplies`** (GET)
    - Retrieves all supply details.
    - **Response**: JSON containing all supply details.
    
  - **`/insert_supply_data`** (POST)
    - Inserts new supply data.
    - **Response**: Success message.
    
  - **`/delete_supply_data`** (DELETE)
    - Deletes supply data based on `supply_id`.
    - **Response**: Success message.

### 7. **`supplies_transaction_controller.py`**
- **Blueprint Name**: `supply_transaction`
  
- **Routes**:
  - **`/get_all_supply_transactions`** (GET)
    - Retrieves all supply transactions.
    - **Response**: JSON containing all supply transactions.
    
  - **`/insert_supply_transaction`** (POST)
    - Inserts a new supply transaction.
    - **Response**: JSON representation of the newly inserted transaction.
    
  - **`/get_single_supply_transaction`** (GET)
    - Retrieves a single supply transaction based on `farmer_id`.
    - **Response**: JSON containing the transaction data.

### 8. **`transaction_controller.py`**
- **Blueprint Name**: `payment_transaction`
  
- **Routes**:
  - **`/get_transaction_data_for_farmer`** (GET)
    - Retrieves transaction data for a specific farmer based on `farmer_id`.
    - **Response**: JSON containing transaction data.
    
  - **`/register_transaction_details`** (POST)
    - Registers a new transaction for a farmer.
    - **Response**: JSON representation of the newly registered transaction.
