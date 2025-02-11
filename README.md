# Learn the Elements of the Periodic Table in the Terminal Window
## Video Demonstration:
https://youtu.be/B2Yg8iJ5KZY

## Description:
A game to learn the 119 elements of the Periodic Table that is played in the terminal window.

## Rules:
Elements are named in the order that they appear in the Periodic Table by ascending atomic number. Both the element's full name and symbol are accepted and neither need to be capitalised. Naming by symbol makes gameplay fast and learning more efficient.

## Features:
Users can ask for a hint if they get stuck. A hint includes information about the element's appearance, category, phase (either solid, liquid, or gas), its period number and group number, and its electron configuration.

Users can ask to see the previous element that they got so they know where they are in the Periodic Table.

Users can also skip an element if they are not sure. They are told which element they skipped and are given its description.

If users would like to quit the program, then they are told all the rest of the elements which they did not get.

## elements.py

In `elements.py`, an `Element` class is defined and `ptable` is defined (a tuple of all the elements of the Periodic Table). Each attribute of an `Element` is assigned from the `PeriodicTableJSON.json` file from the `Periodic-Table-JSON` library (available on GitHub from https://github.com/NMRbox/Periodic-Table-JSON).
