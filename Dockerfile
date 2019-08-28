FROM pinellolab/stream:0.3.8

RUN mkdir /stream
COPY dimred_command_line.py /stream/dimred_command_line.py

ENTRYPOINT []
