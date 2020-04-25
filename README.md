# minecraft-custom-villager-trades-generator
This tool can create custom villager trades for you :) Currently it only allows you to define enchanted books trades (without modifying the code yourself). I will update the program allow more trades without having to update stuff manually :)

# How to use this program v0.3.0-alpha
Input all desired trades into `/input/input.json`. A working example can be found at `/docs/examples`. It requires the following format and parameters (`v0.3.0-alpha`):

```json
"villagers": [
        {
            "info": {
                "profession": "<profession>",
                "type": "<minecraft_biome>"
            },
            "trades": [
                {
                    "buys": [
                        {
                            "item": "<item_name>",
                            "count": <count>
                        },
                        {
                            "item": "<item_name>",
                            "count": <count>
                        }
                    ],
                    "sells": {
                        "item": "enchanted_book",
                        "count": <count>
                    },
                    "enchantments": {
                        "<enchantment_name>": <count>
                    }
                }
            ]
        }
```

`minecraft_item_name`: The minecraft item name of the item the villager should buy / sell

`count`: The amount of items that the villager will buy / sell

`enchantment_name`: The minecraft enchantment name the item should have

`enchantment_level`: The desired enchantment level of the item

You will find the command to spawn your villager in `/output/output.txt`

Start the programm using `python3 create_villager.py`
If you have questions or found a bug, please create an issue. Thank you and have fun :-)

Examples for older versions can be found at `/docs/example/example_input<=v0.X.0-alpha`

# IMPORTANT
Currently the program will only work with villagers that sell enchanted books `villager -> trades -> sells -> item -> enchanted_book`. This will change in the future to allow more options! If you can't wait you will have to modify some parameters in the command that is generated :-)