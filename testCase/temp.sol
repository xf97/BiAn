pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256 public oncePrice = ( 962839029665830984 * 333695685390986766 ) - 819056978231709121 - 648314900720228191  - 321295229925532107220353478184820432; //10^18, integer literal
    uint256 public twicePrice = 12969684161 * ( 17760545774 - 13892550367 + 15533444965 )  - 251630553873314347892; //10^12, integer literal
    uint8 public tokenDecimal;
    address public checkAddress = 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed; //address literal
    address private _address = 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed;
    string public symbol;
    bytes _16jinzhi;
    address[] public users = [0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed, 0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed];
    address payable owner;
    struct Voter {
        uint weight;
        bool voted;
        address delegate;
        uint vote;
    }
    enum State { Created, Locked, Inactive }
    
    constructor() public{
	symbol = "xf's testCase";
	_16jinzhi = hex"001122ff";
	owner = msg.sender;
	tokenDecimal = 6 + 8 + 17 * 11  - 183;
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
