import hashlib
import time #Calculo para execucação do tempo

crypt = hashlib.md5()
crypt.update(b"aps")
print(crypt.hexdigest())

counter = 1 #Conta o número de tentativas da senha

md5_pass = input("Por favor insira a senha criptografada: ")
md5_file = input("Insira a localização do seu arquivo .txt com sua senha: ")

try:
    md5_file = open(md5_file,'r') #Arquivo será lido
except:
    print("\nArquivo não encontrado")
    quit()

for password in md5_file:
    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    start = time.time()
    print("Escaneando a senha %d -----> %s " % (counter,password.strip()))
    counter +=1
    end = time.time()
    t_time = end - start

    if hash_obj == md5_pass:
        print("\nSenha encontrada! A senha é : %s " % password)
        print("Total de tempo : ",t_time,"segundos")
        time.sleep(10)
        break

else:
    print("Senha não encontrada")
