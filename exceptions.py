
ItemInCart = 0
# your automation code will select the items and add 2 items to the cart
# if 2 items are not added then code shall stop
if ItemInCart != 2:
    raise Exception("Products Cart Count not matching")
    pass
# another way to do it
assert(ItemInCart == 2)
# when assert condition doesn't meet it stops the code
