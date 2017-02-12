<?xml version="1.0" encoding="UTF-8"?>
<%@page import="java.util.Enumeration"%>
<%@ page language="java" contentType="application/xml"
    pageEncoding="UTF-8"%>
<%
for(Enumeration e = request.getHeaderNames(); e.hasMoreElements();){
	String name = e.nextElement().toString();
	String value = request.getHeader(name);
	System.out.println(name + ":" + value);
}
int op1 = Integer.parseInt(request.getParameter("op1"));
int op2 = Integer.parseInt(request.getParameter("op2"));
int result = op1 + op2;
%>
<data>
	<op1 value="<%=op1%>"/>
	<op2 value="<%=op2%>"/>
	<result value="<%=result%>"/>
</data>