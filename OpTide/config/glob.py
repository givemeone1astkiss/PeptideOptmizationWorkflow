DATA_PATH='./data/'
OUTPUT_PATH='./out/'
LOG_PATH='./log/'

AMINO_ACIDS:list = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
AMINO_ACIDS_LONG:list = ["ALA", "CYS", "ASP", "GLU", "PHE", "GLY", "HIS", "ILE", "LYS", "LEU", "MET", "ASN", "PRO", "GLN", "ARG", "SER", "THR", "VAL", "TRP", "TYR"]
DEFAULT_LEN = 4

LOGP = {'ILE': -1.12,
        'LEU': -1.25,
        'PHE': -1.71,
        'VAL': -0.46,
        'MET': -0.67,
        'PRO': 0.14,
        'TRP': -2.09,
        'THR': 0.25,
        'GLN': 0.77,
        'CYS': -0.02,
        'TYR': -0.71,
        'ALA': 0.5,
        'SER': 0.46,
        'ASN': 0.85,
        'ARG': 1.81,
        'GLY': 1.15,
        'LYS': 2.8,
        'GLU': 3.63,
        'HIS+': 2.33,
        'ASP': 3.64,
        'GLU0': 0.11,
        'HIS': 0.11}