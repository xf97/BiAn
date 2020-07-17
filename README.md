# BiAn(狴犴)
![logo](BiAnLogo.png)

**BiAn** is a source code level code obfuscation tool developed for Solidity smart contracts. We will obfuscate the Solidity smart contract from the following three aspects:
+ **Layout obfuscation**. In this aspect, I have completed the development of *variable name replacement*, and other functions will be gradually launched.
+ **Data flow obfuscation**. In this aspect, I have completed the development of *Dynamic Generate Static Data* and *Convert Integer Literals to Arithmetic Expressions*, and other functions will also be gradually introduced.
+ **Control flow obfuscation**. This aspect will be developed by the project collaborator *ZhangMeng*.

## Possible use 
We hope that **BiAn** can play a role in the following aspects:
+ Enhance bug smart contracts.
+ Protect the contract source code.

## Open source code used in **BiAn**
In the *Convert Integer Literals to Arithmetic Expressions* function, I use the code from project *Auto-Generate-Expression* (contributed by @threeworld et al). Since our requirements do not exactly match the project *Auto-Generate-Expression*'s function, I rewrite some code.

## License
This program is issued, reproduced or used under the permission of **MIT**. Please indicate the source when using.
