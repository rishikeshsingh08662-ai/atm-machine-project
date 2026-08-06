{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOITZFaxjG3eZXIiEAaAlqS",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rishikeshsingh08662-ai/atm-machine-project/blob/main/to_do_list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ilxsi6EcJJN9"
      },
      "outputs": [],
      "source": [
        "# To-Do List Project\n",
        "\n",
        "print(\"=== TO-DO LIST ===\")\n",
        "\n",
        "tasks = []\n",
        "\n",
        "while True:\n",
        "    print(\"\\n1. Add Task\")\n",
        "    print(\"2. View Tasks\")\n",
        "    print(\"3. Delete Task\")\n",
        "    print(\"4. Exit\")\n",
        "\n",
        "    choice = input(\"Enter your choice: \")\n",
        "\n",
        "    # Add Task\n",
        "    if choice == \"1\":\n",
        "        task = input(\"Enter task: \")\n",
        "        tasks.append(task)\n",
        "        print(\"Task added successfully!\")\n",
        "\n",
        "    # View Tasks\n",
        "    elif choice == \"2\":\n",
        "        if len(tasks) == 0:\n",
        "            print(\"No tasks available.\")\n",
        "        else:\n",
        "            print(\"\\nYour Tasks:\")\n",
        "            for i, task in enumerate(tasks, start=1):\n",
        "                print(f\"{i}. {task}\")\n",
        "\n",
        "    # Delete Task\n",
        "    elif choice == \"3\":\n",
        "        if len(tasks) == 0:\n",
        "            print(\"No tasks to delete.\")\n",
        "        else:\n",
        "            print(\"\\nYour Tasks:\")\n",
        "            for i, task in enumerate(tasks, start=1):\n",
        "                print(f\"{i}. {task}\")\n",
        "\n",
        "            number = int(input(\"Enter task number to delete: \"))\n",
        "\n",
        "            if 1 <= number <= len(tasks):\n",
        "                removed = tasks.pop(number - 1)\n",
        "                print(f\"'{removed}' deleted successfully!\")\n",
        "            else:\n",
        "                print(\"Invalid task number.\")\n",
        "\n",
        "    # Exit\n",
        "    elif choice == \"4\":\n",
        "        print(\"Thank you for using To-Do List!\")\n",
        "        break\n",
        "\n",
        "    else:\n",
        "        print(\"Invalid choice. Please try again.\")"
      ]
    }
  ]
}