import pygame
import math
from pygame.locals import *
from screens import Menu
from screens import Question
from screens import Answer
from screens import Info

class Game:
    # Game constants
    WIDTH = 1024
    HEIGHT = 768
    GAME_NAME = 'Jogo dos Grafos'
    INTRO_TEXT = 'Identifique\n os grafos bipartidos'
    
    #Screens
    MENU = 1
    QUESTION = 2
    ANSWER = 3
    INFO = 4

    #Question state
    CORRECT_ANSWER = 1
    WRONG_ANSWER = 2
    TIMES_UP = 3

    running = True
    current_question = 0
    max_questions = 0

    corrects_ans = 0
    wrong_ans = 0

    current_graph = None
    current_screen = MENU
    state_question = CORRECT_ANSWER
    graphs = []
    num_graph = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.menu_screen = Menu(self)
        self.question_screen = Question(self)
        self.answer_screen = Answer(self)
        pygame.display.set_caption(self.GAME_NAME)
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        
        self.clock = pygame.time.Clock()

    def run(self, graphs):
        menu_screen = Menu(self)
        question_screen = Question(self)
        answer_screen = Answer(self)
        info_screen = Info(self)
        pygame.init()
        self.graphs = graphs
        self.max_questions = len(graphs)
        while self.running:
            if self.current_screen==self.MENU:
                self.corrects_ans = 0
                self.wrong_ans = 0
                menu_screen.run()
            elif self.current_screen==self.QUESTION:
                question_screen.run()
            elif self.current_screen==self.ANSWER:
                 answer_screen.run()
            elif self.current_screen==self.INFO:
                 info_screen.run()

    def quit_game(self):
        self.running = False

    def change_screen(self, screen):
        self.current_screen = screen

    def start_game(self):
        self.current_screen = self.QUESTION
    
    def answer_question(self, ans):
        if self.current_graph.bipartite() == ans:
            self.corrects_ans+=1
            self.state_question = self.CORRECT_ANSWER
        else:
            self.wrong_ans+=1
            self.state_question = self.WRONG_ANSWER
        self.current_screen = self.ANSWER

    def no_answer_question(self):
        self.current_graph.bipartite()
        self.state_question = self.TIMES_UP
        self.current_screen = self.ANSWER

    def next_question(self):
        self.current_question = (self.current_question+1)%self.max_questions #cicle
        self.current_screen = self.QUESTION
