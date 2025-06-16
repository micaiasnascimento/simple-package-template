from setuptools import setup, find_packages

setup(
    name='simple_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Adicione aqui as dependências, se houver
    description='Um pacote simples para cálculos.',
    long_description=open('README.md', encoding='utf-8').read(),  # Garantir a leitura com encoding correto
    long_description_content_type='text/markdown',
    author='Micaias',
    author_email='micaiasnascimentoo@gmail.com',
    url='https://github.com/micaiasnascimento/simple-package-template',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Verifique se você usa MIT ou outra licença
        'Operating System :: OS Independent',
    ],
)
