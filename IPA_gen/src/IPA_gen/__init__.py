# Converts English Text into IPA format. 

import gen_mods                  
print('English Text to IPA Converter\n')
userInput = input('[English]: ').split()
IPA_CMU = gen_mods.getIPA_CMU(userInput)
gen_mods.get_final(IPA_CMU)