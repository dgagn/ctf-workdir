#!/usr/bin/zsh

while [ -f matryoshka.zip ]
do
  zip2john matryoshka.zip > hash.john
  john --wordlist=dict.txt hash.john
  john hash.john --show > output.txt
  unzip -oP "$(grep -Eo "m4try0shk4#[A-Za-z]{2}[0-9]{4}" output.txt)" matryoshka.zip
done