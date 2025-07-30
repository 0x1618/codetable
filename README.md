```python
from codetable import Code, Codes, CodesStorage, msg

codes_storage = CodesStorage()


class UserErrorCodes(Codes):
    NAMESPACE: str = "user"

    EXPORT_TO: CodesStorage = codes_storage  # For example, export status codes to global storage for use in frontend translations.

    ALREADY_EXISTS: str
    DOES_NOT_EXIST: Code = msg("User does not exist.")


print("# UserErrorCodes.ALREADY_EXISTS\n")
print("code:", UserErrorCodes.ALREADY_EXISTS)

print("\n# UserErrorCodes.DOES_NOT_EXIST\n")
print("obj:", UserErrorCodes.DOES_NOT_EXIST)
print("code:", UserErrorCodes.DOES_NOT_EXIST.code)
print("msg:", UserErrorCodes.DOES_NOT_EXIST.msg)

print("\n# UserErrorCodes.export_codes()\n")
print(UserErrorCodes.export_codes())


class CatCodes(Codes):
    NAMESPACE: str = "cat"

    EXPORT_TO: CodesStorage = codes_storage  # We don't call export_codes here, but it will still be exported due to the presence of EXPORT_TO. export_codes is run automatically when EXPORT_TO is present.

    NOT_HUNGRY: Code = msg("Cat is not hungry!")


print("\n# codes_storage\n")
print(codes_storage)

print("\n# codes_storage.to_json()")
print("# !!! You can change ident by passing an argument !!!\n")
print(codes_storage.to_json())

print("\n# codes_storage.to_dict()\n")
print(codes_storage.to_dict())

# # UserErrorCodes.ALREADY_EXISTS

# code: user_already_exists

# # UserErrorCodes.DOES_NOT_EXIST

# obj: Code(code='user_does_not_exist', msg='User does not exist.')
# code: user_does_not_exist
# msg: User does not exist.

# # UserErrorCodes.export_codes()

# {'user_already_exists': None, 'user_does_not_exist': 'User does not exist.'}

# # codes_storage

# CodesStorage(storage={'user_already_exists': None, 'user_does_not_exist': 'User does not exist.', 'cat_not_hungry': 'Cat is not hungry!'})

# # codes_storage.to_json()
# # !!! You can change ident by passing an argument !!!

# {
#     "user_already_exists": null,
#     "user_does_not_exist": "User does not exist.",
#     "cat_not_hungry": "Cat is not hungry!"
# }

# # codes_storage.to_dict()

# {'user_already_exists': None, 'user_does_not_exist': 'User does not exist.', 'cat_not_hungry': 'Cat is not hungry!'}
```
