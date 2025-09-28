import pgzrun
WIDTH = 1000
HEIGHT = 1000
score = 0
time_left = 10
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False
questions = []
question_count = 0
question_index = 0
marquee_box = Rect(0,0,900,150)
question_box = Rect(0,0,700,200)
timer_box = Rect(0,0,150,200)
answer_box1 = Rect(0,0,300,200)
answer_box2 = Rect(0,0,300,200)
answer_box3 = Rect(0,0,300,200)
answer_box4 = Rect(0,0,300,200)
skip_box = Rect(0,0,150,400)

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

marquee_box.move_ip(0,0)
question_box.move_ip(0,160)
timer_box.move_ip(750,160)
answer_box1.move_ip(10,370)
answer_box2.move_ip(320,370)
answer_box3.move_ip(10,600)
answer_box4.move_ip(320,600)
skip_box.move_ip(750,400)

def draw():
    global marquee_message
    screen.clear()
    screen.fill("red")
    screen.draw.filled_rect(marquee_box,"yellow")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(timer_box,"green")
    screen.draw.filled_rect(answer_box1,"orange")
    screen.draw.filled_rect(answer_box2,"orange")
    screen.draw.filled_rect(answer_box3,"orange")
    screen.draw.filled_rect(answer_box4,"orange")
    screen.draw.filled_rect(skip_box,"pink")

    marquee_message = "Welcome to quiz master"
    marquee_message  = marquee_message + f" Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box, color = "blue")
    screen.draw.textbox(
        str(time_left),timer_box,
        color="white", shadow=(0.5, 0.5),
        scolor="dim grey"
    )
    screen.draw.textbox(
        "Skip", skip_box,
        color="black", angle=-90
    )
    screen.draw.textbox(
        question[0].strip(), question_box,
        color="white", shadow=(0.5,0.5),
        scolor="dim grey"
    )
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color = "blue")
        index = index + 1
        
def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right<0:
        marquee_box.left=WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")


def game_over():
    global question, time_left, is_game_over
    message = f"Game over! \nYou got {score} questions correct!"
    question = [message, "-","-","-","-",5]
    time_left = 0 
    is_game_over = True

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index+=1
    
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left, questions
    score+=1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def skip_question():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)



pgzrun.go()
    

