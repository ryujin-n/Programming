VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmturma 
   Caption         =   "UserForm1"
   ClientHeight    =   2610
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4980
   OleObjectBlob   =   "frmturma.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmturma"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub CommandButton1_Click()

    
    If txtregis = "" Then
        msgbox "insiria um valor válido"
        txtregis = ""
        txtregis.SetFocus
        Exit Sub
        
    ElseIf txtNOME = "" Then
        msgbox "insiria um valor válido"
        txtNOME = ""
        txtNOME.SetFocus
        Exit Sub
        
    ElseIf IsNumeric(txtdi) = False Then
        msgbox "insiria um valor válido"
        txtdi = ""
        txtdi.SetFocus
        Exit Sub
        
    ElseIf IsNumeric(txtme) = False Then
        msgbox "insiria um valor válido"
        txtme = ""
        txtme.SetFocus
        Exit Sub
        
    ElseIf IsNumeric(txtan) = False Then
        msgbox "insiria um valor válido"
        txtan = ""
        txtan.SetFocus
        Exit Sub
        
    ElseIf txtcu = "" Then
        msgbox "insiria um valor válido"
        txtcu = ""
        txtcu.SetFocus
        Exit Sub
        
        End If
    
   Do
    
    On Error GoTo erro
    saas = True
    txtregis = WorksheetFunction.VLookup(txtregis, Range("B"), 1, False)
        If saas = True Then
            msgbox " Registro já existente "
            txtregis = ""
            txtregis.SetFocus
            Exit Sub
        End If
    On Error GoTo 0
    Loop While saas = True
    
    txtID = WorksheetFunction.Max(Range("A:A")) + 1
    
    Range("A" & Rows.Count).End(xlUp).Offset(1, 0) = CDec(txtID)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 1) = txtregis
    Range("A" & Rows.Count).End(xlUp).Offset(0, 2) = txtNOME
    Range("A" & Rows.Count).End(xlUp).Offset(0, 3) = CDec(txtdi) & "/" & CDec(txtme) & "/" & CDec(txtan)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 4) = txtcu
    
    msgbox " Dados cadastrados "
Exit Sub

erro:

    saas = False
    Resume Next
    


End Sub
Private Sub UserForm_Initialize()


Dim x As Double
Dim y As Double
Dim z As Double

    txtcu.AddItem "Desenvolvimento"
    txtcu.AddItem "Montagem e Manutenção"
    txtcu.AddItem "Redes e Sistemas"
    txtcu.AddItem "Design Gráfico"
    
    For x = 1 To 31
        txtdi.AddItem (x)
    Next x
    
     For y = 1 To 12
        txtme.AddItem (y)
    Next y
    
     For z = 2000 To 2030
        txtan.AddItem (z)
    Next z
    
End Sub
