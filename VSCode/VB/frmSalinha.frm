VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmSalinha 
   Caption         =   "UserForm1"
   ClientHeight    =   2085
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4050
   OleObjectBlob   =   "frmSalinha.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmSalinha"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub btoCadastrar_Click()

    If Trim(txtTipo) = False Then
        msgbox "O Tipo deve ser preenchido", vbCritical
        txtTipo = ""
        txtTipo.SetFocus
        Exit Sub
    End If


    If IsNumeric(txtNumero) = False Then
        msgbox "Numero deve ser preenchido", vbCritical
        txtNumero = ""
        txtNumero.SetFocus
        Exit Sub
    End If
    
  
    
    If IsNumeric(txtQtde) = False Then
        msgbox "Qtde deve ser preenchido", vbCritical
        txtQtde = ""
        txtQtde.SetFocus
        Exit Sub
    End If
    
    txtCodigo = WorksheetFunction.Max(Range("A:A")) + 1
    
    Range("a" & Rows.Count).End(xlUp).Offset(1, 0) = CDec(txtID)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 1) = CDec(txtNumero)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 2) = CDec(txtQtde)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 3) = txtTipo
    
    msgbox "Dados Cadastrados", vbInformation
    
End Sub

Private Sub btoPesquisar_Click()
    If IsNumeric(txtID) = False Then
        msgbox "ID deve ser preenchido com numero", vbCritical
        txtID = ""
        txtID.SetFocus
        Exit Sub
    End If
    
    On Error GoTo erro
    
    txtNumero = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 2, False)
    txtQtde = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 3, False)
    txtTipo = WorksheetFunction.VLookup(CDec(txtID), Range("A:D"), 4, False)
    
    On Error GoTo 0
    
    Exit Sub
    
erro:
    txtNumero = ""
    txtID = ""
    txtQtde = ""
    txtTipo = ""
    msgbox "ID não encontrado", vbCritical
    Exit Sub
    
End Sub




Private Sub UserForm_Initialize()

    txtTipo.AddItem "Desenvolvimento"
    txtTipo.AddItem "Montagem e Manutenção"
    txtTipo.AddItem "Redes e Sistemas"
    txtTipo.AddItem "Design Gráfico"
    
    
End Sub
