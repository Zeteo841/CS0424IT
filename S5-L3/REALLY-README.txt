L'ordine che ha chiesto e':
1)Host-trovati.png (192.168.50.99 e' parrotOS)
2)OS-fingerprint-metasploitable2.png (ho provato anche windows7: OS-fingerprint-Windows7.png)\
3)Differenze-TCP-SYN-Scan(con-wireshark)-Metasploitable2.png (dimostra che manca l'ACK finale)
  Differenze-TCP-SYN-Scan(no-wireshark)-Metasploitable2.png (usa il comando diff di linux per notare le differenze)
4)Version-detection-metasploitable2-windows7.png

Io in realta' ho voluto provare a bypassare gli IPS/IDS di windows7 e ho aggiunto un file: Bypassati-IDS-IPS-Windows7.png
A dirla tutta, ho immesso anche il file Dubbio.png perche' possiamo notare che con il comando 'nmap -Pn -O ...' funzioni
l'OS-fingerprint, mentre con il comando 'nmap -Pn --script smb-os-discovery' ha problemi.
Ho pensato che sia dovuto appunto agli IPS/IDS e avendo aggiunto il file Bypassati-IDS-IPS-Windows7.png, posso dimostrare che 
ho bypassato gli IPS/IDS.
Magari mi sbaglio e mi sfugge qualcosa, anche perche' ho notato che alla prima scansione di stamattina windows7 anche se accesso
non lo vedevo, ne con 'nmap -sn', ne con ping, mentre dopo aver mandato il comando 'nmap -sS -p 20-25 --source-port 443 -T1 ip' 
(con successo),mi trovava windows7 (rimandando il comando nmap -sn, tra l'altro la foto Host-trovati.png, contiene proprio il suo risultato)
Morale della favola:
La mitica foto Bypassati-IDS-IPS-Windows7.png, bypassa o no, gli IPS/IDS?


 
