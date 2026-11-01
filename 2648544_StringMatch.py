# Check whether the input contains only valid DNA characters.
# A, C, G and T are the only characters allowed.
def validate_dna(sequence):
    if sequence == "":
        return False

    for ch in sequence:
        if ch not in "ACGT":
            return False

    return True



# Convert a list of positions into the required output format.
# If there are no matches, display NONE.

def format_positions(positions):
    if not positions:
        return "NONE"
    return " ".join(str(pos) for pos in positions)

# 1. NAIVE / BRUTE-FORCE STRING MATCHING


def naive_search(text, pattern):
    positions = []
    comparisons = 0

    n = len(text)
    m = len(pattern)

    # No possible match if the pattern is longer than the text.
    if m > n:
        return positions, comparisons

    # Try matching the pattern at every possible position.
    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] == pattern[j]:
                j += 1
            else:
                break

        # The complete pattern matched.
        if j == m:
            positions.append(i)

    return positions, comparisons


# 2. COMPUTE THE LPS ARRAY FOR KMP


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    # length stores the length of the previous matching
    # prefix and suffix.
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            # Try the next smaller prefix instead of
            # starting the comparison from zero.
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps

# 3. KMP STRING MATCHING


def kmp_search(text, pattern):
    positions = []
    comparisons = 0

    n = len(text)
    m = len(pattern)

    if m > n:
        return positions, comparisons, compute_lps(pattern)

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < n:

        # Count each comparison between text and pattern.
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            # Complete pattern found.
            if j == m:
                positions.append(i - j)

                # Move using LPS so overlapping matches
                # are not missed.
                j = lps[j - 1]

        else:
            if j != 0:
                # Reuse information from the LPS array.
                j = lps[j - 1]
            else:
                i += 1

    return positions, comparisons, lps


# 4. BOYER-MOORE - BAD CHARACTER HEURISTIC


def build_bad_character_table(pattern):
    last_position = {}

    # Store the last occurrence of every character.
    for i in range(len(pattern)):
        last_position[pattern[i]] = i

    return last_position


def boyer_moore_search(text, pattern):
    positions = []
    comparisons = 0

    n = len(text)
    m = len(pattern)

    if m > n:
        return positions, comparisons

    last_position = build_bad_character_table(pattern)

    shift = 0

    while shift <= n - m:
        j = m - 1

        # Boyer-Moore compares from right to left.
        while j >= 0:
            comparisons += 1

            if pattern[j] == text[shift + j]:
                j -= 1
            else:
                break

        if j < 0:
            # Complete pattern found.
            positions.append(shift)

            # Shift by one position so overlapping
            # occurrences are also detected.
            shift += 1

        else:
            # Use the bad-character rule to skip positions
            # that cannot produce a match.
            bad_char = text[shift + j]
            last = last_position.get(bad_char, -1)

            shift += max(1, j - last)

    return positions, comparisons

# 5. RUN ONE STRING-MATCHING TEST
def run_search(text, pattern):
    # Validate both DNA strings before processing.
    if not validate_dna(text) or not validate_dna(pattern):
        print("Invalid input")
        return

    # Compute LPS and run the required algorithms.
    lps = compute_lps(pattern)

    naive_positions, naive_comparisons = naive_search(text, pattern)

    kmp_positions, kmp_comparisons, _ = kmp_search(text, pattern)

    bm_positions, bm_comparisons = boyer_moore_search(text, pattern)

    print()
    print("LPS Array :", " ".join(map(str, lps)))

    print(
        "Naive : Positions =",
        format_positions(naive_positions),
        "| Count =", len(naive_positions),
        "| Comparisons =", naive_comparisons
    )

    print(
        "KMP : Positions =",
        format_positions(kmp_positions),
        "| Count =", len(kmp_positions),
        "| Comparisons =", kmp_comparisons
    )

    print(
        "Boyer-Moore : Positions =",
        format_positions(bm_positions),
        "| Count =", len(bm_positions),
        "| Comparisons =", bm_comparisons
    )

# 6. MANDATORY TEST CASES


def run_mandatory_tests():

    test_cases = [
        ("ACGTTAGCTAGCTAGGCTAGCTAG", "GCTAG"),
        ("AAAAAAAAAA", "AAA"),
        ("ACGTACGT", "TTT"),
        ("ACG", "ACGTA"),
        ("AACGAACGAACG", "AACG"),
        ("ATATATATGATAT", "ATAT"),
        ("ACGTXACG", "ACG")
    ]

    print("\n" + "=" * 65)
    print("MANDATORY TEST CASES")
    print("=" * 65)

    for number, (text, pattern) in enumerate(test_cases, start=1):

        print("\nTest Case", number)
        print("Text    :", text)
        print("Pattern :", pattern)

        if not validate_dna(text) or not validate_dna(pattern):
            print("Invalid input")
            continue

        run_search(text, pattern)



# 7. PERFORMANCE COMPARISON


def performance_comparison():

    import random

    print("\n" + "=" * 65)
    print("PERFORMANCE COMPARISON")
    print("=" * 65)

    length = 100000

    # Fixed seed makes the random DNA sequence reproducible.
    random.seed(42)

    random_text = "".join(
        random.choices("ACGT", k=length)
    )

    repetitive_text = "A" * length

    # Pattern length = 10 as required by the lab.
    pattern = "ACGTACGTGC"

    print("\nPattern used:", pattern)
    print("Text length :", length)
    # Random DNA
    

    naive_pos, naive_count = naive_search(random_text, pattern)
    kmp_pos, kmp_count, _ = kmp_search(random_text, pattern)
    bm_pos, bm_count = boyer_moore_search(random_text, pattern)

    print("\nRandom DNA")
   
    print("Naive       Comparisons =", naive_count)
    print("KMP         Comparisons =", kmp_count)
    print("Boyer-Moore Comparisons =", bm_count)

    # Repetitive DNA
   

    naive_pos, naive_count = naive_search(
        repetitive_text, pattern
    )

    kmp_pos, kmp_count, _ = kmp_search(
        repetitive_text, pattern
    )

    bm_pos, bm_count = boyer_moore_search(
        repetitive_text, pattern
    )

    print("\nRepetitive DNA ('A' repeated)")
    
    print("Naive       Comparisons =", naive_count)
    print("KMP         Comparisons =", kmp_count)
    print("Boyer-Moore Comparisons =", bm_count)

    print("\nNote:")
    print("The comparison counts show how many character comparisons")
    print("were performed by each algorithm for the same input.")

# 8. MAIN MENU


def main():

    while True:
        print("\n" + "=" * 65)
        print("GENOSCAN AI - STRING MATCHING")
        print("=" * 65)
        print("1. Run String Matching")
        print("2. Run Mandatory Test Cases")
        print("3. Run Performance Comparison")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            print("\nEnter DNA Text:")
            text = input().strip()

            print("Enter DNA Pattern:")
            pattern = input().strip()

            run_search(text, pattern)

        elif choice == "2":
            run_mandatory_tests()

        elif choice == "3":
            performance_comparison()

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# Start the program
if __name__ == "__main__":
    main()
