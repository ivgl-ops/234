import random
from Sourse.openfile import open_in
from Sourse import *

pizza = "пицца"
marmelade = "мармелад"
donat = "пончики"
chupa = "леденцы"
pancake = "блины"
cookie = "печенье oreo"
cupcake = "капкейки"

slad1 = "салат с креветками"
salad2 = "английский салат"
salad_with_chicken = "азиатский салат с курицей"
salad_with_cheese = "салат с сыром и курицей"
salad_Cesar = "салат цезарь"
salad_cuba = "кубинский  салат"
coleslaw = "коул слоу"
grsalad ="греческий салат"
nisuaz="салат нисуаз"
valdorfsalad="вальдорфский салат"

borch = "борщ"
cheeze_soup = "сырный суп"
chi = "щи"
gribnoy_soup = "грибной суп"
kuriniy_soup = "куриный суп с вермишелью"
rassolnik = "рассольник"
shurpa = "шурпа"
solyanka = "солянка"
soup_frikad = "суп с фрикадельками"
uha = "уха"

befstrog ="бефстроганов"
golubcy="голубцы"
gulyash="гуляш"
jambalaya="джамбалайя"
kartofel_tush="картофель тушёный"
lagman="лагман"
otbivn ="отбивная из курицы"
pasta="паста карбонара"
plov="плов"
zapekanka="запеканка мясная"

shaurma = "шаурма с курицей"
sloyki = "мини-слойки с сосисками"
guak ="гуакамоле"
jarkach="жареные кабачки"
brusketta="брускетта"
tartaletki="тарталетки"

osetinskiy = "осетинский пирог"
pirogi_pech = "пироги печеные"
hachapury = "хачапури по-аджарски"
cheburek = "чебуреки"
samsa = "самса с мясом"
maffin = "маффины"
zebra = 'пирог зебра'
sharlotka = "шарлотка"
pirog_s_kap = "пирог с капустой"

def random_recipe():
    objects = [pizza, marmelade, donat, chupa, pancake, cookie, salad2, slad1, cupcake, salad_with_chicken,
               salad_with_cheese, salad_Cesar, salad_cuba, borch, cheeze_soup,chi,gribnoy_soup,kuriniy_soup,
               rassolnik,shurpa,solyanka,soup_frikad,uha,befstrog,golubcy,gulyash,jambalaya,kartofel_tush,lagman,otbivn,
               pasta,plov,zapekanka, shaurma, sloyki, osetinskiy,pirogi_pech,hachapury,cheburek,samsa,maffin,zebra,sharlotka,
               pirog_s_kap, coleslaw, grsalad, valdorfsalad,nisuaz,guak,jarkach,brusketta,tartaletki]
    recipe = random.choice(objects)
    return recipe
