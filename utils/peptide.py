from config.peptide import AMINO_ACIDS, DEFAULT_LEN, AMINO_ACIDS_LONG
import random
from rdkit import Chem
from collections import defaultdict
from pprint import pprint

def gen_random_peptide(length: int) -> str:
    return ''.join(random.choices(AMINO_ACIDS, k=length))

def format_sequence(a1, a2, a3):
    """Format a sequence of three atoms."""
    if f"{a1.GetSymbol()}{a1.GetDegree()}-" > f"{a3.GetSymbol()}{a3.GetDegree()}":
        return (
            f"{a3.GetSymbol()}{a3.GetDegree()}-"
            f"{a2.GetSymbol()}{a2.GetDegree()}-"
            f"{a1.GetSymbol()}{a1.GetDegree()}"
        )
    return (
        f"{a1.GetSymbol()}{a1.GetDegree()}-"
        f"{a2.GetSymbol()}{a2.GetDegree()}-"
        f"{a3.GetSymbol()}{a3.GetDegree()}"
    )

def gen_fingerprint(smiles: str) -> dict:
    """Generate fingerprint for a given SMILES string."""
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol) # Add hydrogens
    fingerprint = defaultdict(int)
    for bond in mol.GetBonds():
        atom_b = bond.GetBeginAtom()
        atom_a = bond.GetEndAtom()

        for atom_C in atom_b.GetNeighbors():
            if atom_C.GetIdx() == atom_a.GetIdx():
                continue
            seq = format_sequence(atom_a, atom_b, atom_C)
            fingerprint[seq] += 1

        for atom_C in atom_a.GetNeighbors():
            if atom_C.GetIdx() == atom_b.GetIdx():
                continue
            seq = format_sequence(atom_C, atom_a, atom_b)
            fingerprint[seq] += 1

        total_atoms = mol.GetNumAtoms()
        return {k: v / (2 * total_atoms) for k, v in fingerprint.items()}

def short_to_long(sequence: list) -> list:
    """Converting short abbreviations of peptide chains to long abbreviations"""
    long_sequence = []
    for i, aa in enumerate(sequence):
        long_sequence[i] = AMINO_ACIDS_LONG[AMINO_ACIDS.index(aa)]
    return long_sequence

def long_to_short(sequence: list) -> list:
    """Converting long abbreviations of peptide chains to short abbreviations"""
    short_sequence = []
    for i, aa in enumerate(sequence):
        short_sequence[i] = AMINO_ACIDS[AMINO_ACIDS_LONG.index(aa)]
    return short_sequence

def random_mutation(sequence: list) -> list:
    """Randomly mutate one aa in a peptide sequence"""
    mutated_sequence = sequence.copy()
    mutated_sequence[random.randint(0, len(sequence) - 1)] = random.choice(AMINO_ACIDS)
    return mutated_sequence

