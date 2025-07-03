# Fungsi tanpa input parameter dan return value
def say_hello():
    print("hello")

for i in range(10):
    say_hello()


# Fungsi dengan input parameter tanpa return value
def say_hello_to(nama):
    print("hello", nama)

nama_arab = ["alif", "ba", "ta", "tsa", "jim", "ha", "kho"]
for nama in nama_arab:
    say_hello_to(nama)

# Fungsi dengan beberapa input parameter tanpa return value
def katakan_selamat_kepada(nama, event):
    print(f"selamat {event}, {nama}")

katakan_selamat_kepada("upin", "ulang tahun")
katakan_selamat_kepada("ipin", "malam")