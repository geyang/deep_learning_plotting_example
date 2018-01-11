import sys
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import csv
import pandas as pd


def example_one():

    DPI = 300
    PREFIX = "figures/"

    rcParams['axes.labelpad'] = 15

    colors = ['#49b8ff', '#ff7575', '#66c56c', '#f4b247']
    line_style = ['-', '-.', '--', ':']
    plt.figure(figsize=(9, 5))
    plt.title("Learning Curves", fontsize=15)

    for curve in ['method1', "method2", 'method3', 'method4']:

        c = colors.pop(0)
        ls = line_style.pop(0)
        csv_path = "data/" + curve + '.csv'
        df = pd.read_csv(csv_path)
        # keys = [' rew_mean', '+25%', '-25%', 'init_rew_mean', 'init_rew + 25%', 'init_rew - 25%']
        l = len(df['rew_mean'])
        ts = np.linspace(0, 0.25 * l, l + 1)[1:]

        plt.plot(ts, df['rew_mean'], ls, color=c, linewidth=2, label=curve)
        plt.fill_between(ts, df['+25%'], df['-25%'], facecolor=c, alpha=0.3, interpolate=False)

        plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1), framealpha=1, frameon=False, fontsize=14)
        plt.xlabel('Million Time Steps', fontsize=14)
        plt.ylabel('Mean Reward', fontsize=14)
        plt.ylim(- 0.05, 0.65)

        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.savefig(f'{PREFIX}/Learning_Curves.png', dpi=DPI, bbox_inches="tight")


def example_two():
    DPI = 300
    PREFIX = "figures/"
    y = 'cost'
    data_fn = 'data/' + y + '.csv'
    output_fn = "cost.png"
    rcParams['axes.labelpad'] = 15

    df = pd.read_csv(data_fn)

    plt.figure(figsize=(4, 2.66))
    plt.title("cost", fontsize=15)

    colors = ['#49b8ff', '#ff7575', '#66c56c', '#f4b247']
    line_styles = ['-', '-.', '--', ':']
    for alg in ['method1', "method2", 'method3', 'method4']:
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
    plt.savefig(f'{PREFIX}/Cost_Curves.png', dpi=DPI, bbox_inches="tight")


if __name__ == '__main__':
    example_one()
    example_two()
