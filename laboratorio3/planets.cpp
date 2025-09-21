#include <iostream>
#include <vector>
#include <map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <string>
#include <sstream>

using ll = long long;
using pii = std::pair<ll, int>;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    std::cin >> n >> m;
    std::vector<std::map<int, int>> grafo(n + 1);
    std::vector<ll> custos(n + 1, LLONG_MAX);
    custos[1] = 0;

    std::vector<std::unordered_set<int>> restricoes(n + 1);

    for (int i = 0; i < m; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        grafo[a][b] = c;
        grafo[b][a] = c;
    }

    std::cin.ignore(); 
    
    for (int i = 1; i <= n; ++i) {
        std::string linha;
        std::getline(std::cin, linha);
        std::stringstream ss(linha);

        int k;
        ss >> k;
        if (k > 0) {
            int tempo;
            while (ss >> tempo) {
                restricoes[i].insert(tempo);
            }
        }
    }

    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> fila;
    fila.push({0, 1});

    while (!fila.empty()) {
        ll custo_atual = fila.top().first;
        int no_atual = fila.top().second;
        fila.pop();

        if (custo_atual > custos[no_atual]) {
            continue;
        }

        ll tempo_de_partida = custo_atual;
        
        while (restricoes[no_atual].count(tempo_de_partida)) {
            tempo_de_partida++;
        }

        for (auto const& [vizinho, custo_viagem] : grafo[no_atual]) {
            ll novo_custo_chegada = tempo_de_partida + custo_viagem;

            if (novo_custo_chegada < custos[vizinho]) {
                custos[vizinho] = novo_custo_chegada;
                fila.push({novo_custo_chegada, vizinho});
            }
        }
    }

    if (custos[n] == LLONG_MAX) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << custos[n] << std::endl;
    }

    return 0;
}