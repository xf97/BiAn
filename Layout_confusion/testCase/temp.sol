pragma solidity 0.5.16;

contract O06b64504952a7828c2479413727c71e061ae19a2e{
    uint256 public O0ce53a883dfd2a0ed554eef878770ed682e23fda2;
    function O028220e0690a03eaa1c9289369594a1b70d5f8da5() view public returns(uint256){
        return O0ce53a883dfd2a0ed554eef878770ed682e23fda2;
    }
}

contract O0e300b1333824ba18868c36d4c0c2c8915be4dfaf is O06b64504952a7828c2479413727c71e061ae19a2e{
    constructor(uint256 O076d750b4390ce7a6ffc4d86ea1b95cff13c9c8d6) public{
        O0ce53a883dfd2a0ed554eef878770ed682e23fda2 = O076d750b4390ce7a6ffc4d86ea1b95cff13c9c8d6;
    }
}

contract O0a66c2e729c9d9c06c803a9c9e598eb0da5e09175 is O06b64504952a7828c2479413727c71e061ae19a2e{
    function O028220e0690a03eaa1c9289369594a1b70d5f8da5() view public returns(uint256){
        return O0ce53a883dfd2a0ed554eef878770ed682e23fda2 + 10;
    }
}

//right order

contract O02d99983cb292a6fdffbfbbd067bf5e76494bbd25 is O0e300b1333824ba18868c36d4c0c2c8915be4dfaf, O0a66c2e729c9d9c06c803a9c9e598eb0da5e09175{
    address public O0b5a308a22303a0fe3b803ba9f25a1df405f02f3b;
    constructor() public{
        O0b5a308a22303a0fe3b803ba9f25a1df405f02f3b = msg.sender;
    }
}