```python
from codetable import Code, Codes, msg


class UserErrorCodes(Codes):
    NAMESPACE: str = "user"

    ALREADY_EXISTS: Code
    DOES_NOT_EXIST: Code = msg("User does not exist.")


print("# ALREADY_EXISTS\n")
print("obj:", UserErrorCodes.ALREADY_EXISTS)
print("code:", UserErrorCodes.ALREADY_EXISTS.code)
print("msg:", UserErrorCodes.ALREADY_EXISTS.msg)

print("\n# DOES_NOT_EXIST\n")
print("obj:", UserErrorCodes.DOES_NOT_EXIST)
print("code:", UserErrorCodes.DOES_NOT_EXIST.code)
print("msg:", UserErrorCodes.DOES_NOT_EXIST.msg)

# # ALREADY_EXISTS

# obj: Code(code='user_already_exists', msg=None)
# code: user_already_exists
# msg: None

# # DOES_NOT_EXIST

# obj: Code(code='user_does_not_exist', msg='User does not exist.')
# code: user_does_not_exist
# msg: User does not exist.
```
