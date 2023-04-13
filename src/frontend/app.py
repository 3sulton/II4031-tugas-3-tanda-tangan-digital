import datetime
import sys, os.path
be_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/backend/')
sys.path.append(be_dir)
import rsa

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, filedialog, messagebox, StringVar, IntVar
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def App(screen=None):
    global window, gui_title
    global key_length, var_sign, var_verify
    global is_sign_file, message_sign_file_path
    global is_verify_file, message_verify_file_path

    if (screen != None):
        screen.destroy()
    window = Tk()
    gui_title = "Digital Signature RSA & SHA-3"
    window.title(gui_title)
    window.geometry("900x600")
    window.configure(bg = "#F8EFD3")
    

    canvas = Canvas(
        window,
        bg = "#2D6974",
        height = 600,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    # judul
    canvas.place(x = 0, y = 0)
    image_title = PhotoImage(
        file=relative_to_assets("title.png"))
    title = canvas.create_image(
        450.0,
        31.0,
        image=image_title
    )

# ------ GENERATE KEY MENU ------

    # frame - generate key
    image_frame_generate_key = PhotoImage(
        file=relative_to_assets("frame.png"))
    frame_generate_key = canvas.create_image(
        152.0,
        328.0,
        image=image_frame_generate_key
    )

    # title - generate key
    image_title_generate_key = PhotoImage(
        file=relative_to_assets("title-generate-key.png"))
    title_generate_key = canvas.create_image(
        151.0,
        95.0,
        image=image_title_generate_key
    )

    # panjang key
    image_panjang_key = PhotoImage(
        file=relative_to_assets("panjang_key.png"))
    panjang_key = canvas.create_image(
        76.0,
        136.0,
        image=image_panjang_key
    )

    # radio button untuk panjang key
    key_length = IntVar()

    # 512 bit
    image_512_bit = PhotoImage(
        file=relative_to_assets("512_bit.png"))
    b_512_bit = canvas.create_image(
        93.0,
        161.0,
        image=image_512_bit
    )

    bit_512 = Radiobutton(
              window,
              variable = key_length,
              bg = "#CEDFCC",
              value = 512)
    
    bit_512.pack()
    bit_512.place(
        x = 40.0,
        y = 150.0
    )

    # 1024 bit
    image_1024_bit = PhotoImage(
        file=relative_to_assets("1024_bit.png"))
    b_1024_bit = canvas.create_image(
        230.0,
        161.0,
        image=image_1024_bit
    )

    bit_1024 = Radiobutton(
               window,
               variable = key_length,
               bg = "#CEDFCC",
               value = 1024)
    
    bit_1024.pack()
    bit_1024.place(
        x = 170.0,
        y = 150.0
    )

    def loading():
        output_e.delete("1.0", tk.END)
        output_e.insert("1.0", "Loading...")
        output_d.delete("1.0", tk.END)
        output_d.insert("1.0", "Loading...")
        output_n.delete("1.0", tk.END)
        output_n.insert("1.0", "Loading...")

    def key_generator():
        key_len = key_length.get()

        if key_len == 0:
            tk.messagebox.showwarning(title=gui_title, message="Pilih panjang key terlebih dahulu")
            return

        r = rsa.rsa()
        e, d, n = r.get_key(key_len)

        output_e.delete("1.0", tk.END)
        output_e.insert("1.0", e)
        output_d.delete("1.0", tk.END)
        output_d.insert("1.0", d)
        output_n.delete("1.0", tk.END)
        output_n.insert("1.0", n)

        output_public_key.delete("1.0", tk.END)
        output_public_key.insert("1.0", str(e) + "," + str(n))

        output_private_key.delete("1.0", tk.END)
        output_private_key.insert("1.0", str(d) + "," + str(n))

    # Generate Key Button
    button_generate_key = PhotoImage(
        file=relative_to_assets("button_generate_key.png"))
    generate_key = Button(
        image=button_generate_key,
        borderwidth=0,
        highlightthickness=0,
        command=key_generator,
        relief="flat"
    )
    generate_key.place(
        x=77.0,
        y=188.0,
        width=150.0,
        height=30.0
    )

    # Output nilai n
    image_n = PhotoImage(
        file=relative_to_assets("n.png"))
    n = canvas.create_image(
        38.0,
        264.0,
        image=image_n
    )

    entry_output_n = PhotoImage(
        file=relative_to_assets("output.png"))
    entry_bg_output_n = canvas.create_image(
        165.5,
        264.0,
        image=entry_output_n
    )
    output_n = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    output_n.place(
        x=58.0,
        y=249.0,
        width=215.0,
        height=28.0
    )

    # Output nilai e
    image_e = PhotoImage(
        file=relative_to_assets("e.png"))
    e = canvas.create_image(
        38.0,
        306.0,
        image=image_e
    )

    entry_output_e = PhotoImage(
        file=relative_to_assets("output.png"))
    entry_bg_output_e = canvas.create_image(
        165.5,
        306.0,
        image=entry_output_e
    )
    output_e = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    output_e.place(
        x=58.0,
        y=291.0,
        width=215.0,
        height=28.0
    )

    # Output nilai d
    image_d = PhotoImage(
        file=relative_to_assets("d.png"))
    d = canvas.create_image(
        39.0,
        348.0,
        image=image_d
    )

    entry_output_d = PhotoImage(
        file=relative_to_assets("output.png"))
    entry_bg_output_d = canvas.create_image(
        165.5,
        348.0,
        image=entry_output_d
    )
    output_d = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    output_d.place(
        x=58.0,
        y=333.0,
        width=215.0,
        height=28.0
    )

    # Output Public Key
    image_public_key = PhotoImage(
        file=relative_to_assets("public_key.png"))
    public_key = canvas.create_image(
        68.0,
        398.0,
        image=image_public_key
    )

    entry_output_public_key = PhotoImage(
        file=relative_to_assets("output_key.png"))
    entry_bg_output_public_key = canvas.create_image(
        151.5,
        427.0,
        image=entry_output_public_key
    )
    output_public_key = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    output_public_key.place(
        x=30.0,
        y=412.0,
        width=243.0,
        height=28.0
    )

    # Output Private Key
    image_private_key = PhotoImage(
        file=relative_to_assets("private_key.png"))
    private_key = canvas.create_image(
        71.0,
        460.0,
        image=image_private_key
    )

    entry_output_private_key = PhotoImage(
        file=relative_to_assets("output_key.png"))
    entry_bg_output_private_key = canvas.create_image(
        151.5,
        489.0,
        image=entry_output_private_key
    )
    output_private_key = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    output_private_key.place(
        x=30.0,
        y=474.0,
        width=243.0,
        height=28.0
    )

    def save_key():
        # format public key adalah e,n
        # format private key adalah d,n
        public_key = output_public_key.get('1.0', 'end').replace("\n", "")
        private_key = output_private_key.get('1.0', 'end').replace("\n", "")

        if public_key == "" or private_key == "":
            tk.messagebox.showwarning(title=gui_title, message="Generate key terlebih dahulu")
            return
        
        public_file_path = filedialog.asksaveasfilename(
            defaultextension='.pubkey',
            filetypes=[('Custom Files', '*.pubkey'), ('All Files', '*.*')],
            title='Save Public Key',
            initialfile='my_public_key.pubkey'
        )

        if public_file_path == "":
            return

        private_file_path = filedialog.asksaveasfilename(
            defaultextension='.prikey',
            filetypes=[('Custom Files', '*.prikey'), ('All Files', '*.*')],
            title='Save Private Key',
            initialfile='my_private_key.prikey'
        )

        if private_file_path == "":
            return
        
        with open(public_file_path, 'w') as file:
            file.write(public_key)
        with open(private_file_path, 'w') as file:
            file.write(private_key)

        tk.messagebox.showinfo(title=gui_title, message="Key berhasil disimpan")


    button_save_key = PhotoImage(
        file=relative_to_assets("button_save_key.png"))
    save_key = Button(
        image=button_save_key,
        borderwidth=0,
        highlightthickness=0,
        command=save_key,
        relief="flat"
    )
    save_key.place(
        x=77.0,
        y=523.0,
        width=150.0,
        height=30.0
    )

# ------ SIGN MENU ------

    # frame - sign
    image_frame_sign = PhotoImage(
        file=relative_to_assets("frame.png"))
    frame_sign = canvas.create_image(
        450.0,
        328.0,
        image=image_frame_sign
    )

    # title - sign
    image_title_sign = PhotoImage(
        file=relative_to_assets("title_sign.png"))
    title_sign = canvas.create_image(
        449.0,
        95.0,
        image=image_title_sign
    )

    # title - message sign
    image_message_sign = PhotoImage(
        file=relative_to_assets("message.png"))
    message_sign = canvas.create_image(
        362.0,
        136.0,
        image=image_message_sign
    )

    def select_message_sign_file():
        global is_sign_file, message_sign_file_path
        message_sign_file_path = filedialog.askopenfilename(initialdir = Path(__file__),)
        ext = message_sign_file_path.split(".")[-1]
        content = message_sign_file_path
        # jika message yang diload adalah file text, maka tampilkan
        # pesan tersebut di layar
        if ext == "txt":
            is_sign_file = False
            with open(message_sign_file_path, "r") as file:
                content = file.read()
        # jika bukan, maka yang ditampilkan adalah path ke file tersebut
        # dan pathnya akan 
        else:
            is_sign_file = True
        input_message_sign.delete("1.0", tk.END)
        input_message_sign.insert("1.0", content)

    # Choose file message - sign button
    button_choose_file_message_sign = PhotoImage(
        file=relative_to_assets("choose_file.png"))
    choose_file_message_sign = Button(
        image=button_choose_file_message_sign,
        borderwidth=0,
        highlightthickness=0,
        command=select_message_sign_file,
        relief="flat"
    )
    choose_file_message_sign.place(
        x=472.0,
        y=128.0,
        width=100.0,
        height=20.0
    )

    # input message - sign
    entry_input_message_sign = PhotoImage(
        file=relative_to_assets("input_message.png"))
    entry_bg_input_message_sign = canvas.create_image(
        450.5,
        240.0,
        image=entry_input_message_sign
    )
    input_message_sign = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    input_message_sign.place(
        x=329.0,
        y=150.0,
        width=243.0,
        height=178.0
    )

    # title - private key
    image_private_key_sign = PhotoImage(
        file=relative_to_assets("private_key.png"))
    private_key_sign = canvas.create_image(
        369.0,
        363.0,
        image=image_private_key_sign
    )

    def choose_private_key():
        private_key_path = filedialog.askopenfilename(initialdir = Path(__file__),
                                                      defaultextension='.prikey',
                                                      filetypes=[('Custom Files', '*.prikey'), ('All Files', '*.*')],
                                                      title='Load Private Key')
        if private_key_path == "":
            return
        ext = private_key_path.split(".")[-1]
        if ext != "prikey":
            tk.messagebox.showwarning(title=gui_title, message="Pilih file dengan ekstensi .prikey")
            return
        
        with open(private_key_path, "r") as file:
            content = file.read()
        
        input_private_key.delete("1.0", tk.END)
        input_private_key.insert("1.0", content)
        

    # choose file button - private key
    button_choose_file_private = PhotoImage(
        file=relative_to_assets("choose_file.png"))
    choose_file_private = Button(
        image=button_choose_file_private,
        borderwidth=0,
        highlightthickness=0,
        command=choose_private_key,
        relief="flat"
    )
    choose_file_private.place(
        x=471.0,
        y=355.0,
        width=100.0,
        height=20.0
    )

    # input private key
    entry_input_private_key = PhotoImage(
        file=relative_to_assets("input_key.png"))
    entry_bg_input_private_key = canvas.create_image(
        449.5,
        392.0,
        image=entry_input_private_key
    )
    input_private_key = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    input_private_key.place(
        x=328.0,
        y=377.0,
        width=243.0,
        height=28.0
    )

    # Sign Method/location
    image_sign_location_sign = PhotoImage(
        file=relative_to_assets("sign_location.png"))
    sign_location_sign = canvas.create_image(
        379.0,
        441.0,
        image=image_sign_location_sign
    )

    # radio button - sign method
    var_sign = IntVar()

    # Separated File
    image_separated_file_sign = PhotoImage(
        file=relative_to_assets("separated_file.png"))
    separated_file_sign = canvas.create_image(
        409.0,
        466.0,
        image=image_separated_file_sign
    )


    b_separated_file_sign = Radiobutton(
                          window,
                          variable = var_sign,
                          bg = "#CEDFCC",
                          value = 1)
    
    b_separated_file_sign.pack()
    b_separated_file_sign.place(
        x = 325.0,
        y = 455.0
    )

    # Embedded with Message
    image_embedded_with_message_sign = PhotoImage(
        file=relative_to_assets("embedded_with_message.png"))
    embedded_with_message_sign = canvas.create_image(
        450.0,
        492.0,
        image=image_embedded_with_message_sign
    )

    b_embedded_with_message_sign = Radiobutton(
                                   window,
                                   variable = var_sign,
                                   bg = "#CEDFCC",
                                   value = 2)
    
    b_embedded_with_message_sign.pack()
    b_embedded_with_message_sign.place(
        x = 325.0,
        y = 481.0
    )

    def sign():
        # periksa isi message
        msg_sign_teks = input_message_sign.get('1.0', 'end').rstrip()
        if msg_sign_teks == "":
            tk.messagebox.showwarning(title=gui_title, message="Masukkan message yang akan disign")
            return
        
        # periksi isi private key dan hilangkan "\n" di belakang
        private_key = input_private_key.get('1.0', 'end').rstrip()
        if private_key == '':
            tk.messagebox.showwarning(title=gui_title, message="Masukkan key terlebih dahulu")
            return
        
        # periksa lokasi sign
        sign_type = var_sign.get()
        if sign_type == 0:
            tk.messagebox.showwarning(title=gui_title, message="Pilih lokasi sign terlebih dahulu")
            return

        # case kalau dia sudah pilih file, lalu dia malah mengubah isi konten message
        # kalau dia mengedit pesan setelah memilih file, asumsinya dia akan menandatangani pesan bukan file tersebut
        if is_sign_file and msg_sign_teks != message_sign_file_path:
            is_sign_file = False

        # periksa jika dia memilih jenis file tapi embedded
        if is_sign_file and sign_type == 2:
            tk.messagebox.showwarning(title=gui_title, message="Tidak bisa embedded tanda tangan selain file teks")
            return
        
        # ekstrak nilai d dan n dari private key, gunakan ini
        # untuk melakukan enkripsi hasil hash message
        d = int(private_key.split(",")[0])
        n = int(private_key.split(",")[1])


       # jika yang disign adalah file
        if is_sign_file:
            pass # implementasikan, manfaatkan file path yang ada di msg_sign_teks
        # yang disign adalah pesan
        else:
            pass # implementasikan, manfaatkan konten pesan yang ada di msg_sign_teks

        # seperated file
        if sign_type == 1:
            pass # implementasikan
        # embedded with message
        else:
            pass # implementasikan

        # save pesan yang sudah disign dan seperated file jika ada
        # periksa fungsi save_key() untuk melihat contoh save file
        

    button_sign = PhotoImage(
        file=relative_to_assets("button_sign.png"))
    sign = Button(
        image=button_sign,
        borderwidth=0,
        highlightthickness=0,
        command=sign,
        relief="flat"
    )
    sign.place(
        x=375.0,
        y=523.0,
        width=150.0,
        height=30.0
    )

# ------ VERIFY MENU ------
    
    # frame - verify
    image_frame_verify = PhotoImage(
        file=relative_to_assets("frame.png"))
    frame_verify = canvas.create_image(
        748.0,
        328.0,
        image=image_frame_verify
    )

    # title - verify
    image_title_verify = PhotoImage(
        file=relative_to_assets("title_verify.png"))
    title_verify = canvas.create_image(
        747.0,
        95.0,
        image=image_title_verify
    )

    # title - message verify
    image_message_verify = PhotoImage(
        file=relative_to_assets("message.png"))
    message_verify = canvas.create_image(
        660.0,
        136.0,
        image=image_message_verify
    )

    def select_message_verify_file():
        global is_verify_file, message_verify_file_path
        message_verify_file_path = filedialog.askopenfilename(initialdir = Path(__file__),)
        ext = message_verify_file_path.split(".")[-1]
        content = message_verify_file_path
        # jika message yang diload adalah file text, maka tampilkan
        # pesan tersebut di layar
        if ext == "txt":
            is_verify_file = False
            with open(message_verify_file_path, "r") as file:
                content = file.read()
        # jika bukan, maka yang ditampilkan adalah path ke file tersebut
        # dan pathnya akan 
        else:
            is_verify_file = True
        input_message_verify.delete("1.0", tk.END)
        input_message_verify.insert("1.0", content)

    # choose file message verify
    button_choose_file_message_verify = PhotoImage(
        file=relative_to_assets("choose_file.png"))
    choose_file_message_verify = Button(
        image=button_choose_file_message_verify,
        borderwidth=0,
        highlightthickness=0,
        command=select_message_verify_file,
        relief="flat"
    )
    choose_file_message_verify.place(
        x=770.0,
        y=128.0,
        width=100.0,
        height=20.0
    )

    # input message verify
    entry_input_message_verify = PhotoImage(
        file=relative_to_assets("input_message.png"))
    entry_bg_input_message_verify = canvas.create_image(
        748.5,
        240.0,
        image=entry_input_message_verify
    )
    input_message_verify = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    input_message_verify.place(
        x=627.0,
        y=150.0,
        width=243.0,
        height=178.0
    )

    # title - public key
    image_public_key_verify = PhotoImage(
        file=relative_to_assets("public_key.png"))
    public_key_verify = canvas.create_image(
        664.0,
        363.0,
        image=image_public_key_verify
    )

    def choose_public_key():
        public_key_path = filedialog.askopenfilename(initialdir = Path(__file__),
                                                      defaultextension='.pubkey',
                                                      filetypes=[('Custom Files', '*.pubkey'), ('All Files', '*.*')],
                                                      title='Load Public Key')
        if public_key_path == "":
            return
        ext = public_key_path.split(".")[-1]
        if ext != "pubkey":
            tk.messagebox.showwarning(title=gui_title, message="Pilih file dengan ekstensi .prikey")
            return
        
        with open(public_key_path, "r") as file:
            content = file.read()
        
        input_public_key.delete("1.0", tk.END)
        input_public_key.insert("1.0", content)

    # choose file button - public key
    button_choose_file_public = PhotoImage(
        file=relative_to_assets("choose_file.png"))
    choose_file_public = Button(
        image=button_choose_file_public,
        borderwidth=0,
        highlightthickness=0,
        command=choose_public_key,
        relief="flat"
    )
    choose_file_public.place(
        x=769.0,
        y=355.0,
        width=100.0,
        height=20.0
    )

    # input public key
    entry_input_public_key = PhotoImage(
        file=relative_to_assets("input_key.png"))
    entry_bg_input_public_key = canvas.create_image(
        747.5,
        392.0,
        image=entry_input_public_key
    )
    input_public_key = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#26484F",
        font=("Poppins Regular", 15 * -1),
        highlightthickness=1
    )
    input_public_key.place(
        x=626.0,
        y=377.0,
        width=243.0,
        height=28.0
    )

    # Sign Method/location
    image_sign_location_verify = PhotoImage(
        file=relative_to_assets("sign_location.png"))
    sign_location_verify = canvas.create_image(
        677.0,
        441.0,
        image=image_sign_location_verify
    )

    # radio button - sign location
    var_verify = IntVar()

    # Separated File
    image_separated_file_verify = PhotoImage(
        file=relative_to_assets("separated_file.png"))
    separated_file_verify = canvas.create_image(
        707.0,
        466.0,
        image=image_separated_file_verify
    )


    b_separated_file_verify = Radiobutton(
                          window,
                          variable = var_verify,
                          bg = "#CEDFCC",
                          value = 1)
    
    b_separated_file_verify.pack()
    b_separated_file_verify.place(
        x = 623.0,
        y = 455.0
    )

    # choose separated file
    button_choose_file_separated = PhotoImage(
    file=relative_to_assets("choose_file.png"))
    choose_file_separated = Button(
        image=button_choose_file_separated,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_choose_file_separated clicked"),
        relief="flat"
    )
    choose_file_separated.place(
        x=770.0,
        y=455.0,
        width=100.0,
        height=20.0
    )

    # Embedded with Message
    image_embedded_with_message_verify = PhotoImage(
        file=relative_to_assets("embedded_with_message.png"))
    embedded_with_message_verify = canvas.create_image(
        748.0,
        492.0,
        image=image_embedded_with_message_verify
    )

    b_embedded_with_message_verify = Radiobutton(
                                   window,
                                   variable = var_verify,
                                   bg = "#CEDFCC",
                                   value = 2)
    
    b_embedded_with_message_verify.pack()
    b_embedded_with_message_verify.place(
        x = 623.0,
        y = 481.0
    )

    def verify():
        # periksa isi message dan hilangkan "\n" di belakang
        msg_verify_teks = input_message_verify.get('1.0', 'end').rstrip()
        if msg_verify_teks == "":
            tk.messagebox.showwarning(title=gui_title, message="Masukkan message yang akan diverify")
            return
        
        # periksi isi public key dan hilangkan "\n" di belakang
        public_key = input_public_key.get('1.0', 'end').rstrip()
        if public_key == '':
            tk.messagebox.showwarning(title=gui_title, message="Masukkan key terlebih dahulu")
            return
        
        # periksa lokasi sign
        verify_type = var_verify.get()
        if verify_type == 0:
            tk.messagebox.showwarning(title=gui_title, message="Pilih lokasi verify terlebih dahulu")
            return

        # case kalau dia sudah pilih file, lalu dia malah mengubah isi konten message
        # kalau dia mengedit pesan setelah memilih file, asumsinya dia akan memeriksa pesan bukan file tersebut
        if is_verify_file and msg_verify_teks != message_verify_file_path:
            is_verify_file = False

        # periksa jika dia memilih jenis file tapi embedded
        if is_verify_file and verify_type == 2:
            tk.messagebox.showwarning(title=gui_title, message="Tidak bisa embedded tanda tangan selain file teks")
            return
        
        # periksa jika dia memilih seperated file tapi dia belum memilih file path
        # implementasikan
        
        # ekstrak nilai e dan n dari public key, gunakan ini
        # untuk melakukan dekripsi tanda tangan
        e = int(public_key.split(",")[0])
        n = int(public_key.split(",")[1])


        # jika yang diverify adalah file
        if is_verify_file:
            pass # implementasikan, manfaatkan file path yang ada di msg_verify_teks
        # yang diverify adalah pesan
        else:
            pass # implementasikan, manfaatkan konten pesan yang ada di msg_verify_teks

        # seperated file
        if verify_type == 1:
            pass # implementasikan
        # embedded with message
        else:
            pass # implementasikan

        # implementasikan semua kasus yang terjadi

    button_button_verify = PhotoImage(
        file=relative_to_assets("button_verify.png"))
    button_verify = Button(
        image=button_button_verify,
        borderwidth=0,
        highlightthickness=0,
        command=verify,
        relief="flat"
    )
    button_verify.place(
        x=673.0,
        y=523.0,
        width=150.0,
        height=30.0
    )

    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    App()