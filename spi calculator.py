import pandas as pd

overall_results = pd.read_csv(r"C:\Users\sophi\Downloads\ncaa data.csv")
# print(overall_results.head(20))

def spi(results,my_fencer_power):
    Lcat = results[results["Opponent Rank Category"] <= 40]
    Mcat = results[(results["Opponent Rank Category"] >= 50) & (results["Opponent Rank Category"] <= 70)]
    Hcat = results[results["Opponent Rank Category"] >= 80]

    L_win = len(Lcat[Lcat["Win/Loss"]=="W"])
    M_win = len(Mcat[Mcat["Win/Loss"]=="W"])
    H_win = len(Hcat[Hcat["Win/Loss"]=="W"])

    L_win_rate = (L_win + 2) / (len(Lcat) + 3) # adding starting constant of +2 bouts won, +3 bouts fenced
    M_win_rate = (M_win + 1) / (len(Mcat) + 2) # starting constant: +1 bouts won, +2 bouts fenced
    H_win_rate = H_win / (len(Hcat) + 2) # starting constant: +0 bouts won, +2 bouts fenced
    # overall_win = (L_win + 2 + M_win + 1 + H_win) / (len(Lcat) + 3 + len(Mcat) + 2 + len(Hcat) + 2)

    if L_win_rate < H_win_rate:
        L_win_rate = H_win_rate
    elif M_win_rate < H_win_rate:
        M_win_rate = H_win_rate

    L20 = len(Lcat[Lcat["Opponent Rank Category"] == 20])
    L40 = len(Lcat[Lcat["Opponent Rank Category"] == 40])

    M50 = len(Mcat[Mcat["Opponent Rank Category"] == 50])
    M70 = len(Mcat[Mcat["Opponent Rank Category"] == 70])

    L_strength = 30*(0.95)**L20*(1.05)**L40
    M_strength = 40*(0.95)**M50*(1.05)**M70
    H_strength = sum(Hcat["Opponent Rank Category"]) / len(Hcat) - 30

    L = L_strength * L_win_rate
    M = M_strength * M_win_rate
    H = H_strength * H_win_rate

    PRC = my_fencer_power*0.05

    SPI = L + M + H + PRC
    # diffSPI = (L_strength + M_strength + H_strength) * overall_win

    print(SPI) # actual is 28.031875, not 28.996039

    # print(diffSPI) doesn't match actual

spi(overall_results,20)