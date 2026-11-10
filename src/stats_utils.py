import numpy as np

def analyser_ventes(transactions):
  
    arr = np.array(transactions, dtype=float)
    transactions_valides = arr[arr > 0]

    nb_transactions = int(transactions_valides.size)
    somme_totale = float(np.sum(transactions_valides))
    moyenne = float(np.mean(transactions_valides))
    mediane = float(np.median(transactions_valides))
    ecart_type = float(np.std(transactions_valides, ddof=1)) 
    valeur_max = float(np.max(transactions_valides))
    valeur_min = float(np.min(transactions_valides))
    seuil_anomalie = 2 * moyenne
    anomalies = transactions_valides[transactions_valides > seuil_anomalie].tolist()

    return {
        "nb_transactions": nb_transactions,
        "somme_totale": round(somme_totale, 2),
        "moyenne": round(moyenne, 2),
        "mediane": round(mediane, 2),
        "ecart_type": round(ecart_type, 2),
        "min": round(valeur_min, 2),
        "max": round(valeur_max, 2),
        "anomalies": anomalies}



donnees_test = [150.0, -20.0, 0.0, 220.5, 180.0, 95.0, 1200.0,1500.0, 310.0, -5.0, 200.0]

resultats = analyser_ventes(donnees_test)
for cle, valeur in resultats.items():
    print(f"{cle} : {valeur}")