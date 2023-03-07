# OpenAI GPT3 functionalities
#
# Path: src\oai.py

import openai


class Essay:
    def __init__(self, subject, bullets, number_of_paragraphs=1):
        self.subject = subject
        self.bullets = bullets
        self.number_of_paragraphs = number_of_paragraphs
        self.prompt = self.generate_prompt()

    def generate_prompt(self):
        prompt = f"Write an essay about '{self.subject}'.\n"

        if self.number_of_paragraphs > 1:
            prompt += f"Make sure to write {self.number_of_paragraphs} paragraphs.\n"

        prompt += "Here are some points to mentioned in essay:"

        for bullet in self.bullets:
            prompt += f"\n- {bullet}"
        return prompt

    def write_essay(self, max_tokens=1000, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0,
                    stop=["\n", "###"]):
        # config for GPT3 API
        openai.api_key = "<your_key_here>"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=0.9,
            max_tokens=732,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Opps sorry, you beat the AI this time'
        else:
            answer = 'Opps sorry, you beat the AI this time'
        return answer


essay = Essay(subject="Role of AI in education",
              bullets=["AI tools that help my while studying",
                       "AI is always there even when teachers are not",
                       "AI is the future of education"],
              number_of_paragraphs=4
              )

if __name__ == "__main__":
    print(essay.prompt)
    print(essay.write_essay())
