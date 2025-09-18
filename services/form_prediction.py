import pandas as pd

def media_movel_simples(serie_dados, tamanho_janela):
  """
  Calcula a previsão usando a Média Móvel Simples.

  Args:
    serie_dados (list ou pd.Series): A série temporal de dados.
    tamanho_janela (int): O número de períodos anteriores para usar no cálculo da média.

  Returns:
    float: O valor previsto para o próximo período.
  """
  # Pega os últimos 'tamanho_janela' pontos da série
  ultimos_pontos = serie_dados[-tamanho_janela:]
  
  # Calcula e retorna a média
  return sum(ultimos_pontos) / tamanho_janela

# --- Exemplo de Uso ---
# Série de dados históricos (ex: vendas diárias)
dados_vendas = [50, 52, 55, 53, 56, 58, 60, 59, 61, 63]
serie = pd.Series(dados_vendas)

# Prever o próximo valor usando os últimos 3 dias
previsao_mms = media_movel_simples(serie, 3)

print(f"Dados históricos: {dados_vendas}")
print(f"Previsão com Média Móvel Simples (janela=3): {previsao_mms:.2f}")
# A previsão será a média de [59, 61, 63]