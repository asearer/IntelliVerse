"""
Test suite for Web3 LocalChain behavior.
"""

import pytest
import os
import shutil
from web3_module.backend.api import Web3Stub

@pytest.fixture
def clean_ledger():
    test_ledger = "web3_module/test_ledger.json"
    if os.path.exists(test_ledger):
        os.remove(test_ledger)
    yield test_ledger
    if os.path.exists(test_ledger):
        os.remove(test_ledger)

def test_log_to_blockchain(clean_ledger) -> None:
    """
    Verify creating blocks and saving to ledger.
    """
    web3 = Web3Stub(chain_file=clean_ledger)
    assert len(web3.chain) == 1 # Genesis block
    
    data = {"prediction_id": 101, "result": "safe"}
    block_hash = web3.log_to_blockchain(data)
    
    assert isinstance(block_hash, str)
    assert len(web3.chain) == 2
    assert web3.chain[1].data == data
    assert web3.chain[1].previous_hash == web3.chain[0].hash
    
    # Reload to verify persistence
    web3_reloaded = Web3Stub(chain_file=clean_ledger)
    assert len(web3_reloaded.chain) == 2
    assert web3_reloaded.chain[1].hash == block_hash
