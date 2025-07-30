```python
from codetable import Code, Codes, msg


class UserErrorCodes(Codes):
    NAMESPACE: str = "user"

    ALREADY_EXISTS: str
    DOES_NOT_EXIST: Code = msg("User does not exist.")


print("# ALREADY_EXISTS\n")
print("code:", UserErrorCodes.ALREADY_EXISTS)

print("\n# DOES_NOT_EXIST\n")
print("obj:", UserErrorCodes.DOES_NOT_EXIST)
print("code:", UserErrorCodes.DOES_NOT_EXIST.code)
print("msg:", UserErrorCodes.DOES_NOT_EXIST.msg)

# # ALREADY_EXISTS

# code: user_already_exists

# # DOES_NOT_EXIST

# obj: Code(code='user_does_not_exist', msg='User does not exist.')
# code: user_does_not_exist
# msg: User does not exist.
```
