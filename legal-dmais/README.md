# Legal D+ — Link na bio

Página de demonstração do Cerimonial Infantil Legal D+, em Santa Inês, Vila Velha.

## Conteúdo

- `dist/`: página pronta para hospedagem, com `index.html` e imagem de compartilhamento.
- `src/content.json`: dados do negócio, cinco cards e destinos.
- `src/page.html`: estrutura da página.
- `src/style.css`: design system aplicado.
- `src/assets/`: fotografia, fonte Nunito e licença da fonte.
- `scripts/`: geração e verificação do HTML.
- `docs/`: PRD, design system e registro de implementação.

## Vercel

Importe o repositório `links-bio`, selecione **Root Directory: legal-dmais** e **Framework Preset: Other**. Deixe o comando de build vazio. `vercel.json` indica `dist` como diretório publicado; os arquivos dessa pasta já estão prontos.

Esta preparação não cria nem publica um projeto na Vercel automaticamente.

## Editar e gerar novamente

Com Python 3 disponível, edite os arquivos em `src/` e execute dentro desta pasta:

```bash
python scripts/build.py
```

Para as verificações adicionais, é necessário Pillow no Python e Node.js acessível no terminal:

```bash
python scripts/verify.py
```

Após uma alteração, inclua também a versão atualizada de `dist/` no commit.

## Metadados e publicação final

A origem em `src/content.json` ainda é a URL da demonstração original. Ao definir a URL final na Vercel ou o domínio do cliente, atualize `origin` e gere o HTML novamente para ajustar canonical, Open Graph e dados estruturados.

A demonstração usa `noindex, nofollow`. Revise essa escolha para a publicação comercial final.

## Assets e fidelidade

Fonte e imagem do banner estão incorporadas no HTML. A fonte Nunito usa formato WOFF e sua licença é preservada em `src/assets/OFL.txt` e no HTML compilado. A imagem de compartilhamento usa a fotografia original da fachada. Valores, capacidade, horários e números de avaliações não confirmados foram omitidos.

