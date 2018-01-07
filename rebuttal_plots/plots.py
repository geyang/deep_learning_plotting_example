import sys
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import csv
import pandas as pd

DPI = 300
PREFIX = "figures/"

rcParams['axes.labelpad'] = 15

for env in ['KrazyWorld', 'Maze']:
    colors = ['#49b8ff', '#ff7575', '#66c56c', '#f4b247']
    line_style = ['-', '-.', '--', ':']
    plt.figure(figsize=(9, 5))
    plt.title(f"{env} Learning Curves", fontsize=15)
    for t in ['MAML', "RL$^2$"]:

        t_fn = t.replace("$", "").replace("^", "")

        for k in [f"E-{t}", f'{t}']:
            c = colors.pop(0)
            ls = line_style.pop(0)
            fn = k.replace("-", "").replace("$", "").replace("^", "")
            csv_path = f'{env.lower()}/{fn}.csv'
            df = pd.read_csv(csv_path)
            # keys = [' rew_mean', '+25%', '-25%', 'init_rew_mean', 'init_rew + 25%', 'init_rew - 25%']
            l = len(df['rew_mean'])
            ts = np.linspace(0, 0.25 * l, l + 1)[1:]

            plt.plot(ts, df['rew_mean'], ls, color=c, linewidth=2, label=f'{k}')
            plt.fill_between(ts, df['+25%'], df['-25%'], facecolor=c, alpha=0.3, interpolate=False)

    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
    plt.xlabel('Million Time Steps', fontsize=14)
    plt.ylabel('Mean Reward', fontsize=14)
    plt.ylim(- 1.8, 0.65) if env == "Maze" else plt.ylim(- 0.05, 0.65)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(f'{PREFIX}/{env}-Learning_Curves.png', dpi=DPI, bbox_inches="tight")

colors = ['#49b8ff', '#ff7575', '#66c56c', '#f4b247']


rcParams['axes.titlepad'] = 15

for env in ['KrazyWorld', 'Maze']:
    for t, (c1, c2) in zip(["MAML", "RL$^2$"], (colors[:2], colors[2:])):

        t_fn = t.replace("$", "").replace("^", "")

        for k in [f'{t}', f"E-{t}"]:
            plt.figure(figsize=(4, 2.66))
            fn = k.replace("-", "").replace("$", "").replace("^", "")
            output_fn = k.replace('$', '').replace('^', '')
            csv_path = f'{env.lower()}/{fn}.csv'
            df = pd.read_csv(csv_path)
            # keys = [' rew_mean', '+25%', '-25%', 'init_rew_mean', 'init_rew + 25%', 'init_rew - 25%']
            l = len(df['rew_mean'])
            ts = np.linspace(0, 0.25 * l, l + 1)[1:]

            plt.title(f"{k} ({env})", fontsize=15)
            # plt.plot(ts, df['rew_mean'], color=c1, linewidth=2, label=f'{k} $U(\\theta)$')
            plt.plot(ts, df['rew_mean'], color=c1, linewidth=2, label=f'after')
            plt.fill_between(ts, df['+25%'], df['-25%'], facecolor=c1, alpha=0.3, interpolate=False)
            # plt.plot(ts, df['init_rew_mean'], '--', color=c2, linewidth=2, label=f"{k} $\\theta_0$")
            plt.plot(ts, df['init_rew_mean'], '--', color=c2, linewidth=2, label=f"initial")
            plt.fill_between(ts, df['init_rew + 25%'], df['init_rew - 25%'], facecolor=c2, alpha=0.3, interpolate=False)

            plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
            plt.xlabel('Million Time Steps', fontsize=14)
            plt.ylabel('Mean Reward', fontsize=14)
            plt.ylim(- 2.5, 0.65) if env == "Maze" else plt.ylim(- 0.05, 0.65)

            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.savefig(f'{PREFIX}/{env}-{output_fn}.png', dpi=DPI, bbox_inches="tight")


# ["ERL2", "ERL2+25", "ERL2-25", "RL2", "RL2+25", "RL2-25", "EMAML", "EMAML+25", "EMAML-25", "MAML", "MAML+25", "MAML-25"]
env = "KrazyWorld"
y_labels = ['Number of Goals', "Number of Visits", "Number of Deaths"]
for name in ["Goals Found", "Visited Tile Types", "Times Died"]:
    y = y_labels.pop(0)

    data_fn = f"heuristics/{name.replace(' ', '')}.csv"
    output_fn = f"{name}.png"

    df = pd.read_csv(data_fn)

    plt.figure(figsize=(4, 2.66))
    plt.title(f"{name}", fontsize=15)

    colors = ['#49b8ff', '#ff7575', '#66c56c', '#f4b247']
    line_styles = ['-', '-.', '--', ':']
    for alg in ["E-MAML", "MAML", "E-RL$^2$", "RL$^2$"]:
        c = colors.pop(0)
        ls = line_styles.pop(0)

        k = alg.replace("-", "").replace("$", "").replace("^", "")
        l = len(df[k])
        ts = np.linspace(0, 2.5 * l, l + 1)[1:]

        plt.plot(ts, df[k], ls, color=c, linewidth=2, label=alg)
        plt.fill_between(ts, df[f'{k}+25'], df[f'{k}-25'], facecolor=c, alpha=0.3, interpolate=False)

    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
    plt.xlabel('Million Time Steps', fontsize=14)
    plt.ylabel(y, fontsize=14)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(f'{PREFIX}/{name.replace(" ", "_")}-{env}.png', dpi=DPI, bbox_inches="tight")
