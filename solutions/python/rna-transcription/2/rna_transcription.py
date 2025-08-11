TRANSLATION_TABLE = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    """
    Convert a DNA strand to RNA by replacing G->C, C->G, T->A, A->U.

    Args:
        dna_strand: The DNA strand to convert.

    Returns:
        The RNA strand corresponding to the input DNA strand.
    """
    return dna_strand.translate(TRANSLATION_TABLE)
