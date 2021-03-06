from setuptools import setup

setup(name='ShapExplainers',
    version='1.0.2',
    description='Wrappers for shapley value explanations for model interpretability',
    packages=['ShapExplainers'],
    install_requires=["typing",
                      "pandas",
                      "numpy == 1.17.3",
                      'scikit-learn',
                      "shap == 0.34.0",
                      ],
)