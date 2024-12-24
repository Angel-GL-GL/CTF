def countCombinations(crystals, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for crystal in crystals:
        for i in range(crystal, target + 1):
            dp[i] += dp[i - crystal]

    return dp[target]

energy_crystals = input()  
target_energy = input()  

crystals_list = energy_crystals[1:-1].split(", ")  
crystals_list = [int(x) for x in crystals_list]  

print(countCombinations(crystals_list, int(target_energy)))
