import zlib
import struct

def fix_crc_error(input_file, output_file, computed_crc, expected_crc):
    # Baca isi file PNG
    with open(input_file, 'rb') as f:
        png_data = f.read()

    # Temukan posisi chunk IDAT
    idat_offset = png_data.find(b'IDAT')
    if idat_offset == -1:
        print('Chunk IDAT not found')
        return

    # Hitung CRC32 dari data IDAT yang ada
    data_start = idat_offset + 8  # Mulai dari 8 byte setelah string 'IDAT'
    data_end = data_start + struct.unpack('>I', png_data[idat_offset + 4:idat_offset + 8])[0]
    data = png_data[data_start:data_end]
    calculated_crc = zlib.crc32(data) & 0xFFFFFFFF

    # Ubah nilai CRC yang salah
    if calculated_crc != expected_crc:
        print(f'Computed CRC32: {calculated_crc:08x}, Expected CRC32: {expected_crc:08x}')
        print('CRC mismatch, unable to fix')
        return

    # Ganti nilai CRC yang salah dengan yang benar
    png_data = png_data[:idat_offset + 8] + struct.pack('>I', computed_crc) + png_data[idat_offset + 12:]

    # Tulis file PNG yang sudah diperbaiki
    with open(output_file, 'wb') as f:
        f.write(png_data)

    print(f'File {output_file} berhasil diperbaiki')

# Ganti nilai berikut sesuai dengan nilai CRC error yang Anda temukan
computed_crc = 0xdb7dcf2b
expected_crc = 0x92b0a93c

# Panggil fungsi untuk memperbaiki CRC error
fix_crc_error('flag9.png', 'flag9_recovered.png', computed_crc, expected_crc)
