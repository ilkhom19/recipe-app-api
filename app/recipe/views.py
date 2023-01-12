"""
Views for the Recipe APIs.
"""
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Recipe, Tag, Ingredient
from .serializers import (
    RecipeSerializer,
    RecipeDetailSerializer,
    TagSerializer,
    IngredientSerializer,
    RecipeImageSerializer,
)


class RecipeViewSet(viewsets.ModelViewSet):
    """View to manage recipe API"""
    serializer_class = RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for logged in users."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return RecipeSerializer
        elif self.action == 'upload_image':
            return RecipeImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseRecipeAttrViewSet(mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """Base View Set to be inherited in tags, ingredients ViewSets."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return for the logged in user only."""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class TagViewSet(BaseRecipeAttrViewSet):
    """View to manage Tag API."""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(BaseRecipeAttrViewSet):
    """View to manage Ingredient API."""
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
