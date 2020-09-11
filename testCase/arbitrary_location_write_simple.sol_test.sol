pragma solidity ^0.4.25;

contract Wallet {
	uint[] private bonusCodes;
	address private owner;
	constructor() public {
		bonusCodes = new uint[](0);	
		owner = msg.sender;
	}
	function () public payable {
	}
	function PushBonusCode(uint c) public {
 		uint next=1; 
		while(next!=0){ 
			if(next== 1) { 
				bonusCodes.push(c); 
				next= 0; 
			}
		}
	}

	function PopBonusCode() public {
  		uint next=1; 
		while(next!=0){ 
		   if(next== 1) { 
			require(0 <= bonusCodes.length); 
			next= 2; 
			}
		else if(next== 2){ 
			bonusCodes.length --; 
			next= 0; 
			}
		} 
	}

	function UpdateBonusCodeAt(uint idx, uint c) public {
		uint next=1; 
		while(next!=0){ 
			if(next== 1) { 
				require(idx < bonusCodes.length); 
				next= 2; 
				}
			else if(next== 2){ 
				bonusCodes[idx] = c; 
				next= 0; 
				}
			} 
	}

	function Destroy() public {
	uint next=1; 
	while(next!=0){ 
		if(next== 1) { 
			require(msg.sender == owner); 
			next= 2; 
			}
		else if(next== 2) {
			selfdestruct(msg.sender); 
			next= 0; 
			}
		} 
	}
}
