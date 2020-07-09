pragma solidity 0.5.16;

contract O05a1d3ac402a903026d37d33128c693de93ec2b20{
    uint256 public O0afd1cf17b1fbbb87f9bcea8bf7548a09c2162053;
    function O05580b9af589ac31eb232a98e734778215861bc70() view public returns(uint256){
        return O0afd1cf17b1fbbb87f9bcea8bf7548a09c2162053;
    }
}

contract O0c967332fdfc697e43510f0e49a774f76f0ec4455 is O05a1d3ac402a903026d37d33128c693de93ec2b20{
    constructor(uint256 O0d70b9a9db4b702092cb8b0b1791a08ea6d05eae6) public{
        O0afd1cf17b1fbbb87f9bcea8bf7548a09c2162053 = O0d70b9a9db4b702092cb8b0b1791a08ea6d05eae6;
    }
}

contract O00b5c0902409da1c4ab014b05d87424c5e4932cc0 is O05a1d3ac402a903026d37d33128c693de93ec2b20{
    function O05580b9af589ac31eb232a98e734778215861bc70() view public returns(uint256){
        return O0afd1cf17b1fbbb87f9bcea8bf7548a09c2162053 + 10;
    }
}

//right order

contract O0c11964229ba68f0557b8d58c6b518ed4c6f15927 is O0c967332fdfc697e43510f0e49a774f76f0ec4455, O00b5c0902409da1c4ab014b05d87424c5e4932cc0{
    address public O0c5e8f0ebffd3565fa8bcaeb7c46b18f6d4c994eb;
    constructor() public{
        O0c5e8f0ebffd3565fa8bcaeb7c46b18f6d4c994eb = msg.sender;
    }
}