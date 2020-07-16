pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256 public oncePrice =  uint256(getIntFunc(1)); //10^18, integer literal
    uint256 public twicePrice =  uint256(getIntFunc(2)); //10^12, integer literal
    uint8 public tokenDecimal;
    address public checkAddress =  getAddrFunc(0); //address literal
    address private _address =  getAddrFunc(0);
    string public symbol;
    bytes _16jinzhi;
    address[] public users = [ getAddrFunc(0),  getAddrFunc(0)];
    address payable owner;
    struct Voter {
        uint weight;
        bool voted;
        address delegate;
        uint vote;
    }
    enum State { Created, Locked, Inactive }
    
    constructor() public{
	symbol =  getStrFunc(0);
	_16jinzhi = hex"001122ff";
	owner = msg.sender;
	tokenDecimal =  uint8(getIntFunc(0));
    }
    
    function withdraw() external{
        require(msg.sender == owner && tx.origin == checkAddress);
        owner.transfer(address(this).balance);
    }
    
    function pay() external payable{
        require(msg.value == oncePrice);    //1 ether 1 time
        users.push(msg.sender);
    }
	function getAddrFunc(uint256 index) internal view returns(address payable){
 		return _address_constant[index];
 	}
	function getStrFunc(uint256 index) internal view returns(string storage){
 		return _string_constant[index];
 	}
	function getIntFunc(uint256 index) internal view returns(uint256){
 		return _integer_constant[index];
 	}
	address payable[] public _address_constant = [0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed];
	string[] public _string_constant = ["xf's testCase"];
	uint256[] public _integer_constant = [18, 1000000000000000000, 18000000000000];
}
