import json

file = open("data.json")

data = json.load(file)

n = len(data)

def ABC_1():
    data_sorted = []
    for i in range(n):
        max = {
            "ca": 0,
            "id": "0"
        }
        for client in data:
            if client["ca"] > max["ca"]:
                max = client
        data_sorted.append(max)
        data.remove(max)

    for i in range(n):
        if i < n * 0.2:
            data_sorted[i]["abc"] = "A"
        elif i < n * 0.5:
            data_sorted[i]["abc"] = "B"
        else:
            data_sorted[i]["abc"] = "C"

    ca_A = 0
    ca_B = 0
    ca_C = 0
    for client in data_sorted:
        if client["abc"] == "A":
            ca_A += client["ca"]
        if client["abc"] == "B":
            ca_B += client["ca"]
        if client["abc"] == "C":
            ca_C += client["ca"]

    total = ca_A + ca_B + ca_C
    A = 100 * ca_A / total
    B = 100 * ca_B / total
    C = 100 * ca_C / total
    print("A :", A, "%")
    print("B :", B, "%")
    print("C :", C, "%")

def ABC_2():
    data_sorted = []
    for i in range(n):
        max = {
            "ca": 0,
            "id": "0"
        }
        for client in data:
            if client["ca"] > max["ca"]:
                max = client
        data_sorted.append(max)
        data.remove(max)

    ca_total = 0
    ecc = 0
    for i in range(n):
        ca_total += data_sorted[i]["ca"]

    for i in range(n):
        ecc += data_sorted[i]["ca"] / ca_total
        if ecc < 0.8:
            data_sorted[i]["abc"] = "A"
        elif ecc < 0.95:
            data_sorted[i]["abc"] = "B"
        else:
            data_sorted[i]["abc"] = "C"

    n_A = 0
    n_B = 0
    n_C = 0
    for client in data_sorted:
        if client["abc"] == "A":
            n_A += 1
        if client["abc"] == "B":
            n_B += 1
        if client["abc"] == "C":
            n_C += 1

    A = 100 * n_A / n
    B = 100 * n_B / n
    C = 100 * n_C / n
    print("A :", A, "%")
    print("B :", B, "%")
    print("C :", C, "%")

def RFM(data):
    data_sorted_r = []
    for i in range(n):
        max = {
            "recence": 0,
            "id": "0"
        }
        for client in data:
            if client["recence"] > max["recence"]:
                max = client
        data_sorted_r.append(max)
        data.remove(max)
    
    for i in range(n):
        if i < n * 0.2:
            data_sorted_r[i]["score_r"] = 5
        elif i < n * 0.4:
            data_sorted_r[i]["score_r"] = 4
        elif i < n * 0.6:
            data_sorted_r[i]["score_r"] = 3
        elif i < n * 0.8:
            data_sorted_r[i]["score_r"] = 2
        else:
            data_sorted_r[i]["score_r"] = 1
    
    data_sorted_f = []
    for i in range(n):
        max = {
            "frequence": 0,
            "id": "0"
        }
        for client in data_sorted_r:
            if client["frequence"] > max["frequence"]:
                max = client
        data_sorted_f.append(max)
        data_sorted_r.remove(max)
    
    for i in range(n):
        if i < n * 0.2:
            data_sorted_f[i]["score_f"] = 5
        elif i < n * 0.4:
            data_sorted_f[i]["score_f"] = 4
        elif i < n * 0.6:
            data_sorted_f[i]["score_f"] = 3
        elif i < n * 0.8:
            data_sorted_f[i]["score_f"] = 2
        else:
            data_sorted_f[i]["score_f"] = 1

    data_sorted_m = []
    for i in range(n):
        max = {
            "ca": 0,
            "id": "0"
        }
        for client in data_sorted_f:
            if client["ca"] > max["ca"]:
                max = client
        data_sorted_m.append(max)
        data_sorted_f.remove(max)

    for i in range(n):
        if i < n * 0.2:
            data_sorted_m[i]["score_m"] = 5
        elif i < n * 0.4:
            data_sorted_m[i]["score_m"] = 4
        elif i < n * 0.6:
            data_sorted_m[i]["score_m"] = 3
        elif i < n * 0.8:
            data_sorted_m[i]["score_m"] = 2
        else:
            data_sorted_m[i]["score_m"] = 1

    for i in range(n):
        r = data[i]["score_r"]
        f = data[i]["score_f"]
        m = data[i]["score_m"]
        if ((r==4 or r==5) and (f==4 or f==5) and (m==4 or m==5)):
            data[i]["rfm"] = "Champion"
        elif ((r==4 or r==5) and (f==1) and (m==1)):
            data[i]["rfm"] = "Nouveau client"
        elif ((r!=1) and (f>=3) and (m>=3)):
            data[i]["rfm"] = "Client loyal"
        elif ((r>=3) and (f<=3) and (m<=3)):
            data[i]["rfm"] = "Client potentiellement loyal"
        elif ((r==3 or r==4) and (f==1) and (m==1)):
            data[i]["rfm"] = "Client prometteur"
        elif ((r==3 or r==4) and (f==3 or f ==4) and (m==3 or m==4)):
            data[i]["rfm"] = "Client a preter attention"
        elif ((r==2 or r==3) and (f==1 or f==2) and (m==1 or m==2)):
            data[i]["rfm"] = "Client sur le point de dormir"
        elif ((r<=2) and (f>=2 and f <=5) and (m>=2 and m<=5)):
            data[i]["rfm"] = "Client a risque"
        elif ((r<=2) and (f<=2) and (m<=2)):
            data[i]["rfm"] = "Client perdu"
        elif ((r==1) and (f>=4) and (m>=4)):
            data[i]["rfm"] = "Client a ne pas perdre"
        elif ((r==2 or r==3) and (f==2 or f==3) and (m==2 or m==3)):
            data[i]["rfm"] = "Client en hibernation"
        else:
            data[i]["rfm"] = "Autre"

    for client in data:
        print(client)

RFM(data)