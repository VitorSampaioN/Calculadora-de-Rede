# Calculadora de Rede

## Visão Geral
Este aplicativo de calculadora de rede foi desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. Ele permite que os usuários insiram um endereço IP e uma máscara de sub-rede para calcular e exibir diversas informações de rede, incluindo o endereço IP em binário, endereço de rede, endereço de difusão, quantidade e intervalo de endereços disponíveis, e máscara de sub-rede quebrada, se aplicável.

## Funcionalidades Principais
- **Conversão de IP para Binário**: Converte o endereço IP fornecido para sua representação binária.
- **Cálculo do Endereço de Rede**: Calcula e exibe o endereço de rede tanto em formato binário quanto decimal.
- **Cálculo do Endereço de Difusão**: Calcula e exibe o endereço de difusão tanto em formato binário quanto decimal.
- **Exibição de Endereços Disponíveis**: Calcula e exibe o intervalo de endereços IP disponíveis dentro da sub-rede.
- **Máscara de Sub-Rede Quebrada**: Calcula e exibe a máscara de sub-rede quebrada quando aplicável.
- **Interface Intuitiva**: Interface gráfica simples e amigável, facilitando a interação do usuário.

## Como Utilizar
1. **Entrada de Dados**: O usuário insere um endereço IP no formato `xxx.xxx.xxx.xxx` e a máscara de sub-rede correspondente (por exemplo, `24` para uma máscara `255.255.255.0`).
2. **Calcular**: Ao clicar no botão "Calcular", o aplicativo processa as entradas e exibe os resultados na área designada.

## Exemplo de Uso
- **Entrada**:
  - IP: `192.168.10.1`
  - Mask: `24`
- **Saída**:
  - Endereço IP em binário: 11000000 10101000 00001010 00000001
  - Endereço de Rede (binário): 11000000 10101000 00001010 00000000
  - Endereço de Difusão (binário): 11000000 10101000 00001010 11111111
  - Endereço de Rede: 192.168.10.0
  - Endereço de Difusão: 192.168.10.255
  - Quantidade Disponível: 254
  - Endereços Disponíveis: 192.168.10.1 - 192.168.10.254
  - Máscara de Sub-Rede: 255.255.255.0
