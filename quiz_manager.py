#!/usr/bin/env python3
"""
Script de gestion des questions SECUR-SIM
Permet de valider, fusionner et organiser les questions
"""

import json
import os
from typing import Dict, List
from collections import Counter

class QuizManager:
    """Gestionnaire de questions pour SECUR-SIM"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.levels = {
            1: {"nom": "BLS-AED", "target": 100},
            2: {"nom": "First Responder", "target": 100},
            3: {"nom": "Médecine de Catastrophe", "target": 100}
        }
    
    def load_questions(self, niveau: int) -> Dict:
        """Charge les questions d'un niveau"""
        filepath = os.path.join(self.data_dir, f"niveau{niveau}.json")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Fichier {filepath} non trouvé")
            return {"questions": []}
    
    def validate_question(self, question: Dict, niveau: int) -> List[str]:
        """Valide une question et retourne les erreurs"""
        errors = []
        
        # Vérifier les champs obligatoires
        required_fields = ['id', 'titre', 'cas_clinique', 'question', 'options', 'points', 'tags']
        for field in required_fields:
            if field not in question:
                errors.append(f"❌ Champ obligatoire manquant: {field}")
        
        # Vérifier l'ID
        if 'id' in question:
            expected_prefix = f"n{niveau}_q"
            if not question['id'].startswith(expected_prefix):
                errors.append(f"❌ ID invalide: devrait commencer par {expected_prefix}")
        
        # Vérifier les options
        if 'options' in question:
            if len(question['options']) != 4:
                errors.append(f"❌ Il faut exactement 4 options (trouvé: {len(question['options'])})")
            
            correct_count = sum(1 for opt in question['options'] if opt.get('correct', False))
            if correct_count != 1:
                errors.append(f"❌ Il faut exactement 1 bonne réponse (trouvé: {correct_count})")
            
            # Vérifier que les IDs d'options sont a, b, c, d
            option_ids = [opt.get('id', '') for opt in question['options']]
            if sorted(option_ids) != ['a', 'b', 'c', 'd']:
                errors.append(f"❌ Les IDs d'options doivent être a, b, c, d (trouvé: {option_ids})")
            
            # Vérifier les champs des options
            for i, opt in enumerate(question['options']):
                if 'texte' not in opt:
                    errors.append(f"❌ Option {i+1}: champ 'texte' manquant")
                if 'explication' not in opt:
                    errors.append(f"❌ Option {i+1}: champ 'explication' manquant")
                if 'source' not in opt:
                    errors.append(f"❌ Option {i+1}: champ 'source' manquant")
                
                # Vérifier le complément pour la bonne réponse
                if opt.get('correct', False) and 'complement' not in opt:
                    errors.append(f"⚠️  Option correcte: recommandé d'ajouter un 'complement'")
        
        # Vérifier les tags
        if 'tags' in question and len(question['tags']) == 0:
            errors.append(f"⚠️  Recommandé: ajouter au moins 1 tag")
        
        # Vérifier la longueur du cas clinique
        if 'cas_clinique' in question:
            if len(question['cas_clinique']) < 100:
                errors.append(f"⚠️  Cas clinique court (< 100 caractères)")
            if len(question['cas_clinique']) > 1000:
                errors.append(f"⚠️  Cas clinique très long (> 1000 caractères)")
        
        return errors
    
    def validate_all(self, niveau: int) -> Dict:
        """Valide toutes les questions d'un niveau"""
        data = self.load_questions(niveau)
        questions = data.get('questions', [])
        
        results = {
            'total': len(questions),
            'valid': 0,
            'errors': [],
            'warnings': [],
            'duplicate_ids': []
        }
        
        # Vérifier les doublons d'ID
        ids = [q.get('id', '') for q in questions]
        id_counts = Counter(ids)
        duplicates = [id for id, count in id_counts.items() if count > 1]
        if duplicates:
            results['duplicate_ids'] = duplicates
        
        # Valider chaque question
        for i, question in enumerate(questions):
            errors = self.validate_question(question, niveau)
            if errors:
                error_msgs = [f"Question {i+1} (ID: {question.get('id', 'N/A')})"]
                error_msgs.extend([f"  {err}" for err in errors])
                
                # Séparer erreurs et avertissements
                has_errors = any('❌' in err for err in errors)
                if has_errors:
                    results['errors'].extend(error_msgs)
                else:
                    results['warnings'].extend(error_msgs)
            else:
                results['valid'] += 1
        
        return results
    
    def generate_stats(self, niveau: int) -> Dict:
        """Génère des statistiques sur les questions"""
        data = self.load_questions(niveau)
        questions = data.get('questions', [])
        
        stats = {
            'total': len(questions),
            'target': self.levels[niveau]['target'],
            'progression': f"{len(questions)}/{self.levels[niveau]['target']} ({len(questions)/self.levels[niveau]['target']*100:.1f}%)",
            'tags': Counter(),
            'difficultes': Counter()
        }
        
        for q in questions:
            # Compter les tags
            for tag in q.get('tags', []):
                stats['tags'][tag] += 1
            
            # Compter les difficultés
            diff = q.get('difficulte', 1)
            stats['difficultes'][diff] += 1
        
        return stats
    
    def print_report(self):
        """Affiche un rapport complet"""
        print("\n" + "="*60)
        print("📊 RAPPORT SECUR-SIM - GESTION DES QUESTIONS")
        print("="*60 + "\n")
        
        for niveau in [1, 2, 3]:
            nom = self.levels[niveau]['nom']
            print(f"\n{'─'*60}")
            print(f"📚 NIVEAU {niveau} - {nom.upper()}")
            print(f"{'─'*60}")
            
            # Statistiques
            stats = self.generate_stats(niveau)
            print(f"\n✨ Progression: {stats['progression']}")
            
            if stats['total'] > 0:
                print(f"\n🏷️  Tags les plus utilisés:")
                for tag, count in stats['tags'].most_common(5):
                    print(f"   • {tag}: {count}")
                
                print(f"\n📊 Répartition difficultés:")
                for diff in sorted(stats['difficultes'].keys()):
                    count = stats['difficultes'][diff]
                    pct = count / stats['total'] * 100
                    print(f"   • Niveau {diff}: {count} ({pct:.1f}%)")
            
            # Validation
            validation = self.validate_all(niveau)
            
            print(f"\n✅ Questions valides: {validation['valid']}/{validation['total']}")
            
            if validation['duplicate_ids']:
                print(f"\n⚠️  IDs dupliqués: {', '.join(validation['duplicate_ids'])}")
            
            if validation['errors']:
                print(f"\n❌ Erreurs ({len(validation['errors'])} problèmes):")
                for err in validation['errors'][:10]:  # Limiter à 10
                    print(f"   {err}")
                if len(validation['errors']) > 10:
                    print(f"   ... et {len(validation['errors']) - 10} autres")
            
            if validation['warnings']:
                print(f"\n⚠️  Avertissements ({len(validation['warnings'])} problèmes):")
                for warn in validation['warnings'][:5]:  # Limiter à 5
                    print(f"   {warn}")
                if len(validation['warnings']) > 5:
                    print(f"   ... et {len(validation['warnings']) - 5} autres")
        
        print("\n" + "="*60 + "\n")
    
    def merge_files(self, niveau: int, output_file: str = None):
        """Fusionne plusieurs fichiers JSON en un seul"""
        # À implémenter si nécessaire pour fusionner des fichiers de questions
        pass


def main():
    """Fonction principale"""
    import sys
    
    manager = QuizManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "validate":
            niveau = int(sys.argv[2]) if len(sys.argv) > 2 else None
            if niveau:
                validation = manager.validate_all(niveau)
                print(f"\n✅ Résultat validation Niveau {niveau}:")
                print(f"   Valides: {validation['valid']}/{validation['total']}")
                if validation['errors']:
                    print(f"   Erreurs: {len(validation['errors'])}")
                if validation['warnings']:
                    print(f"   Avertissements: {len(validation['warnings'])}")
            else:
                print("Usage: python quiz_manager.py validate <niveau>")
        
        elif command == "stats":
            niveau = int(sys.argv[2]) if len(sys.argv) > 2 else None
            if niveau:
                stats = manager.generate_stats(niveau)
                print(f"\n📊 Statistiques Niveau {niveau}:")
                print(f"   Total: {stats['total']}")
                print(f"   Progression: {stats['progression']}")
            else:
                print("Usage: python quiz_manager.py stats <niveau>")
        
        else:
            print(f"Commande inconnue: {command}")
            print("Commandes disponibles: validate, stats, report")
    
    else:
        # Afficher le rapport complet par défaut
        manager.print_report()


if __name__ == "__main__":
    main()
