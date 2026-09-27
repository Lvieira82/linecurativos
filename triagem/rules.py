SOURCES = {
    "tempo": {
        "title": "Tempo de evolução da ferida",
        "text": "A avaliação de uma ferida considera sua evolução ao longo do tempo. Feridas que permanecem abertas ou não apresentam progresso adequado precisam de avaliação profissional.",
        "url": "https://www.health.qld.gov.au/clinical-practice/guidelines-procedures/clinical-pathways/residential-aged-care-clinical-pathways/all-pathways/chronic-wound-assessment-and-management",
    },
    "avaliacao": {
        "title": "Avaliação estruturada da ferida",
        "text": "Cor, tecido, exsudato, odor, bordas e pele ao redor são elementos usados em avaliações estruturadas de feridas.",
        "url": "https://www.ahrq.gov/patient-safety/settings/long-term-care/resource/ontime/pruhealing/assessment.html",
    },
    "diabetes": {
        "title": "Diabetes e feridas nos pés",
        "text": "Pessoas com diabetes, especialmente quando há ferida no pé, podem precisar de avaliação profissional específica.",
        "url": "https://iwgdfguidelines.org/guidelines-2023/",
    },
    "queimadura": {
        "title": "Encaminhamento de queimaduras",
        "text": "Algumas queimaduras exigem avaliação especializada, incluindo situações relacionadas à profundidade, extensão, localização, mecanismo e suspeita de lesão por inalação.",
        "url": "https://www.ameriburn.org/burn-care-team/resources/guidelines-for-burn-patient-referral",
    },
}

QUESTIONS = {
    "duracao": {"title":"Há quanto tempo existe a ferida?","help":"Escolha a opção mais próxima.","source":"tempo","options":[("recente","Surgiu há menos de 4 semanas"),("prolongada","Está aberta há 4 semanas ou mais"),("nao_sei","Não sei informar")]},
    "origem": {"title":"Como a ferida começou?","help":"Identificar a origem ajuda a direcionar as próximas perguntas.","source":"avaliacao","options":[("trauma","Corte, queda, pancada, atrito ou outro trauma"),("queimadura","Queimadura por calor, líquido quente, produto químico ou eletricidade"),("pressao","Surgiu em área submetida a pressão ou contato prolongado"),("espontanea","Não houve trauma ou queimadura conhecida")]},
    "diabetes": {"title":"A pessoa tem diabetes?","help":"Essa informação é especialmente relevante quando a ferida está no pé.","source":"diabetes","options":[("sim","Sim"),("nao","Não"),("nao_sei","Não sei")]},
    "local": {"title":"Onde está a ferida?","help":"Toque no mapa corporal ou escolha uma região abaixo.","source":"diabetes","options":[("rosto","Rosto / face"),("torax","Tórax"),("abdome","Abdome"),("costas","Costas"),("membro_superior","Membro superior"),("mao","Mão"),("membro_inferior","Membro inferior"),("pe","Pé"),("regiao_genital","Região genital"),("articulacao","Sobre ou ao redor de uma articulação"),("outra","Outro local")]},
    "sinais_urgencia": {"title":"Existe algum destes sinais de alerta?","help":"Se houver qualquer um deles, procure atendimento em vez de continuar a avaliação educativa.","source":"avaliacao","options":[("sim","Sangramento que não para, desmaio, confusão, dificuldade para respirar ou piora rápida"),("nao","Nenhum desses sinais")]},
    "queimadura_especial": {"title":"Se for queimadura: houve eletricidade, produto químico ou suspeita de fumaça/lesão por inalação?","help":"Esses mecanismos podem exigir avaliação especializada.","source":"queimadura","options":[("sim","Sim"),("nao","Não"),("nao_sei","Não sei")]},
    "cor": {"title":"Como está a maior parte do leito da ferida?","help":"Observe sem tocar. Se não souber identificar a cor, escolha 'Não sei'.","source":"avaliacao","options":[("vermelho","Predominantemente vermelho/rosado"),("amarelo","Predominantemente amarelado"),("escuro","Predominantemente marrom, preto ou muito escuro"),("nao_sei","Não sei")]},
    "odor": {"title":"Há odor diferente ou desagradável?","help":"O odor é apenas um dos elementos da avaliação e não permite, sozinho, determinar a causa de uma ferida.","source":"avaliacao","options":[("sim","Sim"),("nao","Não"),("nao_sei","Não sei")]},
    "secrecao": {"title":"Há aumento de secreção ou líquido saindo da ferida?","help":"Observe se houve mudança em relação aos dias anteriores.","source":"avaliacao","options":[("sim","Sim"),("nao","Não"),("nao_sei","Não sei")]},
    "bordas": {"title":"Como estão as bordas?","help":"Observe a forma da borda sem tentar manipulá-la.","source":"avaliacao","options":[("regulares","Parecem regulares e próximas"),("irregulares","Parecem irregulares, enroladas ou afastadas"),("nao_sei","Não sei")]},
}

def build_result(data):
    if data.get("sinais_urgencia") == "sim":
        return {"level":"urgente","title":"Procure atendimento médico com urgência","text":"Foi informado um sinal de alerta que merece avaliação presencial prioritária."}
    if data.get("queimadura_especial") == "sim":
        return {"level":"urgente","title":"Procure avaliação médica","text":"O mecanismo informado para a queimadura pode exigir avaliação especializada."}
    if data.get("diabetes") == "sim" and data.get("local") == "pe":
        return {"level":"breve","title":"Procure avaliação profissional","text":"Ferida no pé em pessoa com diabetes merece avaliação profissional específica."}
    if data.get("duracao") == "prolongada":
        return {"level":"breve","title":"Procure avaliação profissional","text":"A ferida foi informada como aberta por 4 semanas ou mais ou sem evolução adequada. Uma avaliação presencial é recomendada."}
    if data.get("cor") == "escuro" or data.get("odor") == "sim" or data.get("secrecao") == "sim":
        return {"level":"breve","title":"Considere avaliação profissional","text":"Foram relatadas características que justificam avaliação profissional, principalmente se forem novas, estiverem piorando ou vierem acompanhadas de dor, vermelhidão, inchaço ou febre."}
    return {"level":"orientacao","title":"A avaliação educativa não substitui uma consulta","text":"Não foram identificados, pelas respostas fornecidas, critérios de urgência no fluxo. Observe a evolução e procure um profissional se houver piora, novos sinais de alerta ou dificuldade de cicatrização."}
