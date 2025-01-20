#bulletCTF Q6:Embedded_開発スクリプト
from PIL import Image
def text_to_bits(text):
  bits = ''.join(format(ord(char), '08b') for char in text)
  return bits

def load():
  e = open('Flag.txt','r',encoding='UTF-8')
  flag = e.read()
  e.close()
  ftxt =''.join(format(ord(char), '08b') for char in flag)
  return ftxt

def embed_text_to_image(image_path, output_path, text):
  image = Image.open(image_path)
  encoded_image = image.copy()
  width, height = image.size

  bits = text_to_bits(text) + '00000000'
  bit_index = 0

  for y in range(height):
      for x in range(width):
          if bit_index < len(bits):
              r, g, b = image.getpixel((x, y))

              if bit_index < len(bits):
                  r = (r & ~1) | int(bits[bit_index])
                  bit_index += 1

              if bit_index < len(bits):
                  g = (g & ~1) | int(bits[bit_index])
                  bit_index += 1

              if bit_index < len(bits):
                  b = (b & ~1) | int(bits[bit_index])
                  bit_index += 1

              encoded_image.putpixel((x, y), (r, g, b))

  encoded_image.save(output_path)

ftxt = load()
embed_text_to_image('bullet.png','bullet.png',ftxt)
