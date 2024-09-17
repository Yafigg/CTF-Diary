import zlib

# Baca file PNG
with open('flag7.png', 'rb') as f:
    data = f.read()

# Offset untuk IDAT chunk
idat_offset = 0x00070
idat_length = 32780

# Data IDAT (tidak termasuk 4 byte CRC di akhir)
idat_data = data[idat_offset:idat_offset + idat_length]

# Hitung CRC untuk IDAT data
computed_crc = zlib.crc32(idat_data) & 0xffffffff
print(f'Computed CRC: {computed_crc:08x}')

# Ganti CRC di file
# File offset untuk CRC adalah idat_offset + idat_length
crc_offset = idat_offset + idat_length

# Buat file baru dengan CRC yang benar
new_data = data[:crc_offset] + computed_crc.to_bytes(4, byteorder='big') + data[crc_offset + 4:]

with open('flag7_fixed.png', 'wb') as f:
    f.write(new_data)

print('CRC has been fixed and saved as flag7_fixed.png')
