from datetime import datetime

from sanic import Sanic

application = Sanic.get_app()

class Snowflake:
    """
    Snowflake

    64 bits = 5 bits + 6 bits + 43 bits + 10 bits
    """

    def __init__(self, center_id, worker_id) -> None:
        self.center_id = center_id
        self.worker_id = worker_id
        self.last_seq_id = -1
        self.last_timestamp = None

    def get_timestamp(self):
        """
        Return milli timestamp.
        """
        return int(datetime.utcnow().timestamp() * 1000)
        
    def next_id(self) -> int:
        """
        Return next id.
        """
        cur_timestamp = self.get_timestamp()
        while self.last_seq_id == 0b1111111111:
            cur_timestamp = self.get_timestamp()
            if cur_timestamp != self.last_timestamp:
                self.last_seq_id = -1
        else:
            self.last_timestamp = cur_timestamp
            self.last_seq_id = self.last_seq_id + 1
        
        unique_id = self.center_id << 59 | self.worker_id << 53 | self.last_timestamp << 10 | self.last_seq_id
        return unique_id


snowflake = Snowflake(center_id=application.config.CENTER_ID, worker_id=application.config.WORKER_ID)
generate_unique_id = snowflake.next_id
