pragma solidity 0.5.16;

contract O0cd0be00ee1595cdafb5de7175e824e2e59e04a29{
    uint256 public O0c7d860be56da2cc8c029f2e423df3cc371cad294;
    function O050d9feaf125eaaf53a23e79de4f9708631531407() view public returns(uint256){
        return O0c7d860be56da2cc8c029f2e423df3cc371cad294;
    }
}

contract O0375511685009ab646132edf9bd331f9d0681bb87 is O0cd0be00ee1595cdafb5de7175e824e2e59e04a29{
    constructor(uint256 O013f20f180f42a6d0eebe0f1f11f2b432d50bbdfd) public{
        O0c7d860be56da2cc8c029f2e423df3cc371cad294 = O013f20f180f42a6d0eebe0f1f11f2b432d50bbdfd;
    }
}

contract O0ff56674c2c26f08ee793cad798f6dccc441c0486 is O0cd0be00ee1595cdafb5de7175e824e2e59e04a29{
    function O050d9feaf125eaaf53a23e79de4f9708631531407() view public returns(uint256){
        return O0c7d860be56da2cc8c029f2e423df3cc371cad294 + 10;
    }
}

//right order

contract O02126e356b507c7187dd3294a3873bc08d2574cdf is O0375511685009ab646132edf9bd331f9d0681bb87, O0ff56674c2c26f08ee793cad798f6dccc441c0486{
    address public O02fcea571f49b1c83375a435a8fdc82df86db9592;
    constructor() public{
        O02fcea571f49b1c83375a435a8fdc82df86db9592 = O049b25147f04a434d1c4dcbb21f2ed6abcaa1486e.sender;
    }
}