import mysql.connector

mydb = mysql.connector.connect(host="mysql",user="root",password="root",database="database")
mycursor = mydb.cursor()

menu = 0
cod_banco = ''
banco = ''
cliente = ''
pixkey = ''
saldo = ''

print('                                                                          ')
print('                                                                          ')
print('                             Internet Banking                             ')
print('                                                                          ')
print('                          1 - Abrir Conta                                 ')
print('                          2 - Entrar no Banco                             ')
print('                          3 - Sair do Programa                            ')
print('                                                                          ')
 
while menu != 3:
    while menu < 1 or menu > 3:
        menu = int(input('      Digite uma opção: '))
        if menu == 1:
            cod_banco = input('Digite o código do banco: ')
            banco     = input('Digite o nome do banco: ')
            cliente   = input('Digite o seu nome: ')
            pixkey    = input('Digite sua chave pix: ')
            saldo     = input('Digite saldo inicial: ')
            print('')
            print('')
            try:
                sql = "INSERT INTO banco (cod, banco, cliente, pixkey, saldo) VALUES (%s, %s, %s, %s, %s)"
                val = (cod_banco, banco, cliente, pixkey, saldo)
                mycursor.execute(sql, val)
                mydb.commit()
                print('')
                print('')
                print('Conta criada com sucesso!!!')
                print('')
                print('')
                menu = 3
                try:
                    mycursor.execute("SELECT * FROM banco")
                    myresult = mycursor.fetchall()
                    print('')
                    print('')
                    for x in myresult:
                        print(x) 
                    break
                except:
                    print('')
                    print('')
                    print('Erro ao exibir sua conta!!!!!')
                    print('')
                    print('')
                    menu = 0

                menu = 0
            except:
                print('Erro ao tentar criar conta!!!!!')
                print('')
                print('')
                menu = 3
        elif menu == 2:
            print('')
            print('')
            print('Esta área ainda está em desenvolvimento!')
            print('')
            print('')
            menu = 0

        
        
print('---------------------------------| BYE BYE |-----------------------------------')