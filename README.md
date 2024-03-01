# BRKGA para School Timetabling Problem

Este é um projeto que implementa o algoritmo BRKGA (Biased Random-Key Genetic Algorithm) para resolver o School Timetabling Problem (Problema de Agendamento Escolar). O BRKGA é um algoritmo genético que se destaca pela sua eficiência e capacidade de lidar com problemas complexos de otimização combinatória.

## Descrição do Problema

O School Timetabling Problem é um problema desafiador que envolve a alocação eficiente de recursos escolares, como salas de aula, professores e horários, levando em consideração diversas restrições, como disponibilidade de recursos, preferências dos professores e evitar conflitos de horários.

## Solução Proposta

O BRKGA é uma abordagem eficaz para resolver o School Timetabling Problem. Ele se baseia na ideia de representar as soluções como vetores de números reais (chaves aleatórias), em vez de representações binárias tradicionais. Isso permite uma diversificação mais eficaz da população e uma exploração mais eficiente do espaço de busca.

## Funcionalidades

- Implementação do BRKGA para o School Timetabling Problem
- Geração de soluções iniciais aleatórias
- Avaliação da qualidade das soluções utilizando uma função de aptidão
- Operadores genéticos adaptativos, como crossover e mutação
- Visualização dos resultados e estatísticas do processo de otimização

## Instalação e Uso

1. Clone este repositório: `git clone https://github.com/seu-usuario/brkga-timetabling.git`
2. Navegue até o diretório do projeto: `cd brkga-timetabling`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o algoritmo BRKGA: `python main.py`

## Contribuindo

Se você gostaria de contribuir para este projeto, por favor siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para sua contribuição: `git checkout -b minha-contribuicao`
3. Faça suas alterações
4. Faça commit das suas alterações: `git commit -am 'Adicionando uma nova funcionalidade'`
5. Faça push para o branch: `git push origin minha-contribuicao`
6. Abra um pull request
