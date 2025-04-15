
def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión está vacía.")

    try:
        # Validar que solo haya números, espacios, guiones y puntos decimales
        for char in expression:
            if not (char.isdigit() or char in " -.\t"):
                raise ValueError("Caracter inválido en la expresión.")

        # Reemplazar múltiples espacios
        expression = expression.replace('\t', ' ').strip()

        # Separar por el operador de resta y procesar
        tokens = expression.split('-')
        if not tokens[0].strip():
            result = -float(tokens[1])
            tokens = tokens[2:]
        else:
            result = float(tokens[0])

        for token in tokens[1:] if not expression.startswith('-') else tokens:
            token = token.strip()
            if token:
                result -= float(token)

        return result
    except ZeroDivisionError:
        raise
    except ValueError as ve:
        raise ve
    except Exception:
        raise SyntaxError("Sintaxis inválida.")

def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión está vacía.")
    
    try:
        for char in expression:
            if not (char.isdigit() or char in " +.\t-"):
                raise ValueError("Caracter inválido en la expresión.")

        expression = expression.replace('\t', ' ').strip()
        tokens = expression.split('+')
        result = 0.0

        for token in tokens:
            if token.strip():
                result += float(token.strip())

        return result
    except Exception:
        raise SyntaxError("Sintaxis inválida.")


def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión está vacía.")
    
    try:
        for char in expression:
            if not (char.isdigit() or char in " +.\t-"):
                raise ValueError("Caracter inválido en la expresión.")

        expression = expression.replace('\t', ' ').strip()
        tokens = expression.split('+')
        result = 0.0

        for token in tokens:
            if token.strip():
                result += float(token.strip())

        return result
    except Exception:
        raise SyntaxError("Sintaxis inválida.")


def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión está vacía.")

    try:
        for char in expression:

            if not (char.isdigit() or char in " /.\t-"):
                raise ValueError("Caracter inválido en la expresión.")

        expression = expression.replace('\t', ' ').strip()
        tokens = expression.split('/')
        
        if len(tokens) < 2:
            raise SyntaxError("Sintaxis inválida.")
        
        result = float(tokens[0].strip())
        for token in tokens[1:]:
            divisor = float(token.strip())
            if divisor == 0:
                raise ZeroDivisionError("División por cero.")
            result /= divisor

        return result
    except ZeroDivisionError:
        raise

            if not (char.isdigit() or char in " *.\t-"):
                raise ValueError("Caracter inválido en la expresión.")

        expression = expression.replace('\t', ' ').strip()
        tokens = expression.split('*')
        result = 1.0

        for token in tokens:
            if token.strip():
                result *= float(token.strip())

        return result

    except Exception:
        raise SyntaxError("Sintaxis inválida.")
