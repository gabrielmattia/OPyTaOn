from rply import LexerGenerator
import sys




def constroi_regras(lg):
	# insere as regras de formação (expressões regulares) dos tokens da linguagem
	#PREDEFINED IDENTIFIERS
	lg.add('VOID', r'void')
	lg.add('BOOLEAN', r'boolean')
	lg.add('TRUE', r'true')
	lg.add('FALSE', r'false')
	lg.add('READ', r'read')
	lg.add('INTEGER', r'integer')
	lg.add('WRITE', r'write')
	lg.add('LABELS', r'labels')
	lg.add('TYPES', r'types')
	lg.add('VARS', r'vars')
	lg.add('VAR', r'var')
	lg.add('GOTO', r'goto')
	lg.add('RETURN', r'return')
	lg.add('IF', r'if')
	lg.add('ELSE', r'else')
	lg.add('WHILE', r'while')


	lg.add('FUNCTIONS', r'functions')

	# Simbolos de comparacoes
	lg.add('EQUAL', r'\==')
	lg.add('ATTR', r'\=')
	lg.add('NOTEQUAL', r'!=')
	lg.add('NOT', r'\!')
	lg.add('GREATEREQUALTHAN', r'>=')
	lg.add('GREATERTHAN', r'>')
	lg.add('LESSEREQUALTHAN', r'<=')
	lg.add('LESSERTHAN', r'<')
	lg.add('OR', r'\|\|')
	lg.add('AND', r'\&\&')

	# Simbolos especificos de operacoes matematicas e da linguagem
	lg.add('NUMBER', r'\d+')
	lg.add('PLUS', r'\+')
	lg.add('MINUS', r'-')
	lg.add('MUL', r'\*')
	lg.add('DIV', r'/')
	lg.add('LPAREN', r'\(')
	lg.add('RPAREN', r'\)')
	lg.add('LCHAVE', r'\{')
	lg.add('RCHAVE', r'\}')
	lg.add('COMMA', r'\,')
	lg.add('SEMICOLON', r'\;')
	lg.add('COMMA', r'\,')
	lg.add('COLON', r'\:')
	lg.add('LBRACKET', r'\[')
	lg.add('RBRACKET', r'\]')
	lg.add('COLON', r'\:')


	# Simbolos alfa-numericos 
	lg.add('ID', r'[a-z][a-z0-9]*')


	lg.add('MOD', r'%')

	# cria uma regra para ignorar caracteres de espaços
	lg.ignore('\s+')
	lg.ignore('\#.+')

if __name__ == '__main__':

	# cria um objeto LexerGenerator
	lg = LexerGenerator()
	constroi_regras(lg)

	# contrói o analisador léxico
	lexer = lg.build()
	arquivo=open(sys.argv[1])
	reserved = ["integer", "boolean", "true", "false", 'read','write','void','functions','while',
				'if','else','return','goto','var','vars']

	i=1;
	for linha in arquivo:
		linha = linha.strip()
		token=lexer.lex(linha.lower()) 
		try:
			for t in token:
				
				if t.name == "ID" and t.value.lower() in reserved:
				# yield t(t.value.upper(), t.value)
					print(f'< {i}, RESERVED , {t.value:^9} >')
				else:
					print(f'< {i:^2}, {t.name:^16}, {t.value:^9} >')


		except:
			print(f'Erro lexico, linha {i} ')
		i+=1
