import time


def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"{base_fn.__name__} took {end_time - start_time} seconds")

    return enhanced_fn


@timer_dec
def brew_tea():
    print("Brewing TEA")
    time.sleep(0.5)
    print("Tea is ready")


@timer_dec
def bakePizza():
    print("Baking Pizza")
    time.sleep(3)
    print("Pizza is ready")


brew_tea()
bakePizza()
