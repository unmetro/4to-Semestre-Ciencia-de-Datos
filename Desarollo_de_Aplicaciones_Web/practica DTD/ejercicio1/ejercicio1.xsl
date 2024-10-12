<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Biblioteca</title>
            </head>
            <body>
                <h1>Biblioteca</h1>
                <table border="1">
                    <tr>
                        <th>Título</th>
                        <th>Autor</th>
                        <th>Fecha de Nacimiento</th>
                        <th>Año de Publicación</th>
                    </tr>
                    <xsl:for-each select="biblioteca/libro">
                        <tr>
                            <td><xsl:value-of select="titulo"/></td>
                            <td><xsl:value-of select="autor/nombre"/></td>
                            <td><xsl:value-of select="autor/fechaNacimiento"/></td>
                            <td><xsl:value-of select="fechaPublicacion/@año"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
