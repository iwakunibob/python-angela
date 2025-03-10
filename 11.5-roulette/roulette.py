# Blackjack Game Project by Robert Laurie
import art
import random
fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
print(art.logo)
print("Welcome to the Fibonacci Roulette Game")
times = int(input("How many times do you want to spin the roulette wheel? "))
base_bet = int(input("What is your base bet? $"))
max_bet = int(input("What is the table max bet? $"))
chips = int(input("Chip Value purchased? $"))
table = int(input("Range of numbers to bet 1 to 12 or 18? "))
if table == 18:
    payout = 1
else:
    payout = 2
spin_counters = [0] * 37
bet = base_bet
fib_index = 0
for i in range(times):
    spin = random.randint(0,36)
    spin_counters[spin] += 1
    if spin >= 1 and spin <= table:
        chips += bet * payout
        bet = base_bet
        fib_index = 0
    else:
        chips -= bet
        fib_index += 1
        bet = base_bet * fibonacci[fib_index]

    print(f"{i}: Spin={spin} Chips = {chips} Next Bet = {bet} after {fib_index} loses")
    if chips <= 0 or fibonacci[fib_index] * base_bet > max_bet:
        print(f"Game over after {i} spins")
        break

