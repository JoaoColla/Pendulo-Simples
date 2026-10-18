# Análise Experimental de Pêndulo Simples — OHA

Trabalho prático desenvolvido para a disciplina de **Física Teórica 2** do curso de **Engenharia de Computação** da **Universidade Tecnológica Federal do Paraná (UTFPR) — Câmpus Curitiba**.

O projeto utiliza visão computacional (**OpenCV**) para rastrear a posição de um pêndulo simples em vídeo e ajustar os dados experimentais ao modelo teórico do **Oscilador Harmônico Amortecido (OHA)** utilizando **Python**, **SciPy** e **Matplotlib**.

---

##  Contexto Acadêmico

- **Instituição:** Universidade Tecnológica Federal do Paraná (UTFPR) — Câmpus Curitiba
- **Curso:** Engenharia de Computação
- **Disciplina:** Física Teórica 2
- **Objetivo:** Coleta experimental de dados físicos via processamento de imagem, regressão não linear para extração dos parâmetros do OHA e determinação do Fator de Qualidade ($Q$).

---

##  Funcionalidades

- **Detecção de Massa por Binarização:** Isolamento da massa escura em fundo claro usando conversão para escala de cinza e limiarização adaptativa (`cv2.threshold`).
- **Rastreamento de Centroide:** Cálculo da posição $(x, y)$ em tempo real frame a frame por momentos geométricos (`cv2.moments`).
- **Exportação de Dados:** Geração automática da tabela de tempo e coordenadas no formato `.csv`.
- **Ajuste Físico de Curva:** Centralização do referencial na posição de equilíbrio ($x_0$) e regressão não linear via `scipy.optimize.curve_fit`.
- **Cálculo de Parâmetros Físicos:** Extração de amplitude ($A$), coeficiente de amortecimento ($b$), frequência angular ($\omega$), fase inicial ($\phi$) e Fator de Qualidade ($Q$).
- **Visualização Gráfica:** Plotagem comparativa entre os pontos experimentais coletados e a curva teórica do OHA.

---

##  Modelo Físico

A equação ajustada aos dados da posição horizontal $x(t)$ é dada por:

$$x(t) = A \cdot e^{-b t} \cdot \cos(\omega t + \phi)$$

Onde:
- $A$: Amplitude inicial (em pixels)
- $b$: Coeficiente de amortecimento ($s^{-1}$)
- $\omega$: Frequência angular ($\text{rad}/s$)
- $\phi$: Fase inicial ($\text{rad}$)
- $Q$: Fator de qualidade do oscilador, calculado por:

$$Q = \frac{\omega}{2b}$$

---

##  Pré-requisitos e Instalação

Certifique-se de ter o Python 3.8+ instalado. Instale as bibliotecas necessárias executando:

```bash
pip install opencv-python pandas numpy scipy matplotlib