shannon_fano
============

The script implements Shennon-Fano coding algorithm.<br>
For more details, have a look at the wiki page: [Shannon-Fano](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding))<br>
Moreover, the script calculates some additional info:

<ul>
    <li>H_max -> Maximum Entropy message source</li>
    <li>h -> The entropy of the message source</li>
    <li>l_cp -> The average number of binary digits in the code letter</li>
    <li>K_c.c. -> The static compression coefficient</li>
    <li>K_o.э. -> The relative efficiency coefficient</li>
</ul>

Script can accept:
<ul>
    <li>an entire message which need to be encrypted</li>
    <li>a dictionary which indicates involved letters and their frequencies</li>
</ul>

__Pay attention__: script builds the code using only binary coding