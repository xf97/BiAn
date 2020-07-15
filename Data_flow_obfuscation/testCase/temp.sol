pragma solidity 0.6.2;

//based on slither

contract tooManyDigits{
    //In Solidity, scientific counting method is provided to represent big numbers and small numbers, and ether unit is also provided to represent the amount of ether. Trying to write multiple digits in succession with these substitutions, these effectively reduce the chance of making mistakes and make the code easier to understand.
    uint256 public oncePrice = ; //10^18, integer literal
    uint256 public twicePrice = ; //10^12, integer literal
    address public checkAddress = ; //address literal
    address private _address = ;
    string public symbol;
    bytes _16jinzhi;
    address[] public users;
    address payable owner;
    
    constructor() public{
	symbol = 