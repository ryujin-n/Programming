VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmPesquisaP 
   Caption         =   "UserForm1"
   ClientHeight    =   2115
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   3450
   OleObjectBlob   =   "frmPesquisaP.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmPesquisaP"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Option Explicit

Private Sub btoOK_Click()
If IsNumeric(txtIDD) = False Then
        msgbox "Insira um Registro"
        txtIDD = ""
        txtIDD.SetFocus
   End If
    
    On Error GoTo erro
    
     txtNom = WorksheetFunction.VLookup(CDec(txtIDD), Range("A:D"), 3, False)
     txtRegistro = WorksheetFunction.VLookup(CDec(txtIDD), Range("A:D"), 2, False)
     txtAre = WorksheetFunction.VLookup(CDec(txtIDD), Range("A:D"), 4, False)

    On Error GoTo 0
    Exit Sub

erro:
    txtIDD = ""
    txtNom = ""
    txtAre = ""
    txtRegistro = ""
    msgbox "Registro não existe", vbCritical

End Sub

Private Sub UserForm_Click()

End Sub
