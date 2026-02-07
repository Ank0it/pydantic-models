# Project Methods and Uses

This README documents the functions and model validators in this project and how they are used.

## 1_why_pydantic.py

### Imports and why they are used

- `BaseModel` (from `pydantic`)
  - Use case: Define the `Patient` model with type-checked fields.
  - Problem solved: Validates incoming data types (e.g., `age` must be int) and prevents invalid payloads.

- `insert_patient_data(patient: Patient)`
  - Purpose: Print a patient's name and age, then confirm insertion.
  - Usage: Call with a `Patient` instance, e.g., after `patient1 = Patient(**patient_info)`.
  - Reference: [1_why_pydantic.py](1_why_pydantic.py#L7)

- `update_patient_data(patient: Patient)`
  - Purpose: Print a patient's name and age, then confirm update.
  - Usage: Called with `patient1` in the script.
  - Reference: [1_why_pydantic.py](1_why_pydantic.py#L12)

## 2_pydantic_model2.py

### Imports and why they are used

- `BaseModel` (from `pydantic`)
  - Use case: Define the `Patient` model with typed fields.
  - Problem solved: Centralizes validation and parsing for the patient payload.

- `EmailStr` (from `pydantic`)
  - Use case: Enforce valid email format for `email`.
  - Problem solved: Prevents malformed email values from entering the model.

- `AnyUrl` (from `pydantic`)
  - Use case: Validate the `linked_in_urls` field.
  - Problem solved: Ensures the URL is syntactically valid.

- `Field` (from `pydantic`)
  - Use case: Add constraints like `gt`, `lt`, `max_length`, and defaults.
  - Problem solved: Enforces numeric ranges and length limits.

- `List`, `Dict`, `Optional`, `Annotated` (from `typing`)
  - Use case: Express list, dict, optional fields, and field metadata.
  - Problem solved: Makes field intent explicit and improves validation behavior.

- `insert_patient_details(patient: Patient)`
  - Purpose: Print patient details (name, age, weight, married, allergies, contact info) and confirm insertion.
  - Usage: Called after creating `patient1` from `patient_info`.
  - Reference: [2_pydantic_model2.py](2_pydantic_model2.py#L13)

- `update_patient_details(patient: Patient)`
  - Purpose: Print patient details and confirm update.
  - Usage: Call with a `Patient` instance when updating.
  - Reference: [2_pydantic_model2.py](2_pydantic_model2.py#L22)

## 3_field_validator.py

### Imports and why they are used

- `BaseModel` (from `pydantic`)
  - Use case: Define the `Patient` model with typed fields.
  - Problem solved: Validates and parses the input payload.

- `EmailStr` (from `pydantic`)
  - Use case: Enforce valid email format for `email`.
  - Problem solved: Rejects invalid email strings before custom checks run.

- `AnyUrl` (from `pydantic`)
  - Use case: Validate the `linked_in_urls` field.
  - Problem solved: Ensures the URL is syntactically valid.

- `Field` (from `pydantic`)
  - Use case: Add constraints like `gt`, `lt`, `max_length`, and defaults.
  - Problem solved: Enforces numeric ranges and length limits.

- `field_validator` (from `pydantic`)
  - Use case: Add custom validation logic for `email` and `name`.
  - Problem solved: Enforces domain allowlist and normalizes casing.

- `List`, `Dict`, `Optional`, `Annotated` (from `typing`)
  - Use case: Express list, dict, optional fields, and field metadata.
  - Problem solved: Makes field intent explicit and improves validation behavior.

- `email_validator(cls, value)`
  - Purpose: Validate that `email` belongs to allowed domains (`hdfc.com`, `icici.com`).
  - Usage: Runs automatically via `@field_validator('email')` on model creation.
  - Reference: [3_field_validator.py](3_field_validator.py#L17)

- `transform_name(cls, value)`
  - Purpose: Normalize `name` by converting it to uppercase.
  - Usage: Runs automatically via `@field_validator('name')` on model creation.
  - Reference: [3_field_validator.py](3_field_validator.py#L32)

- `insert_patient_details(patient: Patient)`
  - Purpose: Print patient details and confirm insertion.
  - Usage: Called after creating `patient1` from `patient_info`.
  - Reference: [3_field_validator.py](3_field_validator.py#L36)

- `update_patient_details(patient: Patient)`
  - Purpose: Print patient details and confirm update.
  - Usage: Call with a `Patient` instance when updating.
  - Reference: [3_field_validator.py](3_field_validator.py#L45)
