from Dessin import generate_dessins_single, generate_dessins_single2, generate_dessins_single3, generate_dessins_single4, generate_dessins_single_fast
import time
import jsonpickle

# import cProfile
# import re


if __name__ == "__main__":
    # order
    n = 5

    # cProfile.run('re.compile("generate_dessins_single|n")')

    # Generate dessins
    # tic = time.perf_counter()
    # dessins = generate_dessins_single(n)
    # print(len(dessins))
    # for des in dessins:
    #     des.calcEulerChi()
    # toc = time.perf_counter()
    # print(f"Generating time: {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    dessins = generate_dessins_single2(n)
    print(len(dessins))
    for des in dessins:
        des.calcEulerChi()
    toc = time.perf_counter()
    print(f"Generating time: {toc - tic:0.4f} seconds")

    # tic = time.perf_counter()
    # dessins = generate_dessins_single3(n)
    # print(len(dessins))
    # for des in dessins:
    #     des.calcEulerChi()
    # toc = time.perf_counter()
    # print(f"Generating time: {toc - tic:0.4f} seconds")

    # tic = time.perf_counter()
    # dessins = generate_dessins_single4(n)
    # print(len(dessins))
    # for des in dessins:
    #     des.calcEulerChi()
    # toc = time.perf_counter()
    # print(f"Generating time: {toc - tic:0.4f} seconds")

    # tic = time.perf_counter()
    # dessins = generate_dessins_single_fast(n)
    # print(len(dessins))
    # for des in dessins:
    #     des.calcEulerChi()
    # toc = time.perf_counter()
    # print(f"Generating time: {toc - tic:0.4f} seconds")

    # write dessin to file
    tic = time.perf_counter()
    encoded_dessins = jsonpickle.encode(dessins, indent = 4)
    with open(f"data/dessins_order({n}).json", 'w') as f:
        f.write(encoded_dessins)
    toc = time.perf_counter()
    print(f"Writing time: {toc - tic:0.4f} seconds")