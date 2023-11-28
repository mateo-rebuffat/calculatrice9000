import re

class Calculator:
    def __init__(self):
        self.history = []

    def run_calculator(self):
        while True:
            option = input("Choisissez une option:\n"
                           "1. Entrez une expression mathématique\n"
                           "2. Afficher l'historique\n"
                           "3. Effacer l'historique\n"
                           "4. Quitter\n"
                           "Choix: ")

            if option == '1':
                expression = input("Entrez une expression mathématique: ")
                try:
                    result = self.evaluate_expression(expression)
                    print(f"Résultat: {result}")
                    self.history.append(expression)
                except (ValueError, ZeroDivisionError, SyntaxError) as e:
                    print(f"Erreur: {str(e)}")
            elif option == '2':
                self.display_history()
            elif option == '3':
                self.clear_history()
            elif option == '4':
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def evaluate_expression(self, expression):
      # Vérifiez si l'expression est valide
        if not re.match(r'^[0-9+\-*/. ]+$', expression):
            raise ValueError("Expression invalide")

        # Évaluez l'expression en respectant les priorités opératoires
        operators = {'*': (lambda x, y: x * y), '/': (lambda x, y: x / y),
                     '+': (lambda x, y: x + y), '-': (lambda x, y: x - y)}

        numbers = [float(x) for x in re.split(r'[-+*/]', expression)]
        operations = re.findall(r'[-+*/]', expression)

        # Effectuez les opérations en respectant les priorités
        for op in ['*', '/']:
            while op in operations:
                index = operations.index(op)
                result = operators[op](numbers[index], numbers[index + 1])
                numbers[index] = result
                del numbers[index + 1]
                del operations[index]

        for op in ['+', '-']:
            while op in operations:
                index = operations.index(op)
                result = operators[op](numbers[index], numbers[index + 1])
                numbers[index] = result
                del numbers[index + 1]
                del operations[index]

        return numbers[0]
    
    def display_history(self):
        if not self.history:
            print("Historique vide.")
        else:
            print("Historique des calculs:")
            for i, expr in enumerate(self.history, start=1):
                print(f"{i}. {expr}")

    def clear_history(self):
        self.history = []
        print("Historique effacé.")

# Exécution de la calculatrice
calculator = Calculator()
calculator.run_calculator()

# Affichage de l'historique
calculator.display_history()

# Effacement de l'historique
calculator.clear_history()