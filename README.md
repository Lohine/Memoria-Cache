# Memoria Cache

<div align="center">
  Estudamos que a memória cache é muito menor do que a memória principal, em contrapartida ela é muito mais rápida e próxima ao processador. Dessa forma,  com interesse em performance com acessos de forma otimizada, temos políticas de mapeamento e substituição de quais endereços ficam na cache, visto que sempre há disputa por endereços nessa memória. Nessa prática, não vamos pensar em implementação da memória principal (apenas usá-la), ou seja, nos preocuparemos com o endereçamento na cache – testando endereços na cache a princípio vazia e somente fazendo as comparações ditadas pelo método estudado. Ainda, não nos preocuparemos com os endereços em bits ou bytes, mas sim, com fins didáticos, utilizaremos referências de endereços inteiros.
 
## Mapeamento direto 
  <br>
  
  Queremos analisar o passo-a-passo de acesso no mapeamento direto (assim como foi visto em aula feito a mão). Ou seja, enxergar qual posição está sendo disputada nesse mapeamento e como é realizada a troca. Ainda, queremos analisar a quantidade de hits (acertos) e misses (falhas) de acordo com as posições solicitadas pelo processador.

  ## Resumo apresentado 
  ![image](https://github.com/Lohine/Memoria-Cache/assets/91105011/91ef7ef0-3be4-4442-bdf6-ac370f8417b5)

