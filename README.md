# LineCurativos

Aplicação Django para triagem educativa e encaminhamento de pessoas leigas diante de feridas.

## Objetivo

Organizar observações simples (tempo de evolução, origem, localização, diabetes, aparência, odor, secreção, bordas e alterações ao redor) em um fluxo de decisão educativo.

O sistema **não diagnostica**, não classifica infecção por conta própria e não prescreve tratamento.

## Fontes clínicas usadas na primeira versão

- AHRQ — avaliação estruturada de feridas: https://www.ahrq.gov/patient-safety/settings/long-term-care/resource/ontime/pruhealing/assessment.html
- Queensland Health — avaliação e manejo de feridas crônicas: https://www.health.qld.gov.au/clinical-practice/guidelines-procedures/clinical-pathways/residential-aged-care-clinical-pathways/all-pathways/chronic-wound-assessment-and-management
- IWGDF — diretrizes 2023: https://iwgdfguidelines.org/guidelines-2023/
- American Burn Association — critérios de encaminhamento de queimaduras: https://www.ameriburn.org/burn-care-team/resources/guidelines-for-burn-patient-referral

## Instalação

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

No Linux/macOS, use `source .venv/bin/activate`.

## Observação

Antes de qualquer uso institucional ou clínico, o conteúdo das regras deve ser revisado e validado por profissional(is) de saúde habilitado(s), e o projeto deve receber requisitos de privacidade, segurança e governança compatíveis com dados de saúde.
