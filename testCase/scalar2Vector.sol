pragma solidity 0.6.2;

contract testCase{
	bool public var1 = true;
	uint256 private var2 = 0;
	uint8 public var3;
	address public owner;
	string public symbol = setSymbol();
	bytes private name;

	constructor(bytes memory _name) public{
		var3 = 1;
		owner = msg.sender;
		name = _name;
	}

	function useVar1() external{
		var1 = false;
	}

	function useVar2() external returns(uint256){
		var2++;
	}

	function useVar3() external{
		var3 = uint8(var2) + 1;
	}

	function useOwner() external{
		owner = msg.sender;
	}

	function useSymbol() external view returns(string memory){
		return symbol;
	}

	function useName() external view returns(uint256){
		return name.length;
	}

	function setSymbol() internal pure returns(string memory){
		return "xf lalala";
	}
}
