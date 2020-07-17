pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256 public oncePrice = 681714399417178675 / 585320629933435574 / 568421490586080230 + 790587791127690211  + 755399323187675535431554801074176/3607236308023877; //10^18, integer literal
    uint256 public twicePrice = ( 19132350599 - 5239003734 ) * 1537848791 - 13038958654  - 21365866646244931561; //10^12, integer literal
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
	tokenDecimal = ( 8 * 8 ) / 9 + 12  - 10/9;
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
