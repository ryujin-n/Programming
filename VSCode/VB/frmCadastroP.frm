VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmCadastroP 
   Caption         =   "UserForm1"
   ClientHeight    =   2190
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   3660
   OleObjectBlob   =   "frmCadastroP.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmCadastroP"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub btoOK_Click()
    Dim vald As Boolean
    
    txtNOME.SetFocus
    
    If Trim(txtNOME) = "" Then
        msgbox "Preencha o nome", vbCritical
        txtNOME = ""
        txtNOME.SetFocus
        Exit Sub
    ElseIf Trim(txtReg) = "" Then
        msgbox "Preencha o registro", vbCritical
        txtReg = ""
        txtReg.SetFocus
        Exit Sub
    ElseIf Trim(txtArea) = "" Then
        msgbox "Preencha a área", vbCritical
        txtArea = ""
        txtArea.SetFocus
        Exit Sub
    End If
    

    

Do
   On Error GoTo erro
    vald = True
    txtReg = WorksheetFunction.VLookup(txtReg, Range("B:B"), 1, False)
        If vald = True Then
            msgbox "Registro já Existe"
            txtReg = ""
            txtReg.SetFocus
            Exit Sub
        End If

    On Error GoTo 0
    
Loop While vald = True

    txtCodigo = WorksheetFunction.Max(Range("A:A")) + 1
    
    Range("A" & Rows.Count).End(xlUp).Offset(1, 0) = CDec(txtCodigo)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 1) = txtReg
    Range("A" & Rows.Count).End(xlUp).Offset(0, 2) = StrConv(txtNOME, vbProperCase)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 3) = txtArea
    
    msgbox "Dados Cadastrados com sucesso", vbInformation
    Exit Sub
    Unload Me
    
    
erro:
    vald = False
    Resume Next
    
        

End Sub
Private Sub UserForm_Initialize()

    txtArea.AddItem "Desenvolvimento"
    txtArea.AddItem "Montagem e Manutenção"
    txtArea.AddItem "Redes e Sistemas"
    txtArea.AddItem "Design Gráfico"
    


End Sub
