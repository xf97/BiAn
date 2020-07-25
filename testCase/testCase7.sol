pragma solidity 0.6.2;

contract MergeArray{
	uint256[3] public array1 = [1, 3, 4];
	uint256[4] public array2 = [4, 5, 6, 7];
	uint256[2] public array5;
	uint8[7] private array4 = [7, 6, 5, 4, 3, 2, 1];
	uint8[] public array3;

	constructor() public{
		array3.push(2);
	}

	function used() external view returns(uint256){
		uint256 result = array1[1] + array3[0];
		return result;
	}

	function localArray() external pure returns(uint256){
		uint8[2] memory result = [1, 2];
		return result[1];
	}
}
