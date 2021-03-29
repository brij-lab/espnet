#!/bin/bash

# Generate spkid file based on the 'train-.*' subset!

dst=./data
asr_data="$1"
filter_subset="$2"

mkdir -p $dst

spk_file=${asr_data}/LibriSpeech/SPEAKERS.TXT

spk2id=$dst/spk2id; [[ -f $spk2id ]] && rm $spk2id

grep "^^[0-9]*\s+\|.*${filter_subset}" -E ${spk_file} | awk -F'|' '{gsub(/[ ]+/, ""); print $1, NR-1}' > $spk2id

echo "$0 spk2id file created (filter: ${filter_subset})"

