from setuptools import setup, find_packages

setup(name="mbtest",
      version='1.0',
      description="Practice API testing",
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "PyMySQL==1.1.0",
          "pytest==7.4.2",
          "pytest-html==4.0.2",
          "pytest-metadata==3.0.0",
          "requests==2.31.0",
          "requests-oauthlib==1.3.1",
          "WooCommerce==3.0.0",
      ],
      package_data={
          'mbtest': ['src/data/create_order_payload.json'],
      },
      )
