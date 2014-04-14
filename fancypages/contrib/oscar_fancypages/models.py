from ...library import register_content_block
from . import abstract_models


@register_content_block
class SingleProductBlock(abstract_models.AbstractSingleProductBlock):
    pass


@register_content_block
class HandPickedProductsPromotionBlock(
    abstract_models.AbstractHandPickedProductsPromotionBlock
):
    pass


@register_content_block
class AutomaticProductsPromotionBlock(
    abstract_models.AbstractAutomaticProductsPromotionBlock
):
    pass


@register_content_block
class OfferBlock(abstract_models.AbstractOfferBlock):
    pass


@register_content_block
class PrimaryNavigationBlock(abstract_models.AbstractPrimaryNavigationBlock):
    pass
