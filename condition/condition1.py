wallet = 5000
computeurPrice = 900

if computeurPrice < wallet:
    wallet -= computeurPrice
    print("Oui il est possible de payer cette article il vous restera {} euros".format(wallet))
else:
    print("Non ce m'est pas possible solde insufisant")

# -----

if computeurPrice < wallet and computeurPrice < 1000:
    wallet -= computeurPrice
    print("Oui il est possible de payer cette article il vous restera {} euros".format(wallet))
else:
    print("Non ce m'est pas possible solde insufisant")

# -----

if computeurPrice < wallet or computeurPrice < 1000:
    wallet -= computeurPrice
    print("Oui il est possible de payer cette article il vous restera {} euros".format(wallet))
else:
    print("Non ce m'est pas possible solde insufisant")