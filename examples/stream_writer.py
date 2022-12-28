import time

import momentumx as mx


STREAM = "mx://streamer"
THRESHOLD = 10000

now = time.time()
messages_sent = 0
bytes_sent = 0
data_length = int(100e6)

context = mx.Context()
stream = context.stream(STREAM, data_length, 30, True)
while True:
    buffer_state = stream.next()

    if buffer_state:
        buffer_state.data_size = data_length

        stream.send(buffer_state)
        messages_sent += 1
        bytes_sent += data_length

        if messages_sent % THRESHOLD == 0:
            elapsed = time.time() - now
            print("Sent {:.2f} msgs/sec".format(messages_sent / elapsed))
            print("Sent {:.2f} GB/sec".format(bytes_sent / elapsed / 1.0e9))

            messages_sent = 0
            bytes_sent = 0

            now = time.time()
