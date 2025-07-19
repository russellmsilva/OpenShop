import io
import os
import glob
import tempfile
from django.test import override_settings
from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Product
from PIL import Image
from products.forms import ProductForm

#Creates a mock image upload for test without referencing real files from disk
#@todo test actual image files to verify dimensions and format validation as well as check if it's saved properly
def create_test_image():
    img_stream = io.BytesIO()
    image = Image.new('RGB', (100, 100), color='blue')  # Create a 100x100 blue square
    image.save(img_stream, format='JPEG')               # Save as JPEG
    img_stream.seek(0)                                  # Reset stream position

    test_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=img_stream.read(),
        content_type='image/jpeg'
    )

    return test_image

#Helper function to create a test product instance.
def create_test_product(user=None, image=None):
    if user is None:
        user = User.objects.create_user(username='testuser', password='12345')
    if image is None:
        image = create_test_image()

    product = Product.objects.create(
        owner = user,
        name='Test Product',
        description='This is a test product.',
        image=image
    )
    return product

# Test case for product views.
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class ProductViewTest(TestCase):
    # Create a user and log them in for testing.
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    # Clean up any images that may have been created during the test
    def tearDown(self):
        image_dir = os.path.join(settings.MEDIA_ROOT, 'product_images')
        test_images = glob.glob(os.path.join(image_dir, 'test_image*'))
        for img_path in test_images:
            if os.path.exists(img_path):
                os.remove(img_path)

    # Ensure the new product view works correctly.
    def test_new_product_view(self):
        response = self.client.get(reverse('new_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')

    # Ensure the product list view works correctly.
    def test_product_list_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')

    # Ensure a product can be created successfully.
    def test_create_product(self):
        self.test_image = create_test_image()
        response = self.client.post(reverse('new_product'), {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'image': self.test_image
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Product.objects.filter(name='Test Product').exists()) # Check if product was created

# Test case for product model.
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class ProductModelTest(TestCase):
    def setUp(self):
        self.test_image = create_test_image()
        self.product = create_test_product(image=self.test_image)

    # Clean up any images that may have been created during the test
    def tearDown(self):
        image_dir = os.path.join(settings.MEDIA_ROOT, 'product_images')
        test_images = glob.glob(os.path.join(image_dir, 'test_image*'))
        for img_path in test_images:
            if os.path.exists(img_path):
                os.remove(img_path)

    # Ensure that the product is created correctly.
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'This is a test product.')
        self.assertIsNotNone(self.product.owner)
        self.assertEqual(self.product.owner.username, 'testuser')
        self.assertEqual(self.product.image.name.split('/')[-1], self.test_image.name)

    # Ensure that the string representation of the product is correct.
    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

# Test case for product form.
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class ProductFormTest(TestCase):
    def setUp(self):
        self.test_image = create_test_image()

    # Clean up any images that may have been created during the test
    def tearDown(self):
        image_dir = os.path.join(settings.MEDIA_ROOT, 'product_images')
        test_images = glob.glob(os.path.join(image_dir, 'test_image*'))
        for img_path in test_images:
            if os.path.exists(img_path):
                os.remove(img_path)

    # Ensure the product form is valid with correct data.
    def test_product_form_valid(self):
        form_data = {
            'name': 'Test Product',
            'description': 'This is a test product.'
        }
        form_files = {
            'image': self.test_image
        }
        form = ProductForm(data=form_data, files=form_files)
        self.assertTrue(form.is_valid())

    # Ensure the product form is invalid with missing required fields.
    def test_product_form_invalid(self):
        form_data = {
            'name': '',
            'description': ''
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Ensure the product form saves correctly.
    def test_product_form_save(self):
        form_data = {
            'name': 'Test Product',
            'description': 'This is a test product.'
        }
        form_files = {
            'image': self.test_image
        }
        form = ProductForm(data=form_data, files=form_files)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = User.objects.create_user(username='testuser', password='12345')
            product.save()
            self.assertTrue(Product.objects.filter(name='Test Product').exists())

# Test case for product listing.
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class ProductListViewTest(TestCase):
    # Create a user and log them in for testing.
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    # Clean up any images that may have been created during the test
    def tearDown(self):
        image_dir = os.path.join(settings.MEDIA_ROOT, 'product_images')
        test_images = glob.glob(os.path.join(image_dir, 'test_image*'))
        for img_path in test_images:
            if os.path.exists(img_path):
                os.remove(img_path)

    # Ensure the product list view displays products correctly.
    def test_product_list_view(self):
        self.test_image = create_test_image()
        create_test_product(user=self.user, image=self.test_image)  # Create a test product
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertContains(response, 'Test Product')  # Check if the product is listed
        self.assertContains(response, 'test_image.jpg')

        # Ensure the product is displayed in the list
        products = response.context['products']
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'Test Product')
        self.assertEqual(products[0].description, 'This is a test product.')
        self.assertEqual(products[0].owner.username, 'testuser')
        self.assertEqual(products[0].image.name.split('/')[-1], self.test_image.name)
