import time
from typing import Callable


class SnowflakeGeneratorBuilder:
    def __init__(self, node_bits: int = 10, sequence_bits: int = 12):
        self._node_bits = node_bits
        self._sequence_bits = sequence_bits

    def create_generator(
        self, epoch: int = 1288834974657, node_id: int = 0
    ) -> Callable[[], int]:
        max_node_id = (1 << self._node_bits) - 1
        if node_id > max_node_id or node_id < 0:
            raise ValueError(
                f"node_id must not be greater than {max_node_id} or smaller than 0"
            )
        sequence_mask = (1 << self._sequence_bits) - 1
        node_bits = self._node_bits
        sequence_bits = self._sequence_bits
        last_ts = -1
        sequence_id = 0

        def generate_id() -> int:
            nonlocal last_ts, sequence_id

            def current_timestamp() -> int:
                return int(time.time() * 1000)

            def wait_until_next_timestamp() -> int:
                ts = current_timestamp()
                while ts <= last_ts:
                    ts = current_timestamp()
                return ts

            ts = current_timestamp()
            if ts < last_ts:
                raise ValueError("Clock moved backwards. Refusing to generate id.")
            if ts == last_ts:
                sequence_id = (sequence_id + 1) & sequence_mask
                if sequence_id == 0:
                    ts = wait_until_next_timestamp()
            else:
                sequence_id = 0

            last_ts = ts

            return (
                ((ts - epoch) << (node_bits + sequence_bits))
                | (node_id << sequence_bits)
                | sequence_id
            )

        return generate_id
