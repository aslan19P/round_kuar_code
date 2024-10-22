from PIL import Image
import qrcode_styled
from qrcode_styled.pil.image import PilStyledImage

# Путь к изображению логотипа
logo_path = 'logo.png'

# Загружаем изображение логотипа
try:
    logo_image = Image.open(logo_path)
    
    # Увеличиваем размер логотипа для лучшего качества
    logo_size = 150  # Увеличиваем размер для улучшения качества
    logo_image = logo_image.resize((logo_size, logo_size), Image.LANCZOS)

    # Создаем белый фон с отступами
    padding = 10  # Установите желаемый размер отступа
    new_size = (logo_size + padding * 2, logo_size + padding * 2)  # Размер нового изображения с отступами
    white_background = Image.new('RGBA', new_size, (255, 255, 255, 255))  # Белый фон
    # Накладываем логотип на белый фон с отступами
    white_background.paste(logo_image, (padding, padding), logo_image)

    logo_image = white_background  # Обновляем logo_image на новое изображение с белым фоном и отступами

except FileNotFoundError:
    print(f"Файл {logo_path} не найден. Проверьте путь к изображению.")
    exit()

# Создаем QR-код
qr = qrcode_styled.QRCodeStyled(
    version=None,
    error_correction=qrcode_styled.ERROR_CORRECT_H,  # Увеличиваем уровень коррекции ошибок
    border=1,
    box_size=40,
    image_factory=PilStyledImage,
)

# Генерируем QR-код
img = qr.get_image(
    data='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    image=logo_image,
    optimize=20,
)

# Сохраняем в файл PNG
with open('tcats_qr.png', 'wb') as _fh_png:
    img.save(_fh_png, 'PNG')



# # Сохраняем в файл WEBP
# with open('tcats_qr.webp', 'wb') as _fh_webp:
#     img.save(_fh_webp, 'WEBP')