def main():
    pass


def test_how_many_props():
    props = open("./data/metricas.limpo.txt")

    # all lines have 318 props!
    i = 0
    expected_props = 318
    while line := props.readline():
        i += 1
        lista_props = line.split("\t")
        n_props = len(lista_props)

        if n_props != expected_props:
            print(f"line {i} does not have {expected_props} props")


if __name__ == "__main__":
    main()
