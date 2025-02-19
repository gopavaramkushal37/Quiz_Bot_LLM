# your_main_script.py


#import openai
from difflib import SequenceMatcher
import random
#import PyPDF2
from quiz_data_topic_1 import mcq_questions as topic_1_mcq_questions, mcq_choices as topic_1_mcq_choices, \
    mcq_correct_answers as topic_1_mcq_correct_answers, mcq_sources as topic_1_mcq_sources
from quiz_data_topic_1 import true_false_questions as topic_1_true_false_questions, \
    true_false_correct_answers as topic_1_true_false_correct_answers, true_false_sources as topic_1_true_false_sources
from quiz_data_topic_1 import open_ended_questions as topic_1_open_ended_questions, \
    open_ended_correct_answers as topic_1_open_ended_correct_answers, open_ended_sources as topic_1_open_ended_sources

from quiz_data_topic_2 import mcq_questions as topic_2_mcq_questions, mcq_choices as topic_2_mcq_choices, \
    mcq_correct_answers as topic_2_mcq_correct_answers, mcq_sources as topic_2_mcq_sources
from quiz_data_topic_2 import true_false_questions as topic_2_true_false_questions, \
    true_false_correct_answers as topic_2_true_false_correct_answers, true_false_sources as topic_2_true_false_sources
from quiz_data_topic_2 import open_ended_questions as topic_2_open_ended_questions, \
    open_ended_correct_answers as topic_2_open_ended_correct_answers, open_ended_sources as topic_2_open_ended_sources

from quiz_data_topic_3 import mcq_questions as topic_3_mcq_questions, mcq_choices as topic_3_mcq_choices, \
    mcq_correct_answers as topic_3_mcq_correct_answers, mcq_sources as topic_3_mcq_sources
from quiz_data_topic_3 import true_false_questions as topic_3_true_false_questions, \
    true_false_correct_answers as topic_3_true_false_correct_answers, true_false_sources as topic_3_true_false_sources
from quiz_data_topic_3 import open_ended_questions as topic_3_open_ended_questions, \
    open_ended_correct_answers as topic_3_open_ended_correct_answers, open_ended_sources as topic_3_open_ended_sources

from quiz_data_topic_4 import mcq_questions as topic_4_mcq_questions, mcq_choices as topic_4_mcq_choices, \
    mcq_correct_answers as topic_4_mcq_correct_answers, mcq_sources as topic_4_mcq_sources
from quiz_data_topic_4 import true_false_questions as topic_4_true_false_questions, \
    true_false_correct_answers as topic_4_true_false_correct_answers, true_false_sources as topic_4_true_false_sources
from quiz_data_topic_4 import open_ended_questions as topic_4_open_ended_questions, \
    open_ended_correct_answers as topic_4_open_ended_correct_answers, open_ended_sources as topic_4_open_ended_sources

from quiz_data_topic_5 import mcq_questions as topic_5_mcq_questions, mcq_choices as topic_5_mcq_choices, \
    mcq_correct_answers as topic_5_mcq_correct_answers, mcq_sources as topic_5_mcq_sources
from quiz_data_topic_5 import true_false_questions as topic_5_true_false_questions, \
    true_false_correct_answers as topic_5_true_false_correct_answers, true_false_sources as topic_5_true_false_sources
from quiz_data_topic_5 import open_ended_questions as topic_5_open_ended_questions, \
    open_ended_correct_answers as topic_5_open_ended_correct_answers, open_ended_sources as topic_5_open_ended_sources



# Function to check if the user's answer is similar to the correct answer
def is_answer_similar(user_answer, correct_answer, similarity_threshold=0.7):
    similarity = SequenceMatcher(None, user_answer.lower(), correct_answer.lower()).ratio()
    return similarity >= similarity_threshold


correct_answers_count = 0


# Function to conduct a quiz for a single MCQ question
def conduct_mcq_quiz(prompt, choices, correct_answer, source):
    global correct_answers_count  # Use the global variable
    print("\nQuestion:")
    print(prompt)

    # Display answer choices
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Take user input for their choice
    user_choice = input("Enter the number of your choice: ")
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return

    # Check if the user's choice matches the correct answer
    if user_choice == choices.index(correct_answer) + 1:
        print("Your answer is correct!")
        correct_answers_count += 1  # Increment the correct answers count
    else:
        print("Your answer is incorrect.")
        print(f"Correct Answer: {correct_answer}")

    # Print the source after the question
    print(f"Source: {source}")


# Function to conduct a quiz for a single True/False question
def conduct_true_false_quiz(prompt, correct_answer, source):
    global correct_answers_count  # Use the global variable
    print("\nQuestion:")
    print(prompt)

    # Take user input for True/False
    user_answer = input("Your Answer (enter 'True' or 'False'): ").lower()

    if user_answer == "true" and correct_answer or user_answer == "false" and not correct_answer:
        print("Your answer is correct!")
        correct_answers_count += 1  # Increment the correct answers count
    else:
        print("Your answer is incorrect.")
        print(f"Correct Answer: {correct_answer}")

    # Print the source after the question
    print(f"Source: {source}")


# Function to conduct a quiz for a single open-ended question
def conduct_open_ended_quiz(prompt, correct_answer, source):
    global correct_answers_count  # Use the global variable
    print("\nQuestion:")
    print(prompt)

    # Take user input for open-ended question
    user_answer = input("Your Answer: ")

    if is_answer_similar(user_answer, correct_answer):
        print("Your answer is correct!")
        correct_answers_count += 1  # Increment the correct answers count
    else:
        print("Your answer is incorrect.")
        print(f"Correct Answer: {correct_answer}")

    # Print the source after the question
    print(f"Source: {source}")


# Function to choose the type of quiz
def choose_question_type():
    print("Choose the type of questions you want:")
    print("1. Multiple Choice Questions (MCQ)")
    print("2. True/False Questions")
    print("3. Open-ended Questions")

    choice = input("Enter the number of your choice: ")
    return int(choice)


def choose_topic():
    print("Choose the topic for the quiz:")
    print("1. Introduction to NS and Symmetric key encryption")
    print("2. Public key encryption and RSA")
    print("3. Hash, MAC and Digital signature")
    print("4. Random numbers and Stream ciphers")
    print("5. Kerberos and Symmetric key distribution")

    topic_choice = input("Enter the number of your chosen topic: ")
    return int(topic_choice)


# Function to conduct the quiz based on the selected topic and question type
def conduct_quiz(selected_topic, question_type, num_questions_per_topic=10):
    global correct_answers_count
    if selected_topic == 1:
        if question_type == 1:
            questions = list(
                zip(topic_1_mcq_questions, topic_1_mcq_choices, topic_1_mcq_correct_answers, topic_1_mcq_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_mcq_quiz(*questions[index])
        elif question_type == 2:
            questions = list(
                zip(topic_1_true_false_questions, topic_1_true_false_correct_answers, topic_1_true_false_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_true_false_quiz(*questions[index])
        elif question_type == 3:
            questions = list(
                zip(topic_1_open_ended_questions, topic_1_open_ended_correct_answers, topic_1_open_ended_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_open_ended_quiz(*questions[index])
        else:
            print("Invalid choice. Please select a valid question type.")
    elif selected_topic == 2:
        if question_type == 1:
            questions = list(
                zip(topic_2_mcq_questions, topic_2_mcq_choices, topic_2_mcq_correct_answers, topic_2_mcq_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_mcq_quiz(*questions[index])
        elif question_type == 2:
            questions = list(
                zip(topic_2_true_false_questions, topic_2_true_false_correct_answers, topic_2_true_false_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_true_false_quiz(*questions[index])
        elif question_type == 3:
            questions = list(
                zip(topic_2_open_ended_questions, topic_2_open_ended_correct_answers, topic_2_open_ended_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_open_ended_quiz(*questions[index])
        else:
            print("Invalid choice. Please select a valid question type.")
    elif selected_topic == 3:
        if question_type == 1:
            questions = list(
                zip(topic_3_mcq_questions, topic_3_mcq_choices, topic_3_mcq_correct_answers, topic_3_mcq_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_mcq_quiz(*questions[index])
        elif question_type == 2:
            questions = list(
                zip(topic_3_true_false_questions, topic_3_true_false_correct_answers, topic_3_true_false_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_true_false_quiz(*questions[index])
        elif question_type == 3:
            questions = list(
                zip(topic_3_open_ended_questions, topic_3_open_ended_correct_answers, topic_3_open_ended_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_open_ended_quiz(*questions[index])
        else:
            print("Invalid choice. Please select a valid question type.")
    elif selected_topic == 4:
        if question_type == 1:
            questions = list(
                zip(topic_4_mcq_questions, topic_4_mcq_choices, topic_4_mcq_correct_answers, topic_4_mcq_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_mcq_quiz(*questions[index])
        elif question_type == 2:
            questions = list(
                zip(topic_4_true_false_questions, topic_4_true_false_correct_answers, topic_4_true_false_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_true_false_quiz(*questions[index])
        elif question_type == 3:
            questions = list(
                zip(topic_4_open_ended_questions, topic_4_open_ended_correct_answers, topic_4_open_ended_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_open_ended_quiz(*questions[index])
        else:
            print("Invalid choice. Please select a valid question type.")
    elif selected_topic == 5:
        if question_type == 1:
            questions = list(
                zip(topic_5_mcq_questions, topic_5_mcq_choices, topic_5_mcq_correct_answers, topic_5_mcq_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_mcq_quiz(*questions[index])
        elif question_type == 2:
            questions = list(
                zip(topic_5_true_false_questions, topic_5_true_false_correct_answers, topic_5_true_false_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_true_false_quiz(*questions[index])
        elif question_type == 3:
            questions = list(
                zip(topic_5_open_ended_questions, topic_5_open_ended_correct_answers, topic_5_open_ended_sources))
            random.shuffle(questions)
            for index in range(min(len(questions), num_questions_per_topic)):
                conduct_open_ended_quiz(*questions[index])
        else:
            print("Invalid choice. Please select a valid question type.")
    else:
        print("Invalid choice. Please select a valid topic.")

    print("\nQuiz Completed!")
    print(f"You answered {correct_answers_count} out of {num_questions_per_topic} questions correctly.")
    percentage_correct = (correct_answers_count / num_questions_per_topic) * 100
    print(f"Your score: {percentage_correct}%")


# Main function
_name_ = "_main_"
if _name_ == "_main_":
    selected_topic = choose_topic()
    question_type = choose_question_type()
    conduct_quiz(selected_topic, question_type, num_questions_per_topic=10)