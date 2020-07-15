pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256[] public _integer_const = [1000000000000000000, 18000000000000];
    string[] public _string_const = ["xf's testCase"];
    address payable[] public _address_const = [0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed, 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed];
    uint256 public oncePrice = 1000000000000000000; //10^18, integer literal
    uint256 public twicePrice = 18000000000000; //10^12, integer literal
    address public checkAddress = 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed; //address literal
    address private _address = 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed;
    string public symbol;
    bytes _16jinzhi;
    address[] public users;
    address payable owner;
    
    constructor() public{
	symbol = "xf's testCase";
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
}
