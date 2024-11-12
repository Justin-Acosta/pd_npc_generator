from data import data_dictionary
from functions import generate_npc,export_to_xlsx,import_from_xlsx

npc_dictionary = import_from_xlsx("data_dictionary.xlsx")
generate_npc(npc_dictionary)
# export_to_xlsx(data_dictionary)

