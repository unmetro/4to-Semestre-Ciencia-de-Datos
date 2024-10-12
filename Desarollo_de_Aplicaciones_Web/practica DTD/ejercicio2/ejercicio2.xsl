<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Alumnos</title>
            </head>
            <body>
                <h1>Información de los alumnos</h1>
                <table border="1">
                    <tr>
                        <th>CURP</th>
                        <th>Nombre</th>
                        <th>Historia Académica</th>
                    </tr>
                    <xsl:for-each select="alumnos/alumno">
                        <tr>
                            <td><xsl:value-of select="CURP"/></td>
                            <td>
                                <xsl:value-of select="nombre/apellidoPaterno"/> 
                                <xsl:value-of select="nombre/apellidoMaterno"/> 
                                <xsl:value-of select="nombre/nombres"/>
                            </td>
                            <td>
                                <xsl:for-each select="historiaAcademica/asignatura">
                                    <p><strong>Asignatura:</strong> <xsl:value-of select="nombre"/></p>
                                    <p><strong>Calificación:</strong> <xsl:value-of select="calificacion"/></p>
                                    <p><strong>Fecha de Acreditación:</strong> <xsl:value-of select="fechaAcreditacion"/></p>
                                    <p><strong>Tipo de Examen:</strong> <xsl:value-of select="tipoExamen"/></p>
                                    <hr/>
                                </xsl:for-each>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
