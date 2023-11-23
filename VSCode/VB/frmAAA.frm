VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmAAA 
   Caption         =   "Cadastro - AULA"
   ClientHeight    =   3570
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4515
   OleObjectBlob   =   "frmAAA.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmAAA"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub btoCADASTRO_Click()

 Do
    
    If IsNumeric(txtDIA) = False Then
        msgbox "O dia da aula deve ser preenchido com numero", vbCritical
        txtDIA = ""
        txtDIA.SetFocus
        Exit Sub
    End If
    
    If IsNumeric(txtMES) = False Then
        msgbox "O Mês da aula deve ser preenchido com numero", vbCritical
        txtMES = ""
        txtMES.SetFocus
        Exit Sub
    End If
    
    If IsNumeric(txtANO) = False Then
        msgbox "O ano da aula deve ser preenchido com numero", vbCritical
        txtANO = ""
        txtANO.SetFocus
        Exit Sub
    End If
    
    
    On Error GoTo teste
        validador = True
         Data = DateSerial(txtANO, txtMES, txtDIA)
        
        If validador = False Then
            msgbox "a data não existe"
            Exit Sub
        End If
    On Error GoTo 0
    

Loop While Data = ""

   
    txtID = WorksheetFunction.Max(Range("A:A")) + 1
    
    Range("a" & Rows.Count).End(xlUp).Offset(1, 0) = CDec(txtID)
    Range("a" & Rows.Count).End(xlUp).Offset(0, 1) = txtDIA & "/" & txtMES & "/" & txtANO
    Range("a" & Rows.Count).End(xlUp).Offset(0, 2) = txtPERIODO
    Range("a" & Rows.Count).End(xlUp).Offset(0, 3) = txtPROF
    Range("a" & Rows.Count).End(xlUp).Offset(0, 4) = txtTURMA
    Range("a" & Rows.Count).End(xlUp).Offset(0, 5) = txtCH
    Range("a" & Rows.Count).End(xlUp).Offset(0, 6) = txtSALA
    Range("a" & Rows.Count).End(xlUp).Offset(0, 7) = txtMATERIA
    
    msgbox "Dados Cadastrados com sucesso", vbInformation
    Exit Sub
    
teste:
    validador = False
    Resume Next
    Exit Sub
    

End Sub


Private Sub Userform_Initialize()

    Dim x As Integer
    Dim y As Integer
    Dim z As Integer
    Dim t As Integer
    
    For x = 1 To 31
        txtDIA.AddItem (x)
    Next x
    
    For y = 1 To 12
        txtMES.AddItem (y)
    Next y
    
    For z = 2000 To 2024
        txtANO.AddItem (z)
    Next z
    
    For t = 1 To 25
        txtTURMA.AddItem ("T" & t)
    Next t
        
End Sub
