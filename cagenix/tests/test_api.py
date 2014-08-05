import os
import json
import requests

from security import encrypt_password

from apihandler import make_headers, make_post_request, make_put_request, make_get_request, make_delete_request


class TestPractitionersAPI:
    api_url_base = 'http://127.0.0.1:5000/api/v1/practitioners/'
    bad_data = {'cookies': 'cookies'}
    bad_headers_bad_content_type = {'cookies': 'cookies'}
    bad_headers_good_content_type = {'content-type': 'application/json'}
    bad_data_type = {
        'first_name': 'Chocolate',
        'last_name': 'Chip',
        'address_one': '123 Cookie Lane',
        'address_two': '',
        'city': 'Cookieville',
        'state': 'TN',
        'zip_code': '37201',
        'email': 'jason@mailthemyers.com',
        'password': 'cookiesdeal',
        'activation_code': '0342QB6FWP9ZY5J',
        'primary_color': '',
        'secondary_color': '',
        'practice': '',
    }

    good_create_data = {
        'first_name': 'Chocolate',
        'last_name': 'Chip',
        'address_one': '123 Cookie Lane',
        'city': 'Cookieville',
        'state': 'TN',
        'zip_code': '37201',
        'email': 'jason@mailthemyers.com',
        'password': 'cookiesdeal',
        'activation_code': 'DPJE3XFBVM271HC',
    }

    good_edit_data = {
        'first_name': 'Chocolate',
        'last_name': 'Chip',
        'address_one': '123 Cookie Lane',
        'city': 'Cookieville2',
        'state': 'TN',
        'zip_code': '37201',
        'email': 'jason@mailthemyers.com',
    }

    bad_auth_data = {
        'email': 'jason@mailthemyers.com',
        'password': 'bad_cookies',
    }

    good_auth_data = {
        'email': 'jason@mailthemyers.com',
        'password': 'cookies',
    }

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        from cagenix.users.models import User

        self.user = User(first_name='Chocolate', last_name='Chip', email='jason@mailthemyers.com', activation_code='DPJE3XFBVM271HC', password=encrypt_password('cookies'))
        self.user.gen_secret()
        db.session.add(self.user)
        db.session.commit()

    def teardown_method(self, method):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        from cagenix.users.models import User

        user = User.by_email('jason@mailthemyers.com')
        if user:
            db.session.delete(user)
            db.session.commit()

    def test_bad_method(self):
        url = self.api_url_base + 'create'
        request = requests.get(url, headers=self.bad_headers_bad_content_type, data=self.bad_data)
        assert request.status_code == 403

    def test_bad_or_no_content_type(self):
        url = self.api_url_base + 'create'
        response = {
            'request': None,
            'response': {
                'error': 'Content-type not set or Content-type not application/json'
            }
        }
        request = requests.post(url, headers=self.bad_headers_bad_content_type, data=self.bad_data)
        assert request.status_code == 405
        assert response == json.loads(request.text)

    def test_practitioner_create_bad_data(self):
        headers = {
            'content-type': 'application/json',
        }
        url = self.api_url_base + 'create'
        response = {
            'request': {
                'cookies': 'cookies'
            },
            'response': {
                'error': "additional property 'cookies' not defined by 'properties' or 'patternProperties' are not allowed in field '_data'"
            }
        }
        status_code, request = make_post_request(headers, self.bad_data, url)
        assert status_code == 400
        assert response == json.loads(request)

    def test_practitioner_create_bad_data_type(self):
        headers = {
            'content-type': 'application/json',
        }
        url = self.api_url_base + 'create'
        response = {
            'request': {
                'activation_code': '0342QB6FWP9ZY5J',
                'address_one': '123 Cookie Lane',
                'address_two': '',
                'city': 'Cookieville',
                'email': 'jason@mailthemyers.com',
                'first_name': 'Chocolate',
                'last_name': 'Chip',
                'practice': '',
                'primary_color': '',
                'secondary_color': '',
                'state': 'TN',
                'zip_code': '37201'
            },
            'response': {
                'error': "Value u'' for field 'practice' is not of type integer"
            }
        }
        status_code, request = make_post_request(headers, self.bad_data_type, url)
        assert status_code == 400
        assert response == json.loads(request)

    def test_practitioner_create(self):
        headers = {
            'content-type': 'application/json',
        }
        url = self.api_url_base + 'create'
        response = {
            'request': {
                'first_name': 'Chocolate',
                'last_name': 'Chip',
                'address_one': '123 Cookie Lane',
                'city': 'Cookieville',
                'state': 'TN',
                'zip_code': '37201',
                'email': 'jason@mailthemyers.com',
                'activation_code': 'DPJE3XFBVM271HC',
            },
            'response': {
                'practitioner_id': 2
            }
        }
        status_code, request = make_post_request(headers, self.good_create_data, url)
        assert status_code == 201
        assert response == json.loads(request)

    def test_practitioner_good_edit(self):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()
        url = self.api_url_base + str(self.user.id)
        response = {
            'request': {
                'first_name': 'Chocolate',
                'last_name': 'Chip',
                'address_one': '123 Cookie Lane',
                'city': 'Cookieville2',
                'state': 'TN',
                'zip_code': '37201',
                'email': 'jason@mailthemyers.com',
            },
            'response': {
                'practitioner_id': 2,
                'active': True
            }
        }
        headers = make_headers(self.good_edit_data, self.user.email, self.user.secret)
        status_code, request = make_put_request(headers, self.good_edit_data, url)
        assert status_code == 200
        assert response == json.loads(request)

    def test_practitioner_get(self):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()
        url = self.api_url_base + str(self.user.id) + '?'
        response = {
            u'request': {
                u'practitioner_id': 2
            },
            u'response': {
                u'city': None,
                u'first_name': u'Chocolate',
                u'last_name': u'Chip',
                u'practice': None,
                u'secondary_color': None,
                u'address_two': None,
                u'primary_color': None,
                u'state': None,
                u'address_one': None,
                u'active': True,
                u'activation_code': u'DPJE3XFBVM271HC',
                u'email': u'jason@mailthemyers.com',
                u'zip_code': None
            }
        }
        status_code, request = make_get_request(self.user, url)
        assert status_code == 200
        assert response == json.loads(request)

    def test_practitioner_delete(self):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()
        url = self.api_url_base + str(self.user.id)
        response = {
            'request': {
                'practitioner_id': self.user.id,
            },
            'response': {
                'status': 'Success',
            }
        }

        good_delete_data = {
            'practitioner_id': 2,
        }

        headers = make_headers(good_delete_data, self.user.email, self.user.secret)
        status_code, request = make_delete_request(headers, good_delete_data, url)
        assert status_code == 200
        assert response == json.loads(request)

    def test_practitioner_bad_login(self):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()

        headers = {
            'content-type': 'application/json',
        }
        url = self.api_url_base + 'login'
        response = {
            'request': {
                'email': 'jason@mailthemyers.com',
            },
            'response': {
                'error': 'Authentication Failed'
            }
        }
        status_code, request = make_post_request(headers, self.bad_auth_data, url)
        assert status_code == 401
        assert response == json.loads(request)

    def test_practitioner_good_login(self):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()

        headers = {
            'content-type': 'application/json',
        }
        url = self.api_url_base + 'login'
        response = {
            'request': {
                'email': 'jason@mailthemyers.com',
            },
            'response': {
                'secret': self.user.secret,
            }
        }
        status_code, request = make_post_request(headers, self.good_auth_data, url)
        assert status_code == 200
        assert response == json.loads(request)


class TestPatientsAPI:
    api_url_base = 'http://127.0.0.1:5000/api/v1/patients/'

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        from cagenix.users.models import User
        from cagenix.practices.models import Practice
        from cagenix.patients.models import Patient
        self.practice = Practice(practice_name='Cookie Dental Clinic', address_one='123 Cookie Lane', city='Cookieville', state='TN', zip_code='37037', phone='+16155555555', active=True)
        db.session.add(self.practice)
        db.session.commit()
        self.user = User(first_name='Chocolate', last_name='Chip', email='jason@mailthemyers.com', activation_code='DPJE3XFBVM271HC', password=encrypt_password('cookies'))
        self.user.gen_secret()
        self.user.activated = True
        db.session.add(self.user)
        db.session.commit()
        self.patient = Patient(first_name='Chocolate', last_name='Chip', address_one='123 Cookie Lane', city='Cookieville', state='TN', zip_code='37201', email='jason@mailthemyers.com2', practice=self.practice, dentist=self.user)
        db.session.add(self.patient)
        db.session.commit()

    def teardown_method(self, method):
        os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'
        from cagenix import db
        from cagenix.patients.models import Patient
        db.session.delete(self.practice)
        db.session.delete(self.user)

        patient = Patient.by_email('jason@mailthemyers.com')
        if patient:
            db.session.delete(patient)
        if self.patient:
            db.session.delete(self.patient)

        db.session.commit()

    def test_patient_create(self):
        url = self.api_url_base + 'create'
        good_create_data = {
            'first_name': 'Chocolate',
            'last_name': 'Chip',
            'address_one': '123 Cookie Lane',
            'city': 'Cookieville',
            'state': 'TN',
            'zip_code': '37201',
            'email': 'jason@mailthemyers.com',
            'practice_id': self.practice.id,
            'dentist_id': self.user.id,
        }
        response = {
            'request': {
                u'city': u'Cookieville',
                u'first_name': u'Chocolate',
                u'last_name': u'Chip',
                u'dentist_id': 2,
                u'practice_id': 1,
                u'state': u'TN',
                u'address_one': u'123 Cookie Lane',
                u'email': u'jason@mailthemyers.com',
                u'zip_code': u'37201',
                u'practice_id': self.practice.id,
                u'dentist_id': self.user.id,
            },
            'response': {
                'patient_id': 2
            }
        }
        headers = make_headers(good_create_data, self.user.email, self.user.secret)
        status_code, request = make_post_request(headers, good_create_data, url)
        assert status_code == 201
        assert response == json.loads(request)

    def test_patient_delete(self):
        url = self.api_url_base + str(self.patient.id)
        response = {
            'request': {
                'patient_id': self.patient.id,
            },
            'response': {
                'status': 'Success',
            }
        }

        good_delete_data = {
            'patient_id': self.patient.id,
        }

        headers = make_headers(good_delete_data, self.user.email, self.user.secret)
        status_code, request = make_delete_request(headers, good_delete_data, url)
        assert status_code == 200
        assert response == json.loads(request)

    def test_patient_good_edit(self):
        url = self.api_url_base + str(self.patient.id)
        good_edit_data = {
            u'active': True,
            u'first_name': u'Chocolate',
            u'last_name': u'Chip',
            u'address_one': u'123 Cookie Lane',
            u'city': u'Cookieville',
            u'state': u'TN',
            u'zip_code': u'37201',
            u'email': u'jason@mailthemyers.com2',
            u'choice_one': '',
            u'choice_two': '',
            u'choice_three': '',
            u'practice_id': 1,
            u'dentist_id': 2,
        }
        response = {
            'request': {
                u'active': True,
                u'first_name': u'Chocolate',
                u'last_name': u'Chip',
                u'address_one': u'123 Cookie Lane',
                u'city': u'Cookieville',
                u'state': u'TN',
                u'zip_code': u'37201',
                u'email': u'jason@mailthemyers.com2',
                u'choice_one': '',
                u'choice_two': '',
                u'choice_three': '',
                u'practice_id': 1,
                u'dentist_id': 2,
            },
            'response': {
                'patient_id': 1,
                'active': True
            }
        }
        headers = make_headers(good_edit_data, self.user.email, self.user.secret)
        status_code, request = make_put_request(headers, good_edit_data, url)
        print json.loads(request)
        assert status_code == 200
        assert response == json.loads(request)

    def test_practitioner_get(self):
        url = self.api_url_base + str(self.patient.id) + '?'
        response = {
            u'request': {
                u'patient_id': 1
            },
            u'response': {
                u'active': True,
                u'first_name': u'Chocolate',
                u'last_name': u'Chip',
                u'address_one': u'123 Cookie Lane',
                u'address_two': None,
                u'city': u'Cookieville',
                u'state': u'TN',
                u'zip_code': u'37201',
                u'email': u'jason@mailthemyers.com2',
                u'choice_one': None,
                u'choice_two': None,
                u'choice_three': None,
                u'practice': 1,
                u'practitioner': 2,
            }
        }
        status_code, request = make_get_request(self.user, url)
        assert status_code == 200
        assert response == json.loads(request)
