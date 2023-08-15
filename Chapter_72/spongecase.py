import random

try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''sPoNgEtExT, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

    eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass


def englishToSpongecase(message):
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        if random.randint(1, 100) <= 90:
            useUpper = not useUpper
    return spongecase


if __name__ == '__main__':
    main()
