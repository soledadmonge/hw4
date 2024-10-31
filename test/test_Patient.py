import sys
import os
import pytest

sys.path.append(os.path.abspath("../../"))  
from hw5_lib.hw5_lib.hw5 import Patient

def test_add_test():
    patient = Patient(name='Matias', symptoms='Narcolepsy')
    patient.add_test(test_name='fever', test_results=True)
    assert patient.test == [('fever',True)], "The test was not added correctly"


def test_has_covid_no_symptoms():
    patient = Patient(name='Matias', symptoms='Narcolepsy')
    assert patient.has_covid() == 0.05 ,"The initial probability of 0.05 is not correct"


def test_has_covid_with_symptoms():
    patient = Patient(name='Matias', symptoms=['Narcolepsy','fever'])
    assert patient.has_covid() == 0.15, "The probability with 1 relevant_symptom of 0.15 is not correct"
    

def test_has_covid_multiple_symptoms():
    patient = Patient(name='Matias', symptoms=['Narcolepsy','fever','anosmia'])
    assert patient.has_covid() == 0.25, "The probability with 2 relevant_symptoms of 0.25 is not correct"
    

def test_has_covid_positive_test():
    patient = Patient(name='Matias', symptoms='Narcolepsy')
    patient.add_test(test_name='covid', test_results=False)
    assert patient.has_covid() == 0.01,"The probability with covid test False but no symptoms"
    

def test_has_covid_negative_test():
    patient = Patient(name='Matias', symptoms='Narcolepsy')
    patient.add_test(test_name='covid', test_results=False)
    assert patient.has_covid() == 0.01
    

def test_has_covid_has_sypmptoms():
    patient = Patient(name='Matias', symptoms=['fever','anosmia'])
    patient.add_test(test_name='covid', test_results=True)
    assert patient.has_covid() == 1 , "The Probability must be  <= 1"
