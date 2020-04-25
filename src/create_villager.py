from random import randrange
import json

def get_spacer():
    return "},{"

def create_enchantment(id,lvl):
    return "{id:" + str(id) + ",lvl:" + str(lvl) + "}"

def create_villager_body(villager_info):
    return "/summon villager ~ ~1 ~ {VillagerData:{profession:" + villager_info["profession"] + ",level:99,type:" + villager_info["type"] + "},PersistenceRequired:1,Offers:{Recipes:[{"

def get_end():
    return "}]}}"

def create_buys(buy_single_item, items):
    if buy_single_item:
        return "buy:{id:" + items[0]["item"] + ",Count:" + str(items[0]["count"]) + "},"
    else:
        return "buy:{id:" + items[0]["item"] + ",Count:" + str(items[0]["count"]) + "},buyB:{id:" + items[1]["item"] + ",Count:" + str(items[1]["count"]) + "},"


def create_sales(item, count, tags):
    if len(tags) > 0:
        all_tags = ",".join(tags)
        return "sell:{id:" + item + ",Count:" + str(count) +",tag:{StoredEnchantments:[" + all_tags + "]}},maxUses:9999999"
    else:
        return "sell:{id:" + item + ",Count:" + str(count) +"},maxUses:9999999"


def create_villager(villager_data):
    villager = create_villager_body(villager_data["info"])
    for trade in villager_data["trades"]:
        if len(trade["buys"]) > 1:
            villager = villager + create_buys(False, trade["buys"])
        else:
            villager = villager + create_buys(True, trade["buys"])

        items_enchantments = []

        for ench_key in trade["enchantments"]:
                items_enchantments.append(create_enchantment(ench_key,trade["enchantments"][ench_key]))
            
        villager = villager + create_sales(trade["sells"]["item"],trade["sells"]["count"],items_enchantments) + get_spacer()

    villager = villager + get_end()
    return villager

def main():
    all_villagers = []

    with open('../input/input.json') as input_file:
        villager_data = json.load(input_file)
        for villager in villager_data["villagers"]:
            all_villagers.append(create_villager(villager))

    for villager in all_villagers:
        with open('../output/output.txt','a+') as output_file:
            output_file.write(villager + "\n")


if __name__ == "__main__":
    main()
