player_1 = True if input("Enter 'True' if your flag is raided otherwise 'False': ").strip().lower() == 'true' else False
player_2 = True if input("Enter 'True' if your flag is raided otherwise 'False': ").strip().lower() == 'true' else False
player_3 = True if input("Enter 'True' if your flag is raided otherwise 'False': ").strip().lower() == 'true' else False

winner_exist = (
  (player_1 and not player_2 and not player_3) or
  (player_2 and not player_1 and not player_3) or
  (player_3 and not player_2 and not player_1)
)
print(winner_exist)

define_winner = (
  "Winner: player_1" if player_1 == True and winner_exist and player_2 != True and player_3 != True 
  else "Winner: player_2" if player_2 == True and winner_exist and player_1 != True and player_3 != True 
  else "Winner: player_3" if player_3 == True and winner_exist and player_2 != True and player_1 != True 
  else "No clear winner"
)
print(define_winner)
