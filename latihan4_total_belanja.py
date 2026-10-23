harga_barang = 150000
jumlah_barang = 2

total_harga = harga_barang * jumlah_barang
ppn = total_harga * 0.11
total_bayar = total_harga + ppn

print(f"Total Harga Barang : Rp{total_harga}")
print(f"PPN (11%)          : Rp{int(ppn)}")
print(f"Total Bayar        : Rp{int(total_bayar)}")