VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmCONT 
   Caption         =   "Cadastro"
   ClientHeight    =   4515
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4110
   OleObjectBlob   =   "frmCONT.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmCONT"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub btoOK_Click()

    Dim id As Double
    Dim i As Double
    Dim data As Date
    
    data = txtDia & "/" & txtMes & "/" & txtAno
    
    If txtNome = "" Then
        MsgBox "Insira um nome", vbCritical
        txtNome = ""
        txtNome.SetFocus
    End If
    
    If IsNumeric(txtDia) = False Then
        MsgBox "Insira uma data", vbCritical
        txtDia = ""
        txtDia.SetFocus
    ElseIf IsNumeric(txtMes) = False Then
        MsgBox "Insira um mês", vbCritical
        txtMes = ""
        txtMes.SetFocus
    ElseIf IsNumeric(txtAno) = False Then
        MsgBox "Insira um ano", vbCritical
        txtAno = ""
        txtAno.SetFocus
    End If
            
    If IsNumeric(txtDep) = False Then
        MsgBox "Insira um depósito", vbCritical
        txtDep = ""
        txtDep.SetFocus
    End If
    
    id = WorksheetFunction.Max(Range("A:A")) + 1

    Range("A" & Rows.Count).End(xlUp).Offset(1, 0) = id
    Range("A" & Rows.Count).End(xlUp).Offset(0, 1) = txtNome
    Range("A" & Rows.Count).End(xlUp).Offset(0, 2) = data
    Range("A" & Rows.Count).End(xlUp).Offset(0, 3) = CDec(txtDura)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 4) = WorksheetFunction.EDate(data, txtDura)
    Range("A" & Rows.Count).End(xlUp).Offset(0, 4).NumberFormat = "dd/mm/yyyy"
    Range("A" & Rows.Count).End(xlUp).Offset(0, 5) = txtDep * 3
    Range("A" & Rows.Count).End(xlUp).Offset(0, 5).NumberFormat = "$#,##0.00"
    
End Sub

Private Sub btoPesq_Click()

    Dim fc As Range
    
    Set fc = Range("A:F").Find(what:=txtNome, LookIn:=xlValues, lookat:=xlWhole)
    
    If fc Is Nothing Then
        MsgBox "Nome não encontrado :(", vbCritical
        txtNome = ""
        txtDia = ""
        txtMes = ""
        txtAno = ""
        txtDep = ""
        txtDura = ""
    Else
        txtNome = WorksheetFunction.VLookup(txtNome, Range("A:F"), 2, True)
        
        
    
    
End Sub



Private Sub txtMes_Change()
 s = txtMes.ListIndex + 1
 txtDia.Clear

    Select Case s
        Case 2
            For X = 1 To 28
                txtDia.AddItem X
            Next X
        Case 4, 6, 9, 11
            For X = 1 To 30
                txtDia.AddItem X
            Next X
        Case Else
            For X = 1 To 31
                txtDia.AddItem X
            Next X
    End Select
End Sub

Private Sub UserForm_Initialize()

    Dim d As Double
    Dim df As Double
    Dim m As Double
    Dim a As Double
    Dim s As Integer
    Dim du As Integer
    
    For d = 1 To 31
        txtDia.AddItem (d)
    Next d
    
    For m = 1 To 12
        txtMes.AddItem (m)
    Next m
    
    For a = 2000 To Year(Now) + 10
        txtAno.AddItem (a)
    Next a
    
    For dur = 1 To 100
        txtDura.AddItem (dur)
    Next dur
 
End Sub
