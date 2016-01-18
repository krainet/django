from rest_framework import serializers
from images.serializers import ImageSerializer
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    # distance = serializers.SerializerMethodField('get_distance')

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'seller', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'longitude', 'latitude', 'created_at', 'images')
    #
    # def get_distance(self):
    #     location_one = (self.latitude, self.longitude)
    #     location_two = (41.499498, -81.695391)
    #     return great_circle(location_one, location_two).meters

    # def get_json(self):
    #     return {
    #         'id': self.id,
    #         'race': self.race_id,
    #         'seller': self.seller_id,
    #         'gender': self.gender_id,
    #         'sterile': self.sterile,
    #         'description': self.description,
    #         'state': self.state,
    #         'price': self.price,
    #         'category': self.category,
    #         'active': self.active,
    #         'longitude': self.longitude,
    #         'latitude': self.latitude,
    #         'created_at': self.created_at
    #     }

        # read_only_fields = ('category', 'state', 'races', 'seller')

# class ProductsListSerializer(serializers.ModelSerializer):
#
#     category = serializers.StringRelatedField()
#     state = serializers.StringRelatedField()
#     seller = serializers.StringRelatedField()
#
#     class Meta(ProductsSerializer.Meta):
#         fields = ('id', 'name', 'price', 'description', 'category', 'state', 'seller', 'images')





    # def create(self, validated_data):
    #     instance = Product()
    #     product_data = validated_data.get('product')
    #     product = Product.objects.create_user(username=product_data.get('username'),
    #                                           email=product_data.get('email'),
    #                                           password=product_data.get('password'),
    #                                           first_name=product_data.get('first_name'),
    #                                           last_name=product_data.get('last_name'))
    #     if product:
    #         instance.product = product
    #         product_ext = self.update(instance, validated_data)
    #
    #     return product_ext