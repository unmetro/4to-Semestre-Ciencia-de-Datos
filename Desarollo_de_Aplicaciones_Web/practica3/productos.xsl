<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/productos">
        <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    .tarjeta-mascota {
                        background-color: #f0efe5;
                        padding: 20px;
                        margin-bottom: 20px;
                        border: 1px solid #ccc;
                        display: flex;
                    }
                    .tarjeta-mascota img {
                        width: 15rem;
                        height: auto;
                        margin-right: 20px;
                    }
                    .tarjeta-mascota div {
                        flex-grow: 1;
                    }
                    .tarjeta-mascota h2 {
                        margin: 0;
                        font-size: 1.5rem;
                    }
                    .tarjeta-mascota p {
                        margin: 5px 0;
                    }
                    header {
                        margin-bottom: 4rem;
                        background-color: #008080;
                        color: antiquewhite;
                        padding: 2rem;
                    }
                    .logo img {
                        width: 100px;
                        float: left;
                    }
                    nav {
                        text-align: center;
                    }
                    nav a {
                        margin: 0 15px;
                        color: antiquewhite;
                        text-decoration: none;
                    }
                </style>
            </head>
            <body>
                <header>
                    <div class="logo">
                        <img src="/veterinaria/img/logo.png" alt="Logo de la veterinaria"></img>
                    </div>
                    <div>
                        <h1 style="text-align: center;">VETERIANARIA</h1>
                    </div>
                    <nav>
                        <a href="/veterinaria/index.html">Inicio</a>
                        <a href="servicios.html">Servicios</a>
                        <a href="adopciones.html">Adopciones</a>
                        <a href="blog.html">Blog</a>
                        <a href="tienda.html">Tienda</a>
                        <a href="nosotros.html">Nosotros</a>
                        <a href="contacto.html">Contacto</a>
                    </nav>
                </header>

                <h1>Tienda de Producto Para Mascotas</h1>
                <xsl:for-each select="producto">
                    <div class="tarjeta-mascota">
                        <img src="{imagen}" alt="Imagen de {nombre}"></img>
                        <div>
                            <h2><xsl:value-of select="nombre"/></h2>
                            <p><strong>Precio:</strong> <xsl:value-of select="precio"/> MXN</p>
                            <p><strong>Descripción:</strong> <xsl:value-of select="descripcion"/></p>
                            <button>Comprar</button>
                        </div>
                    </div>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
