# PRD — Link na bio | Cerimonial Infantil Legal D+

**Versão:** 1.0  
**Data:** 22/10/2026  
**Responsável pelo projeto:** Italo Carvalho  
**Finalidade desta versão:** especificar uma demonstração de prospecção personalizada para o negócio.  
**Estado da entrega:** requisitos e conteúdo propostos; implementação, validação com o estabelecimento e publicação ainda não realizadas.  
**Referência estrutural:** arquivo fornecido **com banner.html**.  
**Próxima etapa solicitada:** criação do design system, após a conclusão deste PRD.

## 1. Objetivo do produto

Criar uma página para o link da bio do Instagram que apresente o Legal D+, organize seus canais e facilite consultas de data, orçamento, pacotes e visitas.

O produto deve manter a estrutura principal do HTML de referência: banner, três ícones de acesso rápido, cinco cards de links e rodapé. A identidade visual será adaptada à marca do estabelecimento na etapa do design system.

A ação principal é abrir uma conversa no WhatsApp para consultar disponibilidade e orçamento. Consultas de data e visitas dependem da resposta da equipe; o clique não realiza uma reserva nem confirma disponibilidade.

### Público e percurso principal

- **Público inicial:** pessoas e famílias buscando um local para realizar festas infantis em Vila Velha e região. Esta definição é uma hipótese de público para orientar a demonstração.
- **Entrada principal:** link da bio do Instagram; o endereço também poderá ser compartilhado pelo WhatsApp e por QR Code.
- **Percurso esperado:** reconhecer o estabelecimento no banner, selecionar um card e acessar o canal correspondente.
- **Resultado desejado:** iniciar uma conversa de orçamento ou combinar uma visita. A melhoria de conversão é um objetivo a medir, sem resultado garantido nesta fase.

## 2. Base de informações e grau de confirmação

Os dados abaixo provêm do texto e das imagens enviados pelo usuário. As fontes externas não puderam ser consultadas com sucesso nesta preparação; os dados não foram confirmados independentemente com o estabelecimento.

| Informação | Registro disponível | Tratamento no projeto |
|---|---|---|
| Nome informado | Cerimonial Infantil Legal D+ | Nome de referência para identificação e metadados. |
| Marca na peça promocional | Espaço Legal D+ — Cerimonial e Festas | Referência de assinatura visual; confirmar a grafia preferida para a página. |
| Segmento | Local para eventos; festas infantis | Orienta a apresentação e os links. |
| Endereço | Rua Santa Luzia, 78 — Santa Inês, Vila Velha — ES, CEP 29108-035 | Usar no destino de localização; conferir antes da publicação. |
| Telefone | (27) 98883-1009 | O mesmo número é apresentado como WhatsApp na peça promocional. |
| WhatsApp normalizado | +55 27 98883-1009 | Número de destino proposto para as conversas. |
| Instagram | @cerimoniallegaldmais | Perfil fornecido pelo usuário. |
| Google | 44 avaliações; o trecho copiado indica nota 4,2/5 | Registro do material enviado. Quantidade e nota precisam de conferência antes de qualquer destaque numérico. |
| Facebook | Trecho fornecido informa 5/5 e 29 votos | Fonte distinta do Google; não combinar notas ou contagens. |
| Horário | “Fechado · Abre às 09:00” | Informação incompleta. Solicitar dias e horários; não inferir funcionamento diário ou situação “aberto agora”. |
| Referência de localização na peça | Próximo ao Franguinho do Gilsom | Referência complementar, sujeita a confirmação. |
| Frase na peça | “Aqui sua festa se torna um momento especial!” | Texto existente da marca, disponível como referência de conteúdo. |

### 2.1. Oferta documentada na peça promocional

As imagens **image(1).png** e **image(2).png** são cópias idênticas da mesma peça. Ela anuncia:

- Festa completa para **até 39 convidados**.
- Preço de **R$ 3.499**, apresentado como “valor fixo”.
- Decoração.
- Buffet completo.
- Espaço climatizado.
- Brinquedos diversos.
- Mesas e cadeiras.
- Área para churrasco.
- Espaço e cozinha completa e estruturada.

**Validade e condições da oferta não foram informadas.** O anúncio deve ser registrado como evidência do material recebido. Para esta primeira versão, o card de pacotes direcionará à equipe, sem publicar preço, validade ou condições como oferta atual.

O limite de 39 convidados pertence ao pacote anunciado. **A capacidade máxima do espaço permanece desconhecida.**

Um comentário fornecido por Cristina Oliveira menciona contratação do pacote completo ou somente do espaço. Essa modalidade de locação precisa de confirmação do estabelecimento antes de se tornar uma promessa da página.

### 2.2. Informações provenientes de avaliações

Os relatos enviados mencionam ambiente climatizado, brinquedos, atendimento, buffet e experiências em festas. Exemplos rastreáveis no texto do usuário:

| Autor | Informação mencionada | Limite da evidência |
|---|---|---|
| Cristina Oliveira | Brinquedos, Xbox, atendimento e opção de pacote completo ou somente espaço | Relato de cliente; confirmar oferta e equipamentos atuais. |
| Thiago Lorencini | Estrutura para festas infantis, brinquedos e fraldário | Avaliação indicada como antiga; confirmar estrutura atual. |
| Leiliany Teixeira | Atendimento, organização, climatização e localização | Opinião atribuída à autora. |
| Morgana Fonseca | Ambiente climatizado, espaço e acesso | Opinião atribuída à autora. |
| Kleber Venancio da Silva Paschoal | Atendimento e buffet | Opinião atribuída ao autor. |

As avaliações ajudam a identificar assuntos relevantes. Depoimentos e notas não fazem parte dos blocos adicionais desta versão; eventual uso futuro deve preservar a autoria e o sentido do relato.

## 3. Estrutura da página

### 3.1. Correspondência com o HTML de referência

| Bloco existente | Aplicação ao Legal D+ | Requisito |
|---|---|---|
| Container principal — .bio-page | Página centralizada, com largura confortável no celular | Preservar a organização em uma coluna. |
| Banner — .hero / .hero__image | Foto do estabelecimento ou de sua estrutura, acompanhada da marca | Preservar o bloco de destaque e adaptar a imagem ao recorte responsivo. |
| Acessos rápidos — .quick-actions | Instagram, WhatsApp e localização | Manter três acessos com nomes acessíveis. |
| Links — .links / .link-card | Cinco cards adaptados ao negócio | Cada card terá ícone, título, descrição e seta; toda sua área será clicável. |
| Rodapé — .footer | “Conecte-se”, três ícones e identificação do negócio | Reutilizar os mesmos destinos e manter o ano automático. |

A estrutura visual será a mesma do modelo. Cores, fontes, elementos decorativos, tratamento das imagens e estados dos componentes serão especificados no design system.

### 3.2. Banner

**Conteúdo necessário:**

- Nome ou assinatura visual do Legal D+.
- Foto real do espaço, da fachada ou de uma montagem de festa.
- Identificação textual acessível do estabelecimento.
- Texto alternativo descritivo para a imagem.

**Direção de conteúdo proposta:** “Festas infantis em Santa Inês, Vila Velha.”

A marca pode aparecer na arte. O nome também deverá existir como texto HTML acessível, evitando que a identificação dependa apenas de uma imagem.

O recorte deve preservar a marca e a informação principal em telas pequenas. A peça promocional completa não será usada como único banner: contém muito texto e uma oferta sem validade confirmada.

### 3.3. Acessos rápidos

| Posição | Nome acessível | Destino |
|---|---|---|
| 1 | Instagram do Legal D+ | Perfil do Instagram |
| 2 | WhatsApp do Legal D+ | Conversa geral no WhatsApp |
| 3 | Localização do Legal D+ | Perfil do estabelecimento no Google Maps |

### 3.4. Cinco cards e textos propostos

| Ordem | Título | Descrição | Destino inicial |
|---|---|---|---|
| 1 | **Consultar data e orçamento** | Conte a data e a quantidade de convidados para conversar com nossa equipe. | WhatsApp com mensagem de orçamento. |
| 2 | **Conheça nossos pacotes** | Consulte opções, serviços incluídos e condições para sua festa. | WhatsApp com pedido de informações sobre pacotes. |
| 3 | **Conheça o espaço** | Veja o local e encontre informações para planejar sua visita. | Perfil do estabelecimento no Google Maps, com acesso às fotos e informações do local. |
| 4 | **Festas realizadas** | Inspire-se nas comemorações compartilhadas em nosso Instagram. | Perfil do Instagram. |
| 5 | **Agende uma visita** | Converse com nossa equipe para combinar uma visita ao espaço. | WhatsApp com mensagem de visita. |

**Regras dos destinos:**

- O primeiro card recebe a maior prioridade visual.
- O card de pacotes abre uma conversa porque não foi fornecido um catálogo público atual.
- A galeria deste escopo é acessada nos canais existentes. As fotos recebidas são insumos para o banner e para a próxima etapa visual.
- Caso o cliente forneça um catálogo, destaque ou galeria com URL própria, o destino correspondente poderá ser substituído mantendo o card.
- Todos os textos acima são propostas para revisão, não declarações de aprovação do estabelecimento.

### 3.5. Rodapé

- Título: **Conecte-se**.
- Ícones: Instagram, WhatsApp e localização.
- Identificação proposta: **© [ano automático] Cerimonial Infantil Legal D+. Todos os direitos reservados.**
- Os destinos repetidos no rodapé devem ser consistentes com os acessos rápidos.

## 4. Destinos e mensagens preparados

Os links desta seção foram montados a partir dos dados fornecidos. A abertura e o destino final serão verificados durante a implementação.

### 4.1. Canais

- **Instagram:** https://www.instagram.com/cerimoniallegaldmais/
- **Google Maps:** https://www.google.com/maps?cid=14167918038953408247
- **Compartilhamento Google fornecido:** https://share.google/Ed3BjE1jBRX3pGlLs
- **WhatsApp direto:** https://wa.me/5527988831009
- **Facebook informado como referência:** https://www.facebook.com/legaldemaiscerimonial/

O identificador numérico do Google Maps foi extraído do endereço de busca fornecido pelo usuário. A verificação deverá confirmar que ele abre o estabelecimento e o endereço corretos.

### 4.2. Consulta de data e orçamento

Mensagem proposta:

> Olá! Vim pelo link da bio do Legal D+ e gostaria de consultar disponibilidade e orçamento.  
> Data da festa:  
> Quantidade de convidados:  
> Tipo de comemoração:

[Link preparado para orçamento](https://wa.me/5527988831009?text=Ol%C3%A1!%20Vim%20pelo%20link%20da%20bio%20do%20Legal%20D%2B%20e%20gostaria%20de%20consultar%20disponibilidade%20e%20or%C3%A7amento.%0AData%20da%20festa%3A%0AQuantidade%20de%20convidados%3A%0ATipo%20de%20comemora%C3%A7%C3%A3o%3A)

O visitante preenche ou ajusta os dados na conversa. A página não solicita dados de crianças nem inclui o nome de um aniversariante na mensagem padrão.

### 4.3. Informações sobre pacotes

> Olá! Vim pelo link da bio do Legal D+ e gostaria de conhecer os pacotes, os serviços incluídos e as condições para realizar uma festa.

[Link preparado para pacotes](https://wa.me/5527988831009?text=Ol%C3%A1!%20Vim%20pelo%20link%20da%20bio%20do%20Legal%20D%2B%20e%20gostaria%20de%20conhecer%20os%20pacotes%2C%20os%20servi%C3%A7os%20inclu%C3%ADdos%20e%20as%20condi%C3%A7%C3%B5es%20para%20realizar%20uma%20festa.)

### 4.4. Pedido de visita

> Olá! Vim pelo link da bio do Legal D+ e gostaria de combinar uma visita para conhecer o espaço.

[Link preparado para visita](https://wa.me/5527988831009?text=Ol%C3%A1!%20Vim%20pelo%20link%20da%20bio%20do%20Legal%20D%2B%20e%20gostaria%20de%20combinar%20uma%20visita%20para%20conhecer%20o%20espa%C3%A7o.)

### 4.5. Contato geral

> Olá! Vim pelo link da bio do Legal D+ e gostaria de mais informações.

[Link preparado para contato geral](https://wa.me/5527988831009?text=Ol%C3%A1!%20Vim%20pelo%20link%20da%20bio%20do%20Legal%20D%2B%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.)

O clique abre o WhatsApp ou sua versão web com uma mensagem editável. A página não envia mensagens automaticamente.

## 5. Inventário de assets fornecidos

Os nove arquivos foram inspecionados visualmente. As datas das fotografias não foram informadas.

| Arquivo | Dimensões | Conteúdo observado | Uso possível |
|---|---|---|---|
| image.png | 545 × 541 px | Festa com pessoas, decoração e brinquedos ao fundo | Referência de festa realizada. |
| image(1).png | 550 × 557 px | Peça promocional com marca, oferta e lista de itens | Referência de marca, conteúdo comercial e elementos visuais. |
| image(2).png | 550 × 557 px | Cópia idêntica de image(1).png | Mesmo insumo; não representa outra oferta. |
| image(3).png | 680 × 382 px | Montagem de festa com decoração rosa e pessoas | Referência de decoração e festa realizada. |
| image(4).png | 680 × 382 px | Ambiente interno com mesas, decoração, equipamentos e brinquedos | Candidata a referência para apresentação do espaço. |
| image(5).png | 680 × 382 px | Mesa decorada com balões e fundo colorido | Referência de decoração. |
| image(6).png | 680 × 453 px | Fachada do estabelecimento e identificação visual | Referência para reconhecimento do local e possível imagem de destaque. |
| image(7).png | 680 × 382 px | Visão ampla do salão com mesas e brinquedos | Candidata a referência para apresentação do espaço. |
| image(8).png | 287 × 510 px | Visão vertical do salão | Referência complementar; resolução limitada para usos maiores. |

### Materiais a complementar

1. Logo original, preferencialmente em SVG ou PNG transparente.
2. Fotografias atuais e em maior resolução, se disponíveis.
3. Catálogo atual de pacotes e serviços, caso exista.
4. Manual de marca, paleta e fontes, caso existam.
5. URL específica para portfólio ou catálogo, se desejada.

O material recebido já permite especificar a demonstração e orientar o design system. A peça promocional contém a marca, mas não substitui um arquivo original do logotipo.

## 6. Requisitos funcionais

| ID | Requisito | Critério esperado |
|---|---|---|
| RF-01 | Identificar o Legal D+ no banner, no título da página e nos textos acessíveis | Nome correto e ausência de conteúdo de outro estabelecimento na versão personalizada. |
| RF-02 | Oferecer três acessos rápidos | Instagram, WhatsApp e localização abrem os destinos correspondentes. |
| RF-03 | Exibir cinco cards na ordem definida | Título, descrição, ícone e destino correspondem a este PRD. |
| RF-04 | Facilitar orçamento pelo WhatsApp | A mensagem contém origem, data, quantidade de convidados e tipo de comemoração como campos editáveis. |
| RF-05 | Encaminhar dúvidas de pacotes para a equipe | O card abre uma conversa, sem simular catálogo, preço ou disponibilidade que não foram confirmados. |
| RF-06 | Direcionar ao local correto | O link do Google Maps corresponde ao nome e endereço fornecidos. |
| RF-07 | Encaminhar visitas como solicitação | A equipe combina a visita na conversa; não há confirmação automática. |
| RF-08 | Repetir os canais no rodapé | Mesmos destinos dos ícones superiores e ano atualizado automaticamente. |
| RF-09 | Permitir personalização simples | Nome, textos, imagens, links e identidade visual têm pontos de edição identificáveis. |
| RF-10 | Preparar metadados de compartilhamento | Título, descrição, imagem e URL da página são configurados após a definição do endereço final. |

### Metadados propostos

- **Título:** Legal D+ | Festas infantis em Vila Velha.
- **Descrição:** Conheça o Cerimonial Infantil Legal D+, em Santa Inês, Vila Velha. Consulte pacotes, disponibilidade de datas e agende uma visita com a equipe.
- **Imagem de compartilhamento:** a definir na etapa visual com os assets da marca.
- **URL canônica:** preencher após definir o endereço de publicação.

## 7. Requisitos de experiência e implementação

- **Prioridade de uso:** celular, incluindo navegação a partir do Instagram.
- **Layout:** uma coluna; manter o container do modelo, cuja largura máxima atual é 430 px.
- **Responsividade:** verificar telas de 320, 390 e 430 px de largura, além de desktop; não permitir rolagem horizontal.
- **Hierarquia:** o primeiro card deve ser facilmente encontrado e, na referência de 390 × 844 px, deve aparecer integralmente na primeira tela.
- **Toque e teclado:** áreas acionáveis confortáveis, foco visível e nomes acessíveis para os ícones.
- **Leitura:** contraste e tamanhos de texto serão definidos e verificados no design system.
- **Movimento:** respeitar a preferência de movimento reduzido, já contemplada no modelo.
- **Imagens:** otimizar o arquivo de destaque, preservar proporções e definir dimensões para reduzir saltos de layout.
- **Desempenho:** meta inicial de até 500 KB de transferência para o carregamento principal, incluindo a imagem de destaque e eventuais fontes; medir após implementar.
- **Base técnica prevista:** HTML, CSS e JavaScript, com publicação estática no Cloudflare Pages.
- **Endereço de publicação:** pendente. Não foi contratado ou configurado um domínio nesta etapa.
- **Manutenção:** documentar os campos de personalização e os destinos dos links para facilitar atualizações.

A versão descrita consiste em apresentação e encaminhamento para canais existentes. Calendário de reservas, pagamento, formulário de captação, painel administrativo e páginas internas adicionais ficam fora desta versão.

## 8. Pendências para validação com o estabelecimento

| Prioridade | Pergunta ou material | Efeito na entrega |
|---|---|---|
| Alta | Qual nome deve aparecer na página: “Cerimonial Infantil Legal D+”, “Espaço Legal D+” ou outra grafia oficial? | Uniformizar banner, metadados e rodapé. |
| Alta | O WhatsApp (27) 98883-1009 e o endereço continuam corretos? | Validar os canais principais. |
| Alta, se a oferta for publicada | O pacote de R$ 3.499 está vigente? Qual a validade, condições e forma de contratação? | Liberar ou atualizar a apresentação da oferta. |
| Alta, se a modalidade for anunciada | Há contratação apenas do espaço e contratação do pacote completo atualmente? | Definir o texto comercial com precisão. |
| Média | Qual a capacidade máxima do salão e como os convidados são contabilizados nos pacotes? | Informar capacidade sem confundi-la com o pacote de 39 convidados. |
| Média | Quais serviços, brinquedos e equipamentos estão disponíveis hoje? | Atualizar a apresentação da estrutura. |
| Média | Quais são os dias e horários de atendimento e como se combinam as visitas? | Definir informações de funcionamento e expectativa de resposta. |
| Média | Há logo original, fotos atuais, catálogo e links próprios para os conteúdos? | Melhorar fidelidade visual e destinos dos cards. |
| Antes da publicação | Qual será o domínio ou endereço final da página? | Configurar metadados e compartilhamento. |
| Caso se incluam números de avaliações | Qual a nota e a quantidade atuais em cada plataforma? | Manter fonte, nota e contagem corretas. |

As pendências não impedem a preparação do design system. A demonstração pode usar os textos propostos neste PRD com encaminhamento ao atendimento para informações comerciais.

## 9. Critérios de aceite da futura página

Esta lista descreve verificações a realizar após implementar; não constitui resultado de teste já executado.

- [ ] Estrutura principal preservada: banner, três ícones rápidos, cinco cards e rodapé.
- [ ] Identificação do Legal D+ consistente nos elementos visíveis, acessíveis e nos metadados.
- [ ] Identidade visual alinhada ao design system que será criado.
- [ ] Primeiro card com destaque e mensagem de orçamento correta.
- [ ] Mensagens de WhatsApp editáveis, com acentos e quebras de linha corretos.
- [ ] Nenhum link remanescente para a página de curso usada como destino no HTML original.
- [ ] Instagram e Google Maps apontando para o estabelecimento correto.
- [ ] Nenhuma reserva ou visita apresentada como automaticamente confirmada.
- [ ] Oferta de R$ 3.499 e modalidade de locação tratadas conforme a confirmação comercial.
- [ ] Limite do pacote distinguido da capacidade máxima do local.
- [ ] Layout verificado em celular e desktop, sem cortes relevantes ou rolagem horizontal.
- [ ] Navegação por teclado, foco, textos alternativos e preferência de movimento reduzido verificados.
- [ ] Imagens otimizadas, carregamento medido e compartilhamento conferido.
- [ ] Nome, contatos, endereço e textos finais revisados antes da publicação.

## 10. Brief para a próxima etapa: design system

A próxima entrega deverá transformar os insumos de marca em um sistema visual para esta página, cobrindo:

1. Paleta derivada da marca fornecida, com papéis de cor e contraste.
2. Tipografia de títulos, descrições e informações auxiliares.
3. Espaçamento, dimensões, bordas, sombras e raios.
4. Composição do banner e comportamento do recorte das fotografias.
5. Componentes: acessos rápidos, card principal, cards secundários, ícones e rodapé.
6. Estados de interação: padrão, foco, passagem do ponteiro e toque.
7. Regras responsivas e de movimento reduzido.
8. Tratamento da marca e da imagem de compartilhamento.

**Referências observadas nos materiais:** cores vivas, assinatura multicolorida, coroa, balões e imagens de festas e do espaço. Elas são referências existentes, não tokens, fontes ou decisões visuais finais.

A proposta visual deverá equilibrar a linguagem infantil com a clareza necessária ao adulto que organiza a festa.

## 11. Fontes e rastreabilidade

- **F-01 — Mensagem do usuário:** dados copiados do perfil do Google, endereço, telefone, links, contagens e comentários.
- **F-02 — Peça promocional fornecida:** image(1).png; duplicada em image(2).png. Fonte da marca, frase, pacote, preço e itens divulgados.
- **F-03 — Fotografias fornecidas:** image.png e image(3).png a image(8).png. Fonte das observações visuais; sem data informada.
- **F-04 — HTML fornecido:** com banner.html. Fonte da estrutura de componentes; não é a implementação personalizada do Legal D+.
- **F-05 — Instagram informado:** https://www.instagram.com/cerimoniallegaldmais/
- **F-06 — Perfil Google informado:** https://share.google/Ed3BjE1jBRX3pGlLs

### Registro de estado

| Item | Situação nesta entrega |
|---|---|
| Inspeção do HTML e das nove imagens | Realizada. |
| Identificação da duplicidade da peça promocional | Realizada por comparação dos arquivos. |
| PRD e textos de interface | Elaborados como proposta. |
| Confirmação dos dados com o negócio | Pendente. |
| Design system | Próxima etapa solicitada; ainda não elaborado. |
| Página personalizada, testes e publicação | Etapas posteriores; ainda não realizadas. |

