class CacheAss:

    @staticmethod
    def inicializar(tamanho_cache):
        return {i: -1 for i in range(tamanho_cache)}

    @staticmethod
    def imprimir(cache, tec_sub, controle):
        if tec_sub == 1:
            lru = -1
            if len(controle) == len(cache):
                lru = controle[0]
            
            print("Tamanho do conjunto:", len(cache))
            print("Cache: ")
            for chave, valor in cache.items():
                if lru == chave:
                    print(chave, ":", valor, "LRU")
                else: 
                    print(chave, ":", valor)
            print("")

        elif tec_sub == 2:
            lfu = -1
            if len(controle) == len(cache):
                lfu = controle.index(min(controle))

            print("Tamanho do conjunto:", len(cache))
            print("Cache: ")
            for chave, valor in cache.items():
                if lfu == chave:
                    print(chave, ":", valor, "LFU")
                else: 
                    print(chave, ":", valor)
            print("")

        else:
            fifo = -1
            if len(controle) == len(cache):
                fifo = controle[0]

            print("Tamanho do conjunto:", len(cache))
            print("Cache: ")
            for chave, valor in cache.items():
                if fifo == chave:
                    print(chave, ":", valor, "FI")
                else: 
                    print(chave, ":", valor)
            print("")


def mapeamento_ass_conj(pos_memoria):
    tam_conj = 0
    tec_sub = 0

    while True:
        tam_conj = int(input("Escolha o tamanho do conjunto:\n 1 bloco\n 2 blocos\n 4 blocos\n 8 blocos\n 16 blocos\n"))
        if (tam_conj == 1 
            or tam_conj == 2 
            or tam_conj == 4 
            or tam_conj == 8 
            or tam_conj == 16):
            break

        else:
            print("Valor inválido, aperter ENTER para continuar.")
            input()
            continue
    print("----------------------------------------")
    while True:
        print("Escolha entre as técnicas de substituição: ")
        print("1. LRU")
        print("2. LFU")
        print("3. FIFO")
        print("")
        tec_sub = int(input())
        if (tec_sub == 1
            or tec_sub == 2
            or tec_sub == 3):
            break
        
        else:
            print("Técnica inválida, aperter ENTER para continuar.")
            input()
            continue
    print("----------------------------------------")
    # inicializa a cache
    cache = CacheAss.inicializar(tam_conj)

    # contador de hits e misses
    hits = 0
    misses = 0

    # controlador de substituição
    controle = []
    contLinha = 0
    CacheAss.imprimir(cache, tec_sub, controle)

    if tec_sub == 1:
        
        for memoria in pos_memoria:
            print(f"Linha {contLinha} | Posição da memória desejada {memoria}")
            x = 0
            for i in range(len(cache)):
                if cache[i] == memoria:
                    hits += 1
                    print("Status: Hit")
                    controle.remove(i)
                    controle.append(i)
                    x = 1
                    break
                
                elif cache[i] == -1:
                    cache[i] = memoria
                    misses += 1
                    print("Status: Miss")
                    controle.append(i)
                    x = 1
                    break
            
            if x == 0:
                y = controle[0]
                controle.pop(0)
                controle.append(y)
                cache[y] = memoria
                misses += 1
                print("Status: Miss")
            contLinha += 1
            CacheAss.imprimir(cache, tec_sub, controle)
            print(pos_memoria)
            print("")

    elif tec_sub == 2:
         for memoria in pos_memoria:
            print(f"Linha {contLinha} | Posição da memória desejada {memoria}")
            x = 0
            for i in range(len(cache)):
                if cache[i] == memoria:
                    hits += 1
                    print("Status: Hit")
                    controle[i] += 1
                    x = 1
                    break
                
                elif cache[i] == -1:
                    cache[i] = memoria
                    misses += 1
                    print("Status: Miss")
                    controle.append(1)
                    x = 1
                    break

            if x == 0:
                y = controle.index(min(controle))
                controle[y] += 1
                cache[y] = memoria
                misses += 1
                print("Status: Miss")
            contLinha += 1
            CacheAss.imprimir(cache, tec_sub, controle)
            print(pos_memoria)
            print("")

    else:
        for memoria in pos_memoria:
            print(f"Linha {contLinha} | Posição da memória desejada {memoria}")
            x = 0
            for i in range(len(cache)):
                if cache[i] == memoria:
                    hits += 1
                    print("Status: Hit")
                    x = 1
                    break
                
                elif cache[i] == -1:
                    cache[i] = memoria
                    misses += 1
                    print("Status: Miss")
                    controle.append(i)
                    x = 1
                    break

            if x == 0:
                y = controle[0]
                controle.pop(0)
                controle.append(y)
                cache[y] = memoria
                misses += 1
                print("Status: Miss")
            contLinha += 1
            CacheAss.imprimir(cache, tec_sub, controle)
            print(pos_memoria)
            print("")

# imprime o resumo
    total_acessos = len(pos_memoria)
    taxa_hit = (hits / total_acessos) * 100
    print("========================================")
    print("MAPEAMENTO ASSOCIATIVO POR CONJUNTO - PERFORMANCE EM SISTEMAS CIBERFÍSICOS")
    print("")
    print("Resumo:")
    print("")
    print(f"Total de posições de memória acessadas: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de cache hit: {taxa_hit:.2f}%")
    print("")