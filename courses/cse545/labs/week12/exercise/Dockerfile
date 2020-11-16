from debian:stable

RUN apt-get update && apt-get install --no-install-recommends -y \
  afl \
  build-essential \
  clang++-7 \
  less \
  libfuzzer-7-dev \
  nano \
  vim-tiny && \
  update-alternatives --install  /usr/bin/clang clang /usr/bin/clang-7 10 && \
  update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-7 10

WORKDIR "/root"
COPY afl-example afl-example
#COPY libfuzzer-example libfuzzer-example
COPY tinyxml2  tinyxml2
CMD ["/bin/bash"]
