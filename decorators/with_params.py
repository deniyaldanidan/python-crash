# import func
USERS = {"sarah": {"name": "Sarah", "username": "sarah_1", "secret": "sarah_123"}}


def logger(base_fn):
    def logger_enhancer(*args, **kwargs):
        result = base_fn(*args, **kwargs)
        print(f"The result of the {base_fn.__name__} is {result}")
        # return result

    return logger_enhancer


def my_dec(base_fn):
    def my_enhancer(*args, **kwargs):
        if len(args) != 0:
            args = list(args)
            args[0] = USERS[args[0]]
            # args.insert(0, USERS[args[0]])
        if "user" in kwargs:
            name = kwargs["user"]
            kwargs["user"] = USERS[name]
        # print(args)
        # print(kwargs)
        # name = args[0]
        # kwargs["user"] = USERS[name]
        # print(args)
        # print(kwargs)
        return base_fn(*args, **kwargs)

    return my_enhancer


@my_dec
@logger
def find_user(user, arg2):
    print(f"my second argument is {arg2}")
    return user["secret"]
    # return "amen"


find_user(user="sarah", arg2="2nd-fn-argument")
find_user("sarah", "3rd-fn-argument")
