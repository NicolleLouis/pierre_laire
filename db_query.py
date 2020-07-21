sqlite_create_table_query = '''
    CREATE TABLE professionals(
        Type_d_identifiant_PP text not null,
        Identifiant_PP INTEGER PRIMARY KEY,
        Identification_nationale_PP INTEGER not null,
        Code_civilite_d_exercice text,
        Libelle_civilite_d_exercice text,
        Code_civilite text,
        Libelle_civilite text,
        Nom_d_exercice text,
        Prenom_d_exercice text,
        Code_profession text,
        Libelle_profession text,
        Code_categorie_professionnelle text,
        Libelle_categorie_professionnelle text,
        Code_type_savoir_faire text,
        Libelle_type_savoir_faire text,
        Code_savoir_faire text,
        Libelle_savoir_faire text,
        Code_mode_exercice text,
        Libelle_mode_exercice text,
        Numero_SIRET_site text,
        Numero_SIREN_site text,
        Numero_FINESS_site text,
        Numero_FINESS_etablissement_juridique text,
        Identifiant_technique_de_la_structure text,
        Raison_sociale_site text,
        Enseigne_commerciale_site text,
        Complement_destinataire_coord_structure text,
        Complement_point_geographique_coord_structure text,
        Numero_Voie_coord_structure text,
        Indice_repetition_voie_coord_structure text,
        Code_type_de_voie_coord_structure text,
        Libelle_type_de_voie_coord_structure text,
        Libelle_Voie_coord_structure text,
        Mention_distribution_coord_structure text,
        Bureau_cedex_coord_structure text,
        Code_postal_coord_structure text,
        Code_commune_coord_structure text,
        Libelle_commune_coord_structure text,
        Code_pays_coord_structure text,
        Libelle_pays_coord_structure text,
        Telephone_coord_structure text,
        Telephone_2_coord_structure text,
        Telecopie_coord_structure text,
        Adresse_e_mail_coord_structure text,
        Code_Departement_structure text,
        Libelle_Departement_structure text,
        Ancien_identifiant_de_la_structure text,
        Autorite_d_enregistrement text,
        Code_secteur_d_activite text,
        Libelle_secteur_d_activite text,
        Code_section_tableau_pharmaciens text,
        Libelle_section_tableau_pharmaciens text
    );
'''

sqlite_print_table = '''
    SELECT * FROM professionals;
'''

sqlite_drop_table = '''
    DROP TABLE professionals
'''