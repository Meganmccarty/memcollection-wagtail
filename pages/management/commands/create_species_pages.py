from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from pages.models import SpeciesPage
from taxonomy.models import Species
from wagtail.models import Page


class Command(BaseCommand):
    help = "Create a SpeciesPage for every Species in the database that does not already have one."

    def handle(self, *args, **kwargs):
        try:
            parent_page = Page.objects.get(slug="home")
        except Page.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Parent page with slug 'home' does not exist.")
            )
            return

        species_without_pages = Species.objects.filter(species_page__isnull=True)

        for species in species_without_pages:
            species_page = SpeciesPage(
                title=species.binomial,
                species=species,
                slug=slugify(species.binomial),
            )
            parent_page.add_child(instance=species_page)
            self.stdout.write(
                self.style.SUCCESS(f"Created SpeciesPage for {species.binomial}")
            )

        self.stdout.write(self.style.SUCCESS("SpeciesPage creation process completed."))
