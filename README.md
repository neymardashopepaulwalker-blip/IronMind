# IronMind Macropad

Um macropad customizado com 6 switches mecânicos, encoder rotativo e display OLED, desenvolvido do zero como projeto de aprendizado em CAD, programação e design de PCB.

---

## Sobre o Projeto

Criei esse macropad para desenvolver minhas habilidades em três áreas que sempre quis dominar: design de PCB no KiCad, modelagem 3D no Fusion 360 e programação de firmware com KMK/CircuitPython. O resultado ficou muito bom, mesmo com alguns erros no caminho — e aprendi muito com cada um deles!

---

## Funcionalidades

| Tecla | Função |
|---|---|
| SW1 | Abre Claude (claude.ai) |
| SW2 | Abre Jarvis (site pessoal) |
| SW3 | Abre Discord |
| SW4 | Música anterior |
| SW5 | Play / Pause |
| SW6 | Próxima música |
| Encoder (girar) | Volume + / - |
| Encoder (pressionar) | Mute |
| OLED | Mostra volume e info |

---

## Lista de Materiais (BOM)

| Componente | Quantidade |
|---|---|
| Seeeduino XIAO RP2040 | 1x |
| Switch Cherry MX | 6x |
| Rotary Encoder EC11 | 1x |
| Display OLED 0.91" I2C | 1x |
| Diodo 1N4148 | 6x |
| Parafusos M3×16mm | 6x |
| Insertos Heatset M3×5×4mm | 4x |

---

## Estrutura do Repositório

```
IronMind/
├── README.md
├── CAD/
│   ├── Bottom.STEP
│   ├── Top.STEP
│   └── PCB.STEP
├── PCB/
│   ├── IronMind.kicad_pro
│   ├── IronMind.kicad_sch
│   └── IronMind.kicad_pcb
├── Firmware/
│   └── main.py
└── production/
    ├── gerbers.zip
    ├── Top.STEP
    ├── Bottom.STEP
    └── main.py
```

---

## Screenshots

### Esquemático
<img width="1181" height="732" alt="{34E5574C-7BB3-41BE-A11E-5924906EF18A}" src="https://github.com/user-attachments/assets/478c6f1f-bbb4-41f9-b93a-ec6d9fb6eb60" />

### Layout da PCB
<img width="710" height="601" alt="{A24C5048-9C87-4BA9-9754-552800DEA1DA}" src="https://github.com/user-attachments/assets/670872df-8996-4464-9943-bed99b7add6a" />

### Caixa 3D
<img width="1920" height="952" alt="{6D5FCF4E-63A1-4497-AE1E-E1854CBF7453}" src="https://github.com/user-attachments/assets/dc06128f-ac8e-4f14-a10f-7b492511ce93" />


---

## Firmware

O firmware foi escrito em Python usando o KMK. Para instalar:

1. Instale o CircuitPython no XIAO RP2040
2. Copie a pasta `kmk` para a unidade CIRCUITPY
3. Copie o `main.py` para a unidade CIRCUITPY
4. Instale o AutoHotkey e coloque o `ironmind.ahk` na pasta Startup

---

## O que aprendi

- Design de PCB no KiCad do zero
- Modelagem 3D de caixas no Fusion 360
- Firmware com KMK e CircuitPython
- Exportação de Gerbers para fabricação (JLCPCB)

---

## Autor

[@neymardashopepaulwalker-blip](https://github.com/neymardashopepaulwalker-blip)
