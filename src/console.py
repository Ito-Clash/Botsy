import sys
import logging
from bot import Bot


def print_help_master():
    help_text = (
        "Available master console commands:\n"
        "  list                 - List available bots and their status.\n"
        "  start all            - Start all bots.\n"
        "  start {bot name}     - Start the specified bot.\n"
        "  stop all             - Stop all bots.\n"
        "  stop {bot name}      - Stop the specified bot.\n"
        "  <bot name>           - Enter control mode for the specified bot.\n"
        "  show log all         - Show scheduled log info for all bots with status.\n"
        "  help or ?            - Show this help message.\n"
        "  exit                 - Exit the master console."
    )
    print(help_text)


def print_master_prompt():
    print("\nMaster Console: Enter command ('list', 'start', 'stop', bot name, 'show log all', 'help' or 'exit'):")


def print_bot_prompt(bot):
    print(f"\n[Bot {bot.name}] ", end='')


def platform_menu(bot: Bot, platform: str):
    logging.info(f"🔔 Now controlling bot '{bot.name}' on platform '{platform}'.")
    print(f"\nNow controlling bot '{bot.name}' on platform '{platform}'.")
    print("Type commands for this platform (type 'back' to return to the bot menu):")
    adapter = bot.platform_adapters.get(platform.lower())
    if adapter is None:
        print(f"No adapter found for platform {platform}.")
        return
    while True:
        print(f"[{bot.name} - {platform}] ", end='')
        cmd = input().strip().lower()
        if cmd == "back":
            logging.info(f"🔔 Exiting control for platform '{platform}' of bot '{bot.name}'. Returning to bot menu.")
            break
        try:
            # Instead of directly calling adapter methods with empty parameters,
            # route the command to the bot's global command processor so that it
            # can properly determine monitored tweet ids and run the full job logic.
            if cmd.startswith("run post") or cmd.startswith("run comment") or cmd.startswith("run reply"):
                bot.process_console_command(cmd)
            else:
                # For other commands, fall back to global bot command processing.
                bot.process_console_command(cmd)
        except Exception as e:
            logging.error(f"❌ Error executing command '{cmd}' on platform {platform}: {e}")
            input("Press Enter to continue...")


def bot_menu(bot: Bot):
    logging.info(f"🔔 Now controlling bot '{bot.name}'.")
    while True:
        print(f"\nNow controlling bot '{bot.name}'.")
        print(
            "Enter a platform to control (twitter, facebook, instagram, telegram, discord), 'all' for global commands, or 'back' to return to the master console:")
        selection = input().strip().lower()
        if selection == "back":
            logging.info(f"🔔 Exiting control of bot '{bot.name}'. Returning to master console.")
            break
        elif selection == "all":
            print(f"Running global commands for bot '{bot.name}'.")
            while True:
                print(f"[Bot {bot.name} Global] ", end='')
                cmd = input().strip().lower()
                if cmd == "back":
                    break
                try:
                    bot.process_console_command(cmd)
                except Exception as e:
                    logging.error(f"❌ Error executing command '{cmd}': {e}")
                    input("Press Enter to continue...")
        elif selection in bot.platform_adapters:
            platform_menu(bot, selection)
        else:
            print("Invalid platform. Try again.")


def master_console(bots: dict):
    while True:
        print_master_prompt()
        selection = input().strip()
        if selection.lower() == "exit":
            logging.info("Exiting master console.")
            sys.exit(0)
        elif selection.lower() == "list":
            logging.info("Available bots:")
            for bot_name, bot in bots.items():
                logging.info(f" - {bot_name} (Status: {bot.get_status()})")
            input("Press Enter to continue in Master Console...")
        elif selection.lower() in ["help", "?"]:
            print_help_master()
            input("Press Enter to continue in Master Console...")
        elif selection.lower() == "show log all":
            for bot in bots.values():
                print(f"--- {bot.name} (Status: {bot.get_status()}) ---")
                bot.show_log()
                print()
            input("Press Enter to continue in Master Console...")
        elif selection.lower() == "start all":
            for bot in bots.values():
                bot.start()
            logging.info("All bots started.")
            input("Press Enter to continue in Master Console...")
        elif selection.lower() == "stop all":
            for bot in bots.values():
                bot.stop()
            logging.info("All bots stopped.")
            input("Press Enter to continue in Master Console...")
        elif selection.lower().startswith("start "):
            bot_name = selection[6:].strip()
            if bot_name in bots:
                bots[bot_name].start()
            else:
                logging.info(f"Bot '{bot_name}' not found.")
            input("Press Enter to continue in Master Console...")
        elif selection.lower().startswith("stop "):
            bot_name = selection[5:].strip()
            if bot_name in bots:
                bots[bot_name].stop()
            else:
                logging.info(f"Bot '{bot_name}' not found.")
            input("Press Enter to continue in Master Console...")
        elif selection in bots:
            bot_menu(bots[selection])
        else:
            logging.info("Invalid selection. Try again. (Type 'help' for a list of commands.)")
            input("Press Enter to continue in Master Console...")