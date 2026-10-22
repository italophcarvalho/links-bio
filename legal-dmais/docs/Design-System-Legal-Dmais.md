# Design system - Legal D+ | Link na bio

**Versão:** 1.0  
**Data:** 22/10/2026  
**Projeto:** Cerimonial Infantil Legal D+ / Espaço Legal D+  
**Base:** PRD-Legal-Dmais-Link-na-Bio.md e estrutura de com banner.html.  
**Estado:** proposta de interface para a demonstração de prospecção. A validação comercial e a aprovação do estabelecimento continuam conforme o PRD.

## 1. Direção visual

A interface deve expressar uma marca alegre e acolhedora, com leitura fácil para o adulto que organiza uma festa. Azul conduz a navegação, amarelo destaca a ação principal e rosa, verde e violeta aparecem em detalhes.

Os materiais recebidos apresentam assinatura multicolorida, coroa, balões, fachada azul e amarela e fotografias de festas. As cores abaixo são **valores propostos para a interface a partir dessas referências**. Não foram fornecidos manual oficial, códigos de cor ou fontes da marca.

O logotipo original preserva sua composição e cores quando estiver disponível. Nunito é a fonte da interface; não deve ser usada para redesenhar ou substituir a assinatura original. Os exemplos tipográficos deste documento demonstram a hierarquia da interface.

## 2. Estrutura preservada

1. Banner com fotografia e identificação do negócio.
2. Três acessos rápidos: Instagram, WhatsApp e localização.
3. Cinco cards na ordem do PRD.
4. Rodapé com “Conecte-se”, os três canais e ano automático.

Dentro do banner, a identificação em texto HTML garante que nome e localização continuem legíveis e acessíveis. A fotografia ocupa a faixa superior e uma área azul sólida acomoda os textos abaixo.

Não há alteração de escopo para reservas, pagamentos, galeria interna ou novos blocos de página nesta entrega.

## 3. Paleta e tokens de cor

| Token CSS | Valor | Aplicação |
|---|---|---|
| --ds-primary | #0756A3 | Ação principal, banner e ícones azuis |
| --ds-primary-hover | #064581 | Fundo da ação principal ao passar o ponteiro |
| --ds-primary-soft | #EAF3FF | Fundo suave dos ícones azuis |
| --ds-yellow | #FFD43B | Destaques pequenos e ícone do card principal |
| --ds-pink | #E91E78 | Detalhe decorativo da marca |
| --ds-pink-ink | #AE175B | Ícone de pacotes e Instagram |
| --ds-pink-soft | #FFF0F6 | Fundo suave dos ícones rosas |
| --ds-green | #166534 | WhatsApp e ícone de visita |
| --ds-green-soft | #EDF9F1 | Fundo suave dos ícones verdes |
| --ds-purple | #7E22CE | Ícone de festas realizadas |
| --ds-purple-soft | #F5EEFF | Fundo suave dos ícones violetas |
| --ds-background | #F5F9FF | Fundo da página |
| --ds-surface | #FFFFFF | Cards e acessos rápidos |
| --ds-text | #17335C | Títulos em superfícies claras |
| --ds-text-secondary | #4D6078 | Descrições e informações auxiliares |
| --ds-on-primary | #FFFFFF | Títulos sobre azul |
| --ds-on-primary-secondary | #E3EFFF | Descrições sobre azul |
| --ds-border | #D8E6F4 | Separadores e bordas discretas |
| --ds-focus | #0756A3 | Contorno visível de foco |

### Regras de aplicação

- Fundo geral azul muito claro; cards complementares brancos.
- Somente o card “Consultar data e orçamento” usa fundo azul pleno.
- Amarelo destaca o ícone e a seta desse card.
- Cards complementares ganham cor no fundo suave e no traço do ícone.
- Rosa vivo é decorativo. O texto e o ícone rosa utilizam a variante escura pink-ink.
- Títulos ficam em azul escuro; descrições usam text-secondary.
- Informação e função devem continuar compreensíveis por texto e ícone, além da cor.
- Textos sobre fotografia devem ser deslocados para a faixa azul sólida do banner.

## 4. Tipografia

**Família principal:** Nunito.  
**Pesos:** 400, 600, 700 e 800.  
**Fallback:** system-ui, -apple-system, Segoe UI, sans-serif.  
**Base do navegador:** 16 px. As dimensões tipográficas em CSS são expressas em rem.

| Papel | Tamanho | Entrelinha | Peso | Uso |
|---|---|---|---|---|
| Nome no banner | 32 px / 2 rem | 36 px / 1,125 | 800 | “Legal D+” ou assinatura textual validada |
| Título de card | 16 px / 1 rem | 21,6 px / 1,35 | 800 | Títulos em capitalização de frase |
| Descrição | 14 px / 0,875 rem | 20,3 px / 1,45 | 400 | Texto de apoio dos cards e do banner |
| Texto base | 16 px / 1 rem | 24 px / 1,5 | 400 ou 600 | Conteúdo auxiliar quando necessário |
| Rodapé e rótulos | 12 px / 0,75 rem | 18 px / 1,5 | 400 ou 800 | “Conecte-se” e direitos reservados |

**Composição:** títulos dos cards em caixa normal, sem o espaçamento amplo entre letras do modelo original. Títulos e descrições podem quebrar linha; os cards crescem com o conteúdo e com o zoom.

A fonte oficial da interface está no [repositório Nunito do Google Fonts](https://github.com/google/fonts/tree/main/ofl/nunito). Para a implementação, carregar somente os pesos utilizados e manter font-display: swap.

Exemplo de carregamento:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
```

## 5. Espaçamento, dimensões e superfícies

| Token / elemento | Valor padrão |
|---|---|
| Escala de espaçamento | 4, 8, 12, 16, 20, 24, 32, 40, 48 e 64 px |
| Largura máxima do container | 430 px |
| Margem lateral externa no celular | 12 px |
| Margem interna da lista | 20 px |
| Distância entre cards | 12 px |
| Padding interno do card | 16 px |
| Altura mínima do card | 104 px; altura final automática |
| Caixa de ícone do card | 44 × 44 px |
| Acessos rápidos | 52 × 52 px, separados por 12 px |
| Ícones clicáveis do rodapé | 44 × 44 px, separados por 12 px |
| Fotografia no banner | 180 px de altura; 160 px abaixo de 360 px |
| Raio do container | 32 px |
| Raio do card | 24 px |
| Raio dos acessos rápidos | 18 px |
| Raio das caixas de ícones | 16 px |
| Foco | Contorno azul de 3 px, afastado 3 px |
| Sombra do container | 0 18px 48px rgb(7 86 163 / 0.10) |
| Sombra dos cards | 0 8px 24px rgb(23 51 92 / 0.07) |
| Sombra ao passar o ponteiro | 0 12px 28px rgb(23 51 92 / 0.12) |

A borda clara organiza as superfícies. O contorno azul de foco, os textos e os ícones identificam as ações.

## 6. Componentes

### 6.1. Banner

- Classes: .hero, .hero__image e .hero__content.
- Foto real em largura total, usando object-fit: cover e ponto de recorte inicial em 50% 40%.
- Faixa azul abaixo da fotografia com nome em branco e descrição em azul muito claro.
- Identificação proposta: **Legal D+**.
- Descrição: **Festas infantis em Santa Inês, Vila Velha.**
- Altura total automática: o bloco de texto cresce quando necessário.
- Sem o preço de R$ 3.499 na arte de destaque, enquanto a vigência não for confirmada.

Esqueleto para complementar o interior do banner existente:

```html
<section class="hero" aria-label="Cerimonial Infantil Legal D+">
  <img class="hero__image" src="assets/fachada.webp"
       alt="Fachada do Cerimonial Infantil Legal D+ em Vila Velha"
       width="680" height="453" fetchpriority="high">
  <div class="hero__content">
    <h1>Legal D+</h1>
    <p>Festas infantis em Santa Inês, Vila Velha.</p>
  </div>
</section>
```

O caminho da imagem é um exemplo de organização para a futura implementação. A imagem otimizada ainda deverá ser exportada e colocada nesse destino.

### 6.2. Acessos rápidos

- Instagram: ícone rosa escuro; modificador .quick-action--instagram.
- WhatsApp: ícone verde escuro; modificador .quick-action--whatsapp.
- Localização: ícone azul padrão.
- Superfície branca, alvo de toque de 52 px e nome acessível específico.
- Sobreposição visual de 26 px no limite inferior do banner.
- Os três destinos permanecem definidos no PRD.

### 6.3. Cards de navegação

| Ordem | Conteúdo do PRD | Variante CSS | Ícone sugerido |
|---|---|---|---|
| 1 | Consultar data e orçamento | .link-card--primary | Calendário |
| 2 | Conheça nossos pacotes | .link-card--pink | Presente |
| 3 | Conheça o espaço | .link-card padrão | Casa / espaço |
| 4 | Festas realizadas | .link-card--purple | Imagens |
| 5 | Agende uma visita | .link-card--green | Calendário com confirmação |

Cada card mantém a hierarquia **ícone + título e descrição + seta**. Toda sua área é um único link; não colocar outros links ou botões dentro dele.

A caixa do ícone é de 44 px. O ícone usa área de 24 × 24 px, traço de 2 px e pontas arredondadas. A seta utiliza 20 × 20 px. Ícones decorativos recebem aria-hidden e o texto do card comunica a ação.

Os textos completos e destinos devem ser copiados do PRD. Os exemplos de aplicação devem conservar esses mesmos títulos e descrições.

### 6.4. Rodapé

- “Conecte-se” com 12 px e peso 800.
- Separador discreto, três acessos de 44 px e texto de direitos reservados.
- Nome proposto: Cerimonial Infantil Legal D+.
- Ano preenchido automaticamente pelo comportamento já existente no HTML.
- Instagram, WhatsApp e localização repetem os mesmos destinos dos acessos superiores.

## 7. Estados e movimento

| Estado | Comportamento |
|---|---|
| Padrão | Superfície estável, rótulos visíveis e contraste definido |
| Passagem do ponteiro | Elevação de 2 px e sombra levemente ampliada; CTA escurece para primary-hover |
| Foco de teclado | Contorno de 3 px com afastamento de 3 px, sem depender somente da sombra |
| Pressionado | Escala de 0,99 durante a interação |
| Movimento reduzido | Remover transições, animações e transformações |

- Duração padrão: 180 ms.
- Resposta rápida: 120 ms, disponível como token.
- Curva: cubic-bezier(0.2, 0.7, 0.2, 1).
- A elevação por ponteiro se aplica somente quando o dispositivo oferece hover.
- O CSS não altera destinos, não envia mensagens e não adiciona lógica de reservas.

## 8. Responsividade

| Tela | Comportamento |
|---|---|
| 320-359 px | Margem externa 12 px; lista com 16 px; card com padding 12 px, gap 8 px e caixa de ícone 40 px |
| 360-479 px | Lista com 20 px; card com padding 16 px, gap 12 px e caixa de ícone 44 px |
| A partir de 480 px | Container centralizado com máximo de 430 px e margem externa de 24 px |
| Zoom e texto ampliado | Permitir quebra de linha e crescimento vertical; sem altura fixa nos cards |

A lista continua em uma coluna em todas as larguras. Na largura de 390 px, conferir o primeiro card inteiro na primeira tela de referência de 844 px, como definido no PRD.

Não truncar as descrições com reticências, não usar carrossel horizontal e não depender de hover para revelar informação.

## 9. Imagens e marca

| Asset | Uso no sistema |
|---|---|
| image(6).png | Candidata principal para o banner de reconhecimento da fachada |
| image(4).png e image(7).png | Alternativas para apresentar a estrutura interna |
| image(5).png | Referência de decoração e apoio visual |
| image.png e image(3).png | Referências de festas realizadas |
| image(1).png / image(2).png | Referência visual da marca e da peça comercial; arquivos duplicados |
| image(8).png | Referência complementar; resolução menor |

- Preservar a proporção das fotografias e revisar o recorte em cada largura.
- Ajustes de apresentação devem manter a aparência real do estabelecimento.
- Exportar a fotografia principal para WebP ou AVIF e definir suas dimensões.
- Manter a meta total de carregamento principal do PRD: até 500 KB, a medir na implementação.
- Solicitar o logotipo original para sua aplicação final.
- A arte de compartilhamento será derivada do mesmo banner; referência de exportação: 1200 × 630 px, com nome dentro da área central.

## 10. Contraste e acessibilidade

Os pares abaixo foram calculados com a fórmula de luminância relativa da WCAG. Todos passam de 4,5:1. Esse resultado verifica os pares de cor escolhidos; a navegação, o zoom e a composição final serão verificados após implementar.

| Aplicação | Frente | Fundo | Razão |
|---|---|---|---|
| Título / CTA | #FFFFFF | #0756A3 | 7.32:1 |
| Descrição / CTA | #E3EFFF | #0756A3 | 6.29:1 |
| Título / card | #17335C | #FFFFFF | 12.62:1 |
| Descrição / card | #4D6078 | #FFFFFF | 6.44:1 |
| Texto auxiliar / página | #4D6078 | #F5F9FF | 6.10:1 |
| Ícone sobre amarelo | #17335C | #FFD43B | 8.85:1 |
| Ícone azul | #0756A3 | #EAF3FF | 6.54:1 |
| Ícone rosa | #AE175B | #FFF0F6 | 6.20:1 |
| Ícone verde | #166534 | #EDF9F1 | 6.59:1 |
| Ícone violeta | #7E22CE | #F5EEFF | 6.17:1 |

O sistema adota alvos de toque de pelo menos **44 × 44 px**, com **52 × 52 px** nos acessos superiores, como decisão de conforto. O mínimo AA da WCAG 2.2 para tamanho de alvo é 24 × 24 CSS px, com exceções; esses valores maiores são a escolha desta interface.

Referências oficiais:
- [W3C - Contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- [W3C - Tamanho mínimo de alvo](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## 11. Aplicação ao HTML

1. Carregar Nunito e substituir o bloco de estilos antigo pelo CSS completo incluído na seção 12 deste documento.
2. Preservar os grupos .bio-page, .hero, .quick-actions, .links e .footer.
3. Acrescentar o conteúdo textual .hero__content dentro do banner.
4. Aplicar as variantes de card conforme a tabela de componentes.
5. Aplicar os modificadores de cor aos ícones de Instagram e WhatsApp.
6. Substituir foto, nome, descrições, metadados e destinos pelos dados do PRD.
7. Usar os links preparados do PRD e verificar seus destinos.
8. Conferir as regras de contraste, teclado, toque, zoom e carregamento.

Os tokens e as classes são reutilizáveis para outros clientes; nomes, cores e conteúdo devem ser parametrizados conforme cada identidade.

## 12. CSS completo de referência

Este documento reúne a especificação, os tokens e os estilos. O bloco abaixo pode ser copiado para o HTML ou para uma folha de estilos na implementação.

```css
/* Legal D+ - Design system v1.0 - 22/10/2026
   Proposta de interface baseada no material fornecido.
   Carregar Nunito 400/600/700/800 antes deste arquivo.
   Substitui o bloco de estilos do HTML de referência.
*/
:root {
  color-scheme: light;
  --ds-primary: #0756A3;
  --ds-primary-hover: #064581;
  --ds-primary-soft: #EAF3FF;
  --ds-yellow: #FFD43B;
  --ds-pink: #E91E78;
  --ds-pink-ink: #AE175B;
  --ds-pink-soft: #FFF0F6;
  --ds-green: #166534;
  --ds-green-soft: #EDF9F1;
  --ds-purple: #7E22CE;
  --ds-purple-soft: #F5EEFF;
  --ds-background: #F5F9FF;
  --ds-surface: #FFFFFF;
  --ds-text: #17335C;
  --ds-text-secondary: #4D6078;
  --ds-on-primary: #FFFFFF;
  --ds-on-primary-secondary: #E3EFFF;
  --ds-border: #D8E6F4;
  --ds-focus: #0756A3;
  --ds-font: "Nunito", system-ui, -apple-system, "Segoe UI", sans-serif;
  --ds-font-base: 1rem;
  --ds-font-display: 2rem;
  --ds-font-title: 1rem;
  --ds-font-copy: .875rem;
  --ds-font-caption: .75rem;
  --ds-weight-regular: 400;
  --ds-weight-semibold: 600;
  --ds-weight-bold: 700;
  --ds-weight-extra: 800;
  --ds-space-1: 4px;
  --ds-space-2: 8px;
  --ds-space-3: 12px;
  --ds-space-4: 16px;
  --ds-space-5: 20px;
  --ds-space-6: 24px;
  --ds-space-8: 32px;
  --ds-space-10: 40px;
  --ds-space-12: 48px;
  --ds-space-16: 64px;
  --ds-radius-page: 32px;
  --ds-radius-card: 24px;
  --ds-radius-action: 18px;
  --ds-radius-icon: 16px;
  --ds-radius-pill: 999px;
  --ds-page-max: 430px;
  --ds-page-inset: 12px;
  --ds-section-inset: 20px;
  --ds-icon-box: 44px;
  --ds-quick-size: 52px;
  --ds-footer-size: 44px;
  --ds-hero-image-height: 180px;
  --ds-shadow-page: 0 18px 48px rgb(7 86 163 / .10);
  --ds-shadow-card: 0 8px 24px rgb(23 51 92 / .07);
  --ds-shadow-hover: 0 12px 28px rgb(23 51 92 / .12);
  --ds-duration-fast: 120ms;
  --ds-duration-base: 180ms;
  --ds-ease: cubic-bezier(.2, .7, .2, 1);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  min-height: 100svh;
  padding: 12px 12px 28px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background: var(--ds-background);
  color: var(--ds-text);
  font-family: var(--ds-font);
  font-size: var(--ds-font-base);
  line-height: 1.5;
}
a { color: inherit; text-decoration: none; -webkit-tap-highlight-color: transparent; }
img { display: block; max-width: 100%; }
.bio-page {
  width: 100%;
  max-width: var(--ds-page-max);
  background: var(--ds-background);
  border: 1px solid var(--ds-border);
  border-radius: var(--ds-radius-page);
  box-shadow: var(--ds-shadow-page);
  overflow: hidden;
  isolation: isolate;
}
.hero { position: relative; background: var(--ds-primary); }
.hero__image {
  display: block;
  width: 100%;
  height: var(--ds-hero-image-height);
  object-fit: cover;
  object-position: 50% 40%;
}
.hero__content {
  padding: 20px 24px 42px;
  color: var(--ds-on-primary);
  background: var(--ds-primary);
}
.hero__content h1 {
  margin: 0;
  font-size: var(--ds-font-display);
  font-weight: var(--ds-weight-extra);
  line-height: 1.125;
  letter-spacing: -.02em;
  overflow-wrap: anywhere;
}
.hero__content p {
  margin: 6px 0 0;
  color: var(--ds-on-primary-secondary);
  font-size: var(--ds-font-copy);
  line-height: 1.45;
}
.quick-actions {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: -26px;
  padding: 0 24px 28px;
}
.quick-action, .footer-icon {
  display: grid;
  flex: 0 0 auto;
  place-items: center;
  color: var(--ds-primary);
  background: var(--ds-surface);
  border: 1px solid var(--ds-border);
  transition: transform var(--ds-duration-base) var(--ds-ease),
              box-shadow var(--ds-duration-base) var(--ds-ease);
}
.quick-action {
  width: var(--ds-quick-size);
  height: var(--ds-quick-size);
  border-radius: var(--ds-radius-action);
  box-shadow: var(--ds-shadow-card);
}
.quick-action--instagram, .footer-icon--instagram { color: var(--ds-pink-ink); }
.quick-action--whatsapp, .footer-icon--whatsapp { color: var(--ds-green); }
.icon {
  display: block;
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.icon--brand { fill: currentColor; stroke: none; }
.links {
  display: grid;
  gap: 12px;
  padding: 0 var(--ds-section-inset) 24px;
}
.link-card {
  display: grid;
  grid-template-columns: var(--ds-icon-box) minmax(0, 1fr) 20px;
  align-items: center;
  gap: 12px;
  min-height: 104px;
  padding: 16px;
  background: var(--ds-surface);
  border: 1px solid var(--ds-border);
  border-radius: var(--ds-radius-card);
  box-shadow: var(--ds-shadow-card);
  transition: transform var(--ds-duration-base) var(--ds-ease),
              box-shadow var(--ds-duration-base) var(--ds-ease),
              background-color var(--ds-duration-base) var(--ds-ease);
}
.link-icon {
  display: grid;
  width: var(--ds-icon-box);
  height: var(--ds-icon-box);
  place-items: center;
  border-radius: var(--ds-radius-icon);
  background: var(--ds-primary-soft);
  color: var(--ds-primary);
}
.link-content { min-width: 0; }
.link-content strong {
  display: block;
  margin-bottom: 4px;
  color: var(--ds-text);
  font-size: var(--ds-font-title);
  font-weight: var(--ds-weight-extra);
  line-height: 1.35;
  letter-spacing: 0;
  text-transform: none;
  overflow-wrap: anywhere;
}
.link-content span {
  display: block;
  color: var(--ds-text-secondary);
  font-size: var(--ds-font-copy);
  line-height: 1.45;
  overflow-wrap: anywhere;
}
.arrow { color: var(--ds-primary); }
.arrow .icon { width: 20px; height: 20px; }
.link-card--primary {
  color: var(--ds-on-primary);
  background: var(--ds-primary);
  border-color: var(--ds-primary);
}
.link-card--primary .link-content strong { color: var(--ds-on-primary); }
.link-card--primary .link-content span { color: var(--ds-on-primary-secondary); }
.link-card--primary .link-icon { background: var(--ds-yellow); color: var(--ds-text); }
.link-card--primary .arrow { color: var(--ds-yellow); }
.link-card--pink .link-icon { background: var(--ds-pink-soft); color: var(--ds-pink-ink); }
.link-card--purple .link-icon { background: var(--ds-purple-soft); color: var(--ds-purple); }
.link-card--green .link-icon { background: var(--ds-green-soft); color: var(--ds-green); }
.quick-action:focus-visible, .footer-icon:focus-visible, .link-card:focus-visible {
  outline: 3px solid var(--ds-focus);
  outline-offset: 3px;
}
.quick-action:active, .footer-icon:active, .link-card:active { transform: scale(.99); }
@media (hover: hover) {
  .quick-action:hover, .footer-icon:hover, .link-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--ds-shadow-hover);
  }
  .link-card--primary:hover { background: var(--ds-primary-hover); border-color: var(--ds-primary-hover); }
}
.footer { padding: 4px 24px 28px; text-align: center; }
.footer h2 {
  margin: 0 0 16px;
  color: var(--ds-text);
  font-size: var(--ds-font-caption);
  font-weight: var(--ds-weight-extra);
  letter-spacing: .08em;
  text-transform: uppercase;
}
.divider {
  width: min(100%, 240px);
  height: 1px;
  margin: 0 auto 20px;
  background: var(--ds-border);
}
.footer-icons { display: flex; justify-content: center; gap: 12px; margin-bottom: 16px; }
.footer-icon {
  width: var(--ds-footer-size);
  height: var(--ds-footer-size);
  border-radius: var(--ds-radius-icon);
}
.footer-icon .icon { width: 22px; height: 22px; }
.copyright {
  margin: 0;
  color: var(--ds-text-secondary);
  font-size: var(--ds-font-caption);
  line-height: 1.5;
}
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
}
@media (max-width: 359px) {
  :root { --ds-section-inset: 16px; --ds-icon-box: 40px; --ds-hero-image-height: 160px; }
  .hero__content { padding-inline: 20px; }
  .link-card { padding: 12px; gap: 8px; }
  .link-icon .icon { width: 22px; height: 22px; }
}
@media (min-width: 480px) {
  body { padding: 24px 24px 40px; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .quick-action, .footer-icon, .link-card { transform: none !important; }
}
```

## 13. Verificação e próximos passos

- Dez combinações de cor verificadas por cálculo de contraste, todas acima de 4,5:1.
- Tokens CSS e referências de variáveis conferidos.
- Cinco cards, três acessos rápidos, banner e rodapé conforme o PRD.
- Tipografia, espaçamento, cores, variantes, estados, responsividade e regras de imagens definidos neste documento.

A próxima etapa é aplicar o PRD e este design system ao HTML personalizado do Legal D+ e verificar a página no navegador. A especificação de cores e componentes está concluída; os testes da página serão realizados após a implementação.
