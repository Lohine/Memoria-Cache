class Cache:

    @staticmethod
    def inicializar(tamanho_cache):
        return {i: -1 for i in range(tamanho_cache)}

    @staticmethod
    def imprimir(cache):
        print("\nTamanho da cache:", len(cache))
        print("Cache: ")
        for chave, valor in cache.items():
            print(chave, ":", valor)
    
def mapeamento_direto(tamanho_cache, pos_memoria):
    # inicializa a cache
    cache = Cache.inicializar(tamanho_cache)
    contLinha = 0
    # contador de hits e misses
    hits = 0
    misses = 0
    
    Cache.imprimir(cache)

    for posicao_memoria in pos_memoria:
        posicao_cache = posicao_memoria % tamanho_cache
        print(f"Linha {contLinha} | Posição da memória desejada {posicao_memoria}")
        if cache[posicao_cache] == posicao_memoria:
            hits += 1
            print("Status: Hit")
        else:
            misses += 1
            print("Status: Miss")
            cache[posicao_cache] = posicao_memoria
        contLinha += 1
        print("----------------------------------------")
        # imprime a cache atualizada
        Cache.imprimir(cache)
    
    # imprime o resumo
    total_acessos = len(pos_memoria)
    taxa_hit = (hits / total_acessos) * 100

    print("========================================")
    print("\nMAPEAMENTO DIRETO - PERFORMANCE EM SISTEMAS CIBERFÍSICOS")
    print("")
    print("Resumo:")
    print("")
    print(f"Total de posições de memória acessadas: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de cache hit: {taxa_hit:.2f}%")


