# minecraft-custom-villager-trades-generator
This tool can create custom villager trades for you :) Currently it only allows you to define enchanted books trades (without modifying the code yourself). I will update the program allow more trades without having to update stuff manually :)

# How to use this program
Input all desired trades into `/input/input.json`. A working example can be found at `/input/example_input.json`. It requires the following format and parameters:

```
"unique_id": {
        "buys": {
            "item": "minecraft_item_name",
            "count": amount_of_item
        },
        "sells": {
            "item": "minecraft_item_name",
            "count": amount_of_item
        },
        "enchantments": {
            "enchantment_name": enchantment_level
        }
    }
```

`unique_id`: Some unique trade id. You can just use some random number and increase it by 1 for each new trade (this parameter will be removed in a future release)

`minecraft_item_name`: The minecraft item name of the item the villager should buy / sell

`count`: The amount of items that the villager will buy / sell

`enchantment_name`: The minecraft enchantment name the item should have

`enchantment_level`: The desired enchantment level of the item

You will find the command to spawn your villager in `/output/output.txt`

If you have questions or found a bug, please create an issue. Thank you and have fun :-)

# IMPORTANT
Currently the program will only work with villagers that sell enchanted books `sells -> item -> enchanted_book`. This will change in the future to allow more options! If you can't wait you will have to modify some parameters in the command that is generated :-)