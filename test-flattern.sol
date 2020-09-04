pragma solidity ^0.4.16;

contract Ethraffle_v4b {
    struct Contestant {
        address addr;
        uint raffleId;
    }

    event RaffleResult(
        uint raffleId,
        uint winningNumber,
        address winningAddress,
        address seed1,
        address seed2,
        uint seed3,
        bytes32 randHash
    );

    event TicketPurchase(
        uint raffleId,
        address contestant,
        uint number
    );

    event TicketRefund(
        uint raffleId,
        address contestant,
        uint number
    );

    uint public constant prize = 2.5 ether;
    uint public constant fee = 0.03 ether;
    uint public constant totalTickets = 50;
    uint public constant pricePerTicket = (prize + fee) / totalTickets;
    address feeAddress;

    bool public paused = false;
    uint public raffleId = 1;
    // <yes> <report> BAD_RANDOMNESS
    uint public blockNumber = block.number;
    uint nextTicket = 0;
    mapping (uint => Contestant) contestants;
    uint[] gaps;

    function Ethraffle_v4b() public {
        feeAddress = msg.sender;
    }

    function () payable public {
        buyTickets();
    }
	function buyTickets() payable public  { 
		uint next=1; 
		while(next!=0){ 
			if( next==1) {
				if (paused)  next= 2; else next= 4;
			}
			else if(next== 2) { 
				msg.sender.transfer(msg.value);
				next= 3;
			}
			else if(next== 3) 
				return;
			else if(next== 4){   
				next= 5; 
			}
			else if(next== 5) { 
				uint moneySent = msg.value;
				next= 6;
			}
			else if(next== 6) {  
				next= 7; 
			}
			else if( next== 7){
				if (moneySent >= pricePerTicket && nextTicket < totalTickets)
					next= 8; 
				else 
					next= 17;
			}
			else if(next== 8) { 
					uint currTicket = 0;
					next= 9;
			}
			else if( next==9) {
				if (gaps.length > 0)
					next= 10; 
				else 
					next= 12;
			}
			else if(next== 10) { 
				currTicket = gaps[gaps.length - 1];
				next= 11; 
			}
			else if(next== 11) { 
				gaps.length --;
				next= 13; 
			}
			else if(next== 12) { 
				currTicket = nextTicket ++;
				next= 13;
			}
			else if(next== 13){   
				next= 14;
			}
			else if(next== 14) { 
				contestants[currTicket] = Contestant(msg.sender,raffleId);
				next= 15; 
			}
			else if(next== 15) { 
				TicketPurchase(raffleId,msg.sender,currTicket);
				next= 16;
			}
			else if(next== 16) { 
				moneySent -= pricePerTicket;
				next= 7;
			}
			else if(next== 17) {   
				next= 18;
			}
			else if( next==18) {
				if (nextTicket == totalTickets)  
					next= 19; 
				else 
					next= 20;
			}
			else if(next== 19) { 
				chooseWinner();
				next= 20;
			}
			else if(next== 20){   
				next= 21;
			}
			else if( next==21) {
				if (moneySent > 0)  
					next= 22; 
				else 
					next= 23; 
			}
			else if(next== 22) { 
				msg.sender.transfer(moneySent);
				next= 23; 
			}
			else if(next== 23){   
				next= 0;
			}
		} 
	}
	function chooseWinner() private  { 
		uint next=1; 
		while(next!=0){ 
			if(next== 1) { 
				address seed1 = contestants[uint256(block.coinbase) % totalTickets].addr;
				next= 2;
			}
			else if(next== 2) { 
				address seed2 = contestants[uint256(msg.sender) % totalTickets].addr;
				next= 3;
			}
			else if(next== 3) { 
				uint seed3 = block.difficulty; 
				next= 4;
			}
			else if(next== 4) { 
				bytes32 randHash = keccak256(seed1,seed2,seed3);
				next= 5;
			}
			else if(next== 5) { 
				uint winningNumber = uint256(randHash) % totalTickets;
				next= 6;
	 		}
			else if(next== 6) { 
				address winningAddress = contestants[winningNumber].addr;
				next= 7;
			}
			else if(next== 7) { 
				RaffleResult(raffleId,winningNumber,winningAddress,seed1,seed2,seed3,randHash);
				next= 8;
			}
			else if(next== 8) { 
				raffleId ++; 
				next= 9;
			}
			else if(next== 9) { 
				nextTicket = 0;
	 			next= 10;
	 		}
			else if(next== 10) { 
				blockNumber = block.number;
				next= 11;
			}
			else if(next== 11) { 
				winningAddress.transfer(prize);
				next= 12;
			}
			else if(next== 12) { 
				feeAddress.transfer(fee);
				next= 0;
			}
		} 
	}
	function getRefund()  public  { 
		uint next=1;
		while(next!=0){ 
			if(next== 1) { 
				uint refund = 0;
				next= 4;
			}
			else if(next== 2) {  
				next= 5;
			}
			else if(next== 3) {   
				next= 13;
			}
			else if(next== 4) { 
				uint i = 0;
				next= 2; 
			}
			else if( next== 5){ 
				if (i < totalTickets)  
					next= 3; 
				else 
					next= 6;
			}
			else if( next==6) {
				if (msg.sender == contestants[i].addr && raffleId == contestants[i].raffleId)
			  		next= 7;
			  	else 
			  		next= 11;
			  	}
			else if(next== 7) { 
				refund += pricePerTicket; 
				next= 8;
			}
			else if(next== 8) { 
				contestants[i] = Contestant(address(0),0);
 				next= 9;
 			}
			else if(next== 9) { 
				gaps.push(i); 
				next= 10;
			}
			else if(next== 10) { 
				TicketRefund(raffleId,msg.sender,i);
				next= 11;
			}
			else if(next== 11){   
				next= 12;
			}
			else if(next== 12) { 
				i ++; 
				next= 5;
			}
			else if( next==13) {
				if (refund > 0)
					next= 14;
				else 
					next= 15;
			}
			else if(next== 14) { 
				msg.sender.transfer(refund);
				next= 15;
			}
			else if(next== 15){   
				next= 0;
			}
		}
	}
	function endRaffle() public  { 
		uint next=1; 
		while(next!=0){ 
			if( next==1) {
				if (msg.sender == feeAddress)  
					next= 2; 
				else 
					next= 17;
			}
			else if(next== 2) { 
				paused = true;
				next= 5; 
			}
			else if(next== 3) {  
				next= 6;
			}
			else if(next== 4) {   
				next= 12;
			}
			else if(next== 5) { 
				uint i = 0;
				next= 3;
			}
			else if( next== 6){ 
				if (i < totalTickets)  
					next= 4;
					else next= 7;
				}
			else if( next==7) {
				if (raffleId == contestants[i].raffleId)  
					next= 8; 
				else 
					next= 10;
			}
			else if(next== 8) { 
				TicketRefund(raffleId,contestants[i].addr,i);
				next= 9; 
			}
			else if(next== 9) { 
				contestants[i].addr.transfer(pricePerTicket);
				next= 10;
			}
			else if(next== 10){   
				next= 11;
			}
			else if(next== 11) { 
				i ++;
				next= 6;
			}
			else if(next== 12) { 
				RaffleResult(raffleId,totalTickets,address(0),address(0),address(0),0,0);
				next= 13;
			}
			else if(next== 13) { 
				raffleId ++;
				next= 14;
			}
			else if(next== 14) { 
				nextTicket = 0;
				next= 15;
			}
			else if(next== 15) { 
				blockNumber = block.number;
				next= 16;
			}
			else if(next== 16) { 
				gaps.length = 0;
				next= 17;
			}
			else if(next== 17){   
				next= 0; 
			}
		}
	}
	function togglePause()  public  { 
		uint next=1; 
		while(next!=0){ 
			if( next==1) {
				if (msg.sender == feeAddress)  
					next= 2; 
				else 
					next= 3;
			}
			else if(next== 2) { 
				paused = ! paused; 
				next= 3;
			}
			else if(next== 3){   
				next= 0;
			}
		}
	}

	function kill()  public  { 
		uint next=1;
		while(next!=0){ 
			if( next==1) {
				if (msg.sender == feeAddress)  
					next= 2;
				else 
					next= 3;
			}
			else if(next== 2) { 
				selfdestruct(feeAddress); 
				next= 3;
			}
			else if(next== 3){   
				next= 0;
			}
		} 
	}
	
}




