import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

# runs = ['E-MAML', "E-RL^2", "MAML", "RL^2"]
#
# df = pd.read_csv('MAML.csv')
#
# plt.figure(figsize=(8, 3))
# df.plot(kind="line")
# plt.legend(loc="upper left", bbox_to_anchor=(1.04, 1), framealpha=1, frameon=False, )
# plt.savefig('MAML.raw.png', dpi=70, bbox_inches="tight")

DPI = 300

# colors = ["#44b7ff", "#4f5aff", "#ff7272", "#ff4816", ]
colors = ["#44b7ff", "#19a6ff", "#ff7272", "#ff5151"]

for t in ['MAML', "RL$^2$"]:

    plt.figure(figsize=(6, 4))
    t_fn = t.replace("$", "").replace("^", "")

    for k, (c1, c2) in zip([f'{t}', f"E-{t}"], (colors[:2], colors[2:])):
        fn = k.replace("-", "").replace("$", "").replace("^", "")
        df = pd.read_csv(f'{fn}.csv')
        # keys = [' rew_mean', '+25%', '-25%', 'init_rew_mean', 'init_rew + 25%', 'init_rew - 25%']
        l = len(df[' rew_mean'])
        ts = np.linspace(0, 0.25 * l, l + 1)[1:]

        plt.title(f"{t} Before and After Gradient Update", fontsize=15)
        plt.plot(ts, df[' rew_mean'], color=c1, linewidth=2, label=f'{k} $U(\\theta)$')
        plt.fill_between(ts, df['+25%'], df['-25%'], facecolor=c1, alpha=0.3, interpolate=False)
        plt.plot(ts, df['init_rew_mean'], '--', color=c2, linewidth=2, label=f"{k} $\\theta_0$")
        plt.fill_between(ts, df['init_rew + 25%'], df['init_rew - 25%'], facecolor=c2, alpha=0.3, interpolate=False)

    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
    plt.xlabel('Million Time Steps', fontsize=14)
    plt.ylabel('Mean Reward', fontsize=14)
    plt.ylim(- 0.05, 0.65)

    plt.savefig(f'(E-){t_fn}', dpi=DPI, bbox_inches="tight")


for env in ['KrazyGridWorld', 'Maze']:
    colors = ['#49b8ff', '#ff7575', '#f4b247', '#66c56c']
    plt.figure(figsize=(9, 5))
    plt.title(f"{env} Learning Curves", fontsize=15)
    for t in ['MAML', "RL$^2$"]:

        t_fn = t.replace("$", "").replace("^", "")

        for k in [f'{t}', f"E-{t}"]:
            c = colors.pop()
            fn = k.replace("-", "").replace("$", "").replace("^", "")
            df = pd.read_csv(f'{fn}.csv')
            # keys = [' rew_mean', '+25%', '-25%', 'init_rew_mean', 'init_rew + 25%', 'init_rew - 25%']
            l = len(df[' rew_mean'])
            ts = np.linspace(0, 0.25 * l, l + 1)[1:]

            plt.plot(ts, df[' rew_mean'], ('-' if k[0] == "E" else '--'), color=c, linewidth=2, label=f'{k} $U(\\theta)$')
            plt.fill_between(ts, df['+25%'], df['-25%'], facecolor=c, alpha=0.3, interpolate=False)

    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
    plt.xlabel('Million Time Steps', fontsize=14)
    plt.ylabel('Mean Reward', fontsize=14)
    plt.ylim(- 0.05, 0.65)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(f'{env}-Learning_Curves.png', dpi=DPI, bbox_inches="tight")
