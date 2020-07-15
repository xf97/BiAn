pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256[] _int_const = [1000000000000000000, 18000000000000];
    address payable[] _addr_const = [0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed, 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed];
    string[]  _str_const = ["xf's testCase"];
    uint256 public oncePrice = getIntFunc(0); //10^18, integer literal
    uint256 public twicePrice = getIntFunc(1); //10^12, integer literal
    address public checkAddress = getAddrFunc(0); //address literal
    address private _address = getAddrFunc(1);
    string public symbol;
    bytes _16jinzhi;
    address[] public users;
    address payable owner;
    
    constructor() public{
	symbol = getStrFunc(0);
	_16jinzhi = hex"001122ff";
    owner = msg.sender;
    }
    
    function withdraw() external{
        require(msg.sender == owner && tx.origin == checkAddress);
        owner.transfer(address(this).balance);
    }
    
    function pay() external payable{
        require(msg.value == oncePrice);    //1 ether 1 time
        users.push(msg.sender);
    }

    function getIntFunc(uint256 index) internal view returns(uint256){
	return _int_const[index];
    }

    function getAddrFunc(uint256 index) internal view returns(address payable){
	return _addr_const[index];
    }

    function getStrFunc(uint256 index) internal view returns(string storage){
	return _str_const[index];
    }
}
