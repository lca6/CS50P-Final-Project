from elements import ptable, ELEMENTS


def main():
    print(info)
    i = 0
    while True:
        # Checks if user got all elements
        if i < ELEMENTS:
            pass
        else:
            print(congratulations)
            return

        print(progress(i))

        try:
            element = input(f"Atomic Number {i + 1}: ").title().strip()

        # If user forces quit
        except EOFError:
            print(message)
            for elem in ptable[i:]:
                print(f"Atomic Number {i + 1}: {elem.name} ({elem.symbol})")
                i += 1
            return

        else:

            # User must recall elements in order of atomic number
            if element == ptable[i].name or element == ptable[i].symbol:
                print(correct)
                print(ptable[i].summary)
                i += 1

            # If user forgets previous element
            elif "Prev" in element:

                # No previous
                if i == 0:
                    print()
                else:
                    print(previous_element(i))

            # Provide description of that element
            elif "Hint" in element:
                print(hint(i))

            # If user does not know the element
            elif "Idk" in element or "Skip" in element or "Help" in element:
                print(skipped_element(i))
                i += 1

            # If user wants to see the instructions again
            elif "Info" in element:
                print(info)

            # If user inputs an incorrectly spelled element or symbol
            else:
                print(incorrect)
                continue


def progress(i):
    return f"""
{i} done
{ELEMENTS - i} elements remaining\n
"""


def previous_element(i):
    return f"""
Below is the previous element in the Periodic Table:

{ptable[i - 1].name} ({ptable[i - 1].symbol})
"""


def hint(i):
    return f"""
Appearance: {ptable[i].appearance}
Category: {ptable[i].category}
Phase: {ptable[i].phase}
Period {ptable[i].period}
Group {ptable[i].group}
Electron configuration: {ptable[i].electron_configuration}
"""


def skipped_element(i):
    return f"""
Name: {ptable[i].name}
Summary: {ptable[i].summary}
"""


info = f"""
========== Name the {ELEMENTS} elements of the Periodic Table ==========

RULES:

1. Name the elements in order of ascending atomic number.
   This is the number in the top left of each box.

2. Name the elements by their full name or symbol.

HELP:

1. You do not need to capitalise any names or symbols.

2. Text "hint" if you need a hint.

3. Text "prev" to see the previous element.

4. Text "help" or "idk" or "skip" to skip an element.

5. Press CTRL + D to quit the program.

6. Text "info" to see these instructions again.
"""


congratulations = f"""
CONGRATULATIONS. YOU GOT ALL {ELEMENTS} ELEMENTS!
"""


message = """

Below are the remaining elements of the Periodic Table:
"""


correct = """
CORRECT ✅
"""


incorrect = """
❌
"""


if __name__ == "__main__":
    main()
