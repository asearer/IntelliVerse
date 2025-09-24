pragma solidity ^0.8.0;
contract TransactionLogger {}
// Solidity Smart Contract Stub
pragma solidity ^0.8.0;

contract TransactionLogger {
    struct EventLog { string action; string module; uint256 timestamp; }
    EventLog[] public logs;

    function logEvent(string memory action, string memory module) public {
        logs.push(EventLog({action: action, module: module, timestamp: block.timestamp}));
    }
}
