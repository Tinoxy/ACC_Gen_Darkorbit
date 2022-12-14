import accgen


with open("accgen.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()

        if len(line) > 0:
            # this will only run when the line is NOT empty

            data, _ = line.split(';')
            usr, pwd, server = data.split(':')
            usr = usr.strip()
            pwd = pwd.strip()
            server = server.strip()
            print('{:3d} {} is created the account'.format(i, usr))
            accgen.register(usr, pwd, server)
            print(usr + " Register is Done")