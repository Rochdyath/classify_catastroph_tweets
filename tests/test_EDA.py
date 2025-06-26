import pandas as pd
import pytest

@pytest.fixture
def df():
    data = pd.read_csv("data/tweets.csv")
    data = data[['text', 'target']]
    return data

def test_colonnes_presentes(df):
    expected_columns = {'text', 'target'}
    assert expected_columns.issubset(df.columns), "Colonnes essentielles manquantes"

def test_types_colonnes(df):
    assert df['text'].dtype == object, "'text' doit être de type string"
    assert pd.api.types.is_integer_dtype(df['target']), "'target' doit être un entier"

def test_valeurs_manquantes(df):
    assert df.isnull().sum().sum() == 0, "Le dataset contient des valeurs manquantes"

def test_textes_non_vides(df):
    assert (df['text'].str.strip().str.len() > 0).all(), "Certains textes sont vides"

def test_valeurs_target(df):
    valeurs_uniques = set(df['target'].unique())
    assert valeurs_uniques == {0, 1}, f"Valeurs cibles inattendues : {valeurs_uniques}"

def test_longueurs_texte(df):
    longueurs = df['text'].str.len()
    assert longueurs.min() > 0, "Il y a des textes de longueur nulle"
    assert longueurs.max() <= 280, "Il y a des textes trop longs pour un tweet (>280 caractères)"
    moyenne = longueurs.mean()
    assert moyenne > 20, f"Longueur moyenne suspecte : {moyenne}"
