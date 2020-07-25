pragma solidity 0.6.2;

contract Foo {
	bool public b1 = true;
	bool private b2 = false || false;
	bool internal b3;
	bool internal b4;
	uint256 public number = 0;

	constructor() public{
		(b3, b4) = returnTrue();
		//b4 = returnTrue();
	}

	function returnTrue() internal pure returns(bool, bool){
		return (true && true, true);
	}

	function ifState() view external returns(uint256){
		return number;
	}

	function whileState() external pure returns(bool){
		bool b5 = true;
		bool b6 = false;
		return b5 || b6;
	}
}
