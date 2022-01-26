
def print_wallak(n):
    print("Wallak")
    if n <= 2:
        return
    print_wallak(n // 2)

print_wallak(2**100)





