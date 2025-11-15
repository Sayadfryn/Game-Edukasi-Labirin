import random

class Question:
    def __init__(self):
        self.all_shapes = ['square', 'triangle', 'circle', 'trapezoid', 'rectangle', 'pentagon']
        
        self.question_bank = [
            {
                'shape1': 'square',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Persegi (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'triangle',
                'answer': 'square',
                'explanation': 'Segitiga + Segitiga = Persegi (2 segitiga dapat membentuk persegi)'
            },
            {
                'shape1': 'square',
                'shape2': 'square',
                'answer': 'rectangle',
                'explanation': 'Persegi + Persegi = Persegi Panjang (2 persegi membentuk persegi panjang)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'square',
                'answer': 'pentagon',
                'explanation': 'Segitiga (3 sisi) + Persegi (4 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'rectangle',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Persegi Panjang (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'trapezoid',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Trapesium (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'trapezoid',
                'answer': 'pentagon',
                'explanation': 'Segitiga (3 sisi) + Trapesium (4 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'rectangle',
                'shape2': 'square',
                'answer': 'rectangle',
                'explanation': 'Persegi Panjang (4 sisi) + Persegi (4 sisi) = Gabungan bentuk segi empat (seperti persegi panjang lebih panjang)'
            }
        ]
        
        self.current_question = None
        self.used_questions = []
        self.generate_new_question()
    
    def generate_new_question(self):
        if len(self.used_questions) >= len(self.question_bank):
            self.used_questions = []
        
        available_questions = [q for q in self.question_bank if q not in self.used_questions]
        selected_question = random.choice(available_questions)
        self.used_questions.append(selected_question)
        
        answer = selected_question['answer']
        options = [answer]
        
        wrong_options = [s for s in self.all_shapes if s != answer]
        random.shuffle(wrong_options)
        options.extend(wrong_options[:3])
        
        random.shuffle(options)
        
        self.current_question = {
            'shape1': selected_question['shape1'],
            'shape2': selected_question['shape2'],
            'answer': answer,
            'options': options,
            'explanation': selected_question['explanation']
        }
    
    def check_answer(self, answer):
        return answer == self.current_question['answer']