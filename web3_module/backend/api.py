"""
Web3 Blockchain API.

Provides an interface for logging events to an immutable local ledger
(simulated blockchain).
"""

import hashlib
import json
import time
import os
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from utils.logger import setup_logger

logger = setup_logger(__name__)

@dataclass
class Block:
    """A single block in the chain."""
    index: int
    timestamp: float
    data: Dict[str, Any]
    previous_hash: str
    hash: str = ""

    def calculate_hash(self) -> str:
        """Calculate SHA-256 hash of the block content."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Web3Stub:
    """
    Simulated Web3 interface using a local file-based blockchain.
    """

    def __init__(self, chain_file: str = "web3_module/ledger.json"):
        """
        Initialize the blockchain.
        
        Args:
            chain_file: Path to the JSON ledger file.
        """
        self.chain_file = chain_file
        self.chain: List[Block] = []
        self._load_chain()

    def _load_chain(self) -> None:
        """Load chain from file or create genesis block."""
        if os.path.exists(self.chain_file):
            try:
                with open(self.chain_file, 'r') as f:
                    data = json.load(f)
                    self.chain = [Block(**b) for b in data]
                logger.info(f"Loaded blockchain with {len(self.chain)} blocks.")
            except Exception as e:
                logger.error(f"Failed to load chain: {e}. Starting new.", exc_info=True)
                self._create_genesis_block()
        else:
            self._create_genesis_block()

    def _create_genesis_block(self) -> None:
        """Create the first block."""
        genesis_block = Block(0, time.time(), {"info": "Genesis Block"}, "0")
        genesis_block.hash = genesis_block.calculate_hash()
        self.chain = [genesis_block]
        self._save_chain()

    def _save_chain(self) -> None:
        """Persist chain to disk."""
        try:
            os.makedirs(os.path.dirname(self.chain_file), exist_ok=True)
            with open(self.chain_file, 'w') as f:
                json.dump([asdict(b) for b in self.chain], f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save chain: {e}")

    def log_to_blockchain(self, data: Dict[str, Any]) -> str:
        """
        Log data to the blockchain.

        Args:
            data: Data to store (e.g. prediction result).

        Returns:
            str: The hash of the new block.
        """
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        new_block.hash = new_block.calculate_hash()
        
        self.chain.append(new_block)
        self._save_chain()
        
        logger.info(f"Block #{new_block.index} added. Hash: {new_block.hash[:10]}...")
        return new_block.hash
