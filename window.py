# -*- coding utf-8 -*-

from tkinter import *

# Função de Calcular
def calcularRede():
    informacoes.delete("1.0", END)

    try:
        ip_str = campoIP.get().split(".")
        mask = int(campoMask.get())

        if len(ip_str) < 4:
            erro = "\nERRO: por favor, digite um endereço IP válido\nNão se esqueça de colocar os pontos (exemplo: 192.168.10.1)."
            informacoes.insert("1.0", erro)
            return

        ip_int = [int(ip) for ip in ip_str]
        ip_binario = ''.join([bin(octeto)[2:].zfill(8) for octeto in ip_int])

        # Calcula a máscara de sub-rede completa
        mask_binario = (mask * '1' + (32 - mask) * '0')
        mask_int = [int(mask_binario[i:i+8], 2) for i in range(0, 32, 8)]

        # Calcula o endereço de rede
        rede_binario = ''.join(['1' if mask_binario[i] == '1' and ip_binario[i] == '1' else '0' for i in range(32)])
        rede_int = [int(rede_binario[i:i+8], 2) for i in range(0, 32, 8)]

        # Calcula o endereço de difusão
        difusao_binario = rede_binario[:mask] + (32-mask) * '1'
        difusao_int = [int(difusao_binario[i:i+8], 2) for i in range(0, 32, 8)]

        # Calcula os endereços disponíveis
        numero_enderecos_disponiveis = (2 ** (32 - mask)) - 2
        enderecos_disponiveis = f"{rede_int[0]}.{rede_int[1]}.{rede_int[2]}.{rede_int[3]+1} - {difusao_int[0]}.{difusao_int[1]}.{difusao_int[2]}.{difusao_int[3]-1}"

        # Monta o texto com as informações
        texto = f"""Endereço IP em binário:        {' '.join([bin(octeto)[2:].zfill(8) for octeto in ip_int])}
Endereço de Rede (binário):    {' '.join([bin(octeto)[2:].zfill(8) for octeto in rede_int])}
Endereço de Difusão (binário): {' '.join([bin(octeto)[2:].zfill(8) for octeto in difusao_int])}
Endereço de Rede:              {'.'.join(map(str, rede_int))}
Endereço de Difusão:           {'.'.join(map(str, difusao_int))}
Quantidade Disponível:         {numero_enderecos_disponiveis}
Endereços Disponíveis:         {enderecos_disponiveis}
Máscara de Sub-Rede:           {'.'.join(map(str, mask_int))}"""

        informacoes.insert("1.0", texto)

    except Exception as e:
        erro = f"\nERRO: {str(e)}"
        informacoes.insert("1.0", erro)


# Interface Gráfica
window = Tk()

window.title("Calculadora de Rede")

window.geometry("661x694")
window.configure(bg = "#495a87")
canvas = Canvas(
    window,
    bg = "#495a87",
    height = 694,
    width = 661,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    326.5, 45.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    407.5, 156.0,
    image = entry0_img)

campoIP = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

campoIP.place(
    x = 194, y = 135,
    width = 427,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    407.5, 211.5,
    image = entry1_img)

campoMask = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

campoMask.place(
    x = 194, y = 192,
    width = 427,
    height = 37)

canvas.create_text(
    152.5, 155.5,
    text = "IP:",
    fill = "#ffffff",
    font = ("Inter-Medium", int(40.0)))

canvas.create_text(
    121.0, 211.5,
    text = "Mask:",
    fill = "#ffffff",
    font = ("Inter-Medium", int(40.0)))

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    331.0, 495.0,
    image = entry2_img)

informacoes = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

informacoes.place(
    x = 18, y = 313,
    width = 626,
    height = 362)

img0 = PhotoImage(file = f"img0.png")
calcular = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = calcularRede,
    relief = "flat")

calcular.place(
    x = 400, y = 246,
    width = 221,
    height = 52)

window.resizable(False, False)
window.mainloop()
