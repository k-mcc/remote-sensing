# remote-sensing
# Remote Sensing Project: Martian Analogues of Europan Chaos Terrains
## Code for Analysis of SHARAD Radargrams

AUTHOR: Kate McCarthy (kem6ur@virginia.edu, kemccarthy6@gmail.com)
CREATED: November 2022
ASSOCIATED FILES: download_files.py, get_reflector_pixels.py, plot_reflectors.py

## PURPOSE:
For a given orbit, follow the 'INTENDED USAGE' steps below to analyze SHARAD radargrams and produce a map of reflectors and their delay time.

## INTENDED USAGE:

1. Run download_files.py 
* Must set the variable orbit_str to desired orbit
* Location of output:
  * Radargram: ./downloads/images/radargrams/
  * Cluttergram: ./downloads/images/cluttergrams/
  * Geom table: ./downloads/geom/

2. Use radargram and cluttergram to check for reflectors. Open in an image editing app such as Preview and draw on radargram in red where you see reflectors (MAKE SURE THAT HEX VALUE = 0, 0, 255). Save radargram file.

3. Run get_reflector_pixels.py
* Location of output: ./outputs/

4. Run plot_reflectors.py
* Windows will pop up displaying map of reflectors by delay time.
* All CSV files within the ./outputs/ dir will be mapped.
