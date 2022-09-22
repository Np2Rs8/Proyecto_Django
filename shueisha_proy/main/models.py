"""
    Importacion de librerias necesarias.
"""
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

"""
    Tabla de Portada con campos:
        fecha de creación.
        imagen de fondo.
        nombre del tema.
        frase sobre el tema.
        y si está activo.
"""
class Portada(models.Model):
    verbose_name_plural = 'Portadas'
    verbose_name = 'Portada'
    ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    wallpaper = models.ImageField(blank=True, null=True, upload_to="portada")
    name = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    """
        Devuelve el campo del nombre del blog.
    """
    def __str__(self):
        return self.name



"""
    Tabla Blog con campos:
        fecha de creación.
        autor.
        descripcion.
        cuerpo.
        slug. (que habla de los sub-blogs)
        imagen.
        y si está activo.
"""
class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    """
        Se encaga de los sub-blogs como la dirección url que está dada por la descripcion del blog.
    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.description)
        super(Blog, self).save(*args, **kwargs)

    """
        Devuelve el campo de la descripcion del blog.
    """
    def __str__(self):
        return self.description

    """
        Se encaga de los sub-blogs como la dirección url que está dada por la descripcion del blog.
    """
    def get_absolute_url(self):
        return f"/blog/{self.slug}"


"""
    Tabla Review con campos:
        fecha de creación.
        autor.
        descripcion.
        cuerpo.
        slug. (que habla de las sub-reviews)
        imagen.
        y si está activo.
"""
class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'
        verbose_name = 'Review'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="review")
    is_active = models.BooleanField(default=True)

    """
        Se encaga de las sub-reviews como la dirección url que está dada por la descripcion del la review.
    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.description)
        super(Review, self).save(*args, **kwargs)

    """
        Devuelve el campo de la descripcion del blog.
    """
    def __str__(self):
        return self.description

    """
        Se encaga de las sub-reviews como la dirección url que está dada por la descripcion del la review.
    """
    def get_absolute_url(self):
        return f"/review/{self.slug}"


