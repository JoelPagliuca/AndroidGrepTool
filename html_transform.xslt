<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
	<head>
		<title>Stormtrooper</title>
	</head>
	<body>
		<h1>Stormtrooper analysis results</h1>
		<xsl:apply-templates select="stormtrooper/category"/>
	</body>
</html>
</xsl:template>

<xsl:template match="category">
	<h2><xsl:value-of select="@title"/></h2>
	<ul>
		<xsl:apply-templates select="checks"/>
	</ul>
</xsl:template>

<xsl:template match="checks">
	<xsl:apply-templates select="check"/>
</xsl:template>

<xsl:template match="check">
	<li><xsl:value-of select="@regex"/></li>
	<ul><xsl:apply-templates select="file" /></ul>
</xsl:template>

<xsl:template match="file">
	<li><xsl:value-of select="@name"/></li>
	<ul><xsl:apply-templates select="line" /></ul>
</xsl:template>

<xsl:template match="line">
	<li>
	[<xsl:value-of select="@number"/>] <xsl:value-of select="."/>
	</li>
</xsl:template>

</xsl:stylesheet>