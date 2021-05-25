from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    scores_len = len(individual_play_scores)
    dp = [[0 for _ in range(final_score+1)] for _ in range(scores_len)]
    dp[0][0] = 1

    for i in range(scores_len):
        for j in range(final_score+1):
            if dp[i][j] > 0:
                if i+1 < scores_len:
                    dp[i+1][j] += dp[i][j]
                if j+individual_play_scores[i] <= final_score:
                    dp[i][j+individual_play_scores[i]] += dp[i][j]
    return dp[scores_len-1][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
