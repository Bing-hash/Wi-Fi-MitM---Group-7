# Stealthy MitM Attacks in Wi-Fi without a Rogue AP
## RIT Wireless Security - Group-7
### Research and project development in reference to: https://doi.org/10.1109/SP46215.2023.10179441
## Attack
This attack takes advantage of a vulnerability in cross-layer interactions between WPA2/3 and ICMP protocols, which completely evades link layer security mechanisms enforced by the AP, Supplicants, and WPA protocols.
### There are two requirements for this attack to be successful:
One: When the attacker spoofs the legitimate AP to craft an ICMP redirect message, the legitimate AP cannot recognize and filter out those forged ICMP redirect messages. (Referenced paper lists CVE and vulnerable APs)
Two: The forged ICMP redirect messages should pass legitimacy checks on the victim supplicant.
## Countermeasures
### icmp.c is provided for linux kernel 4.18
This icmp.c file features a change to the icmp_redirect function which forces an additional authenticity check when the supplicant receives icmp redirect messages. This change to the icmp_redirect function is effective in mitigating this attack on newer kernel versions as well.
