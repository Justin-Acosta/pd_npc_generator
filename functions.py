import random

def generate_npc(data_dictonary):


      weights = data_dictonary["npc_weights"]
      total_weight = sum(weights)
      weights = [weight / total_weight * 100 for weight in weights]

      npc_dictionary = {
      "npc" : random.choice(data_dictonary["npc"]),
      "tribe" : random.choices(data_dictonary["tribe"], weights=weights, k=1)[0],
      "personality" : random.choice(data_dictonary["personality"]),
      "voice" : random.choice(data_dictonary["voice"]),
      "speech" : random.choice(data_dictonary["speech"]),
      "catchphrase" : random.choice(data_dictonary["catchphrase"]),
      "quirks" : random.choice(data_dictonary["quirks"]),
      "appearance" : random.choice(data_dictonary["appearance"]),
      "statement_piece" : random.choice(data_dictonary["statement_piece"]),
      "interests" : random.choice(data_dictonary["interests"]),
      "fighting_style" : random.choice(data_dictonary["fighting_style"]),
      }

      for key,value in npc_dictionary.items():
            print(f"{key}: {value}")

def export_to_xlsx():
      pass