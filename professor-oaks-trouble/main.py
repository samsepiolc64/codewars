class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype
        self.power = 'weak'
        self.pkmntypes = {'water':'wet','fire':'fiery','grass':'grassy'}
    def info(self):
        if self.level > 20: self.power = 'fair'
        if self.level > 50: self.power = 'strong'
        return f'{self.name}, a {self.pkmntypes[self.pkmntype]} and {self.power} Pokemon.'


x = PokeScan('Squirtle', 51, 'water').info()
print(x)

"""
Test.assert_equals(PokeScan('Squirtle', 0, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
Test.assert_equals(PokeScan('Charmander', 0, 'fire').info(), 'Charmander, a fiery and weak Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 0, 'grass').info(), 'Bulbasaur, a grassy and weak Pokemon.')

Test.assert_equals(PokeScan('Squirtle', 20, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
Test.assert_equals(PokeScan('Charmander', 20, 'fire').info(), 'Charmander, a fiery and weak Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 20, 'grass').info(), 'Bulbasaur, a grassy and weak Pokemon.')

Test.assert_equals(PokeScan('Squirtle', 21, 'water').info(), 'Squirtle, a wet and fair Pokemon.')
Test.assert_equals(PokeScan('Charmander', 21, 'fire').info(), 'Charmander, a fiery and fair Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 21, 'grass').info(), 'Bulbasaur, a grassy and fair Pokemon.')

Test.assert_equals(PokeScan('Squirtle', 50, 'water').info(), 'Squirtle, a wet and fair Pokemon.')
Test.assert_equals(PokeScan('Charmander', 50, 'fire').info(), 'Charmander, a fiery and fair Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 50, 'grass').info(), 'Bulbasaur, a grassy and fair Pokemon.')

Test.assert_equals(PokeScan('Squirtle', 51, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
Test.assert_equals(PokeScan('Charmander', 51, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 51, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')

Test.assert_equals(PokeScan('Squirtle', 100, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
Test.assert_equals(PokeScan('Charmander', 100, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
Test.assert_equals(PokeScan('Bulbasaur', 100, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')


"""