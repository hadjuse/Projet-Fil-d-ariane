import qrcode
import qrcode

# Texte à encoder dans le QR code
texte = "https://hadjuse.github.io/Projet-Fil-d-ariane/"

# Création de l'objet QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Ajout du texte dans l'objet QR code
qr.add_data(texte)
qr.make(fit=True)

# Création de l'image QR code
image = qr.make_image(fill_color="black", back_color="white")

# Sauvegarde de l'image QR code
image.save("qr_code.png")
