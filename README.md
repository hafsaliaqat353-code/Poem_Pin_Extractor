# Poem_Pin_Extractor

A fun steganography-inspired CLI tool that extracts hidden "secret codes" from poems.

## How It Works

Every line of your poem hides a digit — determined by the length of a specific word
in that line. The tool reads your poem and reveals the number hidden inside it.

This is based on a simple linguistic cipher:
- For each line N, it checks the word at index N
- The digit = length of that word
- All digits combined = your secret code

## Requirements

- Python 3.x
- pyfiglet
- colorama

## Use Case

- Fun steganography demo
- CTF / puzzle inspiration
- Learning about linguistic ciphers
- Creative coding / CLI aesthetics

## Disclaimer

This tool works purely on text input you provide yourself.
It does not access any systems, accounts, or external data.
