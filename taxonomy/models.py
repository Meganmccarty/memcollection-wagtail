from django.db import models

from mixins.models import TimeStampMixin


class TaxonomyBase(models.Model):
    """An abstract model for a TaxonomyBase object. This model can be used as the foundation for all
    other taxonomy models.

    Attributes:
        name (str): The scientific name of the taxon.
        common_name (str): The common name of the taxon, if it has one.
        authority (str): The authority of the taxon.
    """

    name = models.CharField(
        max_length=100, help_text="Enter the taxon's scientific name"
    )
    common_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Enter the taxon's common name, if it has one",
    )
    authority = models.CharField(
        max_length=100, help_text="Enter the taxon's authority"
    )

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        """This method returns a string representation of the TaxonomyBase object."""

        return self.name


class Order(TimeStampMixin, TaxonomyBase):
    """A model for an Order object. Inherits from both the TimeStampMixin and TaxonomyBase."""

    pass


class Family(TimeStampMixin, TaxonomyBase):
    """A model for a Family object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        order (Order): The order to which the family belongs.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select an order to which this family belongs",
    )

    class Meta:
        verbose_name_plural = "Families"


class Subfamily(TimeStampMixin, TaxonomyBase):
    """A model for a Subfamily object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        family (Family): The family to which the subfamily belongs.
    """

    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select the family to which this subfamily belongs",
    )

    class Meta:
        verbose_name_plural = "Subfamilies"


class Tribe(TimeStampMixin, TaxonomyBase):
    """A model for a Tribe object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        subfamily (Subfamily): The subfamily to which the tribe belongs.
    """

    subfamily = models.ForeignKey(
        Subfamily,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select the subfamily to which this tribe belongs",
    )


class Genus(TimeStampMixin, TaxonomyBase):
    """A model for a Genus object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        tribe (Tribe): The tribe to which the genus belongs.
    """

    tribe = models.ForeignKey(
        Tribe,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select the tribe to which this genus belongs",
    )

    class Meta:
        verbose_name_plural = "Genera"


class Species(TimeStampMixin, TaxonomyBase):
    """A model for a Species object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        genus (Genus): The genus to which the species belongs.
        mona (str): The MONA (Hodges) number for the species (Lepidoptera only).
        p3 (str): The P3 (Pohl, Patterson, Pelham 2016) number for the species (Lepidoptera only).
        ps (str): The Phylogenetic Sequence (Pohl and Nanz, 2023) number for the species
        (Lepidoptera only).
    """

    genus = models.ForeignKey(
        Genus,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select the genus to which this species belongs",
    )
    mona = models.CharField(
        null=True,
        blank=True,
        verbose_name="MONA #",
        help_text="Enter the MONA (Hodges) number for the species (Lepidoptera only)",
    )
    p3 = models.CharField(
        null=True,
        blank=True,
        verbose_name="P3 #",
        help_text="Enter the P3 (Pohl, Patterson, Pelham 2016) number for the species (Lepidoptera \
            only)",
    )
    ps = models.CharField(
        null=True,
        blank=True,
        verbose_name="PS #",
        help_text="Enter the Phylogenetic Sequence (Pohl and Nanz, 2023) number for the species \
            (Lepidoptera only)",
    )

    class Meta:
        ordering = ["genus", "name"]
        verbose_name_plural = "Species"

    def __str__(self):
        """This method returns a string representation of the Species object."""

        return self.binomial

    @property
    def binomial(self):
        """This method returns the species' binomial."""

        return f"{self.genus.name} {self.name}"


class Subspecies(TimeStampMixin, TaxonomyBase):
    """A model for a Subspecies object. Inherits from both the TimeStampMixin and TaxonomyBase.

    Attributes:
        species (Species): The species to which the subspecies belongs.
        mona (str): The MONA (Hodges) number for the subspecies (Lepidoptera only).
        p3 (str): The P3 (Pohl, Patterson, Pelham 2016) number for the subspecies (Lepidoptera
        only).
        ps (str): The Phylogenetic Sequence (Pohl and Nanz, 2023) number for the subspecies
        (Lepidoptera only).
    """

    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Select the species to which this subspecies belongs",
    )
    mona = models.CharField(
        null=True,
        blank=True,
        verbose_name="MONA #",
        help_text="Enter the MONA (Hodges) number for the subspecies (Lepidoptera only). If it \
            lacks its own MONA number, use the nominate species' number",
    )
    p3 = models.CharField(
        null=True,
        blank=True,
        verbose_name="P3 #",
        help_text="Enter the P3 (Pohl, Patterson, Pelham 2016) number for the subspecies \
            (Lepidoptera only). If it lacks its own P3 number, use the nominate species' number",
    )
    ps = models.CharField(
        null=True,
        blank=True,
        verbose_name="PS #",
        help_text="Enter the Phylogenetic Sequence (Pohl and Nanz, 2023) number for the subspecies \
            (Lepidoptera only). If it lacks its own Phylogenetic Sequence number, use the \
            nominate species' number",
    )

    class Meta:
        ordering = ["species", "name"]
        verbose_name_plural = "Subspecies"

    def __str__(self):
        """This method returns a string representation of the Subspecies object."""

        return self.trinomial

    @property
    def trinomial(self):
        """This method returns the subspecies' trinomial."""

        return f"{self.species} {self.name}"
