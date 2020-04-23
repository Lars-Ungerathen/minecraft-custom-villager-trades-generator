from random import randrange
import json

def get_spacer():
    return "},{"

def create_enchantment(id,lvl):
    return "{id:" + str(id) + ",lvl:" + str(lvl) + "}"

def create_villager_body(v_profession,v_type):
    types = ["plains","taiga","savanna","jungle","desert","snow","swamp"]
    professions = ["farmer","fisherman","shepherd","librarian","cartographer","cleric","armorer","weaponsmith","toolsmith","butcher","leatherworker","mason","nitwit"]

    return "/summon villager ~ ~1 ~ {VillagerData:{profession:" + professions[0] + ",level:99,type:" + types[0] + "},PersistenceRequired:1,Offers:{Recipes:[{"

def get_end():
    return "}]}}"

def create_buys(buy_single_item, items):
    if buy_single_item:
        return "buy:{id:" + items[0] + ",Count:" + str(items[1]) + "},"
    else:
        return "buy:{id:" + items[0] + ",Count:" + str(items[1]) + "},buyB:{id:" + items[2] + ",Count:" + str(items[3]) + "},"

def create_sales(item, count, tags):
    if len(tags) > 0:
        all_tags = ",".join(tags)
        return "sell:{id:" + item + ",Count:" + str(count) +",tag:{StoredEnchantments:[" + all_tags + "]}},maxUses:9999999"
    else:
        return "sell:{id:" + item + ",Count:" + str(count) +"},maxUses:9999999"


def create_villager(items_for_trade):
    villager = create_villager_body(randrange(5),randrange(11))

    for item_key in items_for_trade.keys():
        items_for_trade[item_key]["buys"]

        villager = villager + create_buys(True, [items_for_trade[item_key]["buys"]["item"],items_for_trade[item_key]["buys"]["count"]])

        items_enchantments = []

        for ench_key in items_for_trade[item_key]["enchantments"]:
            items_enchantments.append(create_enchantment(ench_key,items_for_trade[item_key]["enchantments"][ench_key]))
        
        villager = villager + create_sales(items_for_trade[item_key]["sells"]["item"],items_for_trade[item_key]["sells"]["count"],items_enchantments) + get_spacer()

    villager = villager + get_end()
    
    with open('../output/output.txt','w+') as output_file:
        output_file.write(villager)

def main():
    with open('../input/input.json') as input_file:
        villager_data = json.load(input_file)

    create_villager(villager_data)

if __name__ == "__main__":
    main()
