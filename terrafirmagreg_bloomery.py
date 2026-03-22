num_ore = 19
mb_per_ore = 129
mb_per_ingot = 144
mb_per_coal = 144

mb = num_ore * mb_per_ore

num_ingots = int(mb / mb_per_ingot)
num_coal = int(mb / mb_per_coal)
lost_mb = mb % mb_per_ingot

print(f"With {num_ore} ore and {num_coal} coal, you will get {num_ingots} ingots and lose {lost_mb} MB of iron.")