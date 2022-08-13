import functools

user = {"name": "a", "access": "admin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access"] == access_level:
                return func(*args, **kwargs)
            else:
                return "user is not having admin access"

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password(panel):
    if panel == "admin":
        return "123"


@make_secure("billing")
def get_user_password(panel):
    if panel == "billing":
        return "super_secured_password"


if __name__ == '__main__':
    # get_fun = make_secure(get_admin_password)
    print(get_admin_password("admin"))
    print(get_admin_password.__name__)

    print(get_user_password("admin"))
    print(get_user_password.__name__)

    print(get_user_password("billing"))
    print(get_user_password.__name__)