VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmCADASTROMEU 
   Caption         =   "MATÉRIA"
   ClientHeight    =   2370
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   3390
   OleObjectBlob   =   "frmCADASTROMEU.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmCADASTROMEU"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub btoCadastrar_Click()
        
    If Trim(txtNOME) = "" Then
        msgbox "Nome deve ser preenchido", vbCritical
        txtNOME = ""
        txtNOME.SetFocus
        'SetFocus -> onde o cursor do mouse vai para
        Exit Sub
    End If
    
    If IsNumeric(txtCH) = False Then
        msgbox "A carga horária deve ser preenchido com numero", vbCritical
        txtIdade = ""
        txtIdade.SetFocus
        Exit Sub
    End If


 Do
    
    If Trim(txtRegistro) = "" Then
        msgbox "Profissao deve ser preenchido", vbCritical
        txtProfissao = ""
        txtProfissao.SetFocus
        
    End If
    
    On Error GoTo teste
        validador = True
        
        txtRegistro = WorksheetFunction.VLookup(Val(txtRegistro), Range("B:B"), 1, False)
        
        If validador = True Then
            msgbox "numero de registro ja existe"
            Exit Sub
        End If
    On Error GoTo 0
    

Loop While registro <> ""
    
    txtID = WorksheetFunction.Max(Range("A:A")) + 1
    
    Range("a" & Rows.Count).End(xlUp).Offset(1, 0) = CDec(txtID)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 1) = CDec(txtRegistro)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 2) = txtNOME
    Range("a" & Rows.Count).End(xlUp).Offset(0, 3) = CDec(txtCH)
    
    msgbox "Dados Cadastrados com sucesso", vbInformation
    Exit Sub
    
teste:
    validador = False
    Resume Next
    Exit Sub
    
    
End Sub

Private Sub btoPesquisar_Click()
    If IsNumeric(txtID) = False Then
        msgbox "ID deve ser preenchido com um numero VALIDO", vbCritical
        txtID = ""
        txtID.SetFocus
        Exit Sub
    End If
    
    On Error GoTo erro
    
    txtRegistro = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 2, False)
    txtNOME = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 3, False)
    txtCH = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 4, False)
    
    On Error GoTo 0
    
    Exit Sub
    
erro:

    
    txtRegistro = ""
    txtNOME = ""
    txtCH = ""
    txtID = ""
    
    msgbox "ID não encontrado", vbCritical
    
    Exit Sub
End Sub


