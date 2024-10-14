<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/pagina6">
        <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    .profile-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: 20px auto;
                        background-color: #f5f5f5;
                        padding: 20px;
                        border-radius: 15px;
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                        max-width: 900px;
                    }
                    .profile-container img {
                        width: 190px;
                        height: auto;
                        border-radius: 10%;
                        margin-right: 20px;
                    }
                    .profile-container div {
                        text-align: left;
                        max-width: 600px;
                    }
                </style>
            </head>
            <body>
                <div class="profile-container">
                    <img src="cat.jpg" alt="gato"></img>
                    <div>
                        <h2><xsl:value-of select="gato"/></h2>
                        <p><xsl:value-of select="descripcion"/></p>
                    </div>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
