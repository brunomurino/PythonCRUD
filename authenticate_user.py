import hashlib
from database_connect import runQuery

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def authenticate_user(varLogin, varPwrd):

    query = """
    select PWRD_SHA256 FROM USERS WHERE USERNAME = "{}";
    """.format(varLogin)

    rs, _ = runQuery(query)

    user_sha_pwrd = rs[0][0]
    # user_sha_pwrd = "b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c"

    try:
        validUser = encrypt_string(varPwrd) == user_sha_pwrd
    except:
        pass

    return validUser

    # if validUser: # entryPwrd == senha
    #     loginPage.destroy()
        
    # else:
    #     entryLogin = tk.Entry(loginPage).grid(row=1, column=1)
    #     entryPwrd = tk.Entry(loginPage).grid(row=2, column=1)