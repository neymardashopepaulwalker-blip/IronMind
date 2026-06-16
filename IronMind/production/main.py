
# IronMind Macropad - Firmware KMK

#IMPORTAÇÕES
import board                                        # Pinos físicos do XIAO
from kmk.kmk_keyboard import KMKKeyboard            # Cérebro do teclado
from kmk.keys import KC                             # Biblioteca de teclas
from kmk.scanners import DiodeOrientation           # Direção dos diodos
from kmk.modules.encoder import EncoderHandler      # Encoder rotativo
from kmk.extensions.media_keys import MediaKeys     # Teclas de mídia
from kmk.modules.holdtap import HoldTap             # Segurar vs pressionar

#INICIALIZAÇÃO
keyboard = KMKKeyboard()                            # Cria o teclado

#PARTE 3: EXTENSÕES
# MediaKeys permite controlar música e volume
keyboard.extensions.append(MediaKeys())

#PARTE 4: PINOS DA MATRIZ
# Colunas — 3 colunas para os 6 switches
keyboard.col_pins = (board.D0, board.D1, board.D2)

# Linhas — 2 linhas para os 6 switches
keyboard.row_pins = (board.D3, board.D4)

# Direção dos diodos (COL2ROW = corrente vai da coluna para a linha)
# Isso evita "ghosting" quando várias teclas são pressionadas ao mesmo tempo
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#PARTE 5: ENCODER
encoder_handler = EncoderHandler()

# O encoder está nos pinos D8 (A) e D9 (B) do XIAO
encoder_handler.pins = ((board.D8, board.D9, board.D7, False),)
#                         Pino A   Pino B   Botão   Invertido?

# O que o encoder faz:
# Girar direita → Volume aumenta
# Girar esquerda → Volume diminui
# Pressionar → Mute
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)  # (direita, esquerda, pressionar)
]

keyboard.modules.append(encoder_handler)

# ---- PARTE 6: TECLAS ESPECIAIS ----
# Abrir Claude (claude.ai) no navegador
# WIN + R abre o executar, depois digita o endereço
CLAUDE = KC.LWIN(KC.R)

# Abrir seu site Jarvis
JARVIS = KC.LWIN(KC.R)

# Abrir Discord
# WIN + D minimiza tudo, não queremos isso
# Usamos um atalho customizado
DISCORD = KC.LWIN(KC.R)

# Controles de música
PREV = KC.MPRV    # Música anterior
PLAY = KC.MPLY    # Play/Pause
NEXT = KC.MNXT    # Próxima música

# Layout visual:
# [ Claude.IA ] [ Jarvis ] [ Discord ]
# [ Voltar   ] [ Play   ] [ Proximo   ]

keyboard.keymap = [
    # Camada 0 — camada principal
    [
        CLAUDE,  JARVIS,  DISCORD,   # Linha 1 — Apps
        PREV,    PLAY,    NEXT,      # Linha 2 — Música
    ]
]

# O OLED mostra volume e informações de música
# Requer a biblioteca adafruit_displayio_ssd1306
try:
    import busio
    import displayio
    import terminalio
    import adafruit_displayio_ssd1306
    from adafruit_display_text import label

    displayio.release_displays()

    # I2C nos pinos SCL (D5) e SDA (D4) do XIAO
    i2c = busio.I2C(board.SCL, board.SDA)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

    # Cria a tela
    splash = displayio.Group()
    display.show(splash)

    # Texto principal
    text_area = label.Label(
        terminalio.FONT,
        text="IronMind",
        color=0xFFFFFF,
        x=28,
        y=4,
    )

    # Texto de volume
    volume_area = label.Label(
        terminalio.FONT,
        text="Vol: --",
        color=0xFFFFFF,
        x=28,
        y=20,
    )

    splash.append(text_area)
    splash.append(volume_area)

except Exception as e:
    # Se o OLED não conectar, continua sem ele
    print("OLED não encontrado:", e)

# ---- PARTE 9: INICIAR TECLADO ----
if __name__ == "__main__":
    keyboard.go()