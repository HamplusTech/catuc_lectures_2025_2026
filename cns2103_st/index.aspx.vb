Imports System.Data.SqlClient

Partial Class index
    Inherits System.Web.UI.Page

    Protected Sub register_Click(sender As Object, e As EventArgs) Handles register.Click
        Dim cn As SqlConnection = New SqlConnection("Data Source=localhost\SQLEXPRESS;Initial Catalog=catuc_st;Integrated Security=True")
        If cn.State = Data.ConnectionState.Open Then
            cn.Close()
        End If
        cn.Open()

        Dim cm As SqlCommand = New SqlCommand("INSERT into users (username, fullname, password) VALUES (@p,@n,@t)", cn)
        cm.Parameters.AddWithValue("@p", username.Text)
        cm.Parameters.AddWithValue("@n", fullname.Text)
        cm.Parameters.AddWithValue("@t", password.Text)
        cm.ExecuteNonQuery()

        username.Text = ""
        fullname.Text = ""
        password.Text = ""

        ClientScript.RegisterStartupScript(Me.GetType(), "alert", "alert('User Registeration Done!');window.location='index.aspx'", True)
    End Sub
End Class
