This room introduces one to nmap, gobuster, enum4linux, hydra, etc.

---

The nmap scan yields the following results:

`nmap -sC -sV 10.10.140.75`

22, 80, 139, 445, 8009, 8080

---

The gobuster scan yields the following results:

`gobuster dir -u http://10.10.140.75 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt `

Directory found = /development


---
