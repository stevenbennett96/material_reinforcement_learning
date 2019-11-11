import numpy as np
'''
Defines all actions in the Markov Decision Process.
'''


def swap_one_random(mol, bb_db):
    '''Swaps one building block at random.
    '''
    while True:
        selected_new = np.random.choice(bb_db, 1)
        bbs = list(mol.get_building_blocks())
        selected_old = np.random.choice(bbs, 1)
        try:
            new_state = get_constructed_molecule([selected_old, selected_new])
            return new_state
        except Exception:
            print('Could not create molecule.')


def swap_both_random(mol, bb_db):
    '''Swaps both building blocks randomly.
    '''
    while True:
        selected_new = np.random.choice(bb_db, 2)
        try:
            new_state = get_constructed_molecule(selected_new)
            return new_state
        except Exception:
            print('Could not create molecule.')


def swap_one_similar(mol, bb_db):
    '''Swaps a building block for the most similar one.
    '''
    bbs = list(mol.get_building_blocks())
    selected_old = np.random.choice(bbs, 1)
    bb_fp = FingerprintMols.FingerprintMol(selected_old.to_rdkit_mol())
    similarities = [DataStructs.FingerprintSimilarity(bb_fp, fp) for fp in fps]
    similarities_index = sorted(
        similarities,
        key=lambda k: similarities[k],
        reverse=True,
    )
    bb_counter = 0
    while True:
        bb = bb_db[similarities_index[bb_counter]]
        try:
            new_state = get_constructed_molecule([selected_old, bb])
            return new_state
        except Exception:
            bb_counter += 1
            print('Could not create molecule.')


def swap_both_similar(mol, bb_db):
    '''Swaps both building blocks for the most similar one.
    '''
    bbs = list(mol.get_building_blocks())
    bbs_fp = [FingerprintMols.FingerprintMol(bb.to_rdkit_mol()) for bb in bbs]
    similarity_bb1 = [DataStructs.FingerprintSimilarity(
        bbs_fp[0], fp) for fp in bbs_fp]
    similarity_bb2 = [DataStructs.FingerprintSimilarity(
        bbs_fp[1], fp) for fp in bbs_fp]
    # This is ordered by index.
    similarities_index_bb1 = sorted(
        similarity_bb1,
        key=lambda k: similarity_bb1[k],
        reverse=True,
    )
    similarities_index_bb2 = sorted(
        similarity_bb2,
        key=lambda k: similarity_bb2[k],
        reverse=True,
    )
    bb_counter = 0
    while True:
        if bb_counter != 0:
            idx = np.random.choice([0, 1])
            if idx == 0:
                bb1 = bb_db[similarities_index_bb1[bb_counter+1]]
                bb2 = bb_db[similarities_index_bb2[bb_counter]]
            elif idx == 1:
                bb1 = bb_db[similarities_index_bb1[bb_counter]]
                bb2 = bb_db[similarities_index_bb2[bb_counter+1]]
        else:
            bb1 = bb_db[similarities_index_bb1[bb_counter]]
            bb2 = bb_db[similarities_index_bb2[bb_counter]]
        try:
            new_state = get_constructed_molecule([bb1, bb2])
            return new_state
        except Exception:
            bb_counter += 1
            print('Could not create molecule.')


def swap_one_different(mol, bb_db):
    '''Swaps a building block for the most different one.
    '''
    bbs = list(mol.get_building_blocks())
    selected_old = np.random.choice(bbs, 1)
    bb_fp = FingerprintMols.FingerprintMol(selected_old.to_rdkit_mol())
    similarities = [DataStructs.FingerprintSimilarity(bb_fp, fp) for fp in fps]
    similarities_index = sorted(
        similarities,
        key=lambda k: similarities[k],
        reverse=False,
    )
    bb_counter = 0
    while True:
        bb = bb_db[similarities_index[bb_counter]]
        try:
            new_state = get_constructed_molecule([selected_old, bb])
            return new_state
        except Exception:
            bb_counter += 1
            print('Could not create molecule.')


def swap_both_different(mol, bb_db):
    '''Swaps both building blocks for the most different one.
    '''
    bbs = list(mol.get_building_blocks())
    bbs_fp = [FingerprintMols.FingerprintMol(bb.to_rdkit_mol()) for bb in bbs]
    similarity_bb1 = [DataStructs.FingerprintSimilarity(
        bbs_fp[0], fp) for fp in bbs_fp]
    similarity_bb2 = [DataStructs.FingerprintSimilarity(
        bbs_fp[1], fp) for fp in bbs_fp]
    # This is ordered by index.
    similarities_index_bb1 = sorted(
        similarity_bb1,
        key=lambda k: similarity_bb1[k],
        reverse=False,
    )
    similarities_index_bb2 = sorted(
        similarity_bb2,
        key=lambda k: similarity_bb2[k],
        reverse=False,
    )
    bb_counter = 0
    while True:
        if bb_counter != 0:
            idx = np.random.choice([0, 1])
            if idx == 0:
                bb1 = bb_db[similarities_index_bb1[bb_counter+1]]
                bb2 = bb_db[similarities_index_bb2[bb_counter]]
            elif idx == 1:
                bb1 = bb_db[similarities_index_bb1[bb_counter]]
                bb2 = bb_db[similarities_index_bb2[bb_counter+1]]
        else:
            bb1 = bb_db[similarities_index_bb1[bb_counter]]
            bb2 = bb_db[similarities_index_bb2[bb_counter]]
        try:
            new_state = get_constructed_molecule([bb1, bb2])
            return new_state
        except Exception:
            bb_counter += 1
            print('Could not create molecule.')
