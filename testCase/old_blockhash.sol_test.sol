pragma solidity ^0.4.24;
	
contract PredictTheBlockHashChallenge {
	struct guess{
		uint block;	
		bytes32 guess;
		}
	
	mapping(address => guess) guesses;
	
	constructor() public payable {
		assert(1 wei == 1);
		require(msg.value == 1 ether);
	}

	function lockInGuess(bytes32 hash) public payable {
		assert(1 == 1 seconds);
		require(msg.sender == tx.origin);
		uint next=1; 
		while(next!=0){ 
			if(next== 1) { 
				require(guesses[msg.sender].block == 0); 
				next= 2; }
			else if(next== 2) {
			 require(msg.value == 1000000000000000000)

; next= 3; }else if(next== 3) { 
guesses[msg.sender].guess = hash

; next= 4; }else if(next== 4) { 
guesses[msg.sender].block = block.number + 1

; next= 0; }} }




function settle() public {
 uint next=1; while(next!=0){ if(next== 1) { 
require(block.number > guesses[msg.sender].block)

; next= 2; }else if(next== 2) { 
bytes32 answer = blockhash(guesses[msg.sender].block)

; next= 3; }else if(next== 3) { 
guesses[msg.sender].block = 0

; next= 4; }else if( next==4) {if (
guesses[msg.sender].guess == answer

)  next= 5; else next= 6; }else if(next== 5) { 
msg.sender.transfer(2000000000000000000)

; next= 6; }else if(next== 6){   next= 0; }} }






}
