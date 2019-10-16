import fungsi

def  main():
	f = 14
	s = 5

	w = fungsi.usahadanenergi(f, s)

	print("Usaha dan Energi")
	print("Gaya\t: ", f)
	print("Jarak\t ", s)
	print("Usaha\t ", w)
	
	t = 8
	n = 4

	T = fungsi.periodegetaran(t, n)
	print("periode Getaran")
	print("Waktu\t: ", t)
	print("Banyak Getaran\t: ", n)
	print("periode Getaran\t=, T")

	t = 3
	n = 21

	f = fungsi.frekuensigetaran(t, n)
	print("frekuensi Getaran")
	print("Banyak Getaran\t:", n)
	print("Waktu\t: ",t)
	print("frekuensi Getaran\t= ", f)

	t = 3
	n = 21

	f = fungsi.frekuensigetaran(t, n)
	print("frekuensi Getaran")
	print("Banyak Getaran\t: ", n)
	print("Waktu\t ", t)
	print("frekuensi Getaran\t=", f)

	t = 8
	n = 4

	T = fungsi.periodegetaran(t, n)
	print("periode Getaran")
	print("Waktu\t: ", t)
	print("Banyak Getaran\t: ", n)
	print("periode Getaran\t=", T)

if __name__ == "__main__":
  main()
