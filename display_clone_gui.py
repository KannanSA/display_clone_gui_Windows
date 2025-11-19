#Copyright (c) 2025 Kannan Industrials Ltd All rights reserved.
import subprocess
import tkinter as tk
from tkinter import messagebox

def run_displayswitch(mode: str) -> None:
    """
    Call Windows displayswitch.exe with one of:
    /clone   - Duplicate (mirror) displays
    /extend  - Extend desktop across displays
    /internal - PC screen only
    /external - Second screen only
    """
    try:
        subprocess.run(["displayswitch.exe", mode], check=True)
        mode_name = {
            "/clone": "Duplicate (Clone)",
            "/extend": "Extend",
            "/internal": "PC screen only",
            "/external": "Second screen only",
        }.get(mode, mode)

        messagebox.showinfo("Success", f"Display mode set to: {mode_name}")
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "displayswitch.exe not found.\n\n"
            "This tool is only available on Windows 7 and later.\n"
            "Make sure you're running this on Windows."
        )
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Error",
            f"Windows failed to change display mode.\n\nDetails: {e}"
        )
    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Unexpected error:\n{e}"
        )

def set_clone():
    run_displayswitch("/clone")

def set_extend():
    run_displayswitch("/extend")

def set_internal():
    run_displayswitch("/internal")

def set_external():
    run_displayswitch("/external")

def main():
    root = tk.Tk()
    root.title("Display Mode Switcher")
    root.resizable(False, False)

    # Main window layout
    frm = tk.Frame(root, padx=20, pady=20)
    frm.pack()

    title_label = tk.Label(
        frm,
        text="Display Mode Switcher",
        font=("Segoe UI", 14, "bold")
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    info_label = tk.Label(
        frm,
        text=(
            "Use these buttons to change Windows display mode.\n"
            "For cloning your primary monitor to your HDMI TV,\n"
            "click \"Duplicate (Clone)\"."
        ),
        justify="left"
    )
    info_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))

    # Buttons
    btn_clone = tk.Button(
        frm,
        text="Duplicate (Clone)",
        width=18,
        command=set_clone
    )
    btn_clone.grid(row=2, column=0, padx=5, pady=5)

    btn_extend = tk.Button(
        frm,
        text="Extend",
        width=18,
        command=set_extend
    )
    btn_extend.grid(row=2, column=1, padx=5, pady=5)

    btn_internal = tk.Button(
        frm,
        text="PC screen only",
        width=18,
        command=set_internal
    )
    btn_internal.grid(row=3, column=0, padx=5, pady=5)

    btn_external = tk.Button(
        frm,
        text="Second screen only",
        width=18,
        command=set_external
    )
    btn_external.grid(row=3, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
