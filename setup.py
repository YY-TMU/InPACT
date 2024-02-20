import sys
from distutils.core import setup

if sys.version_info < (3, 1):
    sys.exit('Sorry, InPACT requires Python >= 3.1 (Tested with Python 3.6.15)')

setup(name = 'InPACT',
      version = "1.0", 
      description='InPACT is a method that identifies and quantifies IPA sites.',
      url='https://github.com/YY-TMU/InPACT',
      scripts=['inpact/InPACT',
               'inpact/InPACT_annotation_prepare',
               'inpact/InPACT_feat_filter',
               'inpact/InPACT_feat_region',
               'inpact/InPACT_last_base_filter',
               'inpact/InPACT_potential_TE',
               'inpact/InPACT_predict',
               'inpact/InPACT_read_train_model',
               'inpact/InPACT_read_train_prepare',
               'inpact/InPACT_transcript',
               'inpact/InPACT_quantify'],
      install_requires=['pandas == 1.1.5',
                        'numpy == 1.19.5',
                        'pybedtools  == 0.9.0',
                        'HTseq == 0.9.1',
                        'scikit-learn == 1.0.1',
                        'imbalanced-learn == 0.8.1',
                        'joblib == 1.1.0',
                        'pyfasta == 0.5.2' 
                        ],
      python_requires='~=3.6',
      )

