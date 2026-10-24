from flask import Flask, render_template, request

app = Flask(__name__)


def to_decimal(value: str, base: str) -> int:
    value = value.strip()
    if not value:
        raise ValueError("Digite um valor para converter.")

    if base == "decimal":
        return int(value)
    if base == "binary":
        return int(value, 2)
    if base == "hexadecimal":
        normalized = value.lower().removeprefix("0x")
        return int(normalized, 16)
    if base == "octal":
        return int(value, 8)
    raise ValueError("Base inválida.")


def format_number(value: int, base: str) -> str:
    if base == "decimal":
        return str(value)
    if base == "binary":
        return bin(value)[2:]
    if base == "hexadecimal":
        return hex(value)[2:].upper()
    if base == "octal":
        return oct(value)[2:]
    raise ValueError("Base inválida.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/integrantes')
def integrantes():
    membros = [
        {"nome": "Felippe", "funcao": "Desenvolveu a estrutura inicial da página inicial e o design visual."},
        {"nome": "Jean", "funcao": "Implementou as funções de conversão de bases em Python e a lógica do Flask."},
        {"nome": "Lucas", "funcao": "Organizou a apresentação dos resultados e a interface dos formulários de conversão."},
    ]
    return render_template('integrantes.html', membros=membros)


@app.route('/conversao', methods=['GET', 'POST'])
def conversao():
    result = None
    error = None

    if request.method == 'POST':
        conversion = request.form.get('conversion')
        value = request.form.get('valor', '').strip()

        try:
            if conversion == 'decimal_binario':
                decimal = to_decimal(value, 'decimal')
                result = {
                    'titulo': 'Decimal para Binário',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'binary'),
                }
            elif conversion == 'decimal_hexadecimal':
                decimal = to_decimal(value, 'decimal')
                result = {
                    'titulo': 'Decimal para Hexadecimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'hexadecimal'),
                }
            elif conversion == 'decimal_octal':
                decimal = to_decimal(value, 'decimal')
                result = {
                    'titulo': 'Decimal para Octal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'octal'),
                }
            elif conversion == 'binario_decimal':
                decimal = to_decimal(value, 'binary')
                result = {
                    'titulo': 'Binário para Decimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'decimal'),
                }
            elif conversion == 'binario_hexadecimal':
                decimal = to_decimal(value, 'binary')
                result = {
                    'titulo': 'Binário para Hexadecimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'hexadecimal'),
                }
            elif conversion == 'binario_octal':
                decimal = to_decimal(value, 'binary')
                result = {
                    'titulo': 'Binário para Octal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'octal'),
                }
            elif conversion == 'hexadecimal_binario':
                decimal = to_decimal(value, 'hexadecimal')
                result = {
                    'titulo': 'Hexadecimal para Binário',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'binary'),
                }
            elif conversion == 'hexadecimal_decimal':
                decimal = to_decimal(value, 'hexadecimal')
                result = {
                    'titulo': 'Hexadecimal para Decimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'decimal'),
                }
            elif conversion == 'hexadecimal_octal':
                decimal = to_decimal(value, 'hexadecimal')
                result = {
                    'titulo': 'Hexadecimal para Octal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'octal'),
                }
            elif conversion == 'octal_binario':
                decimal = to_decimal(value, 'octal')
                result = {
                    'titulo': 'Octal para Binário',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'binary'),
                }
            elif conversion == 'octal_decimal':
                decimal = to_decimal(value, 'octal')
                result = {
                    'titulo': 'Octal para Decimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'decimal'),
                }
            elif conversion == 'octal_hexadecimal':
                decimal = to_decimal(value, 'octal')
                result = {
                    'titulo': 'Octal para Hexadecimal',
                    'valor_original': value,
                    'valor_convertido': format_number(decimal, 'hexadecimal'),
                }
            else:
                raise ValueError("Conversão inválida.")
        except ValueError as exc:
            error = str(exc)

    return render_template('conversao.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)
