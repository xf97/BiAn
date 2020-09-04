pragma solidity 0.6.2;


/*
Solidity doesn't support floating point Numbers very well, and all integers 
that are divided are rounded down. The use of integer division to calcul-
ate the amount of ethers may cause economic losses.
*/

contract getWageNumber {
                               
                             
                        
    
    constructor() public{
        s2c.DailyWage =  uint256(getIntFunc(6 * ( 3 * 4 + 5 )  - 101));
        s2c.coefficient =  uint256(getIntFunc(2 + 8 - 3 + 0  - 7));
        s2c.boss = msg.sender;
    }
    
    modifier onlyOwner{
        require(msg.sender == s2c.boss);
        _;
    }
    
    function setDailyWage(uint256 _wage) external onlyOwner{
        s2c.DailyWage = _wage;
    }
    
    function setCoefficient(uint256 _co) external onlyOwner{
        s2c.coefficient = _co;
    }
    
    function calculateWage(uint256 dayNumber) external view onlyOwner returns (uint256) {
    //Until now, Solidity doesn't support decimals or fixed-point numbers, and all integer division results are rounded down, which can lead to a loss of accuracy. Avoid using integer division to calculate the amount of ethers. If you have to, try multiplying before dividing to offset the loss of accuracy.
        uint256 baseWage = s2c.DailyWage / s2c.coefficient;
        return baseWage * dayNumber;
    }
	function getIntFunc(uint256 index) internal view returns(uint256){
 		return _integer_constant[index];
 	}
	uint256[] public _integer_constant = [1 - 0 + 2 * 1  + 0, 50 + ( 3 * 89 ) + 70  - 287];
	struct scalar2Vector {
		address boss;
		uint256 DailyWage;
		uint256 coefficient;
	}
	scalar2Vector s2c = scalar2Vector(address(0), 0, 0);
}