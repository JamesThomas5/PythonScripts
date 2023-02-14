import random
from colorama import Fore, Back, Style


gift_ideas = [
    "A night off from cooking dinner (me cooking or takeaway)",
    "A lie in (any day of your choice)",
    "A day of brews (unlimited uses for that day)",
    "An extra TV series choice",
    "Chocolate / sweets of your choice",
    "Breakfast in bed",
    "A free wish",
    "An automatic argument win",
    "Control of the TV remote for 24 hours",
    "Servant for the day",
    "Your pick from the whole list",
    "EVERYTHING!!!",
    "Fuck all! :("
]

print(f"""{Fore.RED}
         LOVELOVELOV                ELOVELOVELO
     VELOVELOVELOVELOVE          LOVELOVELOVELOVELO
  VELOVELOVELOVELOVELOVEL      OVELOVELOVELOVELOVELOVE
 LOVELOVELOVELOVELOVELOVEL    OVELOVELOVELOVELOVELOVELO
VELOVELOVELOVELOVELOVELOVEL  OVELOVELOVELOVELOVELOVELOVE
LOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVE
LOVELOVELOVELOVEL {Fore.WHITE}HAPPY VALENTINES DAY{Fore.RED} ELOVELOVELOVELOVE
 LOVELOVELOVELOVELOV {Fore.WHITE}LOVE YOU LOTS!{Fore.RED} ELOVELOVELOVELOVELO
  VELOVELOVELOVELO {Fore.WHITE}VALENTINES VOUCHER{Fore.RED} LOVELOVELOVELOVE
   LOVELOVELOVELOVELOVE {Fore.WHITE}LOTTERY{Fore.RED} LOVELOVELOVELOVELOVE
     VELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELOVE
       LOVELOVELOVELOVELOVELOVELOVELOVELOVELOVELO
         VELOVELOVELOVELOVELOVELOVELOVELOVELOVE
           LOVELOVELOVELOVELOVELOVELOVELOVELO
             VELOVELOVELOVELOVELOVELOVELOVE
               LOVELOVELOVELOVELOVELOVELO
                OVELOVELOVELOVELOVELOV
                  VELOVELOVELOVELOVEL
                   ELOVELOVELOVELOO
                     OVELOVELOVELO
		       LOVELOVEL
		         LOVEL
                          OVE
                           L
{Style.RESET_ALL}""")
input("Press ENTER to claim your Valentines voucher: ")
random_choice = random.choice(gift_ideas)
if random_choice == "Your pick from the whole list":
    print(f"{Style.BRIGHT}{Fore.YELLOW}{Back.BLUE}{random_choice}{Style.RESET_ALL}\n")
    for gift in gift_ideas[:10]:
        print(gift)
elif random_choice == "EVERYTHING!!!":
    print(f"{Style.BRIGHT}{Fore.YELLOW}{Back.BLUE}{random_choice}{Style.RESET_ALL}\n")
    for gift in gift_ideas[:10]:
        print(gift)
else:
    print(random_choice)
