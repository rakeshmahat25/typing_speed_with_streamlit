import streamlit as st
import random as rd
import time

# Sample texts for the typing test
texts = [
    "A paragraph is a self-contained unit of discourse in writing.",
    "Mastering the skill of typing is a valuable asset in today's digital world. From composing emails to coding, the ability to type efficiently can significantly boost productivity. When you start learning to type, it's normal to make mistakes and feel a bit clumsy. ",
    "However, with consistent practice, you'll find your fingers beginning to move more naturally across the keyboard. One of the best methods to enhance your typing skill is to practice with texts that you enjoy. It could be an excerpt from your favorite book, a news article, or even song lyrics. ",
    "Typing unfamiliar words and phrases also helps expand your vocabulary and trains your brain to react quickly to different letter combinations. As you type, remember to sit comfortably, maintain a good posture, and position your hands correctly.",
    "Your eyes should stay on the screen while your fingers do the work. Developing this habit will help you achieve speed without compromising accuracy. Keep challenging yourself with longer texts, and don't be afraid to make mistakes; they are part of the learning process.",
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet, making it a great way to practice typing. As you type, focus on accuracy first, then gradually increase your speed. Remember to keep your fingers on the home row keys and use the correct finger for each key press. With consistent practice, your typing skills will improve, allowing you to type with speed and confidence.",
    "Typing is a skill that requires both precision and speed. It is important to practice regularly to improve your accuracy and fluency. The best typists are those who can maintain a balance between fast typing and minimal errors. When you practice typing, make sure to focus on each word and use the correct finger placement.",
    "Over time, your muscle memory will improve, and you’ll be able to type without looking at the keyboard. The key to becoming a proficient typist is patience, as improvements come gradually. You might find it helpful to practice with different kinds of text, such as articles, stories, or even random phrases. This will prepare you for various real-life typing scenarios. Stay relaxed, breathe, and type each word as if it were the most important part of the sentence.",
    "Technology has revolutionized the way we live and work, transforming daily tasks into simpler and more efficient processes. With each passing year, new advancements in technology continue to shape our world. From smartphones that connect us to the internet anywhere, to artificial intelligence that helps businesses make smarter decisions, technology is a powerful tool. As you practice typing this text, focus on maintaining a steady rhythm. Typing at a consistent speed can sometimes be more effective than rushing and making errors. Remember, accuracy is the foundation upon which speed is built.",
    "Success is not achieved overnight; it is the result of countless hours of dedication, hard work, and perseverance. Each small step taken toward a goal is a building block of a larger achievement. As you work to improve your typing skills, you may encounter moments of frustration. During those times, remind yourself that every expert was once a beginner. Practicing regularly, even for a few minutes each day, can lead to significant improvement over time. The key is to be consistent, patient, and committed to your growth. This approach applies not just to typing but to every aspect of life.",
    "The journey of a thousand miles begins with a single step. This saying applies to many aspects of life, especially when learning new skills. Typing may seem difficult at first, but with patience and daily practice, it gradually becomes second nature. The more you practice, the more your fingers will learn to glide across the keyboard with ease. Typing speed is not just about pressing keys quickly but also about being comfortable with the layout of the keyboard. Remember to stay relaxed and let your fingers find their rhythm as you type.",
    "Reading opens up new worlds and ideas that enrich our minds. Through books and stories, we can experience different cultures, histories, and perspectives. Reading also enhances our vocabulary and understanding of language, making us better communicators. As you practice typing this passage, focus on maintaining a consistent speed. Typing fluently allows you to put your thoughts into words efficiently, whether you are writing an email, a research paper, or a creative story. The ability to type fast and accurately is a crucial skill in almost every profession.",
    "Nature has a way of reminding us of the beauty in simplicity. A walk in the park, the rustle of leaves in the wind, and the warmth of the sun on our faces can bring a sense of peace and calm. In today’s fast-paced world, it's easy to overlook these small pleasures. Typing, too, can be a mindful activity if you allow it to be. Focus on each word, feel the movement of your fingers, and listen to the gentle clicks of the keyboard. In doing so, you not only enhance your typing speed but also learn to appreciate the process.",
    "Creativity is at the heart of human progress. It is through creativity that we invent, innovate, and bring new ideas to life. Whether you are writing a novel, coding a new app, or solving a complex problem, creativity plays a central role. Typing serves as a bridge between our thoughts and the digital world, allowing us to express ideas quickly and efficiently. The more fluent you become in typing, the more easily you can capture your creative thoughts as they occur. So, keep practicing, and let your fingers dance across the keyboard as you bring your ideas to life."
]

def mistake(partest, user):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != user[i]:
                error += 1
        except IndexError:
            error += 1
    return error

# Function to calculate typing speed
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    if time_R == 0:  # Prevent division by zero
        return 0
    speed = len(userinput) / time_R
    return round(speed, 2)

# Streamlit app layout
st.title("Typing Speed Test")

if 'test_text' not in st.session_state:
    st.session_state['test_text'] = rd.choice(texts)

st.write("Type the following text:")

# Display the original test text
test_text = st.session_state['test_text']
st.text_area("Original Text", value=test_text, height=180, disabled=True)

# Get user input
user_input = st.text_area("Your Input", height=100)
start_time = st.session_state.get('start_time', None)

# Record the start time
if start_time is None:
    if user_input == "":
        st.session_state['start_time'] = time.time()

# Submit button to calculate speed and mistakes
if st.button("Submit"):
    end_time = time.time()

    # Calculate speed and mistakes
    speed = speed_time(st.session_state['start_time'], end_time, user_input)
    errors = mistake(test_text, user_input)

    st.write(f"Typing Speed: {speed} characters per second")
    st.write(f"Errors: {errors}")

# "Reload Test" button to reset the session and start a new test
if st.button("Reload Test"):
    st.session_state['test_text'] = rd.choice(texts)
    st.session_state['start_time'] = None

    # Clear input by resetting the page
    st.experimental_set_query_params(reload_test="true")

    