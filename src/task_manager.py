import graphlib
from typing import Dict

builds_and_tasks = {
    "builds": [
        {
            "name": "forward_interest",
            "tasks": [
                "build_teal_leprechauns",
                "coloring_aqua_centaurs",
                "coloring_navy_golems",
                "enable_lime_leprechauns",
                "enable_lime_leprechauns",
                "enable_olive_humans",
                "enable_silver_humans",
                "write_blue_ogres",
                "write_fuchsia_golems"
            ]
        },
        {
            "name": "front_arm",
            "tasks": [
                "build_lime_golems",
                "coloring_black_goblins",
                "design_maroon_witches",
                "design_teal_golems",
                "design_yellow_centaurs",
                "map_purple_humans",
                "read_aqua_orcs",
                "read_gray_golems",
                "train_white_leprechauns",
                "upgrade_gray_humans"
            ]
        },
        {
            "name": "reach_wind",
            "tasks": [
                "bring_maroon_golems",
                "bring_silver_orcs",
                "build_blue_gorgons",
                "coloring_aqua_golems",
                "coloring_fuchsia_humans",
                "coloring_green_witches",
                "coloring_purple_fairies",
                "coloring_yellow_leprechauns",
                "create_purple_witches",
                "create_silver_gnomes",
                "enable_aqua_goblins",
                "map_gray_leprechauns",
                "map_purple_leprechauns",
                "map_yellow_gnomes",
                "read_fuchsia_orcs",
                "read_gray_humans",
                "read_yellow_gorgons",
                "train_green_centaurs",
                "train_lime_orcs",
                "train_maroon_leprechauns",
                "upgrade_olive_fairies",
                "write_purple_cyclops",
                "write_white_goblins"
            ]
        },
        {
            "name": "voice_central",
            "tasks": [
                "bring_purple_leprechauns",
                "bring_yellow_ogres",
                "build_lime_gorgons",
                "build_navy_humans",
                "coloring_aqua_leprechauns",
                "coloring_purple_centaurs",
                "coloring_teal_centaurs",
                "coloring_white_goblins",
                "design_blue_leprechauns",
                "design_green_gnomes",
                "design_green_orcs",
                "enable_aqua_fairies",
                "enable_black_witches",
                "map_gray_gorgons",
                "read_fuchsia_gorgons",
                "read_gray_ogres",
                "train_aqua_humans",
                "train_fuchsia_leprechauns",
                "train_teal_centaurs",
                "write_blue_goblins"
            ]
        },
        {
            "name": "write_beautiful",
            "tasks": [
                "bring_gray_ogres",
                "bring_green_orcs",
                "bring_silver_leprechauns",
                "bring_silver_witches",
                "bring_teal_cyclops",
                "coloring_fuchsia_orcs",
                "coloring_green_fairies",
                "coloring_maroon_gorgons",
                "coloring_navy_humans",
                "coloring_teal_gnomes",
                "coloring_white_golems",
                "coloring_yellow_centaurs",
                "create_aqua_centaurs",
                "create_navy_witches",
                "design_purple_centaurs",
                "enable_black_humans",
                "enable_black_witches",
                "enable_white_goblins",
                "map_black_goblins",
                "read_gray_leprechauns",
                "read_lime_gnomes",
                "train_white_fairies",
                "train_white_leprechauns",
                "write_maroon_humans",
                "write_purple_leprechauns"
            ]
        }
    ],
    "tasks": [
        {
            "name": "bring_aqua_humans",
            "dependencies": []
        },
        {
            "name": "bring_aqua_leprechauns",
            "dependencies": []
        },
        {
            "name": "bring_black_gnomes",
            "dependencies": []
        },
        {
            "name": "bring_black_golems",
            "dependencies": []
        },
        {
            "name": "bring_black_humans",
            "dependencies": []
        },
        {
            "name": "bring_blue_centaurs",
            "dependencies": []
        },
        {
            "name": "bring_blue_ogres",
            "dependencies": []
        },
        {
            "name": "bring_blue_orcs",
            "dependencies": []
        },
        {
            "name": "bring_fuchsia_gnomes",
            "dependencies": []
        },
        {
            "name": "bring_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "bring_fuchsia_orcs",
            "dependencies": []
        },
        {
            "name": "bring_gray_fairies",
            "dependencies": [
                "build_white_fairies",
                "coloring_fuchsia_fairies",
                "coloring_silver_fairies",
                "design_purple_fairies"
            ]
        },
        {
            "name": "bring_gray_golems",
            "dependencies": []
        },
        {
            "name": "bring_gray_humans",
            "dependencies": [
                "coloring_gray_humans",
                "train_aqua_humans",
                "train_fuchsia_humans",
                "upgrade_yellow_humans"
            ]
        },
        {
            "name": "bring_gray_ogres",
            "dependencies": [
                "coloring_lime_ogres",
                "coloring_olive_ogres",
                "design_olive_ogres",
                "enable_silver_ogres",
                "write_teal_ogres"
            ]
        },
        {
            "name": "bring_green_centaurs",
            "dependencies": []
        },
        {
            "name": "bring_green_golems",
            "dependencies": []
        },
        {
            "name": "bring_green_humans",
            "dependencies": []
        },
        {
            "name": "bring_green_ogres",
            "dependencies": []
        },
        {
            "name": "bring_green_orcs",
            "dependencies": [
                "build_silver_orcs",
                "design_blue_orcs",
                "enable_olive_orcs",
                "train_navy_orcs"
            ]
        },
        {
            "name": "bring_green_witches",
            "dependencies": []
        },
        {
            "name": "bring_lime_centaurs",
            "dependencies": []
        },
        {
            "name": "bring_lime_fairies",
            "dependencies": [
                "design_navy_fairies",
                "read_green_fairies",
                "train_olive_fairies"
            ]
        },
        {
            "name": "bring_lime_golems",
            "dependencies": []
        },
        {
            "name": "bring_maroon_golems",
            "dependencies": [
                "build_black_golems",
                "design_purple_golems",
                "map_gray_golems",
                "read_teal_golems"
            ]
        },
        {
            "name": "bring_maroon_leprechauns",
            "dependencies": []
        },
        {
            "name": "bring_olive_centaurs",
            "dependencies": [
                "enable_yellow_centaurs"
            ]
        },
        {
            "name": "bring_olive_leprechauns",
            "dependencies": []
        },
        {
            "name": "bring_purple_fairies",
            "dependencies": []
        },
        {
            "name": "bring_purple_goblins",
            "dependencies": []
        },
        {
            "name": "bring_purple_humans",
            "dependencies": [
                "enable_fuchsia_humans",
                "read_silver_humans",
                "upgrade_lime_humans"
            ]
        },
        {
            "name": "bring_purple_leprechauns",
            "dependencies": [
                "bring_yellow_leprechauns",
                "design_yellow_leprechauns",
                "map_navy_leprechauns"
            ]
        },
        {
            "name": "bring_silver_leprechauns",
            "dependencies": [
                "read_fuchsia_leprechauns"
            ]
        },
        {
            "name": "bring_silver_orcs",
            "dependencies": []
        },
        {
            "name": "bring_silver_witches",
            "dependencies": [
                "map_green_witches"
            ]
        },
        {
            "name": "bring_teal_cyclops",
            "dependencies": [
                "enable_teal_cyclops"
            ]
        },
        {
            "name": "bring_teal_fairies",
            "dependencies": []
        },
        {
            "name": "bring_teal_humans",
            "dependencies": []
        },
        {
            "name": "bring_white_fairies",
            "dependencies": [
                "coloring_gray_fairies"
            ]
        },
        {
            "name": "bring_white_gnomes",
            "dependencies": []
        },
        {
            "name": "bring_white_gorgons",
            "dependencies": []
        },
        {
            "name": "bring_yellow_humans",
            "dependencies": []
        },
        {
            "name": "bring_yellow_leprechauns",
            "dependencies": [
                "build_white_leprechauns",
                "coloring_yellow_leprechauns",
                "enable_olive_leprechauns",
                "write_purple_leprechauns"
            ]
        },
        {
            "name": "bring_yellow_ogres",
            "dependencies": [
                "build_aqua_ogres",
                "coloring_purple_ogres",
                "create_olive_ogres",
                "design_navy_ogres"
            ]
        },
        {
            "name": "build_aqua_centaurs",
            "dependencies": []
        },
        {
            "name": "build_aqua_ogres",
            "dependencies": [
                "create_gray_ogres",
                "write_green_ogres"
            ]
        },
        {
            "name": "build_aqua_orcs",
            "dependencies": []
        },
        {
            "name": "build_aqua_witches",
            "dependencies": []
        },
        {
            "name": "build_black_goblins",
            "dependencies": []
        },
        {
            "name": "build_black_golems",
            "dependencies": []
        },
        {
            "name": "build_black_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_black_ogres",
            "dependencies": []
        },
        {
            "name": "build_blue_centaurs",
            "dependencies": []
        },
        {
            "name": "build_blue_gnomes",
            "dependencies": []
        },
        {
            "name": "build_blue_gorgons",
            "dependencies": [
                "coloring_lime_gorgons",
                "create_blue_gorgons",
                "enable_purple_gorgons",
                "upgrade_purple_gorgons"
            ]
        },
        {
            "name": "build_blue_witches",
            "dependencies": []
        },
        {
            "name": "build_fuchsia_fairies",
            "dependencies": [
                "bring_purple_fairies",
                "build_olive_fairies",
                "coloring_silver_fairies",
                "read_teal_fairies",
                "train_green_fairies"
            ]
        },
        {
            "name": "build_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "build_fuchsia_humans",
            "dependencies": [
                "bring_yellow_humans",
                "create_aqua_humans",
                "create_fuchsia_humans",
                "create_silver_humans",
                "train_white_humans"
            ]
        },
        {
            "name": "build_fuchsia_witches",
            "dependencies": [
                "upgrade_yellow_witches"
            ]
        },
        {
            "name": "build_gray_golems",
            "dependencies": [
                "bring_lime_golems",
                "train_blue_golems",
                "train_fuchsia_golems",
                "upgrade_purple_golems"
            ]
        },
        {
            "name": "build_gray_gorgons",
            "dependencies": []
        },
        {
            "name": "build_gray_humans",
            "dependencies": []
        },
        {
            "name": "build_gray_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_gray_witches",
            "dependencies": [
                "coloring_maroon_witches",
                "upgrade_fuchsia_witches"
            ]
        },
        {
            "name": "build_green_gnomes",
            "dependencies": []
        },
        {
            "name": "build_green_golems",
            "dependencies": [
                "design_fuchsia_golems",
                "enable_fuchsia_golems",
                "read_fuchsia_golems",
                "write_maroon_golems"
            ]
        },
        {
            "name": "build_lime_golems",
            "dependencies": []
        },
        {
            "name": "build_lime_gorgons",
            "dependencies": [
                "train_white_gorgons",
                "write_navy_gorgons"
            ]
        },
        {
            "name": "build_maroon_goblins",
            "dependencies": []
        },
        {
            "name": "build_maroon_gorgons",
            "dependencies": []
        },
        {
            "name": "build_maroon_humans",
            "dependencies": []
        },
        {
            "name": "build_maroon_orcs",
            "dependencies": []
        },
        {
            "name": "build_navy_humans",
            "dependencies": [
                "create_black_humans"
            ]
        },
        {
            "name": "build_olive_centaurs",
            "dependencies": []
        },
        {
            "name": "build_olive_fairies",
            "dependencies": []
        },
        {
            "name": "build_olive_gnomes",
            "dependencies": []
        },
        {
            "name": "build_olive_goblins",
            "dependencies": []
        },
        {
            "name": "build_olive_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_olive_witches",
            "dependencies": []
        },
        {
            "name": "build_purple_goblins",
            "dependencies": []
        },
        {
            "name": "build_purple_humans",
            "dependencies": []
        },
        {
            "name": "build_purple_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_silver_centaurs",
            "dependencies": []
        },
        {
            "name": "build_silver_gnomes",
            "dependencies": []
        },
        {
            "name": "build_silver_goblins",
            "dependencies": [
                "design_fuchsia_goblins",
                "read_fuchsia_goblins"
            ]
        },
        {
            "name": "build_silver_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_silver_orcs",
            "dependencies": []
        },
        {
            "name": "build_teal_goblins",
            "dependencies": []
        },
        {
            "name": "build_teal_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_teal_orcs",
            "dependencies": [
                "read_teal_orcs"
            ]
        },
        {
            "name": "build_white_fairies",
            "dependencies": []
        },
        {
            "name": "build_white_leprechauns",
            "dependencies": []
        },
        {
            "name": "build_white_witches",
            "dependencies": []
        },
        {
            "name": "build_yellow_ogres",
            "dependencies": []
        },
        {
            "name": "coloring_aqua_centaurs",
            "dependencies": [
                "bring_olive_centaurs",
                "create_maroon_centaurs",
                "create_olive_centaurs"
            ]
        },
        {
            "name": "coloring_aqua_gnomes",
            "dependencies": []
        },
        {
            "name": "coloring_aqua_golems",
            "dependencies": []
        },
        {
            "name": "coloring_aqua_gorgons",
            "dependencies": []
        },
        {
            "name": "coloring_aqua_leprechauns",
            "dependencies": [
                "map_teal_leprechauns",
                "write_purple_leprechauns"
            ]
        },
        {
            "name": "coloring_black_centaurs",
            "dependencies": [
                "map_maroon_centaurs",
                "train_blue_centaurs"
            ]
        },
        {
            "name": "coloring_black_goblins",
            "dependencies": [
                "build_silver_goblins",
                "build_teal_goblins",
                "create_lime_goblins",
                "design_olive_goblins",
                "map_gray_goblins"
            ]
        },
        {
            "name": "coloring_black_ogres",
            "dependencies": []
        },
        {
            "name": "coloring_black_orcs",
            "dependencies": []
        },
        {
            "name": "coloring_blue_gnomes",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_fairies",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_gnomes",
            "dependencies": [
                "enable_silver_gnomes"
            ]
        },
        {
            "name": "coloring_fuchsia_goblins",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_gorgons",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "coloring_fuchsia_leprechauns",
            "dependencies": [
                "build_black_leprechauns",
                "coloring_purple_leprechauns",
                "design_teal_leprechauns",
                "map_white_leprechauns",
                "write_navy_leprechauns"
            ]
        },
        {
            "name": "coloring_fuchsia_orcs",
            "dependencies": [
                "build_aqua_orcs",
                "create_navy_orcs",
                "design_fuchsia_orcs",
                "enable_fuchsia_orcs"
            ]
        },
        {
            "name": "coloring_gray_centaurs",
            "dependencies": []
        },
        {
            "name": "coloring_gray_fairies",
            "dependencies": []
        },
        {
            "name": "coloring_gray_humans",
            "dependencies": []
        },
        {
            "name": "coloring_gray_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_green_centaurs",
            "dependencies": [
                "build_aqua_centaurs",
                "create_silver_centaurs",
                "read_silver_centaurs",
                "write_aqua_centaurs",
                "write_maroon_centaurs"
            ]
        },
        {
            "name": "coloring_green_fairies",
            "dependencies": [
                "build_fuchsia_fairies",
                "coloring_white_fairies",
                "upgrade_blue_fairies"
            ]
        },
        {
            "name": "coloring_green_humans",
            "dependencies": []
        },
        {
            "name": "coloring_green_witches",
            "dependencies": [
                "build_gray_witches",
                "create_white_witches",
                "read_fuchsia_witches",
                "write_maroon_witches"
            ]
        },
        {
            "name": "coloring_lime_fairies",
            "dependencies": []
        },
        {
            "name": "coloring_lime_goblins",
            "dependencies": [
                "build_black_goblins",
                "build_olive_goblins",
                "design_white_goblins",
                "train_purple_goblins",
                "upgrade_olive_goblins"
            ]
        },
        {
            "name": "coloring_lime_golems",
            "dependencies": []
        },
        {
            "name": "coloring_lime_gorgons",
            "dependencies": [
                "coloring_silver_gorgons",
                "upgrade_silver_gorgons"
            ]
        },
        {
            "name": "coloring_lime_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_lime_ogres",
            "dependencies": [
                "read_fuchsia_ogres",
                "upgrade_green_ogres",
                "write_yellow_ogres"
            ]
        },
        {
            "name": "coloring_lime_orcs",
            "dependencies": []
        },
        {
            "name": "coloring_maroon_gnomes",
            "dependencies": [
                "build_olive_gnomes",
                "enable_lime_gnomes",
                "train_olive_gnomes"
            ]
        },
        {
            "name": "coloring_maroon_gorgons",
            "dependencies": [
                "read_silver_gorgons"
            ]
        },
        {
            "name": "coloring_maroon_humans",
            "dependencies": [
                "bring_black_humans",
                "coloring_purple_humans",
                "enable_lime_humans",
                "enable_maroon_humans",
                "enable_purple_humans"
            ]
        },
        {
            "name": "coloring_maroon_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_maroon_witches",
            "dependencies": []
        },
        {
            "name": "coloring_navy_centaurs",
            "dependencies": []
        },
        {
            "name": "coloring_navy_golems",
            "dependencies": [
                "coloring_aqua_golems"
            ]
        },
        {
            "name": "coloring_navy_humans",
            "dependencies": [
                "coloring_maroon_humans",
                "train_yellow_humans"
            ]
        },
        {
            "name": "coloring_olive_centaurs",
            "dependencies": []
        },
        {
            "name": "coloring_olive_gnomes",
            "dependencies": []
        },
        {
            "name": "coloring_olive_goblins",
            "dependencies": [
                "bring_purple_goblins",
                "coloring_fuchsia_goblins",
                "enable_maroon_goblins",
                "upgrade_lime_goblins",
                "write_green_goblins"
            ]
        },
        {
            "name": "coloring_olive_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_olive_ogres",
            "dependencies": [
                "read_purple_ogres",
                "train_aqua_ogres"
            ]
        },
        {
            "name": "coloring_purple_centaurs",
            "dependencies": [
                "coloring_black_centaurs",
                "map_olive_centaurs"
            ]
        },
        {
            "name": "coloring_purple_fairies",
            "dependencies": [
                "bring_lime_fairies",
                "bring_white_fairies",
                "write_olive_fairies"
            ]
        },
        {
            "name": "coloring_purple_golems",
            "dependencies": []
        },
        {
            "name": "coloring_purple_humans",
            "dependencies": []
        },
        {
            "name": "coloring_purple_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_purple_ogres",
            "dependencies": [
                "write_gray_ogres"
            ]
        },
        {
            "name": "coloring_purple_witches",
            "dependencies": []
        },
        {
            "name": "coloring_silver_fairies",
            "dependencies": []
        },
        {
            "name": "coloring_silver_gnomes",
            "dependencies": []
        },
        {
            "name": "coloring_silver_golems",
            "dependencies": [
                "write_teal_golems",
                "write_white_golems"
            ]
        },
        {
            "name": "coloring_silver_gorgons",
            "dependencies": []
        },
        {
            "name": "coloring_silver_humans",
            "dependencies": []
        },
        {
            "name": "coloring_silver_leprechauns",
            "dependencies": []
        },
        {
            "name": "coloring_teal_centaurs",
            "dependencies": [
                "enable_blue_centaurs",
                "map_olive_centaurs",
                "map_teal_centaurs",
                "read_silver_centaurs"
            ]
        },
        {
            "name": "coloring_teal_gnomes",
            "dependencies": [
                "design_blue_gnomes",
                "design_fuchsia_gnomes",
                "enable_maroon_gnomes",
                "enable_navy_gnomes",
                "read_white_gnomes"
            ]
        },
        {
            "name": "coloring_teal_golems",
            "dependencies": []
        },
        {
            "name": "coloring_teal_humans",
            "dependencies": [
                "coloring_green_humans",
                "write_lime_humans"
            ]
        },
        {
            "name": "coloring_teal_witches",
            "dependencies": [
                "read_purple_witches",
                "train_silver_witches"
            ]
        },
        {
            "name": "coloring_white_centaurs",
            "dependencies": []
        },
        {
            "name": "coloring_white_fairies",
            "dependencies": [
                "bring_teal_fairies",
                "build_white_fairies",
                "map_green_fairies",
                "upgrade_white_fairies"
            ]
        },
        {
            "name": "coloring_white_gnomes",
            "dependencies": [
                "build_blue_gnomes",
                "coloring_yellow_gnomes",
                "design_black_gnomes",
                "design_olive_gnomes",
                "upgrade_purple_gnomes"
            ]
        },
        {
            "name": "coloring_white_goblins",
            "dependencies": []
        },
        {
            "name": "coloring_white_golems",
            "dependencies": [
                "build_gray_golems",
                "create_white_golems",
                "design_fuchsia_golems",
                "design_purple_golems",
                "write_white_golems"
            ]
        },
        {
            "name": "coloring_white_gorgons",
            "dependencies": []
        },
        {
            "name": "coloring_white_humans",
            "dependencies": []
        },
        {
            "name": "coloring_yellow_centaurs",
            "dependencies": [
                "create_aqua_centaurs",
                "create_black_centaurs",
                "train_gray_centaurs"
            ]
        },
        {
            "name": "coloring_yellow_gnomes",
            "dependencies": []
        },
        {
            "name": "coloring_yellow_gorgons",
            "dependencies": []
        },
        {
            "name": "coloring_yellow_leprechauns",
            "dependencies": []
        },
        {
            "name": "create_aqua_centaurs",
            "dependencies": []
        },
        {
            "name": "create_aqua_humans",
            "dependencies": []
        },
        {
            "name": "create_aqua_leprechauns",
            "dependencies": []
        },
        {
            "name": "create_black_centaurs",
            "dependencies": [
                "bring_green_centaurs",
                "create_navy_centaurs",
                "map_yellow_centaurs",
                "read_maroon_centaurs",
                "train_yellow_centaurs"
            ]
        },
        {
            "name": "create_black_fairies",
            "dependencies": []
        },
        {
            "name": "create_black_gnomes",
            "dependencies": []
        },
        {
            "name": "create_black_humans",
            "dependencies": [
                "enable_green_humans",
                "enable_lime_humans",
                "write_silver_humans"
            ]
        },
        {
            "name": "create_black_leprechauns",
            "dependencies": []
        },
        {
            "name": "create_blue_centaurs",
            "dependencies": [
                "create_white_centaurs",
                "design_teal_centaurs",
                "read_lime_centaurs"
            ]
        },
        {
            "name": "create_blue_golems",
            "dependencies": []
        },
        {
            "name": "create_blue_gorgons",
            "dependencies": []
        },
        {
            "name": "create_blue_orcs",
            "dependencies": []
        },
        {
            "name": "create_fuchsia_centaurs",
            "dependencies": []
        },
        {
            "name": "create_fuchsia_gnomes",
            "dependencies": []
        },
        {
            "name": "create_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "create_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "create_gray_centaurs",
            "dependencies": [
                "read_aqua_centaurs",
                "read_yellow_centaurs",
                "upgrade_teal_centaurs"
            ]
        },
        {
            "name": "create_gray_goblins",
            "dependencies": []
        },
        {
            "name": "create_gray_ogres",
            "dependencies": []
        },
        {
            "name": "create_green_centaurs",
            "dependencies": []
        },
        {
            "name": "create_green_humans",
            "dependencies": [
                "bring_green_humans"
            ]
        },
        {
            "name": "create_green_orcs",
            "dependencies": []
        },
        {
            "name": "create_lime_fairies",
            "dependencies": []
        },
        {
            "name": "create_lime_goblins",
            "dependencies": []
        },
        {
            "name": "create_maroon_centaurs",
            "dependencies": [
                "coloring_white_centaurs",
                "create_teal_centaurs",
                "design_lime_centaurs",
                "train_purple_centaurs",
                "upgrade_navy_centaurs"
            ]
        },
        {
            "name": "create_maroon_ogres",
            "dependencies": []
        },
        {
            "name": "create_navy_centaurs",
            "dependencies": []
        },
        {
            "name": "create_navy_gnomes",
            "dependencies": [
                "bring_black_gnomes",
                "build_silver_gnomes",
                "coloring_blue_gnomes",
                "coloring_silver_gnomes",
                "map_maroon_gnomes"
            ]
        },
        {
            "name": "create_navy_golems",
            "dependencies": [
                "coloring_lime_golems",
                "design_gray_golems",
                "enable_silver_golems",
                "map_aqua_golems",
                "upgrade_aqua_golems"
            ]
        },
        {
            "name": "create_navy_leprechauns",
            "dependencies": []
        },
        {
            "name": "create_navy_orcs",
            "dependencies": [
                "bring_blue_orcs"
            ]
        },
        {
            "name": "create_navy_witches",
            "dependencies": []
        },
        {
            "name": "create_olive_centaurs",
            "dependencies": [
                "bring_blue_centaurs",
                "read_yellow_centaurs",
                "upgrade_navy_centaurs"
            ]
        },
        {
            "name": "create_olive_goblins",
            "dependencies": [
                "build_olive_goblins",
                "design_purple_goblins",
                "map_olive_goblins",
                "train_teal_goblins",
                "write_silver_goblins"
            ]
        },
        {
            "name": "create_olive_golems",
            "dependencies": []
        },
        {
            "name": "create_olive_humans",
            "dependencies": []
        },
        {
            "name": "create_olive_ogres",
            "dependencies": [
                "map_maroon_ogres",
                "read_navy_ogres"
            ]
        },
        {
            "name": "create_purple_gnomes",
            "dependencies": []
        },
        {
            "name": "create_purple_goblins",
            "dependencies": []
        },
        {
            "name": "create_purple_humans",
            "dependencies": [
                "build_maroon_humans",
                "write_silver_humans",
                "write_white_humans"
            ]
        },
        {
            "name": "create_purple_orcs",
            "dependencies": []
        },
        {
            "name": "create_purple_witches",
            "dependencies": [
                "bring_green_witches",
                "design_teal_witches",
                "upgrade_aqua_witches"
            ]
        },
        {
            "name": "create_silver_centaurs",
            "dependencies": []
        },
        {
            "name": "create_silver_gnomes",
            "dependencies": [
                "coloring_olive_gnomes",
                "create_navy_gnomes",
                "design_silver_gnomes",
                "enable_green_gnomes",
                "enable_maroon_gnomes"
            ]
        },
        {
            "name": "create_silver_goblins",
            "dependencies": []
        },
        {
            "name": "create_silver_golems",
            "dependencies": [
                "map_olive_golems"
            ]
        },
        {
            "name": "create_silver_humans",
            "dependencies": []
        },
        {
            "name": "create_silver_ogres",
            "dependencies": []
        },
        {
            "name": "create_silver_orcs",
            "dependencies": []
        },
        {
            "name": "create_teal_centaurs",
            "dependencies": []
        },
        {
            "name": "create_teal_gnomes",
            "dependencies": []
        },
        {
            "name": "create_teal_goblins",
            "dependencies": [
                "upgrade_navy_goblins",
                "write_navy_goblins"
            ]
        },
        {
            "name": "create_teal_golems",
            "dependencies": []
        },
        {
            "name": "create_teal_gorgons",
            "dependencies": []
        },
        {
            "name": "create_teal_ogres",
            "dependencies": []
        },
        {
            "name": "create_teal_witches",
            "dependencies": []
        },
        {
            "name": "create_white_centaurs",
            "dependencies": []
        },
        {
            "name": "create_white_fairies",
            "dependencies": []
        },
        {
            "name": "create_white_gnomes",
            "dependencies": [
                "map_gray_gnomes",
                "upgrade_maroon_gnomes",
                "write_purple_gnomes"
            ]
        },
        {
            "name": "create_white_goblins",
            "dependencies": []
        },
        {
            "name": "create_white_golems",
            "dependencies": [
                "coloring_lime_golems",
                "write_fuchsia_golems"
            ]
        },
        {
            "name": "create_white_humans",
            "dependencies": []
        },
        {
            "name": "create_white_witches",
            "dependencies": [
                "build_white_witches",
                "design_purple_witches",
                "read_silver_witches",
                "read_teal_witches"
            ]
        },
        {
            "name": "create_yellow_witches",
            "dependencies": []
        },
        {
            "name": "design_aqua_fairies",
            "dependencies": [
                "coloring_lime_fairies",
                "create_lime_fairies",
                "design_lime_fairies",
                "upgrade_fuchsia_fairies"
            ]
        },
        {
            "name": "design_aqua_leprechauns",
            "dependencies": [
                "bring_olive_leprechauns",
                "coloring_lime_leprechauns",
                "create_aqua_leprechauns",
                "write_lime_leprechauns"
            ]
        },
        {
            "name": "design_black_gnomes",
            "dependencies": []
        },
        {
            "name": "design_black_goblins",
            "dependencies": []
        },
        {
            "name": "design_black_gorgons",
            "dependencies": []
        },
        {
            "name": "design_blue_cyclops",
            "dependencies": []
        },
        {
            "name": "design_blue_gnomes",
            "dependencies": [
                "build_green_gnomes",
                "design_teal_gnomes",
                "read_navy_gnomes"
            ]
        },
        {
            "name": "design_blue_humans",
            "dependencies": [
                "create_white_humans",
                "upgrade_green_humans"
            ]
        },
        {
            "name": "design_blue_leprechauns",
            "dependencies": []
        },
        {
            "name": "design_blue_orcs",
            "dependencies": [
                "bring_fuchsia_orcs",
                "design_navy_orcs",
                "upgrade_silver_orcs"
            ]
        },
        {
            "name": "design_fuchsia_gnomes",
            "dependencies": [
                "enable_black_gnomes",
                "map_aqua_gnomes",
                "upgrade_teal_gnomes"
            ]
        },
        {
            "name": "design_fuchsia_goblins",
            "dependencies": []
        },
        {
            "name": "design_fuchsia_golems",
            "dependencies": [
                "bring_black_golems",
                "design_gray_golems",
                "design_yellow_golems",
                "upgrade_green_golems",
                "upgrade_lime_golems"
            ]
        },
        {
            "name": "design_fuchsia_gorgons",
            "dependencies": []
        },
        {
            "name": "design_fuchsia_orcs",
            "dependencies": [
                "coloring_lime_orcs",
                "enable_purple_orcs",
                "read_olive_orcs"
            ]
        },
        {
            "name": "design_fuchsia_witches",
            "dependencies": []
        },
        {
            "name": "design_gray_goblins",
            "dependencies": []
        },
        {
            "name": "design_gray_golems",
            "dependencies": []
        },
        {
            "name": "design_gray_leprechauns",
            "dependencies": []
        },
        {
            "name": "design_green_centaurs",
            "dependencies": []
        },
        {
            "name": "design_green_gnomes",
            "dependencies": [
                "coloring_fuchsia_gnomes",
                "design_white_gnomes",
                "upgrade_gray_gnomes",
                "upgrade_purple_gnomes",
                "upgrade_yellow_gnomes"
            ]
        },
        {
            "name": "design_green_ogres",
            "dependencies": []
        },
        {
            "name": "design_green_orcs",
            "dependencies": [
                "build_teal_orcs",
                "enable_silver_orcs"
            ]
        },
        {
            "name": "design_lime_centaurs",
            "dependencies": []
        },
        {
            "name": "design_lime_fairies",
            "dependencies": []
        },
        {
            "name": "design_lime_humans",
            "dependencies": []
        },
        {
            "name": "design_maroon_golems",
            "dependencies": [
                "coloring_aqua_golems",
                "create_fuchsia_golems",
                "train_fuchsia_golems"
            ]
        },
        {
            "name": "design_maroon_witches",
            "dependencies": [
                "write_teal_witches"
            ]
        },
        {
            "name": "design_navy_fairies",
            "dependencies": []
        },
        {
            "name": "design_navy_humans",
            "dependencies": [
                "coloring_navy_humans"
            ]
        },
        {
            "name": "design_navy_ogres",
            "dependencies": [
                "coloring_black_ogres"
            ]
        },
        {
            "name": "design_navy_orcs",
            "dependencies": []
        },
        {
            "name": "design_olive_gnomes",
            "dependencies": []
        },
        {
            "name": "design_olive_goblins",
            "dependencies": [
                "create_silver_goblins",
                "design_gray_goblins"
            ]
        },
        {
            "name": "design_olive_ogres",
            "dependencies": []
        },
        {
            "name": "design_purple_centaurs",
            "dependencies": [
                "create_gray_centaurs",
                "read_navy_centaurs"
            ]
        },
        {
            "name": "design_purple_fairies",
            "dependencies": []
        },
        {
            "name": "design_purple_goblins",
            "dependencies": []
        },
        {
            "name": "design_purple_golems",
            "dependencies": [
                "coloring_teal_golems",
                "read_aqua_golems"
            ]
        },
        {
            "name": "design_purple_witches",
            "dependencies": []
        },
        {
            "name": "design_silver_gnomes",
            "dependencies": [
                "create_fuchsia_gnomes",
                "map_maroon_gnomes",
                "upgrade_yellow_gnomes"
            ]
        },
        {
            "name": "design_silver_golems",
            "dependencies": []
        },
        {
            "name": "design_silver_gorgons",
            "dependencies": []
        },
        {
            "name": "design_teal_centaurs",
            "dependencies": []
        },
        {
            "name": "design_teal_gnomes",
            "dependencies": []
        },
        {
            "name": "design_teal_goblins",
            "dependencies": []
        },
        {
            "name": "design_teal_golems",
            "dependencies": [
                "coloring_silver_golems",
                "enable_white_golems",
                "train_maroon_golems"
            ]
        },
        {
            "name": "design_teal_leprechauns",
            "dependencies": []
        },
        {
            "name": "design_teal_witches",
            "dependencies": []
        },
        {
            "name": "design_white_fairies",
            "dependencies": [
                "enable_gray_fairies"
            ]
        },
        {
            "name": "design_white_gnomes",
            "dependencies": [
                "enable_teal_gnomes"
            ]
        },
        {
            "name": "design_white_goblins",
            "dependencies": []
        },
        {
            "name": "design_white_ogres",
            "dependencies": []
        },
        {
            "name": "design_white_witches",
            "dependencies": [
                "coloring_purple_witches",
                "create_teal_witches",
                "enable_black_witches",
                "train_maroon_witches",
                "train_navy_witches"
            ]
        },
        {
            "name": "design_yellow_centaurs",
            "dependencies": [
                "create_blue_centaurs",
                "map_fuchsia_centaurs",
                "read_lime_centaurs",
                "upgrade_aqua_centaurs"
            ]
        },
        {
            "name": "design_yellow_golems",
            "dependencies": [
                "coloring_purple_golems",
                "design_silver_golems",
                "read_teal_golems",
                "train_gray_golems",
                "train_maroon_golems"
            ]
        },
        {
            "name": "design_yellow_leprechauns",
            "dependencies": [
                "build_gray_leprechauns",
                "create_navy_leprechauns"
            ]
        },
        {
            "name": "enable_aqua_fairies",
            "dependencies": [
                "design_white_fairies",
                "read_fuchsia_fairies"
            ]
        },
        {
            "name": "enable_aqua_goblins",
            "dependencies": [
                "enable_blue_goblins",
                "train_olive_goblins",
                "upgrade_maroon_goblins",
                "write_fuchsia_goblins"
            ]
        },
        {
            "name": "enable_aqua_witches",
            "dependencies": []
        },
        {
            "name": "enable_black_gnomes",
            "dependencies": []
        },
        {
            "name": "enable_black_humans",
            "dependencies": [
                "bring_gray_humans",
                "bring_purple_humans",
                "design_navy_humans",
                "train_olive_humans"
            ]
        },
        {
            "name": "enable_black_witches",
            "dependencies": [
                "build_fuchsia_witches",
                "coloring_teal_witches",
                "enable_lime_witches",
                "enable_navy_witches",
                "write_white_witches"
            ]
        },
        {
            "name": "enable_blue_centaurs",
            "dependencies": []
        },
        {
            "name": "enable_blue_goblins",
            "dependencies": [
                "create_gray_goblins"
            ]
        },
        {
            "name": "enable_blue_humans",
            "dependencies": []
        },
        {
            "name": "enable_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "enable_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "enable_fuchsia_ogres",
            "dependencies": [
                "bring_blue_ogres",
                "design_white_ogres",
                "train_green_ogres",
                "upgrade_aqua_ogres",
                "write_silver_ogres"
            ]
        },
        {
            "name": "enable_fuchsia_orcs",
            "dependencies": [
                "create_blue_orcs",
                "write_fuchsia_orcs"
            ]
        },
        {
            "name": "enable_gray_fairies",
            "dependencies": []
        },
        {
            "name": "enable_gray_gorgons",
            "dependencies": [
                "build_gray_gorgons",
                "build_maroon_gorgons",
                "coloring_white_gorgons",
                "design_silver_gorgons",
                "write_gray_gorgons"
            ]
        },
        {
            "name": "enable_green_gnomes",
            "dependencies": [
                "create_teal_gnomes"
            ]
        },
        {
            "name": "enable_green_humans",
            "dependencies": []
        },
        {
            "name": "enable_green_leprechauns",
            "dependencies": [
                "build_silver_leprechauns",
                "coloring_silver_leprechauns",
                "train_white_leprechauns",
                "write_white_leprechauns"
            ]
        },
        {
            "name": "enable_lime_gnomes",
            "dependencies": []
        },
        {
            "name": "enable_lime_goblins",
            "dependencies": []
        },
        {
            "name": "enable_lime_humans",
            "dependencies": []
        },
        {
            "name": "enable_lime_leprechauns",
            "dependencies": [
                "map_olive_leprechauns"
            ]
        },
        {
            "name": "enable_lime_witches",
            "dependencies": [
                "build_blue_witches",
                "create_yellow_witches",
                "enable_purple_witches",
                "write_black_witches",
                "write_green_witches"
            ]
        },
        {
            "name": "enable_maroon_gnomes",
            "dependencies": [
                "bring_white_gnomes"
            ]
        },
        {
            "name": "enable_maroon_goblins",
            "dependencies": []
        },
        {
            "name": "enable_maroon_humans",
            "dependencies": []
        },
        {
            "name": "enable_maroon_orcs",
            "dependencies": [
                "bring_green_orcs",
                "create_silver_orcs",
                "design_green_orcs"
            ]
        },
        {
            "name": "enable_navy_gnomes",
            "dependencies": []
        },
        {
            "name": "enable_navy_witches",
            "dependencies": []
        },
        {
            "name": "enable_olive_centaurs",
            "dependencies": [
                "build_blue_centaurs",
                "coloring_navy_centaurs",
                "create_olive_centaurs"
            ]
        },
        {
            "name": "enable_olive_humans",
            "dependencies": [
                "create_aqua_humans"
            ]
        },
        {
            "name": "enable_olive_leprechauns",
            "dependencies": []
        },
        {
            "name": "enable_olive_orcs",
            "dependencies": [
                "create_green_orcs",
                "create_purple_orcs",
                "train_teal_orcs"
            ]
        },
        {
            "name": "enable_purple_gnomes",
            "dependencies": [
                "bring_fuchsia_gnomes",
                "create_purple_gnomes",
                "train_green_gnomes"
            ]
        },
        {
            "name": "enable_purple_gorgons",
            "dependencies": [
                "coloring_silver_gorgons",
                "coloring_yellow_gorgons",
                "create_teal_gorgons",
                "design_black_gorgons",
                "write_teal_gorgons"
            ]
        },
        {
            "name": "enable_purple_humans",
            "dependencies": []
        },
        {
            "name": "enable_purple_orcs",
            "dependencies": []
        },
        {
            "name": "enable_purple_witches",
            "dependencies": []
        },
        {
            "name": "enable_silver_centaurs",
            "dependencies": []
        },
        {
            "name": "enable_silver_gnomes",
            "dependencies": []
        },
        {
            "name": "enable_silver_goblins",
            "dependencies": []
        },
        {
            "name": "enable_silver_golems",
            "dependencies": []
        },
        {
            "name": "enable_silver_humans",
            "dependencies": [
                "create_purple_humans",
                "train_white_humans",
                "write_teal_humans"
            ]
        },
        {
            "name": "enable_silver_ogres",
            "dependencies": [
                "create_silver_ogres",
                "create_teal_ogres",
                "upgrade_black_ogres",
                "write_green_ogres"
            ]
        },
        {
            "name": "enable_silver_orcs",
            "dependencies": [
                "build_maroon_orcs",
                "train_black_orcs"
            ]
        },
        {
            "name": "enable_teal_cyclops",
            "dependencies": [
                "design_blue_cyclops",
                "write_aqua_cyclops"
            ]
        },
        {
            "name": "enable_teal_gnomes",
            "dependencies": []
        },
        {
            "name": "enable_teal_goblins",
            "dependencies": [
                "create_purple_goblins",
                "map_blue_goblins",
                "map_gray_goblins",
                "read_lime_goblins",
                "read_navy_goblins"
            ]
        },
        {
            "name": "enable_teal_gorgons",
            "dependencies": [
                "upgrade_teal_gorgons"
            ]
        },
        {
            "name": "enable_teal_leprechauns",
            "dependencies": []
        },
        {
            "name": "enable_white_goblins",
            "dependencies": []
        },
        {
            "name": "enable_white_golems",
            "dependencies": []
        },
        {
            "name": "enable_white_witches",
            "dependencies": []
        },
        {
            "name": "enable_yellow_centaurs",
            "dependencies": []
        },
        {
            "name": "enable_yellow_humans",
            "dependencies": []
        },
        {
            "name": "map_aqua_gnomes",
            "dependencies": []
        },
        {
            "name": "map_aqua_golems",
            "dependencies": []
        },
        {
            "name": "map_aqua_humans",
            "dependencies": []
        },
        {
            "name": "map_aqua_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_black_goblins",
            "dependencies": [
                "coloring_lime_goblins",
                "create_olive_goblins",
                "create_teal_goblins",
                "enable_teal_goblins",
                "train_teal_goblins"
            ]
        },
        {
            "name": "map_black_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_blue_goblins",
            "dependencies": []
        },
        {
            "name": "map_blue_golems",
            "dependencies": []
        },
        {
            "name": "map_fuchsia_centaurs",
            "dependencies": []
        },
        {
            "name": "map_fuchsia_gnomes",
            "dependencies": []
        },
        {
            "name": "map_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "map_gray_fairies",
            "dependencies": []
        },
        {
            "name": "map_gray_gnomes",
            "dependencies": []
        },
        {
            "name": "map_gray_goblins",
            "dependencies": [
                "build_maroon_goblins",
                "build_purple_goblins",
                "coloring_white_goblins",
                "upgrade_maroon_goblins"
            ]
        },
        {
            "name": "map_gray_golems",
            "dependencies": []
        },
        {
            "name": "map_gray_gorgons",
            "dependencies": []
        },
        {
            "name": "map_gray_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_green_fairies",
            "dependencies": []
        },
        {
            "name": "map_green_humans",
            "dependencies": []
        },
        {
            "name": "map_green_witches",
            "dependencies": [
                "enable_navy_witches",
                "enable_white_witches",
                "read_green_witches"
            ]
        },
        {
            "name": "map_lime_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_maroon_centaurs",
            "dependencies": []
        },
        {
            "name": "map_maroon_gnomes",
            "dependencies": []
        },
        {
            "name": "map_maroon_goblins",
            "dependencies": []
        },
        {
            "name": "map_maroon_golems",
            "dependencies": []
        },
        {
            "name": "map_maroon_ogres",
            "dependencies": []
        },
        {
            "name": "map_navy_golems",
            "dependencies": []
        },
        {
            "name": "map_navy_leprechauns",
            "dependencies": [
                "build_olive_leprechauns",
                "coloring_olive_leprechauns",
                "read_gray_leprechauns"
            ]
        },
        {
            "name": "map_olive_centaurs",
            "dependencies": [
                "build_olive_centaurs",
                "write_blue_centaurs"
            ]
        },
        {
            "name": "map_olive_goblins",
            "dependencies": []
        },
        {
            "name": "map_olive_golems",
            "dependencies": []
        },
        {
            "name": "map_olive_leprechauns",
            "dependencies": [
                "map_black_leprechauns",
                "upgrade_white_leprechauns"
            ]
        },
        {
            "name": "map_olive_orcs",
            "dependencies": []
        },
        {
            "name": "map_purple_humans",
            "dependencies": [
                "bring_purple_humans",
                "design_blue_humans",
                "read_maroon_humans",
                "write_gray_humans",
                "write_yellow_humans"
            ]
        },
        {
            "name": "map_purple_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_silver_gorgons",
            "dependencies": []
        },
        {
            "name": "map_teal_centaurs",
            "dependencies": []
        },
        {
            "name": "map_teal_humans",
            "dependencies": []
        },
        {
            "name": "map_teal_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_white_leprechauns",
            "dependencies": []
        },
        {
            "name": "map_yellow_centaurs",
            "dependencies": []
        },
        {
            "name": "map_yellow_gnomes",
            "dependencies": [
                "coloring_blue_gnomes",
                "coloring_maroon_gnomes",
                "create_white_gnomes"
            ]
        },
        {
            "name": "map_yellow_golems",
            "dependencies": [
                "coloring_teal_golems",
                "create_olive_golems",
                "create_teal_golems",
                "map_blue_golems",
                "map_gray_golems"
            ]
        },
        {
            "name": "map_yellow_humans",
            "dependencies": []
        },
        {
            "name": "map_yellow_leprechauns",
            "dependencies": [
                "write_aqua_leprechauns"
            ]
        },
        {
            "name": "read_aqua_centaurs",
            "dependencies": []
        },
        {
            "name": "read_aqua_golems",
            "dependencies": []
        },
        {
            "name": "read_aqua_humans",
            "dependencies": []
        },
        {
            "name": "read_aqua_orcs",
            "dependencies": [
                "train_fuchsia_orcs"
            ]
        },
        {
            "name": "read_blue_goblins",
            "dependencies": []
        },
        {
            "name": "read_fuchsia_fairies",
            "dependencies": [
                "upgrade_aqua_fairies"
            ]
        },
        {
            "name": "read_fuchsia_goblins",
            "dependencies": []
        },
        {
            "name": "read_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "read_fuchsia_gorgons",
            "dependencies": [
                "enable_gray_gorgons"
            ]
        },
        {
            "name": "read_fuchsia_leprechauns",
            "dependencies": [
                "bring_maroon_leprechauns",
                "map_aqua_leprechauns",
                "read_white_leprechauns"
            ]
        },
        {
            "name": "read_fuchsia_ogres",
            "dependencies": []
        },
        {
            "name": "read_fuchsia_orcs",
            "dependencies": []
        },
        {
            "name": "read_fuchsia_witches",
            "dependencies": [
                "build_aqua_witches",
                "enable_aqua_witches",
                "write_maroon_witches"
            ]
        },
        {
            "name": "read_gray_fairies",
            "dependencies": []
        },
        {
            "name": "read_gray_goblins",
            "dependencies": []
        },
        {
            "name": "read_gray_golems",
            "dependencies": [
                "design_maroon_golems",
                "design_yellow_golems",
                "write_navy_golems"
            ]
        },
        {
            "name": "read_gray_humans",
            "dependencies": [
                "coloring_teal_humans",
                "upgrade_aqua_humans",
                "upgrade_gray_humans"
            ]
        },
        {
            "name": "read_gray_leprechauns",
            "dependencies": []
        },
        {
            "name": "read_gray_ogres",
            "dependencies": []
        },
        {
            "name": "read_green_fairies",
            "dependencies": []
        },
        {
            "name": "read_green_goblins",
            "dependencies": []
        },
        {
            "name": "read_green_humans",
            "dependencies": [
                "enable_blue_humans",
                "enable_yellow_humans"
            ]
        },
        {
            "name": "read_green_witches",
            "dependencies": []
        },
        {
            "name": "read_lime_centaurs",
            "dependencies": []
        },
        {
            "name": "read_lime_gnomes",
            "dependencies": [
                "coloring_olive_gnomes",
                "coloring_white_gnomes",
                "enable_purple_gnomes"
            ]
        },
        {
            "name": "read_lime_goblins",
            "dependencies": []
        },
        {
            "name": "read_maroon_centaurs",
            "dependencies": []
        },
        {
            "name": "read_maroon_gnomes",
            "dependencies": []
        },
        {
            "name": "read_maroon_humans",
            "dependencies": [
                "bring_aqua_humans",
                "bring_purple_humans",
                "enable_fuchsia_humans",
                "map_aqua_humans",
                "write_gray_humans"
            ]
        },
        {
            "name": "read_navy_centaurs",
            "dependencies": [
                "read_aqua_centaurs",
                "upgrade_maroon_centaurs"
            ]
        },
        {
            "name": "read_navy_gnomes",
            "dependencies": []
        },
        {
            "name": "read_navy_goblins",
            "dependencies": []
        },
        {
            "name": "read_navy_ogres",
            "dependencies": []
        },
        {
            "name": "read_olive_orcs",
            "dependencies": []
        },
        {
            "name": "read_purple_golems",
            "dependencies": [
                "bring_gray_golems",
                "build_fuchsia_golems",
                "create_olive_golems",
                "train_teal_golems"
            ]
        },
        {
            "name": "read_purple_ogres",
            "dependencies": []
        },
        {
            "name": "read_purple_witches",
            "dependencies": []
        },
        {
            "name": "read_silver_centaurs",
            "dependencies": [
                "build_silver_centaurs",
                "create_aqua_centaurs",
                "enable_silver_centaurs"
            ]
        },
        {
            "name": "read_silver_gorgons",
            "dependencies": [
                "bring_white_gorgons",
                "coloring_aqua_gorgons",
                "design_fuchsia_gorgons"
            ]
        },
        {
            "name": "read_silver_humans",
            "dependencies": []
        },
        {
            "name": "read_silver_witches",
            "dependencies": []
        },
        {
            "name": "read_teal_fairies",
            "dependencies": []
        },
        {
            "name": "read_teal_golems",
            "dependencies": []
        },
        {
            "name": "read_teal_orcs",
            "dependencies": []
        },
        {
            "name": "read_teal_witches",
            "dependencies": []
        },
        {
            "name": "read_white_gnomes",
            "dependencies": [
                "coloring_aqua_gnomes"
            ]
        },
        {
            "name": "read_white_leprechauns",
            "dependencies": []
        },
        {
            "name": "read_yellow_centaurs",
            "dependencies": []
        },
        {
            "name": "read_yellow_gorgons",
            "dependencies": []
        },
        {
            "name": "train_aqua_humans",
            "dependencies": []
        },
        {
            "name": "train_aqua_ogres",
            "dependencies": []
        },
        {
            "name": "train_black_orcs",
            "dependencies": []
        },
        {
            "name": "train_blue_centaurs",
            "dependencies": []
        },
        {
            "name": "train_blue_goblins",
            "dependencies": [
                "design_black_goblins",
                "read_green_goblins"
            ]
        },
        {
            "name": "train_blue_golems",
            "dependencies": []
        },
        {
            "name": "train_fuchsia_goblins",
            "dependencies": [
                "design_teal_goblins",
                "read_gray_goblins"
            ]
        },
        {
            "name": "train_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "train_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "train_fuchsia_leprechauns",
            "dependencies": [
                "write_yellow_leprechauns"
            ]
        },
        {
            "name": "train_fuchsia_orcs",
            "dependencies": []
        },
        {
            "name": "train_gray_centaurs",
            "dependencies": [
                "coloring_olive_centaurs",
                "create_green_centaurs"
            ]
        },
        {
            "name": "train_gray_golems",
            "dependencies": []
        },
        {
            "name": "train_green_centaurs",
            "dependencies": [
                "create_fuchsia_centaurs",
                "design_green_centaurs",
                "enable_olive_centaurs",
                "upgrade_teal_centaurs",
                "write_maroon_centaurs"
            ]
        },
        {
            "name": "train_green_fairies",
            "dependencies": []
        },
        {
            "name": "train_green_gnomes",
            "dependencies": []
        },
        {
            "name": "train_green_ogres",
            "dependencies": []
        },
        {
            "name": "train_lime_golems",
            "dependencies": [
                "bring_green_golems",
                "upgrade_aqua_golems",
                "write_yellow_golems"
            ]
        },
        {
            "name": "train_lime_gorgons",
            "dependencies": []
        },
        {
            "name": "train_lime_humans",
            "dependencies": [
                "bring_teal_humans",
                "enable_purple_humans",
                "map_teal_humans",
                "upgrade_fuchsia_humans",
                "write_yellow_humans"
            ]
        },
        {
            "name": "train_lime_ogres",
            "dependencies": []
        },
        {
            "name": "train_lime_orcs",
            "dependencies": [
                "enable_maroon_orcs"
            ]
        },
        {
            "name": "train_lime_witches",
            "dependencies": []
        },
        {
            "name": "train_maroon_golems",
            "dependencies": []
        },
        {
            "name": "train_maroon_leprechauns",
            "dependencies": []
        },
        {
            "name": "train_maroon_witches",
            "dependencies": []
        },
        {
            "name": "train_navy_fairies",
            "dependencies": []
        },
        {
            "name": "train_navy_orcs",
            "dependencies": [
                "coloring_black_orcs",
                "map_olive_orcs",
                "write_olive_orcs"
            ]
        },
        {
            "name": "train_navy_witches",
            "dependencies": []
        },
        {
            "name": "train_olive_fairies",
            "dependencies": []
        },
        {
            "name": "train_olive_gnomes",
            "dependencies": []
        },
        {
            "name": "train_olive_goblins",
            "dependencies": [
                "enable_lime_goblins",
                "enable_silver_goblins",
                "map_maroon_goblins",
                "read_blue_goblins",
                "write_olive_goblins"
            ]
        },
        {
            "name": "train_olive_humans",
            "dependencies": [
                "coloring_white_humans",
                "map_fuchsia_humans",
                "map_green_humans"
            ]
        },
        {
            "name": "train_purple_centaurs",
            "dependencies": []
        },
        {
            "name": "train_purple_goblins",
            "dependencies": []
        },
        {
            "name": "train_silver_witches",
            "dependencies": []
        },
        {
            "name": "train_teal_centaurs",
            "dependencies": []
        },
        {
            "name": "train_teal_goblins",
            "dependencies": [
                "create_white_goblins"
            ]
        },
        {
            "name": "train_teal_golems",
            "dependencies": []
        },
        {
            "name": "train_teal_orcs",
            "dependencies": []
        },
        {
            "name": "train_teal_witches",
            "dependencies": []
        },
        {
            "name": "train_white_fairies",
            "dependencies": [
                "bring_gray_fairies",
                "design_aqua_fairies"
            ]
        },
        {
            "name": "train_white_gorgons",
            "dependencies": [
                "coloring_fuchsia_gorgons"
            ]
        },
        {
            "name": "train_white_humans",
            "dependencies": []
        },
        {
            "name": "train_white_leprechauns",
            "dependencies": [
                "coloring_fuchsia_leprechauns",
                "read_white_leprechauns"
            ]
        },
        {
            "name": "train_white_witches",
            "dependencies": [
                "build_aqua_witches",
                "design_fuchsia_witches",
                "train_lime_witches",
                "train_teal_witches",
                "write_white_witches"
            ]
        },
        {
            "name": "train_yellow_centaurs",
            "dependencies": []
        },
        {
            "name": "train_yellow_humans",
            "dependencies": []
        },
        {
            "name": "upgrade_aqua_centaurs",
            "dependencies": [
                "bring_lime_centaurs",
                "coloring_gray_centaurs",
                "create_silver_centaurs"
            ]
        },
        {
            "name": "upgrade_aqua_fairies",
            "dependencies": []
        },
        {
            "name": "upgrade_aqua_golems",
            "dependencies": []
        },
        {
            "name": "upgrade_aqua_humans",
            "dependencies": [
                "bring_aqua_humans",
                "build_gray_humans",
                "coloring_silver_humans",
                "create_olive_humans"
            ]
        },
        {
            "name": "upgrade_aqua_ogres",
            "dependencies": []
        },
        {
            "name": "upgrade_aqua_witches",
            "dependencies": []
        },
        {
            "name": "upgrade_black_humans",
            "dependencies": [
                "write_teal_humans"
            ]
        },
        {
            "name": "upgrade_black_ogres",
            "dependencies": []
        },
        {
            "name": "upgrade_blue_fairies",
            "dependencies": [
                "create_black_fairies",
                "map_gray_fairies"
            ]
        },
        {
            "name": "upgrade_fuchsia_fairies",
            "dependencies": []
        },
        {
            "name": "upgrade_fuchsia_humans",
            "dependencies": []
        },
        {
            "name": "upgrade_fuchsia_witches",
            "dependencies": []
        },
        {
            "name": "upgrade_gray_gnomes",
            "dependencies": [
                "create_black_gnomes",
                "read_maroon_gnomes",
                "upgrade_maroon_gnomes"
            ]
        },
        {
            "name": "upgrade_gray_humans",
            "dependencies": [
                "create_green_humans",
                "map_yellow_humans",
                "upgrade_black_humans",
                "upgrade_silver_humans",
                "write_maroon_humans"
            ]
        },
        {
            "name": "upgrade_green_golems",
            "dependencies": []
        },
        {
            "name": "upgrade_green_humans",
            "dependencies": []
        },
        {
            "name": "upgrade_green_ogres",
            "dependencies": []
        },
        {
            "name": "upgrade_lime_goblins",
            "dependencies": []
        },
        {
            "name": "upgrade_lime_golems",
            "dependencies": []
        },
        {
            "name": "upgrade_lime_humans",
            "dependencies": []
        },
        {
            "name": "upgrade_lime_witches",
            "dependencies": []
        },
        {
            "name": "upgrade_maroon_centaurs",
            "dependencies": []
        },
        {
            "name": "upgrade_maroon_gnomes",
            "dependencies": []
        },
        {
            "name": "upgrade_maroon_goblins",
            "dependencies": []
        },
        {
            "name": "upgrade_maroon_gorgons",
            "dependencies": []
        },
        {
            "name": "upgrade_navy_centaurs",
            "dependencies": []
        },
        {
            "name": "upgrade_navy_goblins",
            "dependencies": []
        },
        {
            "name": "upgrade_navy_golems",
            "dependencies": []
        },
        {
            "name": "upgrade_navy_ogres",
            "dependencies": [
                "bring_green_ogres",
                "build_yellow_ogres",
                "create_maroon_ogres",
                "design_green_ogres"
            ]
        },
        {
            "name": "upgrade_olive_fairies",
            "dependencies": []
        },
        {
            "name": "upgrade_olive_goblins",
            "dependencies": []
        },
        {
            "name": "upgrade_purple_gnomes",
            "dependencies": []
        },
        {
            "name": "upgrade_purple_golems",
            "dependencies": []
        },
        {
            "name": "upgrade_purple_gorgons",
            "dependencies": [
                "map_silver_gorgons"
            ]
        },
        {
            "name": "upgrade_silver_gorgons",
            "dependencies": []
        },
        {
            "name": "upgrade_silver_humans",
            "dependencies": [
                "enable_lime_humans",
                "read_aqua_humans"
            ]
        },
        {
            "name": "upgrade_silver_orcs",
            "dependencies": []
        },
        {
            "name": "upgrade_teal_centaurs",
            "dependencies": []
        },
        {
            "name": "upgrade_teal_gnomes",
            "dependencies": []
        },
        {
            "name": "upgrade_teal_gorgons",
            "dependencies": []
        },
        {
            "name": "upgrade_white_fairies",
            "dependencies": []
        },
        {
            "name": "upgrade_white_leprechauns",
            "dependencies": []
        },
        {
            "name": "upgrade_yellow_gnomes",
            "dependencies": [
                "coloring_olive_gnomes",
                "enable_navy_gnomes",
                "map_fuchsia_gnomes",
                "write_aqua_gnomes",
                "write_teal_gnomes"
            ]
        },
        {
            "name": "upgrade_yellow_golems",
            "dependencies": [
                "bring_fuchsia_golems",
                "coloring_aqua_golems",
                "create_blue_golems",
                "map_navy_golems",
                "upgrade_green_golems"
            ]
        },
        {
            "name": "upgrade_yellow_humans",
            "dependencies": []
        },
        {
            "name": "upgrade_yellow_witches",
            "dependencies": []
        },
        {
            "name": "write_aqua_centaurs",
            "dependencies": []
        },
        {
            "name": "write_aqua_cyclops",
            "dependencies": []
        },
        {
            "name": "write_aqua_gnomes",
            "dependencies": []
        },
        {
            "name": "write_aqua_leprechauns",
            "dependencies": []
        },
        {
            "name": "write_black_witches",
            "dependencies": []
        },
        {
            "name": "write_blue_centaurs",
            "dependencies": []
        },
        {
            "name": "write_blue_goblins",
            "dependencies": [
                "build_teal_goblins",
                "train_blue_goblins",
                "train_fuchsia_goblins"
            ]
        },
        {
            "name": "write_blue_ogres",
            "dependencies": [
                "enable_fuchsia_ogres",
                "upgrade_navy_ogres"
            ]
        },
        {
            "name": "write_blue_witches",
            "dependencies": []
        },
        {
            "name": "write_fuchsia_goblins",
            "dependencies": []
        },
        {
            "name": "write_fuchsia_golems",
            "dependencies": []
        },
        {
            "name": "write_fuchsia_orcs",
            "dependencies": []
        },
        {
            "name": "write_gray_gorgons",
            "dependencies": []
        },
        {
            "name": "write_gray_humans",
            "dependencies": []
        },
        {
            "name": "write_gray_ogres",
            "dependencies": []
        },
        {
            "name": "write_green_goblins",
            "dependencies": []
        },
        {
            "name": "write_green_golems",
            "dependencies": [
                "coloring_fuchsia_golems",
                "upgrade_navy_golems"
            ]
        },
        {
            "name": "write_green_ogres",
            "dependencies": []
        },
        {
            "name": "write_green_witches",
            "dependencies": []
        },
        {
            "name": "write_lime_humans",
            "dependencies": []
        },
        {
            "name": "write_lime_leprechauns",
            "dependencies": []
        },
        {
            "name": "write_maroon_centaurs",
            "dependencies": []
        },
        {
            "name": "write_maroon_golems",
            "dependencies": []
        },
        {
            "name": "write_maroon_humans",
            "dependencies": [
                "build_maroon_humans",
                "coloring_white_humans",
                "create_fuchsia_humans"
            ]
        },
        {
            "name": "write_maroon_leprechauns",
            "dependencies": [
                "bring_aqua_leprechauns",
                "build_purple_leprechauns",
                "coloring_maroon_leprechauns",
                "design_gray_leprechauns"
            ]
        },
        {
            "name": "write_maroon_witches",
            "dependencies": [
                "build_olive_witches",
                "upgrade_lime_witches"
            ]
        },
        {
            "name": "write_navy_goblins",
            "dependencies": []
        },
        {
            "name": "write_navy_golems",
            "dependencies": [
                "map_maroon_golems"
            ]
        },
        {
            "name": "write_navy_gorgons",
            "dependencies": [
                "create_teal_gorgons",
                "read_yellow_gorgons",
                "train_lime_gorgons",
                "upgrade_maroon_gorgons"
            ]
        },
        {
            "name": "write_navy_leprechauns",
            "dependencies": []
        },
        {
            "name": "write_olive_fairies",
            "dependencies": [
                "build_fuchsia_fairies",
                "create_white_fairies",
                "read_gray_fairies",
                "train_navy_fairies"
            ]
        },
        {
            "name": "write_olive_goblins",
            "dependencies": []
        },
        {
            "name": "write_olive_orcs",
            "dependencies": []
        },
        {
            "name": "write_purple_cyclops",
            "dependencies": []
        },
        {
            "name": "write_purple_gnomes",
            "dependencies": []
        },
        {
            "name": "write_purple_leprechauns",
            "dependencies": []
        },
        {
            "name": "write_silver_goblins",
            "dependencies": []
        },
        {
            "name": "write_silver_humans",
            "dependencies": []
        },
        {
            "name": "write_silver_ogres",
            "dependencies": []
        },
        {
            "name": "write_teal_gnomes",
            "dependencies": []
        },
        {
            "name": "write_teal_golems",
            "dependencies": []
        },
        {
            "name": "write_teal_gorgons",
            "dependencies": []
        },
        {
            "name": "write_teal_humans",
            "dependencies": []
        },
        {
            "name": "write_teal_ogres",
            "dependencies": [
                "build_black_ogres",
                "train_lime_ogres"
            ]
        },
        {
            "name": "write_teal_witches",
            "dependencies": []
        },
        {
            "name": "write_white_goblins",
            "dependencies": [
                "coloring_olive_goblins",
                "train_olive_goblins",
                "upgrade_olive_goblins"
            ]
        },
        {
            "name": "write_white_golems",
            "dependencies": []
        },
        {
            "name": "write_white_humans",
            "dependencies": []
        },
        {
            "name": "write_white_leprechauns",
            "dependencies": []
        },
        {
            "name": "write_white_witches",
            "dependencies": [
                "write_blue_witches"
            ]
        },
        {
            "name": "write_yellow_golems",
            "dependencies": []
        },
        {
            "name": "write_yellow_humans",
            "dependencies": [
                "build_purple_humans",
                "design_lime_humans"
            ]
        },
        {
            "name": "write_yellow_leprechauns",
            "dependencies": [
                "coloring_gray_leprechauns",
                "create_black_leprechauns",
                "design_blue_leprechauns",
                "map_lime_leprechauns"
            ]
        },
        {
            "name": "write_yellow_ogres",
            "dependencies": []
        }
    ]
}


class TaskManager:
    def __init__(self, build_name: str, extracted_data: dict):
        self.build_name = build_name
        self.extracted_data = extracted_data
        self.graph: Dict[str, set] = {}

    def get_tasks_by_build_name(self) -> list:
        tasks = [build["tasks"] for build in self.extracted_data["builds"] if build["name"] == self.build_name]
        return tasks[0]

    def create_graph_for_sorting(self, tasks: list) -> None:
        for task in tasks:
            for task_info in self.extracted_data["tasks"]:
                if task_info["name"] == task:
                    self.graph[task] = set(task_info['dependencies'])

    def sort_tasks_by_dependencies(self) -> list:
        ts = graphlib.TopologicalSorter(self.graph)
        return list(ts.static_order())

    def get_sorted_tasks(self) -> list:
        tasks = self.get_tasks_by_build_name()
        self.create_graph_for_sorting(tasks=tasks)
        sorted_data = self.sort_tasks_by_dependencies()
        return sorted_data
