# Benford's Law

Benford's law, also called the Newcomb–Benford law, the law of 
anomalous numbers, or the first-digit law, is an observation 
about the frequency distribution of leading digits in many real-life 
sets of numerical data.

For More information: https://en.wikipedia.org/wiki/Benford%27s_law

### To run

Simply place your numbers in a txt file inside the `source` folder, one number per line
and call `main()` 


```commandline
After activating your virtual environment
$ pip install -r requirements.txt
$ python main.py
```

Results will be saved at `output` folder as `.jgp` format.

_Left some examples in the source and output directories_

### Some Usage examples of Benford's Law

* http://lycofs01.lycoming.edu/~sprgene/M400/BenfordsLaw.pdf
  
* https://blog.auditanalytics.com/benfords-law-and-financial-statements/

>Benford’s Law can recognize the probabilities of highly likely or highly unlikely 
> frequencies of numbers in a data set. The probabilities are based on mathematical logarithms 
> of the occurrence of digits in randomly generated numbers in large data sets. 
> Those who are not aware of this theory and intentionally manipulate numbers
> (e.g., in a fraud) are susceptible to getting caught by the application of 
> Benford’s Law. The IT auditor can also apply Benford’s Law in tests of controls 
> and other IT-related tests of data sets. However, the IT auditor needs to 
> remember to make sure that the constraints (mathematical assumptions of the theory)
> are compatible with the data set to be tested *

\*[https://www.isaca.org/](https://www.isaca.org/resources/isaca-journal/past-issues/2011/understanding-and-applying-benfords-law#:~:text=Benford's%20Law%20can%20recognize%20the,numbers%20in%20large%20data%20sets.)
