from src.logger import logger
from src.oai import Essay


def essay_object_from_user_input():
    print("Welcome to the Essay Generator")
    print("To help you write an essay, I need some information from you.")
    subject = input("Please, enter the subject of the essay: ")
    number_of_paragraphs = int(input("Please, enter the number of paragraphs: "))
    bullets = input("Are there specific points you want to mention in the essay? If yes, please enter them separated "
                    "by comma: ").split(", ")
    return Essay(subject=subject, bullets=bullets, number_of_paragraphs=number_of_paragraphs)


if __name__ == '__main__':
    essay = essay_object_from_user_input()

    print("\nBeautiful, I have all the information I need to write your essay.\n")
    print("Take a look at the prompt, before we generate your essay.")
    print(essay.prompt)

    result = essay.write_essay()
    print("\n We wrote an essay for you. Hope you will like it. Have a look:\n")
    print(result)
    # save result into result.txt file
    with open("result.txt", "w") as f:
        f.write(result)
    logger.info("Result saved in result.txt file")
