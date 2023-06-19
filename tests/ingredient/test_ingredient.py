from src.models.ingredient import Ingredient  # noqa: F401, E261, E501

from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingred_presunto = Ingredient("presunto")
    assert ingred_presunto.name == "presunto"
    assert ingred_presunto.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    ingred_presunto_hash = Ingredient("presunto").__hash__()
    assert ingred_presunto_hash == hash("presunto")

    ingred_presunto_eq = Ingredient("presunto").__eq__(ingred_presunto)
    assert ingred_presunto_eq == True

    ingred_presunto_repr = Ingredient("presunto").__repr__()
    assert ingred_presunto_repr == "Ingredient('presunto')"
