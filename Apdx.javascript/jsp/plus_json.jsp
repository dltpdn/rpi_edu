<%@ page language="java" contentType="application/json"
    pageEncoding="UTF-8"%>
<%
int op1 = Integer.parseInt(request.getParameter("op1"));
int op2 = Integer.parseInt(request.getParameter("op2"));
int result = op1 + op2;
%>
{
 	"op1" : <%=op1%>,
  	"op2" :<%=op2%>,
	"result" : <%=result%>
}