# Guia de Estilos - Templates de E-mail Perfecting

## 🎨 Identidade Visual

### Cores da Marca

**Cor Principal:**
- **Azul Perfecting:** `#3A71D9`
  - Uso: Botões principais, marca "Perfecting", títulos, links e elementos de destaque
  - Representa confiança, profissionalismo e tecnologia

**Cores Secundárias:**
- **Cinza Escuro:** `#333333` - Texto principal
- **Cinza Médio:** `#666666` - Texto secundário e notas
- **Cinza Claro:** `#888888` - Rodapés e informações terciárias
- **Cinza Suave:** `#999999` - Copyright e metadados
- **Branco:** `#FFFFFF` - Fundos de destaque
- **Cinza de Fundo:** `#F9F9F9` ou `#F8F9FA` - Áreas de destaque

**Cores de Borda:**
- Bordas suaves: `#EEEEEE`
- Bordas de destaque: `#3A71D9` (2px sólida)

### ⚠️ Cores Proibidas

Não utilizar em novos templates:
- ❌ Verde `#4CAF50` (usado anteriormente)
- ❌ Gradientes roxos `#667eea` a `#764ba2` (usado anteriormente)
- ❌ Qualquer outra cor que não esteja na paleta oficial

---

## 📐 Estrutura dos Templates

### Anatomia de um Template

```python
from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class NomeDoTemplate(BaseEmailTemplate):
    template_name = "nome_do_template"
    language = "pt-br"
    subject_template = "Assunto do E-mail - Perfecting"
    text_template = (
        "Versão em texto puro do e-mail\n\n"
        "Sempre incluir assinatura: Equipe Perfecting"
    )
    html_template = (
        # Ver seção HTML abaixo
    )
```

### Container Principal

Todos os templates HTML devem usar este container:

```html
<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>
    <!-- Conteúdo aqui -->
</div>
```

---

## 🎯 Elementos de Design

### 1. Títulos (Headings)

```html
<!-- Título Principal (H2) -->
<h2 style='color: #3A71D9;'>Título do E-mail</h2>

<!-- Com marca Perfecting -->
<h2 style='color: #3A71D9;'>
    Bem-vindo(a) à <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>!
</h2>
```

**Regras:**
- Sempre usar `<h2>` para títulos principais
- Cor: `#3A71D9`
- Font-weight: bold (implícito no h2)

### 2. Marca "Perfecting"

Sempre que mencionar "Perfecting", usar o estilo destacado:

```html
<span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>
```

**Aplicações:**
- Dentro de parágrafos
- No rodapé
- Em títulos
- Mensagens de boas-vindas

### 3. Botões (Call-to-Action)

**Botão Padrão:**
```html
<p style='margin: 30px 0; text-align: center;'>
    <a href='{link_url}' style='background-color: #3A71D9; color: white; 
    padding: 14px 32px; text-decoration: none; border-radius: 6px; 
    display: inline-block; font-weight: bold; font-size: 16px;'>
        Texto do Botão
    </a>
</p>
```

**Especificações:**
- Background: `#3A71D9`
- Cor do texto: `white`
- Padding: `14px 32px`
- Border-radius: `6px`
- Font-size: `16px`
- Font-weight: `bold`
- Margem vertical: `30px 0`
- Alinhamento: `center`

### 4. Senhas Provisórias

**Container de Senha:**
```html
<div style='background-color: #f9f9f9; padding: 20px; border-radius: 8px; 
margin: 20px 0; text-align: center;'>
    <p style='font-size:1.3em; font-weight:bold; letter-spacing:2px; 
    background:#ffffff; padding:12px 20px; display:inline-block; 
    border-radius:6px; border: 2px solid #3A71D9; color: #333; margin: 0;'>
        {temp_password}
    </p>
</div>
```

**Especificações:**
- Container: fundo `#f9f9f9`, padding `20px`, border-radius `8px`
- Senha: fundo branco, borda `2px solid #3A71D9`
- Font-size: `1.3em`
- Letter-spacing: `2px`
- Cor do texto: `#333`

### 5. Avisos e Notas

**Nota Importante:**
```html
<p style='color: #666; font-size: 14px;'>
    <strong>⚠️ Informação importante aqui</strong>
</p>
```

**Nota em Itálico:**
```html
<p style='color: #666; font-size: 14px;'>
    <em>Informação secundária ou disclaimers</em>
</p>
```

### 6. Rodapé

**Padrão Simples:**
```html
<p style='margin-top: 40px; color: #888; font-size: 0.9em; 
border-top: 1px solid #eee; padding-top: 20px;'>
    Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>
</p>
```

**Padrão com Copyright:**
```html
<p style='margin: 0; color: #666666; font-size: 14px; line-height: 1.6;'>
    <strong>Equipe <span style='color: #3A71D9;'>Perfecting</span></strong>
</p>
<p style='margin: 10px 0 0; color: #999999; font-size: 12px;'>
    © 2026 <span style='color: #3A71D9;'>Perfecting</span>. Todos os direitos reservados.
</p>
```

### 7. Caixas de Destaque

**Box com Borda Lateral:**
```html
<div style='margin: 30px 0; padding: 25px; background-color: #f8f9fa; 
border-radius: 8px; border-left: 4px solid #3A71D9;'>
    <!-- Conteúdo aqui -->
</div>
```

---

## ✍️ Tipografia

### Hierarquia de Texto

1. **Título Principal (H2)**
   - Font-size: padrão do h2
   - Color: `#3A71D9`
   - Font-weight: bold

2. **Texto Normal**
   - Font-size: `16px` (padrão)
   - Color: `#333333`
   - Line-height: `1.6`

3. **Texto Secundário**
   - Font-size: `14px`
   - Color: `#666666`

4. **Texto Terciário (Rodapé)**
   - Font-size: `0.9em` ou `12px`
   - Color: `#888888` ou `#999999`

### Font-Family

Sempre usar:
```css
font-family: Arial, sans-serif;
```

---

## 📏 Espaçamento

### Margens

- **Entre seções principais:** `30px 0` ou `40px 0`
- **Parágrafos normais:** `0 0 20px` (bottom apenas)
- **Rodapé:** `margin-top: 40px`

### Padding

- **Container principal:** não necessário (usa max-width)
- **Boxes de destaque:** `20px` ou `25px`
- **Botões:** `14px 32px` (vertical horizontal)

---

## 🔤 Assuntos de E-mail

### Formato Padrão

```python
subject_template = "Descrição Clara - Perfecting"
```

**Exemplos:**
- ✅ `"Confirme seu e-mail - Perfecting"`
- ✅ `"Redefinição de senha - Perfecting"`
- ✅ `"Bem-vindo(a) à Perfecting!"`
- ✅ `"Seu acesso à plataforma Perfecting foi criado"`

**Regras:**
- Sempre terminar com "Perfecting" (exceto em boas-vindas)
- Ser claro e direto
- Máximo de 50-60 caracteres

---

## 📧 Versão em Texto Puro

Todos os templates devem ter uma versão `text_template`:

**Estrutura:**
```python
text_template = (
    "Olá {user_name},\n\n"
    "Conteúdo principal do e-mail.\n\n"
    "Informações adicionais.\n\n"
    "Se você não solicitou, ignore esta mensagem.\n\n"
    "Equipe Perfecting"
)
```

**Regras:**
- Usar `\n\n` para separar parágrafos
- Sempre terminar com "Equipe Perfecting"
- Não usar formatação (bold, itálico)
- Incluir URLs completas, não apenas links

---

## 🎨 Templates para Layouts Complexos

Para templates com layout mais elaborado (como `welcome_after_activation`), usar estrutura de tabelas:

```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0" 
width="100%" style="max-width: 600px; margin: 0 auto;">
    <tr>
        <td style="background: #3A71D9; padding: 40px; text-align: center;">
            <h1 style="color: #ffffff; font-size: 32px;">Título</h1>
        </td>
    </tr>
    <tr>
        <td style="padding: 40px; background: #ffffff;">
            <!-- Conteúdo -->
        </td>
    </tr>
</table>
```

---

## 📝 Variáveis de Template

### Variáveis Comuns

- `{user_name}` - Nome do usuário
- `{user_email}` - E-mail do usuário
- `{organization_name}` - Nome da organização
- `{platform_url}` - URL da plataforma
- `{temp_password}` - Senha provisória
- `{confirmation_link}` - Link de confirmação
- `{reset_link}` - Link de reset de senha
- `{expiration_hours}` - Horas para expiração

### Uso em HTML

Sempre escapar variáveis automaticamente (o sistema faz isso):
```html
<p>Olá <strong>{user_name}</strong>,</p>
```

---

## ✅ Checklist de Qualidade

Antes de finalizar um template, verificar:

- [ ] Cor `#3A71D9` usada em botões e marca
- [ ] "Perfecting" sempre destacado com `<span style='color: #3A71D9; font-weight: bold;'>`
- [ ] Container principal com `max-width: 600px`
- [ ] Font-family: `Arial, sans-serif`
- [ ] Botões com padding `14px 32px` e border-radius `6px`
- [ ] Rodapé com assinatura "Equipe Perfecting"
- [ ] Versão `text_template` completa
- [ ] Assunto termina com "- Perfecting" (quando aplicável)
- [ ] Sem cores antigas (#4CAF50, gradientes roxos)
- [ ] Responsivo (max-width funciona em mobile)
- [ ] Todas as variáveis `{variable}` presentes

---

## 🚫 Erros Comuns a Evitar

1. **Não usar cores antigas:**
   - ❌ `#4CAF50` (verde antigo)
   - ❌ `#667eea` ou `#764ba2` (roxo antigo)

2. **Não esquecer a marca:**
   - ❌ `<p>Equipe Perfecting</p>`
   - ✅ `<p>Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span></p>`

3. **Não usar aspas simples dentro de strings Python:**
   - ❌ `"<p style='font-size: 14px; font-family: 'Arial';'>"`
   - ✅ `"<p style='font-size: 14px; font-family: Arial, sans-serif;'>"`

4. **Não esquecer max-width:**
   - ❌ `<div style='font-family: Arial;'>`
   - ✅ `<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>`

---

## 📚 Templates de Referência

Para criar novos templates, consultar:

1. **Template Simples:** `confirm_email_signup.py`
2. **Template com Senha:** `welcome_new_user.py`
3. **Template Avançado:** `welcome_after_activation.py`

---

## 🔄 Versionamento

**Versão:** 1.0  
**Data:** 28 de Março de 2026  
**Última Atualização:** Padronização com cor #3A71D9

---

## 📞 Suporte

Para dúvidas sobre este guia:
- Consultar templates existentes em `src/core/services/email/templates/pt_br/`
- Verificar exemplos no arquivo de demonstração `send_email.py`
