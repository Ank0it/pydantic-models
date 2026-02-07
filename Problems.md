# Project Issues Log

This README captures the unique problems encountered while running the project based on the provided terminal history.

## Unique Problems Faced

1. **Pydantic model field missing type annotation**
   - Error: `A non-annotated attribute was detected: contact_details = typing.Dict[str, str]`
   - Cause: Field declared without a proper type annotation.

2. **Required field missing at runtime**
   - Error: `ValidationError: contact_details - Field required`
   - Cause: Input data missing the required `contact_details` field.

3. **Invalid Python dictionary syntax**
   - Error: `SyntaxError: invalid syntax`
   - Cause: Incorrect dict literal structure (`conatact_details` list with key/value syntax).

4. **Typo in field name access**
   - Error: `AttributeError: 'Patient' object has no attribute 'conatct_details'`
   - Cause: Misspelled attribute name (`conatct_details` vs `contact_details`).

5. **Unterminated string literal in dict**
   - Error: `SyntaxError: unterminated string literal`
   - Cause: Missing quote around a dictionary key (e.g., `weight':87.89`).

6. **Missing optional dependency for email validation**
   - Error: `ImportError: email-validator is not installed`
   - Cause: `EmailStr` requires `email-validator` package.

7. **Failed pip install command**
   - Issue: `pip install 'pydantic[email]` command had a missing closing quote and was interrupted.

8. **Pip launcher points to missing Python 3.13**
   - Error: `Fatal error in launcher: Unable to create process using ... Python313\python.exe`
   - Cause: `pip` shim was configured for a Python 3.13 path that does not exist on this system.

9. **Command canceled during package install**
   - Issue: `python -m pip install 'pydantic[email]` was started with an unterminated quote and then canceled.

10. **Scripts directory not on PATH**
    - Warning: `email_validator.exe is installed ... which is not on PATH`
    - Cause: User scripts folder is not included in the system PATH.

11. **Pydantic V2 deprecation warning for `Field` extras**
   - Warning: `Using extra keyword arguments on Field is deprecated ... Use json_schema_extra instead`
   - Cause: `Field(..., example=...)` uses a deprecated extra key in Pydantic V2.

12. **Email domain validation failure**
   - Error: `Value error, Not a valid domain` for `email`
   - Cause: Email validation failed in the custom field validator.

13. **Printed bound method instead of value**
   - Issue: Output like `<built-in method upper of str object ...>`
   - Cause: Printing `str.upper` (method) instead of calling it (missing `()`).
