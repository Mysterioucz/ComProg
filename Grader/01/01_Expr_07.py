def mosteller(w, h):
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Mosteller formula
    mosteller = ((w * h) ** 0.5) / 60
    return mosteller


def du_bois(w, h):
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Du Bois formula
    du_bois = 0.007184 * (w**0.425) * (h**0.725)
    return du_bois


def fujimoto(w, h):
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Fujimoto formula
    fujimoto = 0.008883 * (w**0.444) * (h**0.663)
    return fujimoto


def main():
    w = float(input())
    h = float(input())
    m = mosteller(w, h)
    d = du_bois(w, h)
    f = fujimoto(w, h)
    print("Mosteller =", round(m, 5))
    print("Du Bois =", round(d, 5))
    print("Fujimoto =", round(f, 5))


exec(input())  # DON'T remove this line
