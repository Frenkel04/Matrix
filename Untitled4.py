{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "def print_maps():\n",
        "    print(maps[0], end = \" \")\n",
        "    print(maps[1], end = \" \")\n",
        "    print(maps[2])\n",
        " \n",
        "    print(maps[3], end = \" \")\n",
        "    print(maps[4], end = \" \")\n",
        "    print(maps[5])\n",
        " \n",
        "    print(maps[6], end = \" \")\n",
        "    print(maps[7], end = \" \")\n",
        "    print(maps[8])    \n",
        "\n",
        "def step_maps(step,symbol):\n",
        "    ind = maps.index(step)\n",
        "    maps[ind] = symbol\n",
        " \n",
        "def get_result():\n",
        "    win = \"\"\n",
        " \n",
        "    for i in victories:\n",
        "        if maps[i[0]] == \"X\" and maps[i[1]] == \"X\" and maps[i[2]] == \"X\":\n",
        "            win = \"X\"\n",
        "        if maps[i[0]] == \"O\" and maps[i[1]] == \"O\" and maps[i[2]] == \"O\":\n",
        "            win = \"O\"   \n",
        "             \n",
        "    return win\n",
        "\n",
        "maps = [1,2,3,\n",
        "        4,5,6,\n",
        "        7,8,9]\n",
        "\n",
        "victories = [[0,1,2],\n",
        "             [3,4,5],\n",
        "             [6,7,8],\n",
        "             [0,3,6],\n",
        "             [1,4,7],\n",
        "             [2,5,8],\n",
        "             [0,4,8],\n",
        "             [2,4,6]]\n",
        " \n",
        "game_over = False\n",
        "player1 = True\n",
        " \n",
        "while game_over == False:\n",
        " \n",
        "    print_maps()\n",
        " \n",
        "    if player1 == True:\n",
        "        symbol = \"X\"\n",
        "        step = int(input(\"Человек 1, ваш ход: \"))\n",
        "    else:\n",
        "        symbol = \"O\"\n",
        "        step = int(input(\"Человек 2, ваш ход: \"))\n",
        " \n",
        "    step_maps(step,symbol)\n",
        "    win = get_result() \n",
        "    if win != \"\":\n",
        "        game_over = True\n",
        "    else:\n",
        "        game_over = False\n",
        " \n",
        "    player1 = not(player1)        \n",
        " \n",
        "     \n",
        "print_maps()\n",
        "print(\"Победил\", win)"
      ],
      "metadata": {
        "id": "6nhe5B-7IoPy"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
