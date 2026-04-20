# altere aqui o tamanho da instância
n = 10000 

adv_nome = f"instancias/adv_{n}.txt"
    
with open(adv_nome, "w") as f: 
    f.write(f"{n}\n") 
    for i in range(1, n):
        f.write(f"0 {i}\n")
            
print(f"Instância '{adv_nome}' gerada com sucesso!")