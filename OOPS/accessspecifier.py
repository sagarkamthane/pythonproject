class Access:

    public_var = "I'm Public"
    _protected_var = "I'm protected"
    __private_var = "I'm Private"


acc = Access()
print(acc.public_var, acc._protected_var)
print(acc._Access__private_var)  # --> private variable can't be accessed directly, access it using object._ClassName__varname