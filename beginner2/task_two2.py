info_karyawan = {'nama' : 'Aksara','nik' : '1211011','pekerjaan' : 'Data Analyst'}
info_karyawan.clear()

#!copy
info_karyawan1 = {'nama' : 'Aksara','nik' : '1211011','pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Cahyo'
print(info_karyawan2)