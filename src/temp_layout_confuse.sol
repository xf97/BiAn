pragma solidity 0.6.2;


/*
Solidity doesn't support floating point Numbers very well, and all integers 
that are divided are rounded down. The use of integer division to calcul-
ate the amount of ethers may cause economic losses.
*/

contract Ox3be60037c4e640cc50f88c83efb262b40bf87498 {
    uint256 public coefficient;
    uint256 public Ox57f6d2af869866f9741b9f33f4bbe61d15506371;
    address public boss;
    
    constructor() public{
        Ox57f6d2af869866f9741b9f33f4bbe61d15506371 = 18 * 11 - ( 89 + 24 )  + 15;
        coefficient =  uint256(Ox1014ff866cf2d8e1f747ce5e540aa977a5c6459c(6 * 8 * 2 - 1  - 94));
        boss = msg.sender;
    }
    
    modifier Oxb41f41088bcad4cb047578ceb8050326e381b1a9{
        require(msg.sender == boss);
        _;
    }
    
    function setDailyWage(uint256 Ox9657f98a3e52c150ce1f6bad4929b37a5865229a) external Oxb41f41088bcad4cb047578ceb8050326e381b1a9{
        Ox57f6d2af869866f9741b9f33f4bbe61d15506371 = Ox9657f98a3e52c150ce1f6bad4929b37a5865229a;
    }
    
    function setCoefficient(uint256 _co) external Oxb41f41088bcad4cb047578ceb8050326e381b1a9{
        coefficient = _co;
    }
    
    function Ox5a6200d067ff121ab418034c9f27e19efacdedff(uint256 Ox805a9edc0f85f11c267743d823860789579a722d) external view Oxb41f41088bcad4cb047578ceb8050326e381b1a9 returns (uint256) {
    //Until now, Solidity doesn't support decimals or fixed-point numbers, and all integer division results are rounded down, which can lead to a loss of accuracy. Avoid using integer division to calculate the amount of ethers. If you have to, try multiplying before dividing to offset the loss of accuracy.
        uint256 Ox29b4089771ec2b3eecd635457b19e2bfc5a118c9 = Ox57f6d2af869866f9741b9f33f4bbe61d15506371 / coefficient;
        return Ox29b4089771ec2b3eecd635457b19e2bfc5a118c9 * Ox805a9edc0f85f11c267743d823860789579a722d;
    }
	function Ox1014ff866cf2d8e1f747ce5e540aa977a5c6459c(uint256 Oxdd3d838b261da8cf328b3dcc16a807dc480d5a90) internal view returns(uint256){
 		return Ox2597e3f7dacf7188b06929988f77d57be2adba6c[Oxdd3d838b261da8cf328b3dcc16a807dc480d5a90];
 	}
	uint256[] public Ox2597e3f7dacf7188b06929988f77d57be2adba6c = [16 * 74 + ( 87 + 43 )  - 1214, 2 - 1 - 0 + 1  + 1];
}