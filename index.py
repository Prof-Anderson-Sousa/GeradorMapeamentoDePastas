import os
import re
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER


def limpar_nome_arquivo(path):
    nome = path.replace("\\", "_").replace(" ", "-")
    nome = re.sub(r'[<>:"/\\|?*]', "", nome)
    return f"mapear_{nome}.bat"


def obter_downloads():
    try:
        chave = OpenKey(HKEY_CURRENT_USER,
                        r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        val, _ = QueryValueEx(chave, "{374DE290-123F-4565-9164-39C4925E467B}")
        return os.path.expandvars(val)
    except:
        return os.path.join(os.environ["USERPROFILE"], "Downloads")


def gerar_script_bat(path_rede, destino):
    conteudo = f"""@echo off
setlocal enabledelayedexpansion

:: Caminho da pasta de rede
set "caminho={path_rede}"

:: Verificar se o caminho ja esta mapeado
for /f "tokens=1,2" %%A in ('net use ^| findstr /i /c:"!caminho!"') do (
    echo Caminho ja mapeado %%A
    goto :fim
)

:: Letras que serao testadas (Z ate D)
set "letras=Z Y X W V U T S R Q P O N M L K J I H G F E D"

:: Procura uma letra de unidade livre
for %%L in (!letras!) do (
    if not exist %%L:\\ (
        set "unidade=%%L:"
        goto :mapear
    )
)

echo ERRO: Nenhuma letra de unidade disponivel para mapeamento.
goto :fim

:mapear
echo Mapeando !unidade! para "!caminho!"...
net use !unidade! "!caminho!" /persistent:yes

if !errorlevel! == 0 (
    echo Unidade mapeada com sucesso em !unidade!.
) else (
    echo Falha ao mapear a unidade de rede.
)

:fim
pause
"""
    # Salvar como UTF-8 sem BOM (evita ´╗┐)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)


def ao_clicar():
    path = entrada.get().strip()
    if not path.startswith("\\\\"):
        messagebox.showerror("Erro", "O caminho deve comecar com \\\\")
        return
    nome = limpar_nome_arquivo(path)
    pasta = Path(obter_downloads()) / nome
    try:
        gerar_script_bat(path, pasta)
        messagebox.showinfo("Sucesso", f"Script gerado com sucesso em:\n{pasta}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# === Interface Gráfica ===
janela = tk.Tk()
janela.title("Gerador de Mapeador de Rede")
janela.geometry("450x160")
janela.configure(bg="#f0f8f0")
janela.resizable(False, False)

frame = tk.Frame(janela, bg="#f0f8f0")
frame.pack(expand=True)

tk.Label(frame, text="Caminho de rede:", font=("Segoe UI", 10), bg="#f0f8f0").pack(pady=(15, 5))

entrada = tk.Entry(frame, width=40, font=("Segoe UI", 10))
entrada.pack()

tk.Button(frame, text="Gerar", command=ao_clicar, font=("Segoe UI", 10), width=12).pack(pady=20)

janela.mainloop()
