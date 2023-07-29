import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores, n_games):
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    if n_games % 10 == 1:
        plt.savefig(f'./plots/{n_games}.png')
    plt.show(block=False)