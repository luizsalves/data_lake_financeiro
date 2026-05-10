# Pacote Completo - Nova Aba Power BI (Overview Chamados TI Hoje)

## 1) Nome da nova aba
- `Overview Chamados TI hoje`

## 2) Pré-requisito de campos (ajuste os nomes conforme seu modelo)
Use uma tabela de fatos (ex.: `Chamados`) com colunas equivalentes:
- `Chamados[IdChamado]` (número/chave do chamado)
- `Chamados[CodigoChamado]` (ex.: TI.002)
- `Chamados[Responsavel]`
- `Chamados[Status]` (ex.: Sem atendimento, No prazo, Em atraso, Em pausa, Encerrado)
- `Chamados[DataAbertura]`
- `Chamados[DataEncerramento]`

## 3) Medidas DAX (copiar e colar)
> Se os nomes das colunas/tabela forem diferentes no seu `.pbix`, troque somente os identificadores.

```DAX
Chamados Total =
COUNTROWS(Chamados)
```

```DAX
Chamados sem atendimento =
CALCULATE(
    [Chamados Total],
    Chamados[Status] = "Sem atendimento"
)
```

```DAX
Chamados no prazo =
CALCULATE(
    [Chamados Total],
    Chamados[Status] = "No prazo"
)
```

```DAX
Chamados em atraso =
CALCULATE(
    [Chamados Total],
    Chamados[Status] = "Em atraso"
)
```

```DAX
Chamados em pausa =
CALCULATE(
    [Chamados Total],
    Chamados[Status] = "Em pausa"
)
```

```DAX
Chamados encerrados =
CALCULATE(
    [Chamados Total],
    Chamados[Status] = "Encerrado"
)
```

```DAX
Dias em aberto =
VAR _fim = COALESCE(Chamados[DataEncerramento], TODAY())
RETURN DATEDIFF(Chamados[DataAbertura], _fim, DAY)
```

```DAX
Aging (texto) =
VAR d = MAX(Chamados[Dias em aberto])
RETURN FORMAT(d, "0") & " dias"
```

```DAX
Qtd Chamados =
DISTINCTCOUNT(Chamados[IdChamado])
```

```DAX
Atendimentos sem chamado =
CALCULATE(
    [Chamados Total],
    ISBLANK(Chamados[IdChamado])
)
```

## 4) Layout da página (igual ao mockup)
Configuração da página:
- Tamanho: `16:9`
- Plano de fundo: cinza claro (`#E6E6E6`)

### Faixa de título (topo)
- Inserir `Forma > Retângulo`
- Texto: `Overview Chamados TI hoje`
- Cor fundo: `#005C84` (ou próxima do azul do mockup)
- Fonte: branca, centralizada

### Linha de cards (5 cards)
Criar 5 visuais de `Cartão`:
1. Chamados sem atendimento -> medida `[Chamados sem atendimento]`
2. Chamados no prazo -> medida `[Chamados no prazo]`
3. Chamados em atraso -> medida `[Chamados em atraso]`
4. Chamados em pausa -> medida `[Chamados em pausa]`
5. Chamados encerrados -> medida `[Chamados encerrados]`

Formato dos cards:
- Fundo: azul `#005C84`
- Título/categoria e valor: branco
- Borda: azul escuro
- Canto reto

Ícones de alerta (triângulos):
- Inserir forma triângulo vermelho nos cards críticos (sem atendimento / no prazo se quiser alerta)
- Inserir triângulo verde para cards positivos (encerrados)

### Tabelas centrais
#### Tabela 1: `Chamados Críticos`
Visual: `Tabela`
Campos:
- `Chamados[CodigoChamado]`
- `Chamados[IdChamado]`
- `[Aging (texto)]`

Filtro do visual:
- Status em (`Sem atendimento`, `Em atraso`)

Ordenação:
- Maior `Dias em aberto` primeiro

#### Tabela 2: `Top chamados com atrasos`
Visual: `Tabela` ou `Matriz`
Campos sugeridos:
- `Chamados[CodigoChamado]`
- `[Qtd Chamados]`
- `[Aging (texto)]`

Filtro do visual:
- `Chamados[Status] = "Em atraso"`

Ordenação:
- `[Qtd Chamados]` desc

### Gráficos inferiores
#### Gráfico A: `Chamados por responsável`
Visual: `Barras agrupadas`
- Eixo Y: `Chamados[Responsavel]`
- Legenda: `Chamados[Status]`
- Valores: `[Qtd Chamados]`

Filtrar legenda para manter:
- `Em pausa`, `Em atraso`, `No prazo`

#### Gráfico B: `Atendimentos sem chamado`
Visual: `Barras agrupadas`
- Eixo Y: `Chamados[Responsavel]`
- Legenda: `Chamados[Status]`
- Valores: `[Atendimentos sem chamado]` (ou `[Qtd Chamados]` com filtro `IdChamado em branco`)

## 5) Tema visual sugerido
- Azul principal: `#005C84`
- Azul borda: `#003E59`
- Fundo página: `#E6E6E6`
- Texto escuro: `#1F1F1F`
- Verde indicador: `#7AC943`
- Vermelho indicador: `#FF1F1F`

## 6) Sequência rápida (10 minutos)
1. Duplicar uma página existente do relatório.
2. Renomear para `Overview Chamados TI hoje`.
3. Criar todas as medidas DAX acima.
4. Montar faixa de título + 5 cards.
5. Inserir as 2 tabelas e aplicar filtros.
6. Inserir os 2 gráficos de barras.
7. Ajustar cores/fontes para o padrão acima.
8. Validar números batendo com filtros de status.

## 7) Validação final
Checklist:
- Total de cards confere com filtros de status.
- Tabela de críticos só mostra sem atendimento/atraso.
- Top atrasos está ordenado corretamente.
- Gráficos por responsável exibem somente status desejados.
- Página está em 16:9 e sem sobreposição de visuais.

---

Se quiser, no próximo passo eu te passo uma versão **100% aderente ao seu modelo**: você me manda print da lista de campos (painel Campos) e eu te devolvo o DAX já com os nomes exatos.
