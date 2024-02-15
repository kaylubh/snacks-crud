from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class SnacksTests(TestCase):

    # user and snack test fixture
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user', password='password'
        )
        self.snack = Snack.objects.create(name='snack', description='snack', purchaser=self.user)

    # model
    def test_model_create(self):
        snack = Snack.objects.create(name='snack', description='snack', purchaser=self.user)

        self.assertEqual(snack.name, 'snack')
        self.assertEqual(snack.description, 'snack')
        self.assertEqual(snack.purchaser, self.user)

    # snacks list page
    def test_snacks_list_page(self):
        url = reverse('snack_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'snack')

    # snacks detail page
    def test_snack_detail_page(self):
        url = reverse('snack_detail', args='1')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'snack')

    # create view
    def test_create_view(self):
        response = self.client.post(
            reverse('snack_create'),
            {
                'name': 'create',
                'description': 'snack',
                'purchaser': self.user.id,
            },
            follow=True
        )

        self.assertRedirects(response, reverse('snack_detail', args='2'))
        self.assertContains(response, 'create')
    
    # update view
    def test_update_view(self):
        response = self.client.post(
            reverse('snack_update', args='1'),
            {
                'name': 'update',
                'description': 'snack',
                'purchaser': self.user.id,
            },
            follow=True
        )

        self.assertRedirects(response, reverse('snack_detail', args='1'))
        self.assertContains(response, 'update')
        
    # delete view
    def test_delete_view(self):
        response = self.client.get(reverse('snack_delete', args='1'))

        self.assertEqual(response.status_code, 200)
