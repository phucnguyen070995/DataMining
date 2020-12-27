import subprocess

def LuuFile(path, data):
    file = open(path, 'a',encoding="utf-8")
    file.writelines(data)
    file.writelines('\n')
    file.close()


start = 2000001
end = 2074719

lengh = len("""<td style="border: 1px solid">""")
for i in range(start,start+1):
	res = '0' + str(i) +','
	result = subprocess.check_output('curl -F "SoBaoDanh=0' + str(i) +'" diemthi.hcm.edu.vn/Home/Show').decode("utf-8")
	print(result)
	# for _ in range(3):
	# 	idx = result.find("""<td style="border: 1px solid">""")
	# 	if idx == -1:
	# 		break
	# 	result = result[idx + lengh:]
	# 	idx = result.find("</td>")
	# 	res += result[:idx].strip()
	# 	result = result[idx:]
	# else:
	# 	LuuFile('out.txt',res)

