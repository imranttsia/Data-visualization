# Data-visualization
In ANACONDA PROMPT
    Create virtual Envornment
        python -m ven eda
        .\eda\Scripts\activate
        Open jupyter notebook
        Add eda.yml file in eda folder
    Run following commands in Anaconda Prompt for package installation
        conda create -n dtale python
        conda activate dtale
        python -m pip install pandas-profiling
        conda install -c conda-forge pandas-profiling=2.6.0.
        pip install --upgrade --force-reinstall pandas
        jupyter nbextension enable --py widgetsnbextension
        conda install -c conda-forge sweetviz
        conda install -c conda-forge dataprep
        conda install -c conda-forge klib
In JUPYTER NOTEBOOK
    Import general libraries
    Upload file
    For dtale run following commands
        pip install dtale
        import dtale
        import dtale.app as dtale_app
        dtale.show(df, ignore_duplicate=True)
    For pandas-profiling
        pip install pandas-profiling
        import sys
        !{sys.executable} -m pip install pandas-profiling
        from markupsafe import escape
        pip install Jinja2==3.0.3
        pandas_profiling.__version__
        import pandas_profiling as pp
        profile = ProfileReport(df)
        profile
    For sweetviz
        import sweetviz as sv
        import numpy as np
        import pandas as pd
        shuffled = df.sample(frac=1)
        df_train, df_test = np.array_split(shuffled, 2) 
        report = sv.compare(df_train, df_test)
        report.show_html()
    For DataPrep
        from dataprep.datasets import load_dataset
        from dataprep.eda import create_report
        create_report(df).show()
    For Klib
        import klib
        import pandas as pd
        klib.missingval_plot(df)
        df_cleaned = klib.data_cleaning(df)
        df_cleaned
    
        
        
