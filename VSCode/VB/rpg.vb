Sub rpg()

Dim problem As String
Dim diff As Integer
Dim race As String
Dim char As String
Dim class As String
Dim action As String
Dim dice As Integer
Dim status As String
Dim sib As String
Dim turn As String

'! IMPORTANTE!!
    '? - Guerreiros tem mais probabilidade de acerto de 20% em ações com foco em força e 
    '? - Ladinos 


    'Introdução
    msgbox"[Você acorda, estava no chão e várias pessoas passam por você, nenhuma delas parecendo dar a mínima pro seu estado]" 
    msgbox"[Você tenta se erguer, conseguindo com dificuldade e se sente perdido, observando as pessoas trombando em você, até que você escuta uma voz amigavel]"
    msgbox"[Você olha pros lados e não vê ninguém, por um momento achou que estava delirando]"
    msgbox"???: " & vbcr & _
    "Aqui em baixo, amigão."
    msgbox"[Assim que você olha pra baixo, você vê uma figura meio engraçada, um Anão loiro que mais parecia um vendedor]"

    
    MsgBox "???: " & vbcr & _
    "Olá, bem vindo a Kirkwall, Andarilho! o Reino dos homens livres, meu nome é VARRIC" & vbCr & _
    "Você tem sorte hoje, pois eu sou seu guia turistico, o melhor de toda Thedas, sem me gabar"
    MsgBox "VARRIC:" & vbCr & _
    "Não sabe falar muito né?"
    MsgBox "VARRIC: " & vbCr & _
    "Okay, tudo bem, pelo menos você tem um nome, certo? sua mãe certamente te ama o suficiente pra te dar um nome"
    MsgBox "VARRIC: " & vbCr & _
    "Ahh você perdeu suas memórias, okay, então já que está em Kirkwall, você pode escolher o seu,afinal todos aqui são livres!!"
Do 
    'Nome do personagem, se for vazio, o Varric vai cassoar da sua cara até você colocar o nome
    char = inputbox("Insira seu nome, andarilho")
        If char = "" Then
            MsgBox "VARRIC:" & vbCr & _
            "Como assim você não tem um nome, olha,eu não posso te chamar de nada" & vbCr & _
            "Então é melhor escolher um nome aí"
        End If
Loop While char = ""

    MsgBox "VARRIC: " & vbCr & _
    "Ótimo, " & StrConv(char, vbProperCase) & ",nome legaal, agora que você tem um nome, o que você sabe fazer? "
    
    class = inputbox("Insira sua classe (Guerreiro, Arqueiro, Ladino ou Mago)")
        If class = "" Then
            MsgBox "VARRIC: " & vbCr & _
            "Não sabe fazer nada? então você vai ser um completo inútil, vai pra esquerda" & vbCr & _
            "que tem um barzinho, baratinho, quem sabe gasta esse restinho de nada que você tem no bolso com alguma bebida"
            Exit Sub
        ElseIf Trim(UCase(class)) = "GUERREIRO" Then
            MsgBox "VARRIC:" & vbCr & _
            "Olha só, esses músculos vão servir pra alguma coisa huh?, vou te dar um presentinho" & vbCr & _
            "considere como um presente de boas vindas!!"
                MsgBox " Você recebeu: x1 Kit de Guerreiro nível 1 ", vbInformation
        ElseIf Trim(UCase(class)) = "ARQUEIRO" Then
            MsgBox "VARRIC:" & vbCr & _
            "Hoh, um arqueiro huh? ótimo, se for bom o suficiente pode até ganhar alguns sovereigns" & vbCr & _
            "Aqui, tome um presentinho de boas vindas"
                MsgBox " Você recebeu: x1 Kit de Arqueiro nível 1 ", vbInformation
        ElseIf Trim(UCase(class)) = "LADINO" Then
            MsgBox "VARRIC:" & vbCr & _
            "Um ladrão?? HAH!! sabia que você parecia divertido, vamos ter muita diversão por aqui na Cidade Baixa!!" & vbCr & _
            "Um ladino precisa de equipamento, aqui, como cortesia!!"
                MsgBox " Você recebeu: x1 Kit de Ladino nível 1"
        ElseIf Trim(UCase(class)) = "MAGO" Then
            MsgBox "VARRIC:" & vbCr & _
            "Um mago, okay fale baixo...magos não são muito bem vistos aqui, sabe...coisa da Chantria"
            MsgBox "VARRIC:" & vbCr & _
            "Não precisa se preocupar com essa baboseira de Chantria por enquanto, aqui, pra você se virar"
            MsgBox " Você recebeu: x1 Kit de Mago nível 1", vbInformation
        End If
        
    MsgBox "VARRIC:" & vbCr & _
    "Okay " & StrConv(char, vbProperCase) & ", venha comigo, assim você não se perde, vou te explicar um pouco sobre Kirkwall"
    MsgBox "VARRIC:" & vbCr & _
    "A gente pode dividir Kirkwal em duas partes: A Cidade Baixa, onde estamos, e a Cidade alta" & vbCr & _
    "Que é onde fica um castelão enorme"
    MsgBox "[ele aponta pro horizonte, você vê um castelo enorme branco com adornos" & vbCr & _
    "dourados, aquele lugar te deixa nervoso"
    MsgBox "VARRIC:" & vbCr & _
    "Olha, eu sei que Kirkwall pode parecer grande e um pouco intimidadora, mas relaxa, aqui tem muitas oportunidades pra um(a)" & class & " como você." & vbCr & _
    "aqui na Cidade Baixa aceitamos todo tipo de pessoa, Humanos, Qunari e Elfos, tudo de bom."
    MsgBox "[Varric te guia pela cidade, todos eram pobes e uma enorme muralha dividia as duas partes de Kirkwall." & vbCr & _
    "Você é apenas uma pessoa simples do campo de Ferelden, que foi atacada pela Quinta Praga e te forçou a fugir com seus pais, que não sobreviveram e sua irmã"
    Do
        sib = inputbox("Qual o nome de sua irmã?")
            If sib = "" Then
                MsgBox "Você precisa de sua irmã para prosseguir na campanha"
            End If
    Loop While sib = ""

    MsgBox"[Suas memórias são falhas e vagas, você só consegue se lembrar de partes do que aconteceu de como foi parar em Kirkwall, você se lembra de seus pais e sua irmã," & sib & "," & vbCr _ &
    "Mas mesmo assim, seus rostos parecem ser apenas um borrão no da  "

    
        
        
    
    
    
End Sub

