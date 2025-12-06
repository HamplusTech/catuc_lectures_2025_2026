<%@ Page Language="VB" AutoEventWireup="false" CodeFile="index.aspx.vb" Inherits="index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:TextBox ID="username" runat="server" ToolTip="Type Username"></asp:TextBox>
        <br />
        <asp:TextBox ID="fullname" runat="server" ToolTip="Type Full Name"></asp:TextBox>
        <br />
        <asp:TextBox ID="password" runat="server" TextMode="Password" ToolTip="Type Password" ></asp:TextBox>
        <br />
        <asp:Button ID="register" runat="server" Text="Register" />
        <asp:Button ID="clear" runat="server" Text="Clear" />
    
    </div>
    </form>
</body>
</html>
