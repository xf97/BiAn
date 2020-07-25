pragma solidity 0.6.2;

contract Foo{
	address public owner;
	uint256 public num = 0;
	constructor() public{
		owner = msg.sender;
	}

	function localNum() external returns(uint256){
		uint a = num;
		num += 1;
		return a;
	}

	function pureNum() external returns(uint256){
		uint b = num;
		num += 2;
		return b;
	}

	function sameNameNum() external returns(uint256){
		uint256 a;
		a = num++;
		return a;
	}

	function localArray() public pure returns(uint256){
		uint[] memory a = new uint[](7);
		a[6] = 5;
		return a[6];
	}
}
